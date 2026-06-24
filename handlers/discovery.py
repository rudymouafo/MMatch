import asyncio

import config
from aiogram import Router, F
from aiogram.types import (
    Message,
    CallbackQuery,
    InputMediaPhoto,
    InputMediaVideo,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)
from aiogram.filters import Command

from database import (
    get_profil,
    charger_profils,
    deja_vus,
    enregistrer_action,
    a_like,
    enregistrer_match,
    bloquer,
    est_bloque,
    enregistrer_report,
    compter_blocages_recus,
    get_filtres,
    calculer_distance_km,
    est_en_pause,
    compter_signalements_recus,
    bannir,
    est_banni,
    est_nouveau,
    stats_utilisateur,
    likes_restants,
    consommer_like,
)
from traductions import t
from keyboards import clavier_swipe, menu_profil

router = Router()

messages_affiches = {}


async def supprimer_anciens(bot, user_id, chat_id):
    ids = messages_affiches.get(user_id, [])
    for mid in ids:
        try:
            await bot.delete_message(chat_id, mid)
        except Exception:
            pass
    messages_affiches[user_id] = []


async def flash_emoji(message, emoji, secondes=6):
    msg = await message.answer(emoji)

    async def supprimer_plus_tard():
        await asyncio.sleep(secondes)
        try:
            await msg.delete()
        except Exception:
            pass

    asyncio.create_task(supprimer_plus_tard())


async def cascade_coeurs(bot, chat_id):
    etapes = ["💞", "💞 💞", "💞 💞 💞", "💞 💞 💞 💞", "💞 💕 💞 💕 💞"]
    msg = await bot.send_message(chat_id, etapes[0])
    for etape in etapes[1:]:
        await asyncio.sleep(0.4)
        try:
            await msg.edit_text(etape)
        except Exception:
            pass
    await asyncio.sleep(1.2)
    try:
        await msg.delete()
    except Exception:
        pass


async def alerter_si_tres_bloque(bot, cible_id):
    nb = compter_blocages_recus(cible_id)
    if nb >= config.SEUIL_BLOCAGES:
        cible = get_profil(cible_id)
        nom_cible = cible["prenom"] if cible else cible_id
        try:
            await bot.send_message(
                config.GROUPE_MODERATION,
                "⚠️ <b>Profil très bloqué</b>\n\n"
                f"<b>{nom_cible}</b> (id <code>{cible_id}</code>) a été bloqué·e par <b>{nb}</b> personnes.\n"
                "<i>Ce profil mérite peut-être votre attention.</i>",
            )
        except Exception:
            pass


async def bannir_si_trop_signale(bot, cible_id):
    nb = compter_signalements_recus(cible_id)
    if nb >= config.SEUIL_BANNISSEMENT and not est_banni(cible_id):
        bannir(cible_id)
        cible = get_profil(cible_id)
        nom_cible = cible["prenom"] if cible else cible_id
        try:
            await bot.send_message(
                config.GROUPE_MODERATION,
                "⛔️ <b>Bannissement automatique</b>\n\n"
                f"<b>{nom_cible}</b> (id <code>{cible_id}</code>) a été signalé·e par "
                f"<b>{nb}</b> personnes différentes.\n"
                "Le profil est désormais <b>banni</b> et invisible pour tous.\n\n"
                "<i>Vérifiez et confirmez si nécessaire.</i>",
            )
        except Exception:
            pass


def genre_vers_recherche(genre):
    if genre == "Homme":
        return "Hommes"
    if genre == "Femme":
        return "Femmes"
    return "Autre"


def correspond(moi, autre):
    ma_recherche_ok = (
        moi["recherche"] == "Tout le monde"
        or genre_vers_recherche(autre["genre"]) == moi["recherche"]
    )
    sa_recherche_ok = (
        autre["recherche"] == "Tout le monde"
        or genre_vers_recherche(moi["genre"]) == autre["recherche"]
    )
    if not (ma_recherche_ok and sa_recherche_ok):
        return False

    filtres = moi.get("filtres", {"age_min": 18, "age_max": 99, "distance": 1000})
    if not (filtres["age_min"] <= autre["age"] <= filtres["age_max"]):
        return False

    d = calculer_distance_km(
        moi.get("lat"), moi.get("lon"),
        autre.get("lat"), autre.get("lon"),
    )
    if d is not None:
        if d > filtres["distance"]:
            return False

    return True


def trouver_prochain_profil(user_id):
    moi = get_profil(user_id)
    if not moi:
        return None, None
    profils = charger_profils()
    vus = deja_vus(user_id)
    for uid, autre in profils.items():
        if uid == str(user_id):
            continue
        if uid in vus:
            continue
        if est_bloque(user_id, uid):
            continue
        if autre.get("en_pause"):
            continue
        if autre.get("banni"):
            continue
        if correspond(moi, autre):
            return uid, autre
    return None, None


