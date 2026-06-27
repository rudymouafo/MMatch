import asyncio
import time

from aiogram import Router, F
from aiogram.types import Message, ReplyKeyboardRemove, InputMediaPhoto, InputMediaVideo
from aiogram.filters import CommandStart, Command
from aiogram.fsm.context import FSMContext

import config
from states import Inscription
from database import profil_existe, enregistrer_profil, set_langue, get_langue
from traductions import t
from keyboards import (
    clavier_genre,
    clavier_recherche,
    clavier_localisation,
    clavier_precedent,
    clavier_medias,
    clavier_telephone,
    clavier_langue,
    clavier_bio,
    clavier_cgu_trad,
    menu_profil,
    menu_principal,
)

router = Router()


# ---------- Barre de progression (8 étapes) ----------
def progression(user_id, etape, total=8):
    pleins = "▰" * etape
    vides = "▱" * (total - etape)
    mot = t(user_id, "etape")
    return f"<b>{mot} {etape}/{total}</b>  {pleins}{vides}\n\n"


# ---------- Animation festive ----------
async def animation_bienvenue(message):
    etapes = ["🎉", "🎉 ✨", "🎉 ✨ 💞", "✨ 💞 🎊 💞 ✨"]
    msg = await message.answer(etapes[0])
    for etape in etapes[1:]:
        await asyncio.sleep(0.4)
        try:
            await msg.edit_text(etape)
        except Exception:
            pass
    await asyncio.sleep(1.0)
    try:
        await msg.delete()
    except Exception:
        pass


# ---------- /start ----------
@router.message(CommandStart())
async def start(message: Message, state: FSMContext):
    if profil_existe(message.from_user.id):
        await message.answer(
            t(message.from_user.id, "deja_inscrit"),
            reply_markup=menu_principal(message.from_user.id),
        )
        return
    await message.answer(
        t(message.from_user.id, "choisir_langue"),
        reply_markup=clavier_langue,
    )
    await state.set_state(Inscription.langue)


# ---------- Choix de la langue ----------
@router.message(Inscription.langue)
async def choisir_langue(message: Message, state: FSMContext):
    texte = message.text or ""
    if "Français" in texte:
        langue = "fr"
    elif "English" in texte:
        langue = "en"
    elif "Русский" in texte:
        langue = "ru"
    else:
        await message.answer("👇", reply_markup=clavier_langue)
        return

    set_langue(message.from_user.id, langue)
    await message.answer(t(message.from_user.id, "langue_ok"))
    await message.answer(
        t(message.from_user.id, "cgu"),
        reply_markup=clavier_cgu_trad(
            t(message.from_user.id, "cgu_accepte"),
            t(message.from_user.id, "cgu_refuse"),
        ),
    )
    await state.set_state(Inscription.cgu)


# ---------- Conditions d'utilisation ----------
@router.message(Inscription.cgu)
async def reponse_cgu(message: Message, state: FSMContext):
    user_id = message.from_user.id
    texte = message.text or ""

    if "✅" in texte:
        await message.answer(
            t(user_id, "demande_prenom"),
            reply_markup=ReplyKeyboardRemove(),
        )
        await state.set_state(Inscription.prenom)
    elif "❌" in texte:
        await state.clear()
        await message.answer(
            t(user_id, "cgu_refuse_msg"),
            reply_markup=ReplyKeyboardRemove(),
        )
    else:
        await message.answer(
            t(user_id, "cgu"),
            reply_markup=clavier_cgu_trad(
                t(user_id, "cgu_accepte"),
                t(user_id, "cgu_refuse"),
            ),
        )


# ---------- Raccourcis du menu permanent (reconnus par icône) ----------
@router.message(F.text.contains("🔥"))
async def raccourci_decouvrir(message: Message, state: FSMContext):
    await state.clear()
    from database import rafraichir_username
    rafraichir_username(message.from_user.id, message.from_user.username)
    from handlers.discovery import envoyer_prochain
    await envoyer_prochain(message, message.from_user.id)


@router.message(F.text.contains("💞"))
async def raccourci_matchs(message: Message, state: FSMContext):
    await state.clear()
    from handlers.chat import afficher_matchs
    await afficher_matchs(message, message.from_user.id)


@router.message(F.text.contains("👤"))
async def raccourci_profil(message: Message, state: FSMContext):
    await state.clear()
    from handlers.profile import ouvrir_menu_profil
    await ouvrir_menu_profil(message, message.from_user.id, state)


