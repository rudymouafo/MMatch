from aiogram import Router, F
from aiogram.types import (
    Message,
    CallbackQuery,
    ReplyKeyboardRemove,
    InputMediaPhoto,
    InputMediaVideo,
)
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

import config
from states import Modification
from traductions import t
from database import get_profil, modifier_champ, stats_utilisateur
from keyboards import (
    menu_profil,
    menu_modifier,
    inline_genre,
    inline_recherche,
    clavier_localisation,
    clavier_medias_fini,
)

router = Router()


# ---------- Construire la fiche d'un profil ----------
def texte_profil(user_id, profil):
    lieu = profil.get("ville") or "📍"
    badge = t(user_id, "badge_verifie") if profil.get("verifie") else ""
    return (
        f"{badge}"
        f"✨ <b>{profil['prenom']}</b>, {profil['age']}\n"
        f"🌍 {lieu}\n"
        f"💫 {profil['genre']} — {profil['recherche']}\n\n"
        f"💬 <i>{profil['bio']}</i>"
    )


# ---------- Afficher le profil (médias + fiche) ----------
async def envoyer_profil(message, user_id, profil, avec_menu=False):
    legende = texte_profil(user_id, profil)
    medias = profil.get("medias", [])
    clavier = menu_modifier(user_id) if avec_menu else None

    if len(medias) == 1:
        m = medias[0]
        if m["type"] == "photo":
            await message.answer_photo(m["file_id"], caption=legende, reply_markup=clavier)
        else:
            await message.answer_video(m["file_id"], caption=legende, reply_markup=clavier)
    elif len(medias) > 1:
        album = []
        for i, m in enumerate(medias):
            cap = legende if i == 0 else None
            if m["type"] == "photo":
                album.append(InputMediaPhoto(media=m["file_id"], caption=cap))
            else:
                album.append(InputMediaVideo(media=m["file_id"], caption=cap))
        await message.answer_media_group(album)
        if avec_menu:
            await message.answer(t(user_id, "retoucher_autre"), reply_markup=menu_modifier(user_id))
    else:
        await message.answer(legende, reply_markup=clavier)


# ---------- Afficher l'aperçu après une modification ----------
async def apercu_apres_modif(message, user_id):
    profil = get_profil(user_id)
    await message.answer(t(user_id, "profil_maj"))
    await envoyer_profil(message, user_id, profil, avec_menu=True)


# ---------- Annuler une modification en cours ----------
@router.message(Command("annuler", "cancel"))
async def annuler_modification(message: Message, state: FSMContext):
    await state.clear()
    await message.answer(t(message.from_user.id, "pas_de_changement"), reply_markup=ReplyKeyboardRemove())
    await message.answer(t(message.from_user.id, "voici_ton_menu"), reply_markup=menu_modifier(message.from_user.id))


# ---------- Commande /profil ou /profile ----------
@router.message(Command("profil", "profile"))
async def commande_profil(message: Message):
    profil = get_profil(message.from_user.id)
    if not profil:
        await message.answer(t(message.from_user.id, "pas_de_profil"))
        return
    await message.answer(
        t(message.from_user.id, "espace_profil", prenom=profil['prenom']),
        reply_markup=menu_profil(message.from_user.id),
    )


# ---------- Bouton : Voir mon profil ----------
@router.callback_query(F.data == "voir_profil")
async def voir_profil(callback: CallbackQuery):
    user_id = callback.from_user.id
    profil = get_profil(user_id)
    await callback.answer()
    if not profil:
        await callback.message.answer(t(user_id, "profil_aucun"))
        return
    await callback.message.answer(t(user_id, "voici_profil"))
    await envoyer_profil(callback.message, user_id, profil)


