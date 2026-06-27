import json
import os
from config import DB_FILE
import math
import time
import datetime

ACTIONS_FILE = "actions.json"
MATCHES_FILE = "matches.json"
BLOCKS_FILE = "blocks.json"
REPORTS_FILE = "reports.json"

from geopy.geocoders import Nominatim

_geolocateur = Nominatim(user_agent="m_match_bot")


def ville_depuis_gps(lat, lon):
    """Transforme des coordonnées GPS en nom de quartier ou ville."""
    if lat is None or lon is None:
        return None
    try:
        lieu = _geolocateur.reverse((lat, lon), language="fr", timeout=5)
        if not lieu or not lieu.raw.get("address"):
            return None
        adr = lieu.raw["address"]
        return (
            adr.get("suburb")
            or adr.get("neighbourhood")
            or adr.get("city_district")
            or adr.get("city")
            or adr.get("town")
            or adr.get("village")
            or adr.get("municipality")
            or adr.get("county")
            or adr.get("state")
        )
    except Exception:
        return None
    
async def ville_depuis_gps_async(lat, lon):
    """Version non-bloquante : exécute l'appel Nominatim dans un thread séparé."""
    import asyncio
    loop = asyncio.get_event_loop()
    return await loop.run_in_executor(None, ville_depuis_gps, lat, lon)


# ---------- Profils ----------
def charger_profils():
    if not os.path.exists(DB_FILE):
        return {}
    with open(DB_FILE, "r", encoding="utf-8") as f:
        contenu = f.read().strip()
        if not contenu:
            return {}
        return json.loads(contenu)


def sauver_profils(profils):
    with open(DB_FILE, "w", encoding="utf-8") as f:
        json.dump(profils, f, ensure_ascii=False, indent=2)


def profil_existe(user_id):
    return str(user_id) in charger_profils()


def enregistrer_profil(user_id, profil):
    profils = charger_profils()
    profils[str(user_id)] = profil
    sauver_profils(profils)


def get_profil(user_id):
    return charger_profils().get(str(user_id))


def modifier_champ(user_id, champ, valeur):
    profils = charger_profils()
    uid = str(user_id)
    if uid in profils:
        profils[uid][champ] = valeur
        sauver_profils(profils)


def rafraichir_username(user_id, username):
    """Met à jour le username Telegram dans le profil s'il a changé."""
    profils = charger_profils()
    uid = str(user_id)
    if uid not in profils:
        return
    actuel = profils[uid].get("username")
    if actuel != username:
        profils[uid]["username"] = username
        sauver_profils(profils)


# ---------- Actions (like / pass / block / report) ----------
def charger_actions():
    if not os.path.exists(ACTIONS_FILE):
        return {}
    with open(ACTIONS_FILE, "r", encoding="utf-8") as f:
        contenu = f.read().strip()
        if not contenu:
            return {}
        return json.loads(contenu)


def sauver_actions(actions):
    with open(ACTIONS_FILE, "w", encoding="utf-8") as f:
        json.dump(actions, f, ensure_ascii=False, indent=2)


def enregistrer_action(user_id, cible_id, action):
    actions = charger_actions()
    uid = str(user_id)
    if uid not in actions:
        actions[uid] = {}
    actions[uid][str(cible_id)] = {"action": action, "date": time.time()}
    sauver_actions(actions)


def _info_action(val):
    """Compatibilité : ancienne action = str, nouvelle = dict {action, date}."""
    if isinstance(val, dict):
        return val.get("action"), val.get("date", 0)
    return val, 0  # ancienne donnée sans date


def deja_vus(user_id):
    """Profils à NE PLUS montrer : likés, bloqués, signalés (définitifs),
    ET passés il y a moins de 24h."""
    actions = charger_actions()
    mes_actions = actions.get(str(user_id), {})
    maintenant = time.time()
    exclus = set()
    for cible_id, val in mes_actions.items():
        action, date = _info_action(val)
        if action in ("like", "block", "report"):
            exclus.add(cible_id)  # définitif
        elif action == "pass":
            if maintenant - date < 24 * 3600:
                exclus.add(cible_id)  # passé il y a moins de 24h
            # sinon : recyclable, on ne l'exclut pas
    return exclus


def vus_definitivement(user_id):
    """Profils définitivement écartés (likés, bloqués, signalés) — jamais recyclés."""
    actions = charger_actions()
    mes_actions = actions.get(str(user_id), {})
    exclus = set()
    for cible_id, val in mes_actions.items():
        action, _ = _info_action(val)
        if action in ("like", "block", "report"):
            exclus.add(cible_id)
    return exclus


