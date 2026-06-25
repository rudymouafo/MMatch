from aiogram.fsm.state import State, StatesGroup



class Inscription(StatesGroup):
    langue = State()
    cgu = State()
    prenom = State()
    age = State()
    genre = State()
    recherche = State()
    localisation = State()
    bio = State()
    medias = State()
    telephone = State()


class Modification(StatesGroup):
    prenom = State()
    age = State()
    localisation = State()
    bio = State()
    medias = State()


class Discussion(StatesGroup):
    en_chat = State()

class Filtres(StatesGroup):
    age_min = State()
    age_max = State()
    distance = State()


class Verification(StatesGroup):
    selfie = State()

class ChangementLangue(StatesGroup):
    choix = State()

class Navigation(StatesGroup):
    menu_profil = State()
    menu_modifier = State()
    menu_parametres = State()

