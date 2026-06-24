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
#   MENUS DU PROFIL (boutons inline)
# ====================================================
def menu_profil(user_id):
    from traductions import t
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=t(user_id, "btn_decouvrir_profils"), callback_data="decouvrir")],
        [InlineKeyboardButton(text=t(user_id, "btn_mes_matchs"), callback_data="mes_matchs")],
        [InlineKeyboardButton(text=t(user_id, "btn_voir_profil"), callback_data="voir_profil")],
        [InlineKeyboardButton(text=t(user_id, "btn_mes_stats"), callback_data="mes_stats")],
        [InlineKeyboardButton(text=t(user_id, "btn_modifier_profil"), callback_data="modifier_profil")],
    ])


def menu_modifier(user_id):
    from traductions import t
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=t(user_id, "btn_edit_prenom"), callback_data="edit_prenom"),
         InlineKeyboardButton(text=t(user_id, "btn_edit_age"), callback_data="edit_age")],
        [InlineKeyboardButton(text=t(user_id, "btn_edit_genre"), callback_data="edit_genre"),
         InlineKeyboardButton(text=t(user_id, "btn_edit_recherche"), callback_data="edit_recherche")],
        [InlineKeyboardButton(text=t(user_id, "btn_edit_localisation"), callback_data="edit_localisation"),
         InlineKeyboardButton(text=t(user_id, "btn_edit_bio"), callback_data="edit_bio")],
        [InlineKeyboardButton(text=t(user_id, "btn_edit_medias"), callback_data="edit_medias")],
        [InlineKeyboardButton(text=t(user_id, "btn_retour"), callback_data="retour_menu")],
    ])


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
#   MENU PARAMÈTRES (s'adapte à pause + vérifié)
# ====================================================
def menu_parametres(user_id, en_pause=False, verifie=False):
    from traductions import t
    if en_pause:
        bouton_pause = InlineKeyboardButton(text=t(user_id, "btn_pause_off"), callback_data="pause")
    else:
        bouton_pause = InlineKeyboardButton(text=t(user_id, "btn_pause_on"), callback_data="pause")

    if verifie:
        bouton_verif = InlineKeyboardButton(text=t(user_id, "btn_deja_verifie"), callback_data="deja_verifie")
    else:
        bouton_verif = InlineKeyboardButton(text=t(user_id, "btn_verifier"), callback_data="verifier")

    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=t(user_id, "btn_filtres"), callback_data="filtres")],
        [InlineKeyboardButton(text=t(user_id, "btn_langue"), callback_data="changer_langue")],
        [bouton_verif],
        [bouton_pause],
        [InlineKeyboardButton(text=t(user_id, "btn_supprimer"), callback_data="supprimer")],
    ])


# def clavier_choix_langue():
#     """Boutons inline pour changer de langue depuis les paramètres."""
#     return InlineKeyboardMarkup(inline_keyboard=[
#         [InlineKeyboardButton(text="🇫🇷 Français", callback_data="setlang_fr")],
#         [InlineKeyboardButton(text="🇬🇧 English", callback_data="setlang_en")],
#         [InlineKeyboardButton(text="🇷🇺 Русский", callback_data="setlang_ru")],
#     ])


# ====================================================
#   BOUTONS DU SWIPE (découverte)
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