def deja_touches(user_id):
    """Tous les profils sur lesquels on a déjà fait une action (peu importe laquelle)."""
    actions = charger_actions()
    return set(actions.get(str(user_id), {}).keys())


def a_like(user_id, cible_id):
    actions = charger_actions()
    val = actions.get(str(user_id), {}).get(str(cible_id))
    action, _ = _info_action(val)
    return action == "like"


def reset_actions(user_id):
    actions = charger_actions()
    uid = str(user_id)
    if uid in actions:
        del actions[uid]
        sauver_actions(actions)


# ---------- Matchs ----------
def charger_matches():
    """Structure : { 'user_id': ['autre_id', ...] }"""
    if not os.path.exists(MATCHES_FILE):
        return {}
    with open(MATCHES_FILE, "r", encoding="utf-8") as f:
        contenu = f.read().strip()
        if not contenu:
            return {}
        return json.loads(contenu)


def sauver_matches(matches):
    with open(MATCHES_FILE, "w", encoding="utf-8") as f:
        json.dump(matches, f, ensure_ascii=False, indent=2)


def enregistrer_match(user_a, user_b):
    """Enregistre un match entre deux personnes (dans les deux sens)."""
    matches = charger_matches()
    a, b = str(user_a), str(user_b)
    matches.setdefault(a, [])
    matches.setdefault(b, [])
    if b not in matches[a]:
        matches[a].append(b)
    if a not in matches[b]:
        matches[b].append(a)
    sauver_matches(matches)


def get_matches(user_id):
    """Renvoie la liste des ids des matchs d'un utilisateur."""
    return charger_matches().get(str(user_id), [])


def sont_matchs(user_a, user_b):
    """Vrai si les deux personnes ont matché."""
    return str(user_b) in get_matches(user_a)


# ---------- Blocages ----------
def charger_blocks():
    if not os.path.exists(BLOCKS_FILE):
        return {}
    with open(BLOCKS_FILE, "r", encoding="utf-8") as f:
        contenu = f.read().strip()
        if not contenu:
            return {}
        return json.loads(contenu)


def sauver_blocks(blocks):
    with open(BLOCKS_FILE, "w", encoding="utf-8") as f:
        json.dump(blocks, f, ensure_ascii=False, indent=2)


def bloquer(user_id, cible_id):
    """user_id bloque cible_id."""
    blocks = charger_blocks()
    uid = str(user_id)
    blocks.setdefault(uid, [])
    if str(cible_id) not in blocks[uid]:
        blocks[uid].append(str(cible_id))
    sauver_blocks(blocks)


def est_bloque(user_id, cible_id):
    """Vrai si l'un a bloqué l'autre (dans un sens ou dans l'autre)."""
    blocks = charger_blocks()
    a = str(cible_id) in blocks.get(str(user_id), [])
    b = str(user_id) in blocks.get(str(cible_id), [])
    return a or b


# ---------- Signalements ----------
def charger_reports():
    if not os.path.exists(REPORTS_FILE):
        return []
    with open(REPORTS_FILE, "r", encoding="utf-8") as f:
        contenu = f.read().strip()
        if not contenu:
            return []
        return json.loads(contenu)


def enregistrer_report(signaleur_id, cible_id):
    reports = charger_reports()
    reports.append({"par": str(signaleur_id), "cible": str(cible_id)})
    with open(REPORTS_FILE, "w", encoding="utf-8") as f:
        json.dump(reports, f, ensure_ascii=False, indent=2)


def compter_blocages_recus(cible_id):
    """Compte combien de personnes ont bloqué cible_id."""
    blocks = charger_blocks()
    total = 0
    for bloqueur, liste in blocks.items():
        if str(cible_id) in liste:
            total += 1
    return total


def compter_signalements_recus(cible_id):
    """Compte combien de personnes DIFFÉRENTES ont signalé cible_id."""
    reports = charger_reports()
    signaleurs = set()
    for r in reports:
        if r["cible"] == str(cible_id):
            signaleurs.add(r["par"])
    return len(signaleurs)


# ---------- Filtres de recherche ----------
def get_filtres(user_id):
    """Renvoie les filtres d'un utilisateur, ou les valeurs par défaut."""
    profil = get_profil(user_id)
    if not profil:
        return None
    return profil.get("filtres", {
        "age_min": 18,
        "age_max": 99,
        "distance": 15000,
    })


