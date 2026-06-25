from aiogram import Router, F
from aiogram.types import (
    Message,
    CallbackQuery,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)
from aiogram.filters import Command

import config
from traductions import t
from database import get_profil, get_matches, est_bloque

router = Router()


async def envoyer_contact_match(bot, destinataire_id, profil_autre):
    """Envoie la carte de contact d'un match."""
    prenom = profil_autre.get("prenom", "")
    username = profil_autre.get("username")
    telephone = profil_autre.get("telephone")

    if telephone:
        vcard = None
        if username:
            vcard = (
                "BEGIN:VCARD\n"
                "VERSION:3.0\n"
                f"FN:{prenom}\n"
                f"TEL;TYPE=CELL:{telephone}\n"
                f"X-TELEGRAM:@{username}\n"
                "END:VCARD"
            )
        await bot.send_contact(
            int(destinataire_id),
            phone_number=telephone,
            first_name=prenom,
            vcard=vcard,
        )
    elif username:
        await bot.send_message(
            int(destinataire_id),
            t(destinataire_id, "contact_username", prenom=prenom, username=username),
        )


# ---------- Voir la liste de mes matchs ----------
@router.message(Command("matches"))
async def cmd_matchs(message: Message):
    await afficher_matchs(message, message.from_user.id)


@router.callback_query(F.data == "mes_matchs")
async def cb_matchs(callback: CallbackQuery):
    await callback.answer()
    await afficher_matchs(callback.message, callback.from_user.id)


async def afficher_matchs(message, user_id):
    matchs = get_matches(user_id)
    matchs = [mid for mid in matchs if not est_bloque(user_id, mid)]
    if not matchs:
        await message.answer(t(user_id, "pas_de_match"))
        return

    await message.answer(t(user_id, "tes_matchs"))

    for mid in matchs:
        profil = get_profil(mid)
        if not profil:
            continue
        # Petite fiche + bouton pour récupérer le contact
        bouton = InlineKeyboardMarkup(inline_keyboard=[[
            InlineKeyboardButton(
                text=t(user_id, "btn_voir_contact", prenom=profil['prenom']),
                callback_data=f"contact_{mid}",
            )
        ]])
        await message.answer(
            f"💞 <b>{profil['prenom']}</b>, {profil.get('age', '')}",
            reply_markup=bouton,
        )


# ---------- Récupérer le contact d'un match ----------
@router.callback_query(F.data.startswith("contact_"))
async def donner_contact(callback: CallbackQuery):
    cible_id = callback.data.replace("contact_", "")
    user_id = callback.from_user.id
    await callback.answer()

    if est_bloque(user_id, cible_id):
        await callback.message.answer(t(user_id, "conv_indispo"))
        return

    profil = get_profil(cible_id)
    if not profil:
        await callback.message.answer(t(user_id, "profil_indispo"))
        return

    await envoyer_contact_match(callback.bot, user_id, profil)