from aiogram import Router, F
from aiogram.types import (
    Message,
    CallbackQuery,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    ReplyKeyboardMarkup,
    KeyboardButton,
    ReplyKeyboardRemove,
)
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

import config
from states import Discussion
from traductions import t
from database import (
    get_profil,
    get_matches,
    sont_matchs,
    bloquer,
    est_bloque,
    enregistrer_report,
    compter_blocages_recus,
    compter_signalements_recus,
    bannir,
    est_banni,
)

router = Router()


def clavier_quitter(user_id):
    return ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text=t(user_id, "btn_quitter_conv"))]],
        resize_keyboard=True,
    )


def bouton_repondre(expediteur_id, dest_id):
    return InlineKeyboardMarkup(inline_keyboard=[[
        InlineKeyboardButton(text=t(dest_id, "btn_repondre"), callback_data=f"chat_{expediteur_id}")
    ]])


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


# ---------- Voir la liste de mes matchs ----------
@router.message(Command("matchs"))
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

    boutons = []
    for mid in matchs:
        profil = get_profil(mid)
        if profil:
            boutons.append([InlineKeyboardButton(
                text=f"💬 {profil['prenom']}",
                callback_data=f"chat_{mid}",
            )])
    clavier = InlineKeyboardMarkup(inline_keyboard=boutons)
    await message.answer(t(user_id, "tes_matchs"), reply_markup=clavier)


# ---------- Ouvrir une conversation ----------
@router.callback_query(F.data.startswith("chat_"))
async def ouvrir_chat(callback: CallbackQuery, state: FSMContext):
    cible_id = callback.data.replace("chat_", "")
    user_id = callback.from_user.id
    await callback.answer()

    if est_bloque(user_id, cible_id):
        await callback.message.answer(t(user_id, "conv_indispo"))
        return
    if not sont_matchs(user_id, cible_id):
        await callback.message.answer(t(user_id, "plus_en_match"))
        return

    profil = get_profil(cible_id)
    await state.update_data(cible_id=cible_id)
    await state.set_state(Discussion.en_chat)

    moderation = InlineKeyboardMarkup(inline_keyboard=[[
        InlineKeyboardButton(text="🚩 Signaler", callback_data=f"report_chat_{cible_id}"),
        InlineKeyboardButton(text="🚫 Bloquer", callback_data=f"block_chat_{cible_id}"),
    ]])

    await callback.message.answer(
        t(user_id, "conv_ouverte", prenom=profil['prenom']),
        reply_markup=clavier_quitter(user_id),
    )
    await callback.message.answer(t(user_id, "souci_personne"), reply_markup=moderation)


# ---------- Signaler depuis la conversation ----------
@router.callback_query(F.data.startswith("report_chat_"))
async def signaler_chat(callback: CallbackQuery, state: FSMContext):
    cible_id = callback.data.replace("report_chat_", "")
    user_id = callback.from_user.id

    enregistrer_report(user_id, cible_id)
    bloquer(user_id, cible_id)
    await state.clear()

    await callback.answer(t(user_id, "signalement_envoye"), show_alert=True)

    signaleur = get_profil(user_id)
    cible = get_profil(cible_id)
    nom_signaleur = signaleur["prenom"] if signaleur else user_id
    nom_cible = cible["prenom"] if cible else cible_id
    try:
        await callback.bot.send_message(
            config.GROUPE_MODERATION,
            "🚨 <b>Nouveau signalement (conversation)</b>\n\n"
            f"Signalé par : <b>{nom_signaleur}</b> (id <code>{user_id}</code>)\n"
            f"Profil visé : <b>{nom_cible}</b> (id <code>{cible_id}</code>)",
        )
    except Exception:
        pass

    await bannir_si_trop_signale(callback.bot, cible_id)

    await callback.message.answer(
        t(user_id, "signalement_conv_bloque"),
        reply_markup=ReplyKeyboardRemove(),
    )


# ---------- Bloquer depuis la conversation ----------
@router.callback_query(F.data.startswith("block_chat_"))
async def bloquer_chat(callback: CallbackQuery, state: FSMContext):
    cible_id = callback.data.replace("block_chat_", "")
    user_id = callback.from_user.id

    bloquer(user_id, cible_id)
    await state.clear()

    await callback.answer(t(user_id, "profil_bloque_alert"), show_alert=True)

    await alerter_si_tres_bloque(callback.bot, cible_id)

    await callback.message.answer(
        t(user_id, "personne_bloquee"),
        reply_markup=ReplyKeyboardRemove(),
    )


# ---------- Quitter la conversation ----------
@router.message(Discussion.en_chat, F.text.contains("🚪"))
async def quitter_chat(message: Message, state: FSMContext):
    await state.clear()
    await message.answer(
        t(message.from_user.id, "conv_fermee"),
        reply_markup=ReplyKeyboardRemove(),
    )


# ---------- Relais des messages texte ----------
@router.message(Discussion.en_chat, F.text)
async def relais_texte(message: Message, state: FSMContext):
    data = await state.get_data()
    cible_id = data.get("cible_id")
    user_id = message.from_user.id
    moi = get_profil(user_id)

    if est_bloque(user_id, cible_id) or not sont_matchs(user_id, cible_id):
        await message.answer(t(user_id, "conv_indispo"), reply_markup=ReplyKeyboardRemove())
        await state.clear()
        return

    try:
        await message.bot.send_message(
            int(cible_id),
            t(cible_id, "msg_relais", prenom=moi['prenom'], texte=message.text),
            reply_markup=bouton_repondre(user_id, cible_id),
        )
    except Exception:
        await message.answer(t(user_id, "msg_non_envoye"))


# ---------- Relais des photos ----------
@router.message(Discussion.en_chat, F.photo)
async def relais_photo(message: Message, state: FSMContext):
    data = await state.get_data()
    cible_id = data.get("cible_id")
    user_id = message.from_user.id
    moi = get_profil(user_id)

    if est_bloque(user_id, cible_id) or not sont_matchs(user_id, cible_id):
        await message.answer(t(user_id, "conv_indispo"), reply_markup=ReplyKeyboardRemove())
        await state.clear()
        return

    try:
        await message.bot.send_photo(
            int(cible_id),
            message.photo[-1].file_id,
            caption=t(cible_id, "photo_relais", prenom=moi['prenom']),
            reply_markup=bouton_repondre(user_id, cible_id),
        )
    except Exception:
        await message.answer(t(user_id, "photo_non_envoyee"))