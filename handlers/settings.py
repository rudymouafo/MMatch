from aiogram import Router, F
from aiogram.types import (
    Message,
    CallbackQuery,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    ReplyKeyboardRemove,
)
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

import config
from states import Filtres, ChangementLangue, Navigation, Verification
from traductions import t
from database import (
    get_profil,
    get_filtres,
    set_filtres,
    mettre_en_pause,
    est_en_pause,
    supprimer_compte,
    est_verifie,
    set_langue,
)
from keyboards import menu_principal, menu_parametres, clavier_langue

router = Router()


# ====================================================
#   OUVRIR LE MENU PARAMÈTRES
# ====================================================
async def ouvrir_menu_parametres(message, user_id, state):
    await message.answer(
        t(user_id, "parametres_ouvre"),
        reply_markup=menu_parametres(user_id, est_en_pause(user_id), est_verifie(user_id)),
    )
    await state.set_state(Navigation.menu_parametres)


@router.message(Command("parametres"))
async def cmd_parametres(message: Message, state: FSMContext):
    await ouvrir_menu_parametres(message, message.from_user.id, state)


# ====================================================
#   MENU PARAMÈTRES : boutons reconnus par icône
# ====================================================

# ---------- 🎯 Filtres ----------
@router.message(Navigation.menu_parametres, F.text.contains("🎯"))
async def bouton_filtres(message: Message, state: FSMContext):
    await demarrer_reglage(message, message.from_user.id, state)


@router.message(Command("filters"))
async def cmd_filtres(message: Message, state: FSMContext):
    await demarrer_reglage(message, message.from_user.id, state)


# ---------- 🗣️ Langue ----------
@router.message(Navigation.menu_parametres, F.text.contains("🗣️"))
async def bouton_langue(message: Message, state: FSMContext):
    await message.answer(
        t(message.from_user.id, "changer_langue"),
        reply_markup=clavier_langue,
    )
    await state.set_state(ChangementLangue.choix)


# ---------- 🛡️ Vérifier ----------
@router.message(Navigation.menu_parametres, F.text.contains("🛡️"))
async def bouton_verifier(message: Message, state: FSMContext):
    user_id = message.from_user.id
    if est_verifie(user_id):
        await message.answer(t(user_id, "deja_verifie"))
        return
    await message.answer(t(user_id, "verif_explication"))
    await state.set_state(Verification.selfie)


# ---------- ✅ Déjà vérifié (juste un message) ----------
@router.message(Navigation.menu_parametres, F.text.contains("✅"))
async def bouton_deja_verifie(message: Message):
    await message.answer(t(message.from_user.id, "deja_verifie"))


# ---------- ⏸️ / ▶️ Pause ----------
@router.message(Navigation.menu_parametres, F.text.contains("⏸️"))
async def bouton_pause_on(message: Message, state: FSMContext):
    await basculer_pause(message, message.from_user.id, state)


@router.message(Navigation.menu_parametres, F.text.contains("▶️"))
async def bouton_pause_off(message: Message, state: FSMContext):
    await basculer_pause(message, message.from_user.id, state)


async def basculer_pause(message, user_id, state):
    profil = get_profil(user_id)
    if not profil:
        await message.answer(t(user_id, "pas_de_profil"))
        return
    if est_en_pause(user_id):
        mettre_en_pause(user_id, False)
        await message.answer(
            t(user_id, "pause_activee"),
            reply_markup=menu_parametres(user_id, False, est_verifie(user_id)),
        )
    else:
        mettre_en_pause(user_id, True)
        await message.answer(
            t(user_id, "pause_misee"),
            reply_markup=menu_parametres(user_id, True, est_verifie(user_id)),
        )
    await state.set_state(Navigation.menu_parametres)


# ---------- 🗑️ Supprimer ----------
@router.message(Navigation.menu_parametres, F.text.contains("🗑️"))
async def bouton_supprimer(message: Message):
    uid = message.from_user.id
    confirmation = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=t(uid, "btn_supprimer_oui"), callback_data="supprimer_confirme")],
        [InlineKeyboardButton(text=t(uid, "btn_supprimer_non"), callback_data="supprimer_annule")],
    ])
    await message.answer(t(uid, "supprimer_demande"), reply_markup=confirmation)


# ---------- 🔙 Retour (paramètres → menu principal) ----------
@router.message(Navigation.menu_parametres, F.text.contains("🔙"))
async def retour_depuis_parametres(message: Message, state: FSMContext):
    await state.clear()
    await message.answer(
        t(message.from_user.id, "voici_ton_menu"),
        reply_markup=menu_principal(message.from_user.id),
    )