async def montrer_profil(message, user_id, cible_id, profil):
    lieu = profil.get("ville") or "📍"
    badge_verif = t(user_id, "badge_verifie") if profil.get("verifie") else ""
    badge_new = t(user_id, "badge_nouveau") if est_nouveau(profil) else ""
    legende = (
        f"{badge_verif}{badge_new}"
        f"✨ <b>{profil['prenom']}</b>, {profil['age']}\n"
        f"🌍 {lieu}\n\n"
        f"💬 <i>{profil['bio']}</i>"
    )
    medias = profil.get("medias", [])
    ids = []

    if len(medias) == 0:
        msg = await message.answer_photo(
            config.PLACEHOLDER_URL,
            caption=legende,
            reply_markup=clavier_swipe(user_id, cible_id),
        )
        ids.append(msg.message_id)
        messages_affiches[user_id] = ids
        return

    if len(medias) == 1:
        m = medias[0]
        if m["type"] == "photo":
            msg = await message.answer_photo(m["file_id"])
        else:
            msg = await message.answer_video(m["file_id"])
        ids.append(msg.message_id)
    elif len(medias) > 1:
        album = []
        for m in medias:
            if m["type"] == "photo":
                album.append(InputMediaPhoto(media=m["file_id"]))
            else:
                album.append(InputMediaVideo(media=m["file_id"]))
        envoyes = await message.answer_media_group(album)
        for msg in envoyes:
            ids.append(msg.message_id)

    fiche = await message.answer(legende, reply_markup=clavier_swipe(user_id, cible_id))
    ids.append(fiche.message_id)

    messages_affiches[user_id] = ids


async def envoyer_prochain(message, user_id):
    from database import noter_activite
    noter_activite(user_id)
    if est_en_pause(user_id):
        await message.answer(t(user_id, "profil_en_pause"))
        return
    cible_id, profil = trouver_prochain_profil(user_id)
    if not profil:
        await message.answer(
            t(user_id, "plus_de_profils"),
            reply_markup=menu_profil(user_id),
        )
        return
    await montrer_profil(message, user_id, cible_id, profil)


async def notifier_match(bot, user_a_id, user_b_id):
    profil_a = get_profil(user_a_id)
    profil_b = get_profil(user_b_id)
    if not profil_a or not profil_b:
        return

    bouton_a = InlineKeyboardMarkup(inline_keyboard=[[
        InlineKeyboardButton(text=t(user_a_id, "match_revoir", prenom=profil_b['prenom']), callback_data=f"revoir_{user_b_id}")
    ]])
    bouton_b = InlineKeyboardMarkup(inline_keyboard=[[
        InlineKeyboardButton(text=t(user_b_id, "match_revoir", prenom=profil_a['prenom']), callback_data=f"revoir_{user_a_id}")
    ]])

    texte_pour_a = t(user_a_id, "match_titre", prenom=profil_b['prenom'])
    texte_pour_b = t(user_b_id, "match_titre", prenom=profil_a['prenom'])

    await cascade_coeurs(bot, int(user_a_id))
    await cascade_coeurs(bot, int(user_b_id))

    try:
        await bot.send_message(int(user_a_id), texte_pour_a, reply_markup=bouton_a)
    except Exception:
        pass
    try:
        await bot.send_message(int(user_b_id), texte_pour_b, reply_markup=bouton_b)
    except Exception:
        pass


# ---------- Lancer la découverte ----------
@router.message(Command("decouvrir"))
async def cmd_decouvrir(message: Message):
    await envoyer_prochain(message, message.from_user.id)


@router.callback_query(F.data == "decouvrir")
async def cb_decouvrir(callback: CallbackQuery):
    await callback.answer()
    await envoyer_prochain(callback.message, callback.from_user.id)


# ---------- Passer ----------
@router.callback_query(F.data.startswith("pass_"))
async def passer(callback: CallbackQuery):
    cible_id = callback.data.replace("pass_", "")
    user_id = callback.from_user.id
    enregistrer_action(user_id, cible_id, "pass")
    await callback.answer()
    await supprimer_anciens(callback.bot, user_id, callback.message.chat.id)
    await envoyer_prochain(callback.message, user_id)