@router.message(F.text.contains("⚙️"))
async def raccourci_parametres(message: Message, state: FSMContext):
    await state.clear()
    from handlers.settings import ouvrir_menu_parametres
    await ouvrir_menu_parametres(message, message.from_user.id, state)


# ---------- Annuler ----------
@router.message(Command("annuler", "cancel"))
async def annuler(message: Message, state: FSMContext):
    await state.clear()
    await message.answer(
        t(message.from_user.id, "annule"),
        reply_markup=ReplyKeyboardRemove(),
    )


# ====================================================
#   RETOUR EN ARRIÈRE pendant l'inscription
#   (boutons « Précédent » reconnus par l'icône ⬅️)
# ====================================================

@router.message(Inscription.age, F.text.contains("⬅️"))
async def retour_vers_prenom(message: Message, state: FSMContext):
    await message.answer(
        progression(message.from_user.id, 1) + t(message.from_user.id, "demande_prenom"),
        reply_markup=ReplyKeyboardRemove(),
    )
    await state.set_state(Inscription.prenom)


@router.message(Inscription.genre, F.text.contains("⬅️"))
async def retour_vers_age(message: Message, state: FSMContext):
    await message.answer(
        progression(message.from_user.id, 2) + t(message.from_user.id, "demande_age", prenom=""),
        reply_markup=clavier_precedent(message.from_user.id),
    )
    await state.set_state(Inscription.age)


@router.message(Inscription.recherche, F.text.contains("⬅️"))
async def retour_vers_genre(message: Message, state: FSMContext):
    await message.answer(
        progression(message.from_user.id, 3) + t(message.from_user.id, "demande_genre"),
        reply_markup=clavier_genre(message.from_user.id),
    )
    await state.set_state(Inscription.genre)


@router.message(Inscription.localisation, F.text.contains("⬅️"))
async def retour_vers_recherche(message: Message, state: FSMContext):
    await message.answer(
        progression(message.from_user.id, 4) + t(message.from_user.id, "demande_recherche"),
        reply_markup=clavier_recherche(message.from_user.id),
    )
    await state.set_state(Inscription.recherche)


@router.message(Inscription.bio, F.text.contains("⬅️"))
async def retour_vers_localisation(message: Message, state: FSMContext):
    await message.answer(
        progression(message.from_user.id, 5) + t(message.from_user.id, "demande_localisation"),
        reply_markup=clavier_localisation(message.from_user.id),
    )
    await state.set_state(Inscription.localisation)


@router.message(Inscription.medias, F.text.contains("⬅️"))
async def retour_vers_bio(message: Message, state: FSMContext):
    await message.answer(
        progression(message.from_user.id, 6) + t(message.from_user.id, "demande_bio"),
        reply_markup=clavier_precedent(message.from_user.id),
    )
    await state.set_state(Inscription.bio)


# ---------- Étape 1 : prénom ----------
@router.message(Inscription.prenom)
async def saisir_prenom(message: Message, state: FSMContext):
    if not message.text:
        await message.answer(
            t(message.from_user.id, "prenom_invalide", min=config.PRENOM_MIN, max=config.PRENOM_MAX)
        )
        return
    prenom = message.text.strip()
    if len(prenom) < config.PRENOM_MIN or len(prenom) > config.PRENOM_MAX:
        await message.answer(
            t(message.from_user.id, "prenom_invalide", min=config.PRENOM_MIN, max=config.PRENOM_MAX)
        )
        return
    await state.update_data(prenom=prenom)
    await message.answer(
        t(message.from_user.id, "demande_age", prenom=prenom) + "\n\n" + progression(message.from_user.id, 2),
        reply_markup=clavier_precedent(message.from_user.id),
    )
    await state.set_state(Inscription.age)


# ---------- Étape 2 : âge ----------
@router.message(Inscription.age)
async def saisir_age(message: Message, state: FSMContext):
    if not message.text:
        await message.answer(t(message.from_user.id, "age_invalide"))
        return
    texte = message.text.strip()
    if not texte.isdigit():
        await message.answer(t(message.from_user.id, "age_invalide"))
        return
    age = int(texte)
    if age < config.AGE_MIN:
        await message.answer(t(message.from_user.id, "age_trop_jeune"))
        await state.clear()
        return
    if age > config.AGE_MAX:
        await message.answer(t(message.from_user.id, "age_trop_vieux"))
        return
    await state.update_data(age=age)
    await message.answer(
        progression(message.from_user.id, 3) + t(message.from_user.id, "demande_genre"),
        reply_markup=clavier_genre(message.from_user.id),
    )
    await state.set_state(Inscription.genre)