def set_filtres(user_id, age_min, age_max, distance):
    """Enregistre les filtres dans le profil de l'utilisateur."""
    modifier_champ(user_id, "filtres", {
        "age_min": age_min,
        "age_max": age_max,
        "distance": distance,
    })


def calculer_distance_km(lat1, lon1, lat2, lon2):
    """Distance en km entre deux points GPS (formule de Haversine)."""
    if None in (lat1, lon1, lat2, lon2):
        return None
    R = 6371  # rayon de la Terre en km
    d_lat = math.radians(lat2 - lat1)
    d_lon = math.radians(lon2 - lon1)
    a = (math.sin(d_lat / 2) ** 2
         + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2))
         * math.sin(d_lon / 2) ** 2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return R * c


# ---------- Pause du profil ----------
def mettre_en_pause(user_id, en_pause):
    """Active ou désactive la pause d'un profil."""
    modifier_champ(user_id, "en_pause", en_pause)


def est_en_pause(user_id):
    profil = get_profil(user_id)
    return bool(profil and profil.get("en_pause"))


# ---------- Suppression du compte ----------
def supprimer_compte(user_id):
    """Efface définitivement le profil, ses actions et ses matchs (RGPD)."""
    uid = str(user_id)

    profils = charger_profils()
    if uid in profils:
        del profils[uid]
        sauver_profils(profils)

    actions = charger_actions()
    actions.pop(uid, None)
    for autre in list(actions.keys()):
        actions[autre].pop(uid, None)
    sauver_actions(actions)

    matches = charger_matches()
    matches.pop(uid, None)
    for autre in list(matches.keys()):
        if uid in matches[autre]:
            matches[autre].remove(uid)
    sauver_matches(matches)


# ---------- Vérification de profil ----------
def set_verifie(user_id, verifie):
    """Marque un profil comme vérifié (True) ou non (False)."""
    modifier_champ(user_id, "verifie", verifie)


def est_verifie(user_id):
    profil = get_profil(user_id)
    return bool(profil and profil.get("verifie"))


def set_verification_en_cours(user_id, en_cours):
    """Indique si une demande de vérification est en attente."""
    modifier_champ(user_id, "verif_en_cours", en_cours)


def verification_en_cours(user_id):
    profil = get_profil(user_id)
    return bool(profil and profil.get("verif_en_cours"))


# ---------- Bannissement ----------
def bannir(user_id):
    """Bannit un profil : il devient invisible partout (comme une pause forcée)."""
    modifier_champ(user_id, "banni", True)
    modifier_champ(user_id, "en_pause", True)


def est_banni(user_id):
    profil = get_profil(user_id)
    return bool(profil and profil.get("banni"))


def debannir(user_id):
    """Lève le bannissement d'un profil et le réactive."""
    modifier_champ(user_id, "banni", False)
    modifier_champ(user_id, "en_pause", False)


# ---------- Statistiques (admin) ----------
def statistiques():
    """Renvoie un dictionnaire de statistiques globales."""
    profils = charger_profils()
    total = len(profils)
    verifies = sum(1 for p in profils.values() if p.get("verifie"))
    en_pause = sum(1 for p in profils.values() if p.get("en_pause"))
    bannis = sum(1 for p in profils.values() if p.get("banni"))

    matches = charger_matches()
    paires = set()
    for uid, liste in matches.items():
        for autre in liste:
            paires.add(frozenset((uid, autre)))
    nb_matchs = len(paires)

    return {
        "total": total,
        "verifies": verifies,
        "en_pause": en_pause,
        "bannis": bannis,
        "matchs": nb_matchs,
    }


# ---------- Statistiques personnelles d'un utilisateur ----------
def stats_utilisateur(user_id):
    """Renvoie les stats personnelles : likes reçus, matchs."""
    uid = str(user_id)

    actions = charger_actions()
    likes_recus = 0
    for autre, cibles in actions.items():
        val = cibles.get(uid)
        action, _ = _info_action(val)
        if action == "like":
            likes_recus += 1

    nb_matchs = len(get_matches(user_id))

    return {"likes_recus": likes_recus, "matchs": nb_matchs}


# ---------- Profil "nouveau" (inscrit récemment) ----------
def est_nouveau(profil, jours=3):
    """Vrai si le profil a été créé il y a moins de X jours."""
    date_inscription = profil.get("date_inscription")
    if not date_inscription:
        return False
    secondes = jours * 24 * 3600
    return (time.time() - date_inscription) < secondes


# ---------- Activité et rappels ----------
def noter_activite(user_id):
    """Met à jour l'horodatage de dernière activité d'un utilisateur."""
    modifier_champ(user_id, "derniere_activite", time.time())


