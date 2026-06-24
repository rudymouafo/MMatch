from aiogram import Router, F
from aiogram.types import (
    Message,
    CallbackQuery,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

import config
from states import Verification
from traductions import t
from database import get_profil, est_verifie, set_verifie

router = Router()


# ---------- Lancer la vérification ----------
@router.callback_query(F.data == "verifier")
async def demarrer_verification(callback: CallbackQuery, state: FSMContext):
    user_id = callback.from_user.id
    await callback.answer()

    if est_verifie(user_id):
        await callback.message.answer(t(user_id, "deja_verifie"))
        return

    await callback.message.answer(t(user_id, "verif_explication"))
    await state.set_state(Verification.selfie)


@router.message(Command("verifier"))
async def cmd_verification(message: Message, state: FSMContext):
    user_id = message.from_user.id
    if est_verifie(user_id):
        await message.answer(t(user_id, "deja_verifie"))
        return
    await message.answer(t(user_id, "verif_explication"))
    await state.set_state(Verification.selfie)


# ---------- Réception du selfie ----------
@router.message(Verification.selfie, F.photo)
async def recevoir_selfie(message: Message, state: FSMContext):
    user_id = message.from_user.id
    profil = get_profil(user_id)
    await state.clear()

    # Boutons de décision pour le groupe de modération
    decision = InlineKeyboardMarkup(inline_keyboard=[[
        InlineKeyboardButton(text="✅ Valider", callback_data=f"verif_ok_{user_id}"),
        InlineKeyboardButton(text="❌ Rejeter", callback_data=f"verif_no_{user_id}"),
    ]])

    nom = profil["prenom"] if profil else user_id
    try:
        await message.bot.send_photo(
            config.GROUPE_MODERATION,
            message.photo[-1].file_id,
            caption=(
                "🪪 <b>Demande de vérification</b>\n\n"
                f"Profil : <b>{nom}</b> (id <code>{user_id}</code>)\n"
                "<i>Vérifiez que le selfie correspond aux photos du profil.</i>"
            ),
            reply_markup=decision,
        )
    except Exception:
        pass

    await message.answer(t(user_id, "verif_recue"))


@router.message(Verification.selfie)
async def selfie_pas_photo(message: Message):
    await message.answer(t(message.from_user.id, "verif_pas_photo"))


# ---------- Décision de l'admin : valider ----------
@router.callback_query(F.data.startswith("verif_ok_"))
async def valider_verification(callback: CallbackQuery):
    cible_id = callback.data.replace("verif_ok_", "")
    set_verifie(cible_id, True)
    await callback.answer("Profil validé ✅", show_alert=True)

    try:
        await callback.message.edit_caption(
            (callback.message.caption or "") + "\n\n✅ <b>VALIDÉ</b>",
        )
    except Exception:
        pass

    try:
        await callback.bot.send_message(int(cible_id), t(cible_id, "verif_validee"))
    except Exception:
        pass


# ---------- Décision de l'admin : rejeter ----------
@router.callback_query(F.data.startswith("verif_no_"))
async def rejeter_verification(callback: CallbackQuery):
    cible_id = callback.data.replace("verif_no_", "")
    await callback.answer("Profil rejeté ❌", show_alert=True)

    try:
        await callback.message.edit_caption(
            (callback.message.caption or "") + "\n\n❌ <b>REJETÉ</b>",
        )
    except Exception:
        pass

    try:
        await callback.bot.send_message(int(cible_id), t(cible_id, "verif_refusee"))
    except Exception:
        pass