# ---------- Étape 3 : genre (reconnu par icône) ----------
@router.message(Inscription.genre)
async def saisir_genre(message: Message, state: FSMContext):
    texte = message.text or ""
    if "👨" in texte:
        genre = "Homme"
    elif "👩" in texte:
        genre = "Femme"
    elif "⚧️" in texte:
        genre = "Autre"
    else:
        await message.answer(
            t(message.from_user.id, "genre_invalide"),
            reply_markup=clavier_genre(message.from_user.id),
        )
        return
    await state.update_data(genre=genre)
    await message.answer(
        progression(message.from_user.id, 4) + t(message.from_user.id, "demande_recherche"),
        reply_markup=clavier_recherche(message.from_user.id),
    )
    await state.set_state(Inscription.recherche)


# ---------- Étape 4 : recherche (reconnu par icône) ----------
@router.message(Inscription.recherche)
async def saisir_recherche(message: Message, state: FSMContext):
    texte = message.text or ""
    if "👨" in texte:
        recherche = "Hommes"
    elif "👩" in texte:
        recherche = "Femmes"
    elif "✨" in texte:
        recherche = "Tout le monde"
    else:
        await message.answer(
            t(message.from_user.id, "recherche_invalide"),
            reply_markup=clavier_recherche(message.from_user.id),
        )
        return
    await state.update_data(recherche=recherche)
    await message.answer(
        progression(message.from_user.id, 5) + t(message.from_user.id, "demande_localisation"),
        reply_markup=clavier_localisation(message.from_user.id),
    )
    await state.set_state(Inscription.localisation)


# ---------- Étape 5 : localisation (GPS uniquement) ----------
@router.message(Inscription.localisation, F.location)
async def saisir_localisation_gps(message: Message, state: FSMContext):
    from database import ville_depuis_gps_async
    lat = message.location.latitude
    lon = message.location.longitude
    ville = await ville_depuis_gps_async(lat, lon)
    await state.update_data(lat=lat, lon=lon, ville=ville)
    await message.answer(
        progression(message.from_user.id, 6) + t(message.from_user.id, "localisation_gps_ok"),
        reply_markup=clavier_bio(message.from_user.id),
    )
    await message.answer(t(message.from_user.id, "demande_bio_optionnelle"))
    await state.set_state(Inscription.bio)


@router.message(Inscription.localisation, F.text)
async def localisation_pas_de_texte(message: Message, state: FSMContext):
    # Le bouton ⬅️ Précédent est géré par un autre handler, on l'ignore ici
    if "⬅️" in (message.text or ""):
        return
    await message.answer(
        t(message.from_user.id, "localisation_gps_obligatoire"),
        reply_markup=clavier_localisation(message.from_user.id),
    )


# ---------- Étape 6 : bio ----------
@router.message(Inscription.bio, F.text.contains("⏭️"))
async def passer_bio(message: Message, state: FSMContext):
    await state.update_data(bio="", medias=[])
    await message.answer(
        progression(message.from_user.id, 7) + t(message.from_user.id, "demande_bio"),
        reply_markup=clavier_medias(message.from_user.id),
    )
    await state.set_state(Inscription.medias)


@router.message(Inscription.bio)
async def saisir_bio(message: Message, state: FSMContext):
    if not message.text:
        await message.answer(t(message.from_user.id, "demande_bio_optionnelle"),
                             reply_markup=clavier_bio(message.from_user.id))
        return
    bio = message.text.strip()
    if len(bio) > config.BIO_MAX:
        await message.answer(t(message.from_user.id, "bio_trop_longue", max=config.BIO_MAX))
        return
    await state.update_data(bio=bio, medias=[])
    await message.answer(
        progression(message.from_user.id, 7) + t(message.from_user.id, "demande_bio"),
        reply_markup=clavier_medias(message.from_user.id),
    )
    await state.set_state(Inscription.medias)


# ---------- Étape 7 : médias ----------
@router.message(Inscription.medias, F.photo)
async def recevoir_photo(message: Message, state: FSMContext):
    data = await state.get_data()
    medias = data.get("medias", [])
    if len(medias) >= config.MEDIAS_MAX:
        await message.answer(
            t(message.from_user.id, "media_max", max=config.MEDIAS_MAX),
            reply_markup=clavier_medias(message.from_user.id),
        )
        return
    medias.append({"type": "photo", "file_id": message.photo[-1].file_id})
    await state.update_data(medias=medias)
    await message.answer(
        t(message.from_user.id, "media_photo_ok", n=len(medias), max=config.MEDIAS_MAX),
        reply_markup=clavier_medias(message.from_user.id),
    )