# ====================================================
#   RÉGLAGE DES FILTRES
# ====================================================
async def demarrer_reglage(message, user_id, state):
    filtres = get_filtres(user_id)
    if filtres is None:
        await message.answer(t(user_id, "pas_de_profil"))
        return
    await message.answer(
        t(user_id, "filtres_actuels",
          age_min=filtres['age_min'], age_max=filtres['age_max'], distance=filtres['distance']),
        reply_markup=ReplyKeyboardRemove(),
    )
    await state.set_state(Filtres.age_min)


@router.message(Filtres.age_min)
async def regler_age_min(message: Message, state: FSMContext):
    uid = message.from_user.id
    if not message.text:
        await message.answer(t(uid, "nombre_simple", ex=20))
        return
    texte = message.text.strip()
    if not texte.isdigit():
        await message.answer(t(uid, "nombre_simple", ex=20))
        return
    age_min = int(texte)
    if age_min < 18:
        await message.answer(t(uid, "age_min_18"))
        return
    if age_min > 99:
        await message.answer(t(uid, "age_trop_eleve"))
        return
    await state.update_data(age_min=age_min)
    await message.answer(t(uid, "demande_age_max", min=age_min))
    await state.set_state(Filtres.age_max)


@router.message(Filtres.age_max)
async def regler_age_max(message: Message, state: FSMContext):
    uid = message.from_user.id
    if not message.text:
        await message.answer(t(uid, "nombre_simple", ex=35))
        return
    texte = message.text.strip()
    if not texte.isdigit():
        await message.answer(t(uid, "nombre_simple", ex=35))
        return
    age_max = int(texte)
    data = await state.get_data()
    age_min = data["age_min"]
    if age_max < age_min:
        await message.answer(t(uid, "age_max_trop_bas", min=age_min))
        return
    if age_max > 99:
        await message.answer(t(uid, "age_trop_eleve"))
        return
    await state.update_data(age_max=age_max)
    await message.answer(t(uid, "demande_distance"))
    await state.set_state(Filtres.distance)


@router.message(Filtres.distance)
async def regler_distance(message: Message, state: FSMContext):
    uid = message.from_user.id
    if not message.text:
        await message.answer(t(uid, "distance_km"))
        return
    texte = message.text.strip()
    if not texte.isdigit():
        await message.answer(t(uid, "distance_km"))
        return
    distance = int(texte)
    if distance < 1:
        await message.answer(t(uid, "distance_min_1"))
        return
    if distance > 20000:
        distance = 20000

    data = await state.get_data()
    set_filtres(uid, data["age_min"], data["age_max"], distance)

    await message.answer(
        t(uid, "filtres_enregistres",
          age_min=data['age_min'], age_max=data['age_max'], distance=distance),
        reply_markup=menu_principal(uid),
    )
    await state.clear()


# ====================================================
#   CHANGEMENT DE LANGUE
# ====================================================
@router.message(ChangementLangue.choix, F.text.contains("🇫🇷"))
async def langue_fr(message: Message, state: FSMContext):
    await appliquer_langue(message, state, "fr")


@router.message(ChangementLangue.choix, F.text.contains("🇬🇧"))
async def langue_en(message: Message, state: FSMContext):
    await appliquer_langue(message, state, "en")


@router.message(ChangementLangue.choix, F.text.contains("🇷🇺"))
async def langue_ru(message: Message, state: FSMContext):
    await appliquer_langue(message, state, "ru")


async def appliquer_langue(message, state, langue):
    user_id = message.from_user.id
    set_langue(user_id, langue)
    await message.answer(t(user_id, "langue_changee"))
    await ouvrir_menu_parametres(message, user_id, state)


# ====================================================
#   SUPPRESSION DU COMPTE (confirmation inline)
# ====================================================
@router.callback_query(F.data == "supprimer_annule")
async def annuler_suppression(callback: CallbackQuery, state: FSMContext):
    uid = callback.from_user.id
    await callback.answer()
    await callback.message.answer(t(uid, "supprimer_annule"))
    await ouvrir_menu_parametres(callback.message, uid, state)


@router.callback_query(F.data == "supprimer_confirme")
async def confirmer_suppression(callback: CallbackQuery, state: FSMContext):
    user_id = callback.from_user.id
    await callback.answer()
    await state.clear()
    supprimer_compte(user_id)
    await callback.message.answer(
        t(user_id, "supprimer_confirme"),
        reply_markup=ReplyKeyboardRemove(),
    )