def a_match_non_ouvert(user_id):
    """Vrai si l'utilisateur a au moins un match (pour le rappel 'match en attente')."""
    return len(get_matches(user_id)) > 0


def profils_a_relancer(inactif_apres_h, pas_avant_h):
    """Renvoie la liste des (user_id, profil) à relancer."""
    profils = charger_profils()
    maintenant = time.time()
    seuil_inactif = inactif_apres_h * 3600
    seuil_rappel = pas_avant_h * 3600
    a_relancer = []

    for uid, profil in profils.items():
        if profil.get("en_pause") or profil.get("banni"):
            continue
        derniere = profil.get("derniere_activite")
        if not derniere:
            continue
        if (maintenant - derniere) < seuil_inactif:
            continue
        dernier_rappel = profil.get("dernier_rappel", 0)
        if (maintenant - dernier_rappel) < seuil_rappel:
            continue
        a_relancer.append((uid, profil))

    return a_relancer


def noter_rappel(user_id):
    """Mémorise qu'on vient d'envoyer un rappel à cet utilisateur."""
    modifier_champ(user_id, "dernier_rappel", time.time())


# ---------- Limite de likes quotidienne ----------
def _aujourdhui():
    """Renvoie la date du jour au format texte 'AAAA-MM-JJ'."""
    return datetime.date.today().isoformat()


def likes_restants(user_id, limite_normale, limite_verifie):
    """Renvoie le nombre de likes qu'il reste à l'utilisateur aujourd'hui."""
    profil = get_profil(user_id)
    if not profil:
        return 0

    limite = limite_verifie if profil.get("verifie") else limite_normale

    compteur = profil.get("likes_jour", {})
    if compteur.get("date") != _aujourdhui():
        return limite

    utilises = compteur.get("nombre", 0)
    return max(0, limite - utilises)


def consommer_like(user_id):
    """Incrémente le compteur de likes du jour pour l'utilisateur."""
    profil = get_profil(user_id)
    if not profil:
        return
    compteur = profil.get("likes_jour", {})
    if compteur.get("date") != _aujourdhui():
        compteur = {"date": _aujourdhui(), "nombre": 0}
    compteur["nombre"] = compteur.get("nombre", 0) + 1
    modifier_champ(user_id, "likes_jour", compteur)


# ---------- Langue de l'utilisateur ----------
def set_langue(user_id, langue):
    """Enregistre la langue choisie ('fr', 'en', 'ru')."""
    profils = charger_profils()
    uid = str(user_id)
    if uid in profils:
        profils[uid]["langue"] = langue
        sauver_profils(profils)
    else:
        langues = _charger_langues()
        langues[uid] = langue
        _sauver_langues(langues)


def get_langue(user_id):
    """Renvoie la langue de l'utilisateur, 'fr' par défaut."""
    profil = get_profil(user_id)
    if profil and profil.get("langue"):
        return profil["langue"]
    langues = _charger_langues()
    return langues.get(str(user_id), "fr")


def _charger_langues():
    if not os.path.exists("langues.json"):
        return {}
    with open("langues.json", "r", encoding="utf-8") as f:
        contenu = f.read().strip()
        return json.loads(contenu) if contenu else {}


def _sauver_langues(langues):
    with open("langues.json", "w", encoding="utf-8") as f:
        json.dump(langues, f, ensure_ascii=False, indent=2)

def likes_recus_en_attente(user_id):
    """Compte les personnes qui ont liké user_id SANS qu'il les ait likées en retour."""
    actions = charger_actions()
    uid = str(user_id)
    mes_actions = actions.get(uid, {})
    total = 0
    for autre, cibles in actions.items():
        if autre == uid:
            continue
        val = cibles.get(uid)
        action, _ = _info_action(val)
        if action == "like":
            # Est-ce que j'ai déjà liké cette personne ? (sinon c'est en attente)
            mon_action, _ = _info_action(mes_actions.get(autre))
            if mon_action != "like":
                total += 1
    return total


def peut_notifier_like(user_id, intervalle_heures=3):
    """Anti-spam : vrai si on n'a pas notifié cette personne depuis X heures."""
    profil = get_profil(user_id)
    if not profil:
        return False
    dernier = profil.get("derniere_notif_like", 0)
    return (time.time() - dernier) > intervalle_heures * 3600


def noter_notif_like(user_id):
    """Mémorise qu'on vient d'envoyer une notif de like."""
    modifier_champ(user_id, "derniere_notif_like", time.time())