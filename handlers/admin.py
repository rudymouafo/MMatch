from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command

import config
from database import (
    get_profil,
    statistiques,
    bannir,
    debannir,
    est_banni,
)

router = Router()


# ---------- Vérifier si la personne a le droit d'utiliser les commandes admin ----------
async def est_admin(message: Message) -> bool:
    user_id = message.from_user.id

    # 1. C'est l'admin principal (toi) → autorisé partout
    if user_id == config.ADMIN_ID:
        return True

    # 2. C'est dans le groupe de modération, et la personne y est admin
    if message.chat.id == config.GROUPE_MODERATION:
        try:
            membre = await message.bot.get_chat_member(config.GROUPE_MODERATION, user_id)
            if membre.status in ("creator", "administrator"):
                return True
        except Exception:
            pass

    return False


# ---------- /stats ----------
@router.message(Command("stats"))
async def cmd_stats(message: Message):
    if not await est_admin(message):
        return
    s = statistiques()
    await message.answer(
        "📊 <b>Statistiques M_Match</b>\n\n"
        f"👥 Inscrits : <b>{s['total']}</b>\n"
        f"✅ Vérifiés : <b>{s['verifies']}</b>\n"
        f"⏸️ En pause : <b>{s['en_pause']}</b>\n"
        f"⛔️ Bannis : <b>{s['bannis']}</b>\n"
        f"💞 Matchs : <b>{s['matchs']}</b>"
    )


# ---------- /voir <id> ----------
@router.message(Command("voir"))
async def cmd_voir(message: Message):
    if not await est_admin(message):
        return
    parties = message.text.split()
    if len(parties) < 2:
        await message.answer("Usage : <code>/voir &lt;id&gt;</code>")
        return
    cible_id = parties[1]
    profil = get_profil(cible_id)
    if not profil:
        await message.answer("Aucun profil trouvé avec cet identifiant.")
        return

    lieu = profil.get("ville") or "📍 À proximité"
    statut = []
    if profil.get("verifie"):
        statut.append("✅ vérifié")
    if profil.get("en_pause"):
        statut.append("⏸️ en pause")
    if profil.get("banni"):
        statut.append("⛔️ banni")
    statut_txt = ", ".join(statut) if statut else "actif"

    legende = (
        f"👤 <b>{profil['prenom']}</b>, {profil['age']} ans\n"
        f"🌍 {lieu}\n"
        f"💫 {profil['genre']} — recherche : {profil['recherche']}\n"
        f"💬 <i>{profil['bio']}</i>\n\n"
        f"📌 Statut : {statut_txt}\n"
        f"🆔 <code>{cible_id}</code>"
    )

    medias = profil.get("medias", [])
    if medias and medias[0]["type"] == "photo":
        await message.answer_photo(medias[0]["file_id"], caption=legende)
    elif medias and medias[0]["type"] == "video":
        await message.answer_video(medias[0]["file_id"], caption=legende)
    else:
        await message.answer(legende)


# ---------- /bannir <id> ----------
@router.message(Command("bannir"))
async def cmd_bannir(message: Message):
    if not await est_admin(message):
        return
    parties = message.text.split()
    if len(parties) < 2:
        await message.answer("Usage : <code>/bannir &lt;id&gt;</code>")
        return
    cible_id = parties[1]
    profil = get_profil(cible_id)
    if not profil:
        await message.answer("Aucun profil trouvé avec cet identifiant.")
        return

    bannir(cible_id)
    await message.answer(f"⛔️ <b>{profil['prenom']}</b> (id <code>{cible_id}</code>) a été <b>banni</b>.")
    # On prévient l'utilisateur banni
    try:
        await message.bot.send_message(
            int(cible_id),
            "⛔️ Ton profil a été suspendu par la modération de M_Match.\n"
            "Si tu penses qu'il s'agit d'une erreur, contacte le support.",
        )
    except Exception:
        pass


# ---------- /debannir <id> ----------
@router.message(Command("debannir"))
async def cmd_debannir(message: Message):
    if not await est_admin(message):
        return
    parties = message.text.split()
    if len(parties) < 2:
        await message.answer("Usage : <code>/debannir &lt;id&gt;</code>")
        return
    cible_id = parties[1]
    profil = get_profil(cible_id)
    if not profil:
        await message.answer("Aucun profil trouvé avec cet identifiant.")
        return

    debannir(cible_id)
    await message.answer(f"♻️ <b>{profil['prenom']}</b> (id <code>{cible_id}</code>) a été <b>réactivé</b>.")
    try:
        await message.bot.send_message(
            int(cible_id),
            "♻️ Bonne nouvelle ! Ton profil M_Match a été réactivé.\n"
            "Tu peux de nouveau découvrir des profils. 🌸",
        )
    except Exception:
        pass