# ---------- Bouton : Modifier mon profil ----------
@router.callback_query(F.data == "modifier_profil")
async def modifier_profil(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer(
        t(callback.from_user.id, "que_retoucher"),
        reply_markup=menu_modifier(callback.from_user.id),
    )


# ---------- Mes statistiques perso ----------
@router.callback_query(F.data == "mes_stats")
async def mes_stats(callback: CallbackQuery):
    user_id = callback.from_user.id
    await callback.answer()
    profil = get_profil(user_id)
    if not profil:
        await callback.message.answer(t(user_id, "pas_de_profil"))
        return
    stats = stats_utilisateur(user_id)
    statut = t(user_id, "statut_verifie") if profil.get("verifie") else t(user_id, "statut_non_verifie")
    await callback.message.answer(
        t(user_id, "stats_titre", likes=stats['likes_recus'], matchs=stats['matchs'], statut=statut)
    )


# ---------- Bouton : Retour au menu ----------
@router.callback_query(F.data == "retour_menu")
async def retour_menu(callback: CallbackQuery):
    user_id = callback.from_user.id
    profil = get_profil(user_id)
    await callback.answer()
    await callback.message.answer(
        t(user_id, "espace_profil", prenom=profil['prenom']),
        reply_markup=menu_profil(user_id),
    )


# ====================================================
#   MODIFICATION DES CHAMPS
# ====================================================

# ---------- Prénom ----------
@router.callback_query(F.data == "edit_prenom")
async def edit_prenom(callback: CallbackQuery, state: FSMContext):
    await callback.answer()
    await callback.message.answer(t(callback.from_user.id, "demande_nouveau_prenom"))
    await state.set_state(Modification.prenom)


@router.message(Modification.prenom)
async def set_prenom(message: Message, state: FSMContext):
    if not message.text:
        await message.answer(t(message.from_user.id, "prenom_court", min=config.PRENOM_MIN, max=config.PRENOM_MAX))
        return
    prenom = message.text.strip()
    if len(prenom) < config.PRENOM_MIN or len(prenom) > config.PRENOM_MAX:
        await message.answer(t(message.from_user.id, "prenom_court", min=config.PRENOM_MIN, max=config.PRENOM_MAX))
        return
    modifier_champ(message.from_user.id, "prenom", prenom)
    await state.clear()
    await apercu_apres_modif(message, message.from_user.id)


# ---------- Âge ----------
@router.callback_query(F.data == "edit_age")
async def edit_age(callback: CallbackQuery, state: FSMContext):
    await callback.answer()
    await callback.message.answer(t(callback.from_user.id, "demande_nouvel_age"))
    await state.set_state(Modification.age)


@router.message(Modification.age)
async def set_age(message: Message, state: FSMContext):
    if not message.text:
        await message.answer(t(message.from_user.id, "age_chiffres"))
        return
    texte = message.text.strip()
    if not texte.isdigit():
        await message.answer(t(message.from_user.id, "age_chiffres"))
        return
    age = int(texte)
    if age < config.AGE_MIN or age > config.AGE_MAX:
        await message.answer(t(message.from_user.id, "age_surprenant", min=config.AGE_MIN, max=config.AGE_MAX))
        return
    modifier_champ(message.from_user.id, "age", age)
    await state.clear()
    await apercu_apres_modif(message, message.from_user.id)


# ---------- Genre ----------
@router.callback_query(F.data == "edit_genre")
async def edit_genre(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer(t(callback.from_user.id, "demande_nouveau_genre"), reply_markup=inline_genre(callback.from_user.id))


@router.callback_query(F.data.startswith("set_genre_"))
async def set_genre(callback: CallbackQuery):
    valeur = callback.data.replace("set_genre_", "")
    modifier_champ(callback.from_user.id, "genre", valeur)
    await callback.answer(t(callback.from_user.id, "cest_note"))
    await apercu_apres_modif(callback.message, callback.from_user.id)


# ---------- Recherche ----------
@router.callback_query(F.data == "edit_recherche")
async def edit_recherche(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer(t(callback.from_user.id, "demande_nouvelle_recherche"), reply_markup=inline_recherche(callback.from_user.id))


@router.callback_query(F.data.startswith("set_recherche_"))
async def set_recherche(callback: CallbackQuery):
    valeur = callback.data.replace("set_recherche_", "")
    modifier_champ(callback.from_user.id, "recherche", valeur)
    await callback.answer(t(callback.from_user.id, "cest_note"))
    await apercu_apres_modif(callback.message, callback.from_user.id)


# ---------- Localisation (GPS uniquement) ----------
@router.callback_query(F.data == "edit_localisation")
async def edit_localisation(callback: CallbackQuery, state: FSMContext):
    await callback.answer()
    await callback.message.answer(
        t(callback.from_user.id, "demande_nouvelle_loc"),
        reply_markup=clavier_localisation(callback.from_user.id),
    )
    await state.set_state(Modification.localisation)


@router.message(Modification.localisation, F.location)
async def set_localisation_gps(message: Message, state: FSMContext):
    from database import ville_depuis_gps
    lat = message.location.latitude
    lon = message.location.longitude
    ville = ville_depuis_gps(lat, lon)
    modifier_champ(message.from_user.id, "lat", lat)
    modifier_champ(message.from_user.id, "lon", lon)
    modifier_champ(message.from_user.id, "ville", ville)
    await state.clear()
    await message.answer(t(message.from_user.id, "loc_maj"), reply_markup=ReplyKeyboardRemove())
    await apercu_apres_modif(message, message.from_user.id)


@router.message(Modification.localisation, F.text)
async def loc_modif_pas_de_texte(message: Message, state: FSMContext):
    await message.answer(
        t(message.from_user.id, "localisation_gps_obligatoire"),
        reply_markup=clavier_localisation(message.from_user.id),
    )


# ---------- Bio ----------
@router.callback_query(F.data == "edit_bio")
async def edit_bio(callback: CallbackQuery, state: FSMContext):
    await callback.answer()
    await callback.message.answer(t(callback.from_user.id, "demande_nouvelle_bio"))
    await state.set_state(Modification.bio)


@router.message(Modification.bio)
async def set_bio(message: Message, state: FSMContext):
    if not message.text:
        await message.answer(t(message.from_user.id, "demande_nouvelle_bio"))
        return
    bio = message.text.strip()
    if len(bio) > config.BIO_MAX:
        await message.answer(t(message.from_user.id, "bio_trop_longue", max=config.BIO_MAX))
        return
    modifier_champ(message.from_user.id, "bio", bio)
    await state.clear()
    await apercu_apres_modif(message, message.from_user.id)


# ---------- Médias ----------
@router.callback_query(F.data == "edit_medias")
async def edit_medias(callback: CallbackQuery, state: FSMContext):
    await callback.answer()
    await state.update_data(nouveaux_medias=[])
    await callback.message.answer(
        t(callback.from_user.id, "demande_nouveaux_medias", max=config.MEDIAS_MAX),
        reply_markup=clavier_medias_fini(callback.from_user.id),
    )
    await state.set_state(Modification.medias)


@router.message(Modification.medias, F.photo)
async def medias_photo(message: Message, state: FSMContext):
    data = await state.get_data()
    medias = data.get("nouveaux_medias", [])
    if len(medias) >= config.MEDIAS_MAX:
        await message.answer(t(message.from_user.id, "media_max_atteint", max=config.MEDIAS_MAX))
        return
    medias.append({"type": "photo", "file_id": message.photo[-1].file_id})
    await state.update_data(nouveaux_medias=medias)
    await message.answer(t(message.from_user.id, "media_ajoute", n=len(medias), max=config.MEDIAS_MAX))


@router.message(Modification.medias, F.video)
async def medias_video(message: Message, state: FSMContext):
    data = await state.get_data()
    medias = data.get("nouveaux_medias", [])
    if len(medias) >= config.MEDIAS_MAX:
        await message.answer(t(message.from_user.id, "media_max_atteint", max=config.MEDIAS_MAX))
        return
    medias.append({"type": "video", "file_id": message.video.file_id})
    await state.update_data(nouveaux_medias=medias)
    await message.answer(t(message.from_user.id, "media_ajoute_video", n=len(medias), max=config.MEDIAS_MAX))


@router.message(Modification.medias, F.text.contains("✅"))
async def medias_fini(message: Message, state: FSMContext):
    data = await state.get_data()
    medias = data.get("nouveaux_medias", [])
    if len(medias) == 0:
        await message.answer(t(message.from_user.id, "media_min_un"))
        return
    modifier_champ(message.from_user.id, "medias", medias)
    await state.clear()
    await message.answer(t(message.from_user.id, "medias_maj"), reply_markup=ReplyKeyboardRemove())
    await apercu_apres_modif(message, message.from_user.id)