@router.message(Inscription.medias, F.video)
async def recevoir_video(message: Message, state: FSMContext):
    data = await state.get_data()
    medias = data.get("medias", [])
    if len(medias) >= config.MEDIAS_MAX:
        await message.answer(
            t(message.from_user.id, "media_max", max=config.MEDIAS_MAX),
            reply_markup=clavier_medias(message.from_user.id),
        )
        return
    medias.append({"type": "video", "file_id": message.video.file_id})
    await state.update_data(medias=medias)
    await message.answer(
        t(message.from_user.id, "media_video_ok", n=len(medias), max=config.MEDIAS_MAX),
        reply_markup=clavier_medias(message.from_user.id),
    )


# ---------- Passage des médias à l'étape téléphone (reconnu par ✅) ----------
@router.message(Inscription.medias, F.text.contains("✅"))
async def medias_vers_telephone(message: Message, state: FSMContext):
    data = await state.get_data()
    medias = data.get("medias", [])
    if len(medias) == 0:
        await message.answer(t(message.from_user.id, "media_min"))
        return
    await message.answer(
        progression(message.from_user.id, 8) + t(message.from_user.id, "demande_telephone"),
        reply_markup=clavier_telephone(message.from_user.id),
    )
    await state.set_state(Inscription.telephone)


# ---------- Étape 8 : téléphone (partage du contact) ----------
@router.message(Inscription.telephone, F.contact)
async def recevoir_telephone(message: Message, state: FSMContext):
    # Sécurité : on n'accepte que le numéro de l'utilisateur lui-même
    if message.contact.user_id != message.from_user.id:
        await message.answer(t(message.from_user.id, "telephone_obligatoire"),
                             reply_markup=clavier_telephone(message.from_user.id))
        return

    telephone = message.contact.phone_number
    username = message.from_user.username  # peut être None
    await state.update_data(telephone=telephone, username=username)

    # Encouragement selon que l'utilisateur a un username ou non
    if username:
        await message.answer(t(message.from_user.id, "rappel_username_ok", username=username))
    else:
        await message.answer(t(message.from_user.id, "rappel_username_manquant"))

    await finir_inscription(message, state)


@router.message(Inscription.telephone, F.text.contains("⬅️"))
async def retour_vers_medias(message: Message, state: FSMContext):
    await message.answer(
        progression(message.from_user.id, 7) + t(message.from_user.id, "demande_bio"),
        reply_markup=clavier_medias(message.from_user.id),
    )
    await state.set_state(Inscription.medias)


@router.message(Inscription.telephone)
async def telephone_pas_de_contact(message: Message, state: FSMContext):
    if "⬅️" in (message.text or ""):
        return
    await message.answer(
        t(message.from_user.id, "telephone_obligatoire"),
        reply_markup=clavier_telephone(message.from_user.id),
    )


# ---------- Fin : enregistrement + récapitulatif ----------
async def finir_inscription(message: Message, state: FSMContext):
    data = await state.get_data()
    medias = data.get("medias", [])

    enregistrer_profil(message.from_user.id, {
        "prenom": data["prenom"],
        "age": data["age"],
        "genre": data["genre"],
        "recherche": data["recherche"],
        "ville": data.get("ville"),
        "lat": data.get("lat"),
        "lon": data.get("lon"),
        "bio": data["bio"],
        "medias": medias,
        "telephone": data.get("telephone"),
        "username": data.get("username"),
        "date_inscription": time.time(),
        "langue": get_langue(message.from_user.id),
    })

    lieu = data.get("ville") or "📍"
    legende = (
        f"✨ <b>{data['prenom']}</b>, {data['age']}\n"
        f"🌍 {lieu}\n\n"
        f"💬 <i>{data['bio']}</i>"
    )

    await animation_bienvenue(message)
    await message.answer(
        t(message.from_user.id, "profil_pret"),
        reply_markup=ReplyKeyboardRemove(),
    )

    if len(medias) == 1:
        m = medias[0]
        if m["type"] == "photo":
            await message.answer_photo(m["file_id"], caption=legende)
        else:
            await message.answer_video(m["file_id"], caption=legende)
    else:
        album = []
        for i, m in enumerate(medias):
            cap = legende if i == 0 else None
            if m["type"] == "photo":
                album.append(InputMediaPhoto(media=m["file_id"], caption=cap))
            else:
                album.append(InputMediaVideo(media=m["file_id"], caption=cap))
        await message.answer_media_group(album)

    await message.answer(
        t(message.from_user.id, "pret_aventure"),
        reply_markup=menu_principal(message.from_user.id),
    )
    await state.clear()