# ---------- J'aime ----------
@router.callback_query(F.data.startswith("like_"))
async def aimer(callback: CallbackQuery):
    cible_id = callback.data.replace("like_", "")
    user_id = callback.from_user.id

    restants = likes_restants(user_id, config.LIKES_PAR_JOUR, config.LIKES_PAR_JOUR_VERIFIE)
    if restants <= 0:
        await callback.answer()
        await callback.message.answer(
            t(user_id, "limite_likes"),
            reply_markup=menu_profil(user_id),
        )
        return

    consommer_like(user_id)
    enregistrer_action(user_id, cible_id, "like")
    await callback.answer()

    if not a_like(cible_id, user_id):
        try:
            stats = stats_utilisateur(cible_id)
            if stats["likes_recus"] == 1:
                await callback.bot.send_message(
                    int(cible_id),
                    t(cible_id, "like_recu"),
                )
        except Exception:
            pass

    if a_like(cible_id, user_id):
        enregistrer_match(user_id, cible_id)
        await notifier_match(callback.bot, user_id, cible_id)

    await supprimer_anciens(callback.bot, user_id, callback.message.chat.id)
    await flash_emoji(callback.message, "❤️")
    await envoyer_prochain(callback.message, user_id)


# ---------- Signaler ----------
@router.callback_query(F.data.startswith("report_"))
async def signaler(callback: CallbackQuery):
    cible_id = callback.data.replace("report_", "")
    user_id = callback.from_user.id

    enregistrer_report(user_id, cible_id)
    bloquer(user_id, cible_id)
    enregistrer_action(user_id, cible_id, "pass")

    await callback.answer(t(user_id, "signalement_envoye"), show_alert=True)

    signaleur = get_profil(user_id)
    cible = get_profil(cible_id)
    nom_signaleur = signaleur["prenom"] if signaleur else user_id
    nom_cible = cible["prenom"] if cible else cible_id
    try:
        await callback.bot.send_message(
            config.GROUPE_MODERATION,
            "🚨 <b>Nouveau signalement</b>\n\n"
            f"Signalé par : <b>{nom_signaleur}</b> (id <code>{user_id}</code>)\n"
            f"Profil visé : <b>{nom_cible}</b> (id <code>{cible_id}</code>)",
        )
    except Exception:
        pass

    await bannir_si_trop_signale(callback.bot, cible_id)

    await callback.message.answer(t(user_id, "profil_plus_montre"))
    await supprimer_anciens(callback.bot, user_id, callback.message.chat.id)
    await envoyer_prochain(callback.message, user_id)


# ---------- Bloquer ----------
@router.callback_query(F.data.startswith("block_"))
async def bloquer_profil(callback: CallbackQuery):
    cible_id = callback.data.replace("block_", "")
    user_id = callback.from_user.id

    bloquer(user_id, cible_id)
    enregistrer_action(user_id, cible_id, "pass")

    await callback.answer(t(user_id, "profil_bloque_alert"), show_alert=True)

    await alerter_si_tres_bloque(callback.bot, cible_id)

    await callback.message.answer(t(user_id, "profil_bloque_msg"))
    await supprimer_anciens(callback.bot, user_id, callback.message.chat.id)
    await envoyer_prochain(callback.message, user_id)


# ---------- Arrêter la découverte ----------
@router.callback_query(F.data == "stop_decouverte")
async def stop(callback: CallbackQuery):
    user_id = callback.from_user.id
    await callback.answer()
    await supprimer_anciens(callback.bot, user_id, callback.message.chat.id)
    await callback.message.answer(t(user_id, "petite_pause"), reply_markup=menu_profil(user_id))


# ---------- Revoir le profil d'un match ----------
@router.callback_query(F.data.startswith("revoir_"))
async def revoir_profil(callback: CallbackQuery):
    cible_id = callback.data.replace("revoir_", "")
    user_id = callback.from_user.id
    profil = get_profil(cible_id)
    await callback.answer()
    if not profil:
        await callback.message.answer(t(user_id, "profil_indispo"))
        return

    lieu = profil.get("ville") or "📍"
    badge_verif = t(user_id, "badge_verifie") if profil.get("verifie") else ""
    badge_new = t(user_id, "badge_nouveau") if est_nouveau(profil) else ""
    legende = (
        f"{badge_verif}{badge_new}"
        f"✨ <b>{profil['prenom']}</b>, {profil['age']}\n"
        f"🌍 {lieu}\n\n"
        f"💬 <i>{profil['bio']}</i>"
    )
    medias = profil.get("medias", [])

    if len(medias) == 0:
        await callback.message.answer_photo(config.PLACEHOLDER_URL, caption=legende)
    elif len(medias) == 1:
        m = medias[0]
        if m["type"] == "photo":
            await callback.message.answer_photo(m["file_id"], caption=legende)
        else:
            await callback.message.answer_video(m["file_id"], caption=legende)
    else:
        album = []
        for i, m in enumerate(medias):
            cap = legende if i == 0 else None
            if m["type"] == "photo":
                album.append(InputMediaPhoto(media=m["file_id"], caption=cap))
            else:
                album.append(InputMediaVideo(media=m["file_id"], caption=cap))
        await callback.message.answer_media_group(album)