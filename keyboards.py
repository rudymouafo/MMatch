from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)


# ====================================================
#   CLAVIERS DE L'INSCRIPTION (traduits)
# ====================================================

def clavier_genre(user_id):
    from traductions import t
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text=t(user_id, "btn_homme")),
             KeyboardButton(text=t(user_id, "btn_femme")),
             KeyboardButton(text=t(user_id, "btn_autre"))],
            [KeyboardButton(text=t(user_id, "btn_precedent"))],
        ],
        resize_keyboard=True,
    )


def clavier_recherche(user_id):
    from traductions import t
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text=t(user_id, "btn_rech_hommes")),
             KeyboardButton(text=t(user_id, "btn_rech_femmes"))],
            [KeyboardButton(text=t(user_id, "btn_rech_tous"))],
            [KeyboardButton(text=t(user_id, "btn_precedent"))],
        ],
        resize_keyboard=True,
    )


def clavier_localisation(user_id):
    from traductions import t
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text=t(user_id, "btn_position"), request_location=True)],
            [KeyboardButton(text=t(user_id, "btn_precedent"))],
        ],
        resize_keyboard=True,
    )


def clavier_precedent(user_id):
    from traductions import t
    return ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text=t(user_id, "btn_precedent"))]],
        resize_keyboard=True,
    )


def clavier_medias(user_id):
    from traductions import t
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text=t(user_id, "btn_termine"))],
            [KeyboardButton(text=t(user_id, "btn_precedent"))],
        ],
        resize_keyboard=True,
    )


def clavier_medias_fini(user_id):
    from traductions import t
    return ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text=t(user_id, "btn_termine"))]],
        resize_keyboard=True,
    )


def clavier_telephone(user_id):
    from traductions import t
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text=t(user_id, "btn_partager_numero"), request_contact=True)],
            [KeyboardButton(text=t(user_id, "btn_precedent"))],
        ],
        resize_keyboard=True,
    )


# ---------- Choix de la langue (boutons du bas) ----------
clavier_langue = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🇫🇷 Français")],
        [KeyboardButton(text="🇬🇧 English")],
        [KeyboardButton(text="🇷🇺 Русский")],
    ],
    resize_keyboard=True,
)


def clavier_cgu_trad(txt_accepte, txt_refuse):
    """Clavier CGU avec boutons du bas (textes traduits)."""
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text=txt_accepte)],
            [KeyboardButton(text=txt_refuse)],
        ],
        resize_keyboard=True,
    )


# ====================================================
#   MENU PERMANENT (toujours visible en bas)
# ====================================================
def menu_principal(user_id):
    from traductions import t
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text=t(user_id, "menu_decouvrir")), KeyboardButton(text=t(user_id, "menu_matchs"))],
            [KeyboardButton(text=t(user_id, "menu_profil")), KeyboardButton(text=t(user_id, "menu_parametres"))],
        ],
        resize_keyboard=True,
        is_persistent=True,
    )


# ====================================================
#   MENU PROFIL (clavier du bas)
# ====================================================
def menu_profil(user_id):
    from traductions import t
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text=t(user_id, "btn_voir_profil"))],
            [KeyboardButton(text=t(user_id, "btn_mes_stats"))],
            [KeyboardButton(text=t(user_id, "btn_modifier_profil"))],
            [KeyboardButton(text=t(user_id, "btn_retour"))],
        ],
        resize_keyboard=True,
    )


# ====================================================
#   MENU MODIFIER (clavier du bas)
# ====================================================
def menu_modifier(user_id):
    from traductions import t
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text=t(user_id, "btn_edit_prenom")),
             KeyboardButton(text=t(user_id, "btn_edit_age"))],
            [KeyboardButton(text=t(user_id, "btn_edit_genre")),
             KeyboardButton(text=t(user_id, "btn_edit_recherche"))],
            [KeyboardButton(text=t(user_id, "btn_edit_localisation")),
             KeyboardButton(text=t(user_id, "btn_edit_bio"))],
            [KeyboardButton(text=t(user_id, "btn_edit_medias"))],
            [KeyboardButton(text=t(user_id, "btn_retour"))],
        ],
        resize_keyboard=True,
    )


# ====================================================
#   MENU PARAMÈTRES (clavier du bas, s'adapte à pause + vérifié)
# ====================================================
def menu_parametres(user_id, en_pause=False, verifie=False):
    from traductions import t
    if en_pause:
        bouton_pause = KeyboardButton(text=t(user_id, "btn_pause_off"))
    else:
        bouton_pause = KeyboardButton(text=t(user_id, "btn_pause_on"))

    if verifie:
        bouton_verif = KeyboardButton(text=t(user_id, "btn_deja_verifie"))
    else:
        bouton_verif = KeyboardButton(text=t(user_id, "btn_verifier"))

    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text=t(user_id, "btn_filtres"))],
            [KeyboardButton(text=t(user_id, "btn_langue"))],
            [bouton_verif],
            [bouton_pause],
            [KeyboardButton(text=t(user_id, "btn_supprimer"))],
            [KeyboardButton(text=t(user_id, "btn_retour"))],
        ],
        resize_keyboard=True,
    )


# ====================================================
#   CHOIX GENRE / RECHERCHE (inline, pour modification)
# ====================================================
def inline_genre(user_id):
    from traductions import t
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=t(user_id, "ig_homme"), callback_data="set_genre_Homme"),
         InlineKeyboardButton(text=t(user_id, "ig_femme"), callback_data="set_genre_Femme"),
         InlineKeyboardButton(text=t(user_id, "ig_autre"), callback_data="set_genre_Autre")],
    ])


def inline_recherche(user_id):
    from traductions import t
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=t(user_id, "ir_hommes"), callback_data="set_recherche_Hommes"),
         InlineKeyboardButton(text=t(user_id, "ir_femmes"), callback_data="set_recherche_Femmes")],
        [InlineKeyboardButton(text=t(user_id, "ir_tous"), callback_data="set_recherche_Tout le monde")],
    ])


# ====================================================
#   BOUTONS DU SWIPE (découverte) — restent inline
# ====================================================
def clavier_swipe(user_id, cible_id):
    from traductions import t
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=t(user_id, "sw_passer"), callback_data=f"pass_{cible_id}"),
         InlineKeyboardButton(text=t(user_id, "sw_jaime"), callback_data=f"like_{cible_id}")],
        [InlineKeyboardButton(text=t(user_id, "sw_signaler"), callback_data=f"report_{cible_id}"),
         InlineKeyboardButton(text=t(user_id, "sw_bloquer"), callback_data=f"block_{cible_id}")],
        [InlineKeyboardButton(text=t(user_id, "sw_arreter"), callback_data="stop_decouverte")],
    ])