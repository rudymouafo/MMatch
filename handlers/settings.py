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
from states import Filtres, ChangementLangue
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
from keyboards import menu_profil, menu_parametres, clavier_langue

router = Router()


# ---------- Ouvrir le menu Paramètres ----------
@router.message(Command("parametres"))
async def cmd_parametres(message: Message):
    uid = message.from_user.id
    await message.answer(
        t(uid, "parametres_ouvre"),
        reply_markup=menu_parametres(uid, est_en_pause(uid), est_verifie(uid)),
    )


# ---------- Afficher les filtres actuels ----------
@router.callback_query(F.data == "filtres")
async def afficher_filtres(callback: CallbackQuery, state: FSMContext):
    await callback.answer()
    await demarrer_reglage(callback.message, callback.from_user.id, state)


@router.message(Command("filters"))
async def cmd_filtres(message: Message, state: FSMContext):
    await demarrer_reglage(message, message.from_user.id, state)


async def demarrer_reglage(message, user_id, state):
    filtres = get_filtres(user_id)
    if filtres is None:
        await message.answer(t(user_id, "pas_de_profil"))
        return

    await message.answer(
        t(user_id, "filtres_actuels",
          age_min=filtres['age_min'], age_max=filtres['age_max'], distance=filtres['distance'])
    )
    await state.set_state(Filtres.age_min)


# ---------- Étape 1 : âge minimum ----------
@router.message(Filtres.age_min)
async def regler_age_min(message: Message, state: FSMContext):
    uid = message.from_user.id
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


# ---------- Étape 2 : âge maximum ----------
@router.message(Filtres.age_max)
async def regler_age_max(message: Message, state: FSMContext):
    uid = message.from_user.id
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


# ---------- Étape 3 : distance ----------
@router.message(Filtres.distance)
async def regler_distance(message: Message, state: FSMContext):
    uid = message.from_user.id
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
    await state.clear()

    await message.answer(
        t(uid, "filtres_enregistres",
          age_min=data['age_min'], age_max=data['age_max'], distance=distance),
        reply_markup=menu_profil(uid),
    )


# ====================================================
#   CHANGEMENT DE LANGUE
# ====================================================
@router.callback_query(F.data == "changer_langue")
async def demander_langue(callback: CallbackQuery, state: FSMContext):
    await callback.answer()
    await callback.message.answer(
        t(callback.from_user.id, "changer_langue"),
        reply_markup=clavier_langue,
    )
    await state.set_state(ChangementLangue.choix)


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
    await state.clear()
    await message.answer(
        t(user_id, "langue_changee"),
        reply_markup=ReplyKeyboardRemove(),
    )
    await message.answer(
        t(user_id, "parametres_ouvre"),
        reply_markup=menu_parametres(user_id, est_en_pause(user_id), est_verifie(user_id)),
    )


# ====================================================
#   PAUSE DU PROFIL
# ====================================================
@router.callback_query(F.data == "pause")
async def basculer_pause(callback: CallbackQuery):
    user_id = callback.from_user.id
    profil = get_profil(user_id)
    await callback.answer()
    if not profil:
        await callback.message.answer(t(user_id, "pas_de_profil"))
        return

    if est_en_pause(user_id):
        mettre_en_pause(user_id, False)
        await callback.message.answer(
            t(user_id, "pause_activee"),
            reply_markup=menu_parametres(user_id, False, est_verifie(user_id)),
        )
    else:
        mettre_en_pause(user_id, True)
        await callback.message.answer(
            t(user_id, "pause_misee"),
            reply_markup=menu_parametres(user_id, True, est_verifie(user_id)),
        )


# ====================================================
#   SUPPRESSION DU COMPTE
# ====================================================
@router.callback_query(F.data == "supprimer")
async def demander_suppression(callback: CallbackQuery):
    uid = callback.from_user.id
    await callback.answer()
    confirmation = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=t(uid, "btn_supprimer_oui"), callback_data="supprimer_confirme")],
        [InlineKeyboardButton(text=t(uid, "btn_supprimer_non"), callback_data="supprimer_annule")],
    ])
    await callback.message.answer(t(uid, "supprimer_demande"), reply_markup=confirmation)


@router.callback_query(F.data == "supprimer_annule")
async def annuler_suppression(callback: CallbackQuery):
    uid = callback.from_user.id
    await callback.answer()
    await callback.message.answer(
        t(uid, "supprimer_annule"),
        reply_markup=menu_parametres(uid, est_en_pause(uid), est_verifie(uid)),
    )


@router.callback_query(F.data == "supprimer_confirme")
async def confirmer_suppression(callback: CallbackQuery):
    user_id = callback.from_user.id
    await callback.answer()
    supprimer_compte(user_id)
    await callback.message.answer(
        t(user_id, "supprimer_confirme"),
        reply_markup=ReplyKeyboardRemove(),
    )