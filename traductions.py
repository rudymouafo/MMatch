from database import get_langue

TRADUCTIONS = {
    # ---------- Choix de la langue ----------
    "choisir_langue": {
        "fr": "🌍 <b>Choisis ta langue</b>\n\nSelect your language\nВыбери язык",
        "en": "🌍 <b>Choisis ta langue</b>\n\nSelect your language\nВыбери язык",
        "ru": "🌍 <b>Choisis ta langue</b>\n\nSelect your language\nВыбери язык",
    },
    "langue_ok": {
        "fr": "Parfait, on continue en français ! 🇫🇷",
        "en": "Great, let's continue in English! 🇬🇧",
        "ru": "Отлично, продолжим на русском! 🇷🇺",
    },

    # ---------- Conditions d'utilisation ----------
    "cgu": {
        "fr": ("💞 <b>Bienvenue sur M_Match</b> 💞\n<i>L'amour commence ici. ✨</i>\n\n"
               "Avant de créer ton profil, prends un instant pour lire nos règles 🌸\n\n"
               "📜 <b>Les règles de M_Match</b>\n"
               "• Tu dois avoir <b>18 ans ou plus</b>.\n"
               "• Sois <b>respectueux·se</b> : pas d'insultes ni de contenu choquant.\n"
               "• Utilise <b>tes vraies photos</b>.\n"
               "• Pas de publicité ni d'arnaque.\n"
               "• Tes données servent uniquement aux rencontres. Tu peux supprimer ton compte à tout moment.\n\n"
               "En continuant, tu acceptes ces règles."),
        "en": ("💞 <b>Welcome to M_Match</b> 💞\n<i>Love starts here. ✨</i>\n\n"
               "Before creating your profile, please take a moment to read our rules 🌸\n\n"
               "📜 <b>M_Match rules</b>\n"
               "• You must be <b>18 or older</b>.\n"
               "• Be <b>respectful</b>: no insults or shocking content.\n"
               "• Use <b>your real photos</b>.\n"
               "• No advertising or scams.\n"
               "• Your data is only used for matching. You can delete your account anytime.\n\n"
               "By continuing, you accept these rules."),
        "ru": ("💞 <b>Добро пожаловать в M_Match</b> 💞\n<i>Любовь начинается здесь. ✨</i>\n\n"
               "Прежде чем создать профиль, ознакомься с правилами 🌸\n\n"
               "📜 <b>Правила M_Match</b>\n"
               "• Тебе должно быть <b>18 лет или больше</b>.\n"
               "• Будь <b>уважителен</b>: без оскорблений и шокирующего контента.\n"
               "• Используй <b>свои настоящие фото</b>.\n"
               "• Без рекламы и мошенничества.\n"
               "• Данные используются только для знакомств. Ты можешь удалить аккаунт в любой момент.\n\n"
               "Продолжая, ты принимаешь эти правила."),
    },
    "cgu_accepte": {
        "fr": "✅ J'accepte",
        "en": "✅ I accept",
        "ru": "✅ Принимаю",
    },
    "cgu_refuse": {
        "fr": "❌ Je refuse",
        "en": "❌ I decline",
        "ru": "❌ Отказываюсь",
    },
    "cgu_refuse_msg": {
        "fr": "Pas de souci 🌷\n\nTu dois accepter nos règles pour utiliser M_Match.\nTape /start quand tu veux. 💞",
        "en": "No problem 🌷\n\nYou must accept our rules to use M_Match.\nType /start whenever you want. 💞",
        "ru": "Без проблем 🌷\n\nЧтобы пользоваться M_Match, нужно принять правила.\nНапиши /start когда захочешь. 💞",
    },

    # ---------- Inscription ----------
    "demande_prenom": {
        "fr": "Merci ! 🌸 Créons ton profil maintenant.\n\nPour commencer, dis-moi : <b>quel est ton prénom ?</b>",
        "en": "Thank you! 🌸 Let's create your profile.\n\nFirst, tell me: <b>what's your first name?</b>",
        "ru": "Спасибо! 🌸 Давай создадим твой профиль.\n\nДля начала: <b>как тебя зовут?</b>",
    },
    "demande_age": {
        "fr": "Enchanté, <b>{prenom}</b> ! 😊\n\nEt quel <b>âge</b> as-tu ?",
        "en": "Nice to meet you, <b>{prenom}</b>! 😊\n\nHow <b>old</b> are you?",
        "ru": "Приятно познакомиться, <b>{prenom}</b>! 😊\n\nСколько тебе <b>лет</b>?",
    },
    "deja_inscrit": {
        "fr": "💞 <b>Te revoilà sur M_Match !</b>\n<i>De nouveaux cœurs t'attendent peut-être… ✨</i>\n\nQue souhaites-tu faire ?",
        "en": "💞 <b>Welcome back to M_Match!</b>\n<i>New hearts might be waiting for you… ✨</i>\n\nWhat would you like to do?",
        "ru": "💞 <b>С возвращением в M_Match!</b>\n<i>Возможно, новые сердца уже ждут тебя… ✨</i>\n\nЧто хочешь сделать?",
    },
    "etape": {
        "fr": "Étape",
        "en": "Step",
        "ru": "Шаг",
    },
# ---------- Boutons genre / recherche (icône + texte) ----------
    "btn_homme": {"fr": "👨 Homme", "en": "👨 Man", "ru": "👨 Мужчина"},
    "btn_femme": {"fr": "👩 Femme", "en": "👩 Woman", "ru": "👩 Женщина"},
    "btn_autre": {"fr": "⚧️ Autre", "en": "⚧️ Other", "ru": "⚧️ Другое"},
    "btn_rech_hommes": {"fr": "👨 Hommes", "en": "👨 Men", "ru": "👨 Мужчины"},
    "btn_rech_femmes": {"fr": "👩 Femmes", "en": "👩 Women", "ru": "👩 Женщины"},
    "btn_rech_tous": {"fr": "✨ Tout le monde", "en": "✨ Everyone", "ru": "✨ Все"},
    "btn_precedent": {"fr": "⬅️ Précédent", "en": "⬅️ Back", "ru": "⬅️ Назад"},
    "btn_position": {"fr": "📍 Partager ma position", "en": "📍 Share my location", "ru": "📍 Поделиться геопозицией"},
    "btn_termine": {"fr": "✅ Terminé", "en": "✅ Done", "ru": "✅ Готово"},

    # ---------- Étape 3 : genre ----------
    "demande_genre": {
        "fr": "Joli ! Et tu es… 💫",
        "en": "Nice! And you are… 💫",
        "ru": "Отлично! А ты… 💫",
    },
    "genre_invalide": {
        "fr": "Pour continuer, choisis l'un des boutons ci-dessous 👇",
        "en": "To continue, pick one of the buttons below 👇",
        "ru": "Чтобы продолжить, выбери одну из кнопок ниже 👇",
    },

    # ---------- Étape 4 : recherche ----------
    "demande_recherche": {
        "fr": "Et le cœur sur qui balance-t-il ? 💘",
        "en": "And who makes your heart skip a beat? 💘",
        "ru": "И к кому лежит твоё сердце? 💘",
    },
    "recherche_invalide": {
        "fr": "Choisis l'un des boutons ci-dessous, pour que je sache qui te présenter 👇",
        "en": "Pick one of the buttons below so I know who to show you 👇",
        "ru": "Выбери одну из кнопок ниже, чтобы я знал, кого показывать 👇",
    },

    # ---------- Étape 5 : localisation ----------
    "demande_localisation": {
        "fr": "Dis-moi <b>où tu te trouves</b> 🌍\n\nPartage ta position avec le bouton ci-dessous,\nou écris simplement le <b>nom de ta ville</b>.",
        "en": "Tell me <b>where you are</b> 🌍\n\nShare your location with the button below,\nor simply type the <b>name of your city</b>.",
        "ru": "Скажи, <b>где ты находишься</b> 🌍\n\nПоделись геопозицией кнопкой ниже,\nили просто напиши <b>название своего города</b>.",
    },
    "localisation_gps_ok": {
        "fr": "Position enregistrée ✨\n\nRaconte-toi en quelques mots… une <b>petite bio</b> qui te ressemble 💬",
        "en": "Location saved ✨\n\nTell us a bit about yourself… a <b>short bio</b> that suits you 💬",
        "ru": "Геопозиция сохранена ✨\n\nРасскажи о себе в нескольких словах… <b>короткое описание</b>, которое тебе подходит 💬",
    },
    "localisation_ville_ok": {
        "fr": "C'est noté ✨\n\nRaconte-toi en quelques mots… une <b>petite bio</b> qui te ressemble 💬",
        "en": "Got it ✨\n\nTell us a bit about yourself… a <b>short bio</b> that suits you 💬",
        "ru": "Записано ✨\n\nРасскажи о себе в нескольких словах… <b>короткое описание</b>, которое тебе подходит 💬",
    },
    "ville_trop_courte": {
        "fr": "J'aimerais en savoir un peu plus 🌍\nÉcris le nom de ta ville, ou partage ta position avec le bouton.",
        "en": "I'd like to know a bit more 🌍\nType your city name, or share your location with the button.",
        "ru": "Хотелось бы узнать чуть больше 🌍\nНапиши название города или поделись геопозицией кнопкой.",
    },

    # ---------- Étape 6 : bio ----------
    "demande_bio": {
        "fr": "Magnifique ! ✨\n\nPour finir, montre-toi sous ton meilleur jour 📸\nEnvoie <b>1 à 3 photos</b> et/ou une <b>petite vidéo</b>, une par une.\n\n<i>Quand tu as terminé, appuie sur</i> « ✅ Terminé » <i>(minimum 1).</i>",
        "en": "Wonderful! ✨\n\nFinally, show yourself at your best 📸\nSend <b>1 to 3 photos</b> and/or a <b>short video</b>, one by one.\n\n<i>When you're done, tap</i> « ✅ Done » <i>(at least 1).</i>",
        "ru": "Прекрасно! ✨\n\nИ напоследок — покажи себя с лучшей стороны 📸\nОтправь <b>от 1 до 3 фото</b> и/или <b>короткое видео</b>, по одному.\n\n<i>Когда закончишь, нажми</i> « ✅ Готово » <i>(минимум 1).</i>",
    },
    "bio_trop_longue": {
        "fr": "J'adore ton enthousiasme ! 😄 Mais c'est un peu trop long.\n<i>(max {max} caractères)</i>",
        "en": "I love your enthusiasm! 😄 But it's a little too long.\n<i>(max {max} characters)</i>",
        "ru": "Мне нравится твой энтузиазм! 😄 Но это немного длинновато.\n<i>(макс. {max} символов)</i>",
    },

    # ---------- Étape 7 : médias ----------
    "media_photo_ok": {
        "fr": "Superbe 📸 <i>({n}/{max})</i>\nEnvoie-en un autre, ou appuie sur « ✅ Terminé ».",
        "en": "Great 📸 <i>({n}/{max})</i>\nSend another, or tap « ✅ Done ».",
        "ru": "Отлично 📸 <i>({n}/{max})</i>\nОтправь ещё или нажми « ✅ Готово ».",
    },
    "media_video_ok": {
        "fr": "Superbe 🎬 <i>({n}/{max})</i>\nEnvoie-en un autre, ou appuie sur « ✅ Terminé ».",
        "en": "Great 🎬 <i>({n}/{max})</i>\nSend another, or tap « ✅ Done ».",
        "ru": "Отлично 🎬 <i>({n}/{max})</i>\nОтправь ещё или нажми « ✅ Готово ».",
    },
    "media_max": {
        "fr": "Tu as déjà <b>{max}</b> médias, c'est parfait ainsi ! ✨\nAppuie sur « ✅ Terminé ».",
        "en": "You already have <b>{max}</b> media, that's perfect! ✨\nTap « ✅ Done ».",
        "ru": "У тебя уже <b>{max}</b> медиа, отлично! ✨\nНажми « ✅ Готово ».",
    },
    "media_min": {
        "fr": "Il me faut au moins une photo ou une vidéo pour finir 📸\nMontre-toi un peu, tu vas faire des heureux·ses ! 😊",
        "en": "I need at least one photo or video to finish 📸\nShow yourself a little, you'll make some people happy! 😊",
        "ru": "Нужно хотя бы одно фото или видео, чтобы закончить 📸\nПокажи себя — кого-то это точно порадует! 😊",
    },

    # ---------- Erreurs prénom / âge ----------
    "prenom_invalide": {
        "fr": "Hmm, j'aimerais un prénom un peu plus complet 🌸\n<i>(entre {min} et {max} caractères)</i>",
        "en": "Hmm, I'd like a slightly fuller name 🌸\n<i>(between {min} and {max} characters)</i>",
        "ru": "Хм, хотелось бы имя чуть полнее 🌸\n<i>(от {min} до {max} символов)</i>",
    },
    "age_invalide": {
        "fr": "Oups, je n'ai pas compris 🙂\nÉcris simplement ton âge en chiffres <i>(par exemple : 25)</i>.",
        "en": "Oops, I didn't get that 🙂\nJust type your age in numbers <i>(for example: 25)</i>.",
        "ru": "Упс, я не понял 🙂\nПросто напиши свой возраст цифрами <i>(например: 25)</i>.",
    },
    "age_trop_jeune": {
        "fr": "Merci d'être passé·e 🌷\n\nM_Match est réservé aux <b>18 ans et plus</b>. À très bientôt !",
        "en": "Thanks for stopping by 🌷\n\nM_Match is for <b>18 and older</b>. See you soon!",
        "ru": "Спасибо, что заглянул·а 🌷\n\nM_Match только для <b>18 лет и старше</b>. До скорого!",
    },
    "age_trop_vieux": {
        "fr": "Hmm, cet âge me semble un peu surprenant 🤔\nPeux-tu me redonner ton âge ?",
        "en": "Hmm, that age seems a bit surprising 🤔\nCould you tell me your age again?",
        "ru": "Хм, этот возраст немного удивляет 🤔\nМожешь указать возраст ещё раз?",
    },

    # ---------- Fin d'inscription ----------
    "profil_pret": {
        "fr": "🎉 <b>Et voilà, ton profil est prêt !</b>\n\nVoici comment les autres te verront 👇",
        "en": "🎉 <b>There you go, your profile is ready!</b>\n\nHere's how others will see you 👇",
        "ru": "🎉 <b>Готово, твой профиль создан!</b>\n\nВот как тебя увидят другие 👇",
    },
    "pret_aventure": {
        "fr": "💞 <b>Te voilà prêt·e pour l'aventure !</b>\n\nUtilise le menu en bas pour découvrir des profils 👇",
        "en": "💞 <b>You're all set for the adventure!</b>\n\nUse the menu below to discover profiles 👇",
        "ru": "💞 <b>Ты готов·а к приключению!</b>\n\nИспользуй меню внизу, чтобы смотреть анкеты 👇",
    },
    "annule": {
        "fr": "Pas de souci, on arrête là. 🌸\n\nReviens quand tu veux avec /start.",
        "en": "No problem, we'll stop here. 🌸\n\nCome back anytime with /start.",
        "ru": "Без проблем, останавливаемся. 🌸\n\nВозвращайся в любой момент с /start.",
    },
    # ---------- Menu permanent ----------
    "menu_decouvrir": {"fr": "🔥 Découvrir", "en": "🔥 Discover", "ru": "🔥 Смотреть"},
    "menu_matchs": {"fr": "💞 Mes matchs", "en": "💞 My matches", "ru": "💞 Мои совпадения"},
    "menu_profil": {"fr": "👤 Mon profil", "en": "👤 My profile", "ru": "👤 Мой профиль"},
    "menu_parametres": {"fr": "⚙️ Paramètres", "en": "⚙️ Settings", "ru": "⚙️ Настройки"},

    # ---------- Espace profil ----------
    "espace_profil": {
        "fr": "💞 <b>Ton espace M_Match</b>\n\nQue souhaites-tu faire, {prenom} ?",
        "en": "💞 <b>Your M_Match space</b>\n\nWhat would you like to do, {prenom}?",
        "ru": "💞 <b>Твой профиль M_Match</b>\n\nЧто хочешь сделать, {prenom}?",
    },
    "pas_de_profil": {
        "fr": "Tu n'as pas encore de profil 🌸\nTape /start pour créer le tien.",
        "en": "You don't have a profile yet 🌸\nType /start to create yours.",
        "ru": "У тебя ещё нет профиля 🌸\nНапиши /start, чтобы создать его.",
    },

    # ---------- Menu paramètres (titre) ----------
    "parametres_titre": {
        "fr": "⚙️ <b>Paramètres</b>\n\nQue souhaites-tu régler ?",
        "en": "⚙️ <b>Settings</b>\n\nWhat would you like to adjust?",
        "ru": "⚙️ <b>Настройки</b>\n\nЧто хочешь настроить?",
    },

    # ---------- Boutons du menu profil (inline) ----------
    "btn_decouvrir_profils": {"fr": "🔥 Découvrir des profils", "en": "🔥 Discover profiles", "ru": "🔥 Смотреть анкеты"},
    "btn_mes_matchs": {"fr": "💞 Mes matchs", "en": "💞 My matches", "ru": "💞 Мои совпадения"},
    "btn_voir_profil": {"fr": "👁 Voir mon profil", "en": "👁 View my profile", "ru": "👁 Посмотреть мой профиль"},
    "btn_mes_stats": {"fr": "📊 Mes statistiques", "en": "📊 My stats", "ru": "📊 Моя статистика"},
    "btn_modifier_profil": {"fr": "✏️ Modifier mon profil", "en": "✏️ Edit my profile", "ru": "✏️ Изменить профиль"},

    # ---------- Boutons du menu paramètres (inline) ----------
    "btn_filtres": {"fr": "⚙️ Mes filtres de recherche", "en": "⚙️ My search filters", "ru": "⚙️ Мои фильтры поиска"},
    "btn_verifier": {"fr": "🛡️ Vérifier mon profil", "en": "🛡️ Verify my profile", "ru": "🛡️ Подтвердить профиль"},
    "btn_deja_verifie": {"fr": "✅ Profil vérifié", "en": "✅ Verified profile", "ru": "✅ Профиль подтверждён"},
    "btn_pause_on": {"fr": "⏸️ Mettre mon profil en pause", "en": "⏸️ Pause my profile", "ru": "⏸️ Поставить профиль на паузу"},
    "btn_pause_off": {"fr": "▶️ Réactiver mon profil", "en": "▶️ Reactivate my profile", "ru": "▶️ Возобновить профиль"},
    "btn_supprimer": {"fr": "🗑️ Supprimer mon compte", "en": "🗑️ Delete my account", "ru": "🗑️ Удалить аккаунт"},

    # ---------- Découverte ----------
    "badge_verifie": {
        "fr": "✅ <b>Profil vérifié</b>\n",
        "en": "✅ <b>Verified profile</b>\n",
        "ru": "✅ <b>Подтверждённый профиль</b>\n",
    },
    "badge_nouveau": {
        "fr": "🆕 <b>Nouveau sur M_Match</b>\n",
        "en": "🆕 <b>New on M_Match</b>\n",
        "ru": "🆕 <b>Новенький в M_Match</b>\n",
    },
    "profil_en_pause": {
        "fr": "⏸️ <b>Ton profil est en pause.</b>\n\nRéactive-le dans ⚙️ Paramètres pour reprendre la découverte. 🌸",
        "en": "⏸️ <b>Your profile is paused.</b>\n\nReactivate it in ⚙️ Settings to resume discovering. 🌸",
        "ru": "⏸️ <b>Твой профиль на паузе.</b>\n\nВключи его в ⚙️ Настройках, чтобы продолжить просмотр. 🌸",
    },
    "plus_de_profils": {
        "fr": "💫 <b>Tu as fait le tour pour le moment !</b>\n\nDe nouveaux cœurs arrivent chaque jour…\nReviens vite, l'amour n'attend pas. 🌸",
        "en": "💫 <b>You've seen everyone for now!</b>\n\nNew hearts arrive every day…\nCome back soon, love won't wait. 🌸",
        "ru": "💫 <b>Пока ты посмотрел·а всех!</b>\n\nКаждый день появляются новые сердца…\nВозвращайся скорее, любовь не ждёт. 🌸",
    },
    "match_titre": {
        "fr": "💞 <b>C'est un match !</b> 💞\n\nToi et <b>{prenom}</b> vous êtes plu·e·s mutuellement 🥰\n\nLancez-vous… le premier message est souvent le plus beau ! ✨",
        "en": "💞 <b>It's a match!</b> 💞\n\nYou and <b>{prenom}</b> liked each other 🥰\n\nGo for it… the first message is often the sweetest! ✨",
        "ru": "💞 <b>Это совпадение!</b> 💞\n\nТы и <b>{prenom}</b> понравились друг другу 🥰\n\nСделай шаг… первое сообщение часто самое приятное! ✨",
    },
    "match_revoir": {
        "fr": "👤 Revoir {prenom}",
        "en": "👤 See {prenom} again",
        "ru": "👤 Снова посмотреть {prenom}",
    },
    "like_recu": {
        "fr": "💖 <b>Quelqu'un vient de t'aimer !</b>\n\nLance la découverte 🔥 pour voir si le courant passe… qui sait, c'est peut-être un futur match ! 💞",
        "en": "💖 <b>Someone just liked you!</b>\n\nStart discovering 🔥 to see if there's a spark… who knows, it could be a future match! 💞",
        "ru": "💖 <b>Кто-то только что лайкнул тебя!</b>\n\nНачни просмотр 🔥, чтобы проверить, есть ли искра… кто знает, может это будущее совпадение! 💞",
    },
    "limite_likes": {
        "fr": "💔 <b>Tu as utilisé tous tes likes pour aujourd'hui !</b>\n\nReviens demain pour continuer à aimer 🌸\n<i>(Astuce : les profils vérifiés ✅ ont droit à plus de likes par jour !)</i>",
        "en": "💔 <b>You've used all your likes for today!</b>\n\nCome back tomorrow to keep liking 🌸\n<i>(Tip: verified profiles ✅ get more likes per day!)</i>",
        "ru": "💔 <b>Ты использовал·а все лайки на сегодня!</b>\n\nВозвращайся завтра, чтобы продолжить 🌸\n<i>(Совет: подтверждённые профили ✅ получают больше лайков в день!)</i>",
    },
    "signalement_envoye": {
        "fr": "Signalement envoyé. Merci 🌸",
        "en": "Report sent. Thank you 🌸",
        "ru": "Жалоба отправлена. Спасибо 🌸",
    },
    "profil_plus_montre": {
        "fr": "Merci, ce profil ne te sera plus montré. 🌸",
        "en": "Thanks, this profile won't be shown to you again. 🌸",
        "ru": "Спасибо, этот профиль больше не будет показан. 🌸",
    },
    "profil_bloque_alert": {
        "fr": "Profil bloqué 🚫",
        "en": "Profile blocked 🚫",
        "ru": "Профиль заблокирован 🚫",
    },
    "profil_bloque_msg": {
        "fr": "Ce profil est bloqué et ne te sera plus montré. 🌸",
        "en": "This profile is blocked and won't be shown to you again. 🌸",
        "ru": "Этот профиль заблокирован и больше не будет показан. 🌸",
    },
    "petite_pause": {
        "fr": "Petite pause 🌸\nReviens dès que l'envie te prend ! ✨",
        "en": "Quick break 🌸\nCome back whenever you feel like it! ✨",
        "ru": "Небольшой перерыв 🌸\nВозвращайся, когда захочешь! ✨",
    },
    "profil_indispo": {
        "fr": "Ce profil n'est plus disponible. 🌸",
        "en": "This profile is no longer available. 🌸",
        "ru": "Этот профиль больше недоступен. 🌸",
    },
    # ---------- Messagerie / matchs ----------
    "pas_de_match": {
        "fr": "Tu n'as pas encore de match… mais ça ne saurait tarder ! 🌸\n\nLance la découverte et trouve la perle rare. 🔥",
        "en": "You don't have any matches yet… but it won't be long! 🌸\n\nStart discovering and find that special someone. 🔥",
        "ru": "У тебя пока нет совпадений… но это ненадолго! 🌸\n\nНачни просмотр и найди свою половинку. 🔥",
    },
    "tes_matchs": {
        "fr": "💞 <b>Tes matchs</b>\n\nAvec qui as-tu envie d'échanger ? ✨",
        "en": "💞 <b>Your matches</b>\n\nWho would you like to chat with? ✨",
        "ru": "💞 <b>Твои совпадения</b>\n\nС кем хочешь пообщаться? ✨",
    },
    "conv_indispo": {
        "fr": "Cette conversation n'est plus disponible. 🌸",
        "en": "This conversation is no longer available. 🌸",
        "ru": "Этот разговор больше недоступен. 🌸",
    },
    "plus_en_match": {
        "fr": "Vous n'êtes plus en match. 🌸",
        "en": "You're no longer a match. 🌸",
        "ru": "Вы больше не совпадение. 🌸",
    },
    "conv_ouverte": {
        "fr": "💬 Te voilà en conversation avec <b>{prenom}</b> 🥰\n\n<i>Tes messages lui sont transmis en toute discrétion.</i>\nLance-toi… un joli mot fait toujours son effet ! ✨",
        "en": "💬 You're now chatting with <b>{prenom}</b> 🥰\n\n<i>Your messages are passed on discreetly.</i>\nGo ahead… a kind word always works! ✨",
        "ru": "💬 Теперь ты общаешься с <b>{prenom}</b> 🥰\n\n<i>Твои сообщения передаются конфиденциально.</i>\nСмелее… доброе слово всегда работает! ✨",
    },
    "souci_personne": {
        "fr": "Un souci avec cette personne ?",
        "en": "A problem with this person?",
        "ru": "Проблема с этим человеком?",
    },
    "btn_quitter_conv": {
        "fr": "🚪 Quitter la conversation",
        "en": "🚪 Leave the conversation",
        "ru": "🚪 Покинуть разговор",
    },
    "conv_fermee": {
        "fr": "Conversation refermée 🌸\nReviens quand tu veux depuis « 💞 Mes matchs ».",
        "en": "Conversation closed 🌸\nCome back anytime from « 💞 My matches ».",
        "ru": "Разговор закрыт 🌸\nВозвращайся в любой момент через « 💞 Мои совпадения ».",
    },
    "signalement_conv_bloque": {
        "fr": "Merci. Cette personne est bloquée, vous ne vous verrez plus. 🌸",
        "en": "Thank you. This person is blocked, you won't see each other again. 🌸",
        "ru": "Спасибо. Этот человек заблокирован, вы больше не увидите друг друга. 🌸",
    },
    "personne_bloquee": {
        "fr": "Cette personne est bloquée, vous ne vous verrez plus. 🌸",
        "en": "This person is blocked, you won't see each other again. 🌸",
        "ru": "Этот человек заблокирован, вы больше не увидите друг друга. 🌸",
    },
    "msg_non_envoye": {
        "fr": "Ton message n'a pas pu être envoyé. 😔\nRéessaie dans un instant.",
        "en": "Your message couldn't be sent. 😔\nTry again in a moment.",
        "ru": "Твоё сообщение не удалось отправить. 😔\nПопробуй ещё раз через мгновение.",
    },
    "photo_non_envoyee": {
        "fr": "Ta photo n'a pas pu être envoyée. 😔\nRéessaie dans un instant.",
        "en": "Your photo couldn't be sent. 😔\nTry again in a moment.",
        "ru": "Твоё фото не удалось отправить. 😔\nПопробуй ещё раз через мгновение.",
    },
    "msg_relais": {
        "fr": "💬 <b>{prenom}</b> :\n{texte}",
        "en": "💬 <b>{prenom}</b>:\n{texte}",
        "ru": "💬 <b>{prenom}</b>:\n{texte}",
    },
    "photo_relais": {
        "fr": "📸 <i>Une photo de {prenom}</i>",
        "en": "📸 <i>A photo from {prenom}</i>",
        "ru": "📸 <i>Фото от {prenom}</i>",
    },
    "btn_repondre": {
        "fr": "💬 Répondre",
        "en": "💬 Reply",
        "ru": "💬 Ответить",
    },
    # ---------- Profil : affichage et modification ----------
    "profil_maj": {
        "fr": "✨ <b>C'est tout beau, c'est à jour !</b> Voici ton profil :",
        "en": "✨ <b>All set, it's updated!</b> Here's your profile:",
        "ru": "✨ <b>Готово, обновлено!</b> Вот твой профиль:",
    },
    "retoucher_autre": {
        "fr": "✏️ Envie de retoucher autre chose ?",
        "en": "✏️ Want to edit something else?",
        "ru": "✏️ Хочешь изменить что-то ещё?",
    },
    "pas_de_changement": {
        "fr": "Pas de changement, c'est noté. 🌸",
        "en": "No changes, got it. 🌸",
        "ru": "Без изменений, понятно. 🌸",
    },
    "voici_ton_menu": {
        "fr": "Voici ton menu 👇",
        "en": "Here's your menu 👇",
        "ru": "Вот твоё меню 👇",
    },
    "profil_aucun": {
        "fr": "Aucun profil trouvé 🌸\nTape /start pour créer le tien.",
        "en": "No profile found 🌸\nType /start to create yours.",
        "ru": "Профиль не найден 🌸\nНапиши /start, чтобы создать свой.",
    },
    "voici_profil": {
        "fr": "Voici ton profil, tel que les autres le voient 👇",
        "en": "Here's your profile, as others see it 👇",
        "ru": "Вот твой профиль, каким его видят другие 👇",
    },
    "que_retoucher": {
        "fr": "✏️ <b>Que souhaites-tu retoucher ?</b>\n\nChoisis un élément ci-dessous 👇",
        "en": "✏️ <b>What would you like to edit?</b>\n\nPick an item below 👇",
        "ru": "✏️ <b>Что хочешь изменить?</b>\n\nВыбери пункт ниже 👇",
    },
    "stats_titre": {
        "fr": "📊 <b>Tes statistiques</b>\n\n💖 Personnes qui t'ont aimé : <b>{likes}</b>\n💞 Tes matchs : <b>{matchs}</b>\n🛡️ Statut : <b>{statut}</b>\n\n<i>Continue de swiper pour faire grimper ces chiffres ! 🔥</i>",
        "en": "📊 <b>Your stats</b>\n\n💖 People who liked you: <b>{likes}</b>\n💞 Your matches: <b>{matchs}</b>\n🛡️ Status: <b>{statut}</b>\n\n<i>Keep swiping to raise these numbers! 🔥</i>",
        "ru": "📊 <b>Твоя статистика</b>\n\n💖 Лайкнули тебя: <b>{likes}</b>\n💞 Твои совпадения: <b>{matchs}</b>\n🛡️ Статус: <b>{statut}</b>\n\n<i>Продолжай свайпать, чтобы поднять эти цифры! 🔥</i>",
    },
    "statut_verifie": {
        "fr": "✅ Vérifié",
        "en": "✅ Verified",
        "ru": "✅ Подтверждён",
    },
    "statut_non_verifie": {
        "fr": "Non vérifié",
        "en": "Not verified",
        "ru": "Не подтверждён",
    },
    "demande_nouveau_prenom": {
        "fr": "Écris ton nouveau <b>prénom</b> 💫",
        "en": "Type your new <b>first name</b> 💫",
        "ru": "Напиши своё новое <b>имя</b> 💫",
    },
    "demande_nouvel_age": {
        "fr": "Écris ton nouvel <b>âge</b> 🎂",
        "en": "Type your new <b>age</b> 🎂",
        "ru": "Напиши свой новый <b>возраст</b> 🎂",
    },
    "demande_nouveau_genre": {
        "fr": "Tu es… 💫",
        "en": "You are… 💫",
        "ru": "Ты… 💫",
    },
    "demande_nouvelle_recherche": {
        "fr": "Le cœur balance sur… 💘",
        "en": "Your heart leans toward… 💘",
        "ru": "Твоё сердце склоняется к… 💘",
    },
    "demande_nouvelle_loc": {
        "fr": "Partage ta nouvelle position 🌍\nou écris le <b>nom de ta ville</b>.",
        "en": "Share your new location 🌍\nor type the <b>name of your city</b>.",
        "ru": "Поделись новой геопозицией 🌍\nили напиши <b>название города</b>.",
    },
    "loc_maj": {
        "fr": "Position mise à jour ✨",
        "en": "Location updated ✨",
        "ru": "Геопозиция обновлена ✨",
    },
    "loc_maj_ville": {
        "fr": "Localisation mise à jour ✨",
        "en": "Location updated ✨",
        "ru": "Местоположение обновлено ✨",
    },
    "demande_nouvelle_bio": {
        "fr": "Écris ta nouvelle <b>bio</b> 💬",
        "en": "Type your new <b>bio</b> 💬",
        "ru": "Напиши своё новое <b>описание</b> 💬",
    },
    "demande_nouveaux_medias": {
        "fr": "Montre-toi sous ton meilleur jour 📸\nEnvoie <b>1 à {max}</b> photos/vidéos, une par une.\n\n<i>Cela remplacera tes médias actuels.</i>\nAppuie sur « ✅ Terminé » quand c'est bon.",
        "en": "Show yourself at your best 📸\nSend <b>1 to {max}</b> photos/videos, one by one.\n\n<i>This will replace your current media.</i>\nTap « ✅ Done » when ready.",
        "ru": "Покажи себя с лучшей стороны 📸\nОтправь <b>от 1 до {max}</b> фото/видео, по одному.\n\n<i>Это заменит твои текущие медиа.</i>\nНажми « ✅ Готово », когда закончишь.",
    },
    "media_ajoute": {
        "fr": "Ajouté 📸 <i>({n}/{max})</i>",
        "en": "Added 📸 <i>({n}/{max})</i>",
        "ru": "Добавлено 📸 <i>({n}/{max})</i>",
    },
    "media_ajoute_video": {
        "fr": "Ajouté 🎬 <i>({n}/{max})</i>",
        "en": "Added 🎬 <i>({n}/{max})</i>",
        "ru": "Добавлено 🎬 <i>({n}/{max})</i>",
    },
    "media_max_atteint": {
        "fr": "Tu as atteint le maximum de <b>{max}</b> médias ✨\nAppuie sur « ✅ Terminé ».",
        "en": "You've reached the maximum of <b>{max}</b> media ✨\nTap « ✅ Done ».",
        "ru": "Ты достиг·ла максимума в <b>{max}</b> медиа ✨\nНажми « ✅ Готово ».",
    },
    "media_min_un": {
        "fr": "Il me faut au moins une photo ou une vidéo 📸",
        "en": "I need at least one photo or video 📸",
        "ru": "Нужно хотя бы одно фото или видео 📸",
    },
    "medias_maj": {
        "fr": "Tes médias sont mis à jour ✨",
        "en": "Your media is updated ✨",
        "ru": "Твои медиа обновлены ✨",
    },
    "prenom_court": {
        "fr": "J'aimerais un prénom un peu plus complet 🌸\n<i>(entre {min} et {max} caractères)</i>",
        "en": "I'd like a slightly fuller name 🌸\n<i>(between {min} and {max} characters)</i>",
        "ru": "Хотелось бы имя чуть полнее 🌸\n<i>(от {min} до {max} символов)</i>",
    },
    "age_chiffres": {
        "fr": "Écris simplement ton âge en chiffres 🙂\n<i>(par exemple : 25)</i>",
        "en": "Just type your age in numbers 🙂\n<i>(for example: 25)</i>",
        "ru": "Просто напиши свой возраст цифрами 🙂\n<i>(например: 25)</i>",
    },
    "age_surprenant": {
        "fr": "Hmm, cet âge me semble un peu surprenant 🤔\n<i>(entre {min} et {max} ans)</i>",
        "en": "Hmm, that age seems a bit surprising 🤔\n<i>(between {min} and {max})</i>",
        "ru": "Хм, этот возраст немного удивляет 🤔\n<i>(от {min} до {max})</i>",
    },
    "cest_note": {
        "fr": "C'est noté ✨",
        "en": "Got it ✨",
        "ru": "Записано ✨",
    },
    # ---------- Paramètres : filtres ----------
    "parametres_ouvre": {
        "fr": "⚙️ <b>Paramètres</b>\n\nQue souhaites-tu régler ?",
        "en": "⚙️ <b>Settings</b>\n\nWhat would you like to adjust?",
        "ru": "⚙️ <b>Настройки</b>\n\nЧто хочешь настроить?",
    },
    "filtres_actuels": {
        "fr": "⚙️ <b>Tes filtres de recherche</b>\n\nActuellement :\n🎂 Âge : <b>{age_min} – {age_max} ans</b>\n📍 Distance max : <b>{distance} km</b>\n\nRéglons-les ensemble.\nQuel est l'<b>âge minimum</b> que tu recherches ? <i>(18 ou plus)</i>",
        "en": "⚙️ <b>Your search filters</b>\n\nCurrently:\n🎂 Age: <b>{age_min} – {age_max}</b>\n📍 Max distance: <b>{distance} km</b>\n\nLet's adjust them together.\nWhat's the <b>minimum age</b> you're looking for? <i>(18 or more)</i>",
        "ru": "⚙️ <b>Твои фильтры поиска</b>\n\nСейчас:\n🎂 Возраст: <b>{age_min} – {age_max}</b>\n📍 Макс. расстояние: <b>{distance} км</b>\n\nНастроим вместе.\nКакой <b>минимальный возраст</b> ты ищешь? <i>(18 или больше)</i>",
    },
    "nombre_simple": {
        "fr": "Écris un nombre, tout simplement 🙂 <i>(ex : {ex})</i>",
        "en": "Just type a number 🙂 <i>(e.g. {ex})</i>",
        "ru": "Просто напиши число 🙂 <i>(напр. {ex})</i>",
    },
    "age_min_18": {
        "fr": "L'âge minimum est <b>18 ans</b>. Réessaie :",
        "en": "The minimum age is <b>18</b>. Try again:",
        "ru": "Минимальный возраст — <b>18</b>. Попробуй ещё раз:",
    },
    "age_trop_eleve": {
        "fr": "Cet âge me semble un peu élevé 🤔. Réessaie :",
        "en": "That age seems a bit high 🤔. Try again:",
        "ru": "Этот возраст кажется великоватым 🤔. Попробуй ещё раз:",
    },
    "demande_age_max": {
        "fr": "Et l'<b>âge maximum</b> ? <i>(au moins {min})</i>",
        "en": "And the <b>maximum age</b>? <i>(at least {min})</i>",
        "ru": "А <b>максимальный возраст</b>? <i>(минимум {min})</i>",
    },
    "age_max_trop_bas": {
        "fr": "L'âge maximum doit être au moins {min}. Réessaie :",
        "en": "The maximum age must be at least {min}. Try again:",
        "ru": "Максимальный возраст должен быть не меньше {min}. Попробуй ещё раз:",
    },
    "demande_distance": {
        "fr": "Parfait ! Et la <b>distance maximale</b> en km ? 📍\n<i>(ex : 50 — ne s'applique qu'aux profils ayant partagé leur position)</i>",
        "en": "Perfect! And the <b>maximum distance</b> in km? 📍\n<i>(e.g. 50 — only applies to profiles who shared their location)</i>",
        "ru": "Отлично! А <b>максимальное расстояние</b> в км? 📍\n<i>(напр. 50 — применяется только к профилям, поделившимся геопозицией)</i>",
    },
    "distance_km": {
        "fr": "Écris un nombre en km 🙂 <i>(ex : 50)</i>",
        "en": "Type a number in km 🙂 <i>(e.g. 50)</i>",
        "ru": "Напиши число в км 🙂 <i>(напр. 50)</i>",
    },
    "distance_min_1": {
        "fr": "La distance doit être d'au moins 1 km. Réessaie :",
        "en": "The distance must be at least 1 km. Try again:",
        "ru": "Расстояние должно быть не меньше 1 км. Попробуй ещё раз:",
    },
    "filtres_enregistres": {
        "fr": "✅ <b>Tes filtres sont enregistrés !</b>\n\n🎂 Âge : <b>{age_min} – {age_max} ans</b>\n📍 Distance max : <b>{distance} km</b>\n\nPlace à la découverte ! 🔥",
        "en": "✅ <b>Your filters are saved!</b>\n\n🎂 Age: <b>{age_min} – {age_max}</b>\n📍 Max distance: <b>{distance} km</b>\n\nTime to discover! 🔥",
        "ru": "✅ <b>Твои фильтры сохранены!</b>\n\n🎂 Возраст: <b>{age_min} – {age_max}</b>\n📍 Макс. расстояние: <b>{distance} км</b>\n\nВремя для просмотра! 🔥",
    },
    # ---------- Paramètres : pause ----------
    "pause_activee": {
        "fr": "▶️ <b>Ton profil est de nouveau actif !</b>\n\nTu réapparais dans la découverte, et tu peux explorer à nouveau. 🔥",
        "en": "▶️ <b>Your profile is active again!</b>\n\nYou reappear in discovery, and you can explore again. 🔥",
        "ru": "▶️ <b>Твой профиль снова активен!</b>\n\nТы снова появляешься в просмотре и можешь искать. 🔥",
    },
    "pause_misee": {
        "fr": "⏸️ <b>Ton profil est en pause.</b>\n\nTu n'apparais plus dans la découverte, et tu ne verras plus de profils.\n<i>Tes matchs et conversations sont conservés.</i>\n\nReviens ici quand tu veux pour réactiver ton profil. 🌸",
        "en": "⏸️ <b>Your profile is paused.</b>\n\nYou no longer appear in discovery, and you won't see profiles.\n<i>Your matches and conversations are kept.</i>\n\nCome back here anytime to reactivate your profile. 🌸",
        "ru": "⏸️ <b>Твой профиль на паузе.</b>\n\nТы больше не появляешься в просмотре и не видишь профили.\n<i>Твои совпадения и переписки сохранены.</i>\n\nВозвращайся сюда в любой момент, чтобы снова включить профиль. 🌸",
    },
    # ---------- Paramètres : suppression ----------
    "btn_supprimer_oui": {
        "fr": "🗑️ Oui, tout supprimer",
        "en": "🗑️ Yes, delete everything",
        "ru": "🗑️ Да, удалить всё",
    },
    "btn_supprimer_non": {
        "fr": "🔙 Non, annuler",
        "en": "🔙 No, cancel",
        "ru": "🔙 Нет, отмена",
    },
    "supprimer_demande": {
        "fr": "🗑️ <b>Supprimer ton compte ?</b>\n\nCette action est <b>définitive</b> : ton profil, tes likes, tes matchs et tes conversations seront effacés et ne pourront pas être récupérés.\n\nEs-tu sûr·e ?",
        "en": "🗑️ <b>Delete your account?</b>\n\nThis action is <b>permanent</b>: your profile, likes, matches and conversations will be erased and cannot be recovered.\n\nAre you sure?",
        "ru": "🗑️ <b>Удалить аккаунт?</b>\n\nЭто действие <b>необратимо</b>: твой профиль, лайки, совпадения и переписки будут удалены без возможности восстановления.\n\nТы уверен·а?",
    },
    "supprimer_annule": {
        "fr": "Ouf, on garde tout ! 🌸\nReviens quand tu veux dans les paramètres.",
        "en": "Phew, we keep everything! 🌸\nCome back to settings anytime.",
        "ru": "Уф, всё сохранено! 🌸\nВозвращайся в настройки в любой момент.",
    },
    "supprimer_confirme": {
        "fr": "🗑️ <b>Ton compte a été supprimé.</b>\n\nToutes tes données ont été effacées. Merci d'avoir fait un bout de chemin avec M_Match. 🌸\n\n<i>Si tu changes d'avis un jour, tape /start pour recréer un profil.</i>",
        "en": "🗑️ <b>Your account has been deleted.</b>\n\nAll your data has been erased. Thank you for walking a while with M_Match. 🌸\n\n<i>If you change your mind one day, type /start to create a new profile.</i>",
        "ru": "🗑️ <b>Твой аккаунт удалён.</b>\n\nВсе твои данные стёрты. Спасибо, что был·а с M_Match. 🌸\n\n<i>Если однажды передумаешь, напиши /start, чтобы создать новый профиль.</i>",
    },
    # ---------- Vérification ----------
    "deja_verifie": {
        "fr": "✅ <b>Tu es déjà vérifié·e !</b>\n\nTon profil affiche le badge de confiance. 🌸",
        "en": "✅ <b>You're already verified!</b>\n\nYour profile shows the trust badge. 🌸",
        "ru": "✅ <b>Ты уже подтверждён·а!</b>\n\nНа твоём профиле есть значок доверия. 🌸",
    },
    "verif_explication": {
        "fr": "✅ <b>Vérifier ton profil</b>\n\nLa vérification rassure les autres et t'offre un joli badge ✅ — en plus de quelques avantages (comme plus de likes par jour).\n\n<b>Comment ça marche ?</b>\nEnvoie-moi un <b>selfie</b> en train de faire un <b>signe de la main</b> 👋\n<i>(une photo prise à l'instant, pas une ancienne photo).</i>\n\nUn membre de l'équipe vérifiera que c'est bien toi. 🌸",
        "en": "✅ <b>Verify your profile</b>\n\nVerification reassures others and gives you a nice ✅ badge — plus a few perks (like more likes per day).\n\n<b>How does it work?</b>\nSend me a <b>selfie</b> doing a <b>hand wave</b> 👋\n<i>(a photo taken right now, not an old one).</i>\n\nA team member will check that it's really you. 🌸",
        "ru": "✅ <b>Подтверди свой профиль</b>\n\nПодтверждение успокаивает других и даёт красивый значок ✅ — плюс несколько бонусов (например, больше лайков в день).\n\n<b>Как это работает?</b>\nОтправь мне <b>селфи</b>, где ты <b>машешь рукой</b> 👋\n<i>(фото, сделанное прямо сейчас, не старое).</i>\n\nЧлен команды проверит, что это действительно ты. 🌸",
    },
    "verif_pas_photo": {
        "fr": "J'ai besoin d'une <b>photo</b> selfie 📸\nEnvoie-moi une photo de toi en train de faire un signe de la main 👋",
        "en": "I need a <b>photo</b> selfie 📸\nSend me a photo of yourself doing a hand wave 👋",
        "ru": "Мне нужно <b>фото</b>-селфи 📸\nОтправь фото, где ты машешь рукой 👋",
    },
    "verif_recue": {
        "fr": "Merci ! 🌸\n\nTon selfie a bien été envoyé à l'équipe. La vérification prend en général moins de <b>48h</b>.\n\nJe te préviens dès que c'est validé ! ✨",
        "en": "Thank you! 🌸\n\nYour selfie has been sent to the team. Verification usually takes less than <b>48h</b>.\n\nI'll let you know as soon as it's approved! ✨",
        "ru": "Спасибо! 🌸\n\nТвоё селфи отправлено команде. Подтверждение обычно занимает меньше <b>48 часов</b>.\n\nЯ сообщу, как только всё одобрят! ✨",
    },
    "verif_validee": {
        "fr": "✅ <b>Félicitations, ton profil est vérifié !</b>\n\nTu portes désormais le badge de confiance ✅\nLes autres te feront davantage confiance, et tu profites de quelques avantages. 🌸✨",
        "en": "✅ <b>Congratulations, your profile is verified!</b>\n\nYou now wear the trust badge ✅\nOthers will trust you more, and you get a few perks. 🌸✨",
        "ru": "✅ <b>Поздравляем, твой профиль подтверждён!</b>\n\nТеперь у тебя значок доверия ✅\nДругие будут больше доверять тебе, и ты получаешь несколько бонусов. 🌸✨",
    },
    "verif_refusee": {
        "fr": "Ta demande de vérification n'a pas pu être validée cette fois. 🌸\n\nCela arrive si le selfie n'est pas net, ne montre pas le signe de la main, ou ne correspond pas à tes photos.\n\nTu peux réessayer quand tu veux depuis ⚙️ Paramètres. ✨",
        "en": "Your verification request couldn't be approved this time. 🌸\n\nThis happens if the selfie isn't clear, doesn't show the hand wave, or doesn't match your photos.\n\nYou can try again anytime from ⚙️ Settings. ✨",
        "ru": "Твой запрос на подтверждение не удалось одобрить в этот раз. 🌸\n\nТакое бывает, если селфи нечёткое, не показывает жест рукой или не совпадает с твоими фото.\n\nМожешь попробовать снова в любой момент в ⚙️ Настройках. ✨",
    },
    # ---------- Aide / FAQ ----------
    "aide_titre": {
        "fr": "💞 <b>Aide & Questions fréquentes</b>\n\nVoici tout ce qu'il faut savoir sur M_Match 🌸",
        "en": "💞 <b>Help & FAQ</b>\n\nHere's everything you need to know about M_Match 🌸",
        "ru": "💞 <b>Помощь и частые вопросы</b>\n\nВот всё, что нужно знать о M_Match 🌸",
    },
    "aide_q1": {
        "fr": "❓ <b>Comment ça marche ?</b>\nLance la découverte 🔥, et pour chaque profil : ❤️ si ça te plaît, 👎 pour passer. Quand deux personnes s'aiment, c'est un <b>match</b> 💞 et vous pouvez discuter !",
        "en": "❓ <b>How does it work?</b>\nStart discovering 🔥, and for each profile: ❤️ if you like, 👎 to pass. When two people like each other, it's a <b>match</b> 💞 and you can chat!",
        "ru": "❓ <b>Как это работает?</b>\nНачни просмотр 🔥, и для каждого профиля: ❤️ если нравится, 👎 чтобы пропустить. Когда двое нравятся друг другу — это <b>совпадение</b> 💞 и вы можете общаться!",
    },
    "aide_q2": {
        "fr": "✏️ <b>Modifier mon profil ?</b>\nVa dans 👤 Mon profil → ✏️ Modifier. Tu peux changer ton prénom, ton âge, tes photos, ta bio, etc.",
        "en": "✏️ <b>Edit my profile?</b>\nGo to 👤 My profile → ✏️ Edit. You can change your name, age, photos, bio, and more.",
        "ru": "✏️ <b>Изменить профиль?</b>\nЗайди в 👤 Мой профиль → ✏️ Изменить. Можно поменять имя, возраст, фото, описание и т.д.",
    },
    "aide_q3": {
        "fr": "✅ <b>Comment être vérifié·e ?</b>\nDans ⚙️ Paramètres → ✅ Vérifier. Envoie un selfie en faisant un signe de la main 👋. Une fois validé, tu portes le badge ✅ et profites de plus de likes par jour.",
        "en": "✅ <b>How to get verified?</b>\nIn ⚙️ Settings → ✅ Verify. Send a selfie doing a hand wave 👋. Once approved, you wear the ✅ badge and get more likes per day.",
        "ru": "✅ <b>Как пройти подтверждение?</b>\nВ ⚙️ Настройках → ✅ Подтвердить. Отправь селфи с жестом рукой 👋. После одобрения у тебя значок ✅ и больше лайков в день.",
    },
    "aide_q4": {
        "fr": "⚙️ <b>Filtres et pause ?</b>\nDans ⚙️ Paramètres, tu peux régler l'âge et la distance des profils, mettre ton profil en pause, ou le supprimer.",
        "en": "⚙️ <b>Filters and pause?</b>\nIn ⚙️ Settings, you can set the age and distance of profiles, pause your profile, or delete it.",
        "ru": "⚙️ <b>Фильтры и пауза?</b>\nВ ⚙️ Настройках можно настроить возраст и расстояние профилей, поставить профиль на паузу или удалить его.",
    },
    "aide_q5": {
        "fr": "🛡️ <b>Sécurité ?</b>\nSur chaque profil et dans les conversations, tu peux 🚩 Signaler ou 🚫 Bloquer. Nous prenons la sécurité très au sérieux 🌸",
        "en": "🛡️ <b>Safety?</b>\nOn every profile and in conversations, you can 🚩 Report or 🚫 Block. We take safety very seriously 🌸",
        "ru": "🛡️ <b>Безопасность?</b>\nВ каждом профиле и в переписках можно 🚩 Пожаловаться или 🚫 Заблокировать. Мы очень серьёзно относимся к безопасности 🌸",
    },
    "aide_contact": {
        "fr": "📨 <b>Besoin d'aide ?</b>\nÉcris-nous : {contact}",
        "en": "📨 <b>Need help?</b>\nContact us: {contact}",
        "ru": "📨 <b>Нужна помощь?</b>\nНапиши нам: {contact}",
    },
    # ---------- Rappels automatiques ----------
    "rappel_match_attente": {
        "fr": "💞 <b>Tu as un match qui attend !</b>\n\n<b>{prenom}</b> et toi vous êtes plu·e·s… mais la conversation n'a pas encore commencé. 🌸\n\nLance-toi, un petit mot suffit pour briser la glace ! ✨",
        "en": "💞 <b>You have a match waiting!</b>\n\n<b>{prenom}</b> and you liked each other… but the conversation hasn't started yet. 🌸\n\nGo for it, a little word is enough to break the ice! ✨",
        "ru": "💞 <b>Тебя ждёт совпадение!</b>\n\n<b>{prenom}</b> и ты понравились друг другу… но разговор ещё не начался. 🌸\n\nСделай шаг, пары слов хватит, чтобы растопить лёд! ✨",
    },
    "rappel_inactif": {
        "fr": "🌸 <b>De nouveaux cœurs t'attendent sur M_Match !</b>\n\nÇa fait un moment qu'on ne t'a pas vu·e… De nouveaux profils sont peut-être arrivés près de chez toi. 🔥\n\nReviens jeter un œil, ta perle rare est peut-être là ! 💞",
        "en": "🌸 <b>New hearts are waiting for you on M_Match!</b>\n\nIt's been a while since we saw you… New profiles may have arrived near you. 🔥\n\nCome take a look, your special someone might be there! 💞",
        "ru": "🌸 <b>Новые сердца ждут тебя в M_Match!</b>\n\nДавно тебя не было… Возможно, рядом появились новые профили. 🔥\n\nЗагляни, твоя половинка может быть здесь! 💞",
    },
    "rappel_verif": {
        "fr": "✅ <b>Pense à vérifier ton profil !</b>\n\nUn profil vérifié inspire plus confiance et reçoit plus de likes. 🌸\n\nVa dans ⚙️ Paramètres → ✅ Vérifier, c'est rapide ! ✨",
        "en": "✅ <b>Remember to verify your profile!</b>\n\nA verified profile inspires more trust and gets more likes. 🌸\n\nGo to ⚙️ Settings → ✅ Verify, it's quick! ✨",
        "ru": "✅ <b>Не забудь подтвердить профиль!</b>\n\nПодтверждённый профиль вызывает больше доверия и получает больше лайков. 🌸\n\nЗайди в ⚙️ Настройки → ✅ Подтвердить, это быстро! ✨",
    },
    # ---------- Rappels (version simple, sans prénom) ----------
    "rappel_match_attente_simple": {
        "fr": "💞 <b>Tu as un match qui t'attend !</b>\n\nQuelqu'un a flashé sur toi… ne le/la fais pas attendre 🥰\nReviens vite faire un coucou ! ✨",
        "en": "💞 <b>You have a match waiting for you!</b>\n\nSomeone has a crush on you… don't keep them waiting 🥰\nCome back soon and say hi! ✨",
        "ru": "💞 <b>Тебя ждёт совпадение!</b>\n\nКто-то запал на тебя… не заставляй ждать 🥰\nВозвращайся скорее и поздоровайся! ✨",
    },
    "rappel_inactif_simple": {
        "fr": "🌸 <b>On ne t'a pas vu·e depuis un moment…</b>\n\nDe nouveaux profils t'attendent peut-être sur M_Match 🔥\nReviens découvrir qui pourrait te plaire ! 💞",
        "en": "🌸 <b>We haven't seen you in a while…</b>\n\nNew profiles may be waiting for you on M_Match 🔥\nCome back and discover who you might like! 💞",
        "ru": "🌸 <b>Тебя давно не было…</b>\n\nВозможно, в M_Match тебя ждут новые анкеты 🔥\nВозвращайся и посмотри, кто может понравиться! 💞",
    },
    # ---------- Sous-menu Modifier ----------
    "btn_edit_prenom": {"fr": "✏️ Prénom", "en": "✏️ First name", "ru": "✏️ Имя"},
    "btn_edit_age": {"fr": "🎂 Âge", "en": "🎂 Age", "ru": "🎂 Возраст"},
    "btn_edit_genre": {"fr": "💫 Genre", "en": "💫 Gender", "ru": "💫 Пол"},
    "btn_edit_recherche": {"fr": "💘 Recherche", "en": "💘 Looking for", "ru": "💘 Ищу"},
    "btn_edit_localisation": {"fr": "🌍 Localisation", "en": "🌍 Location", "ru": "🌍 Местоположение"},
    "btn_edit_bio": {"fr": "💬 Bio", "en": "💬 Bio", "ru": "💬 Описание"},
    "btn_edit_medias": {"fr": "📸 Mes médias", "en": "📸 My media", "ru": "📸 Мои медиа"},
    "btn_retour": {"fr": "🔙 Retour", "en": "🔙 Back", "ru": "🔙 Назад"},

    # ---------- Choix genre / recherche (inline) ----------
    "ig_homme": {"fr": "👨 Homme", "en": "👨 Man", "ru": "👨 Мужчина"},
    "ig_femme": {"fr": "👩 Femme", "en": "👩 Woman", "ru": "👩 Женщина"},
    "ig_autre": {"fr": "⚧️ Autre", "en": "⚧️ Other", "ru": "⚧️ Другое"},
    "ir_hommes": {"fr": "👨 Hommes", "en": "👨 Men", "ru": "👨 Мужчины"},
    "ir_femmes": {"fr": "👩 Femmes", "en": "👩 Women", "ru": "👩 Женщины"},
    "ir_tous": {"fr": "✨ Tout le monde", "en": "✨ Everyone", "ru": "✨ Все"},
    # ---------- Sous-menu Modifier ----------
    "btn_edit_prenom": {"fr": "✏️ Prénom", "en": "✏️ First name", "ru": "✏️ Имя"},
    "btn_edit_age": {"fr": "🎂 Âge", "en": "🎂 Age", "ru": "🎂 Возраст"},
    "btn_edit_genre": {"fr": "💫 Genre", "en": "💫 Gender", "ru": "💫 Пол"},
    "btn_edit_recherche": {"fr": "💘 Recherche", "en": "💘 Looking for", "ru": "💘 Ищу"},
    "btn_edit_localisation": {"fr": "🌍 Localisation", "en": "🌍 Location", "ru": "🌍 Местоположение"},
    "btn_edit_bio": {"fr": "💬 Bio", "en": "💬 Bio", "ru": "💬 Описание"},
    "btn_edit_medias": {"fr": "📸 Mes médias", "en": "📸 My media", "ru": "📸 Мои медиа"},
    "btn_retour": {"fr": "🔙 Retour", "en": "🔙 Back", "ru": "🔙 Назад"},

    # ---------- Choix genre / recherche (inline) ----------
    "ig_homme": {"fr": "👨 Homme", "en": "👨 Man", "ru": "👨 Мужчина"},
    "ig_femme": {"fr": "👩 Femme", "en": "👩 Woman", "ru": "👩 Женщина"},
    "ig_autre": {"fr": "⚧️ Autre", "en": "⚧️ Other", "ru": "⚧️ Другое"},
    "ir_hommes": {"fr": "👨 Hommes", "en": "👨 Men", "ru": "👨 Мужчины"},
    "ir_femmes": {"fr": "👩 Femmes", "en": "👩 Women", "ru": "👩 Женщины"},
    "ir_tous": {"fr": "✨ Tout le monde", "en": "✨ Everyone", "ru": "✨ Все"},

    # ---------- Boutons du swipe (découverte) ----------
    "sw_passer": {"fr": "👎 Passer", "en": "👎 Pass", "ru": "👎 Пропустить"},
    "sw_jaime": {"fr": "❤️ J'aime", "en": "❤️ Like", "ru": "❤️ Нравится"},
    "sw_signaler": {"fr": "🚩 Signaler", "en": "🚩 Report", "ru": "🚩 Пожаловаться"},
    "sw_bloquer": {"fr": "🚫 Bloquer", "en": "🚫 Block", "ru": "🚫 Заблокировать"},
    "sw_arreter": {"fr": "🔙 Arrêter", "en": "🔙 Stop", "ru": "🔙 Стоп"},
    # ---------- Changement de langue ----------
    "btn_langue": {"fr": "🌍 Langue", "en": "🌍 Language", "ru": "🌍 Язык"},
    "changer_langue": {
        "fr": "🌍 <b>Choisis ta langue</b>\n\nSélectionne la langue de M_Match ci-dessous 👇",
        "en": "🌍 <b>Choose your language</b>\n\nSelect M_Match's language below 👇",
        "ru": "🌍 <b>Выбери язык</b>\n\nВыбери язык M_Match ниже 👇",
    },
    "langue_changee": {
        "fr": "✅ <b>Langue mise à jour !</b>\n\nM_Match te parle maintenant en français 🇫🇷",
        "en": "✅ <b>Language updated!</b>\n\nM_Match now speaks to you in English 🇬🇧",
        "ru": "✅ <b>Язык обновлён!</b>\n\nТеперь M_Match говорит с тобой по-русски 🇷🇺",
    },

    "localisation_gps_obligatoire": {
        "fr": "📍 Pour continuer, appuie sur le bouton <b>« Partager ma position »</b> juste en dessous 👇\n\n<i>C'est nécessaire pour te montrer des profils proches de toi.</i>",
        "en": "📍 To continue, tap the <b>« Share my location »</b> button just below 👇\n\n<i>This is needed to show you profiles near you.</i>",
        "ru": "📍 Чтобы продолжить, нажми кнопку <b>« Поделиться местоположением »</b> чуть ниже 👇\n\n<i>Это нужно, чтобы показывать тебе профили рядом с тобой.</i>",
    },
    "bio_attendue": {
        "fr": "✍️ Écris quelques mots sur toi pour ta bio 🌸\n<i>(juste du texte, pas de photo ici).</i>",
        "en": "✍️ Write a few words about yourself for your bio 🌸\n<i>(text only, no photo here).</i>",
        "ru": "✍️ Напиши пару слов о себе для описания 🌸\n<i>(только текст, без фото).</i>",
    },
    # ---------- Étape numéro / vérification ----------
    "btn_partager_numero": {
        "fr": "📱 Partager mon numéro",
        "en": "📱 Share my number",
        "ru": "📱 Поделиться номером",
    },
    "demande_telephone": {
        "fr": "📱 <b>Dernière étape : vérification</b>\n\nPour la sécurité de tous, partage ton numéro de téléphone en appuyant sur le bouton ci-dessous 👇\n\n<i>Ton numéro reste confidentiel et ne sera jamais affiché sur ton profil.</i>",
        "en": "📱 <b>Last step: verification</b>\n\nFor everyone's safety, share your phone number by tapping the button below 👇\n\n<i>Your number stays private and will never be shown on your profile.</i>",
        "ru": "📱 <b>Последний шаг: проверка</b>\n\nДля безопасности всех поделись своим номером телефона, нажав кнопку ниже 👇\n\n<i>Твой номер останется конфиденциальным и никогда не появится в профиле.</i>",
    },
    "telephone_obligatoire": {
        "fr": "📱 Pour finaliser ton inscription, appuie sur le bouton <b>« Partager mon numéro »</b> ci-dessous 👇\n\n<i>C'est une étape obligatoire pour la sécurité.</i>",
        "en": "📱 To complete your registration, tap the <b>« Share my number »</b> button below 👇\n\n<i>This is a required step for safety.</i>",
        "ru": "📱 Чтобы завершить регистрацию, нажми кнопку <b>« Поделиться номером »</b> ниже 👇\n\n<i>Это обязательный шаг для безопасности.</i>",
    },
    # ---------- Échange de contacts au match ----------
    "contact_username": {
        "fr": "📲 Tu peux contacter <b>{prenom}</b> directement sur Telegram : @{username}\n\nLance-toi… le premier message est souvent le plus beau ! ✨",
        "en": "📲 You can contact <b>{prenom}</b> directly on Telegram: @{username}\n\nGo for it… the first message is often the sweetest! ✨",
        "ru": "📲 Ты можешь связаться с <b>{prenom}</b> напрямую в Telegram: @{username}\n\nСделай шаг… первое сообщение часто самое приятное! ✨",
    },
    "contact_numero": {
        "fr": "📲 Voici le contact de <b>{prenom}</b> 👆\nAppuie dessus pour démarrer la conversation sur Telegram ! ✨",
        "en": "📲 Here is <b>{prenom}</b>'s contact 👆\nTap it to start the conversation on Telegram! ✨",
        "ru": "📲 Вот контакт <b>{prenom}</b> 👆\nНажми, чтобы начать разговор в Telegram! ✨",
    },
    "contact_indispo": {
        "fr": "💞 Tu as matché avec <b>{prenom}</b> ! Malheureusement, son contact n'est pas disponible pour le moment. 🌸",
        "en": "💞 You matched with <b>{prenom}</b>! Unfortunately, their contact isn't available right now. 🌸",
        "ru": "💞 У тебя совпадение с <b>{prenom}</b>! К сожалению, их контакт сейчас недоступен. 🌸",
    },
    "match_titre": {
        "fr": "💞✨ <b>C'EST UN MATCH !</b> ✨💞\n\n<b>{prenom}</b> et toi vous plaisez ! 🥰\n\nVoici son contact juste en dessous 👇\nLance-toi… le premier message est souvent le plus beau ! 💌",
        "en": "💞✨ <b>IT'S A MATCH!</b> ✨💞\n\nYou and <b>{prenom}</b> liked each other! 🥰\n\nHere is their contact just below 👇\nGo for it… the first message is often the sweetest! 💌",
        "ru": "💞✨ <b>ЭТО СОВПАДЕНИЕ!</b> ✨💞\n\nТы и <b>{prenom}</b> понравились друг другу! 🥰\n\nВот их контакт чуть ниже 👇\nСделай шаг… первое сообщение часто самое приятное! 💌",
    },
    "btn_voir_contact": {
        "fr": "📲 Contacter {prenom}",
        "en": "📲 Contact {prenom}",
        "ru": "📲 Связаться с {prenom}",
    },
    # ---------- Carte de contact (lien Telegram, sans numéro) ----------
    "carte_contact": {
        "fr": "╭───────────────╮\n   📲 <b>{prenom}</b>\n   👉 <a href=\"https://t.me/{username}\">Ouvrir la conversation</a>\n╰───────────────╯\n\n<i>Clique sur le lien pour discuter directement sur Telegram 💬</i>",
        "en": "╭───────────────╮\n   📲 <b>{prenom}</b>\n   👉 <a href=\"https://t.me/{username}\">Open the chat</a>\n╰───────────────╯\n\n<i>Tap the link to chat directly on Telegram 💬</i>",
        "ru": "╭───────────────╮\n   📲 <b>{prenom}</b>\n   👉 <a href=\"https://t.me/{username}\">Открыть чат</a>\n╰───────────────╯\n\n<i>Нажми на ссылку, чтобы общаться прямо в Telegram 💬</i>",
    },
    "contact_sans_username": {
        "fr": "💞 Tu as matché avec <b>{prenom}</b> ! Mais cette personne n'a pas encore de nom d'utilisateur Telegram public, le contact n'est pas disponible pour le moment. 🌸",
        "en": "💞 You matched with <b>{prenom}</b>! But this person doesn't have a public Telegram username yet, so the contact isn't available right now. 🌸",
        "ru": "💞 У тебя совпадение с <b>{prenom}</b>! Но у этого человека пока нет публичного имени пользователя Telegram, поэтому контакт недоступен. 🌸",
    },
    # ---------- Encouragement username ----------
    "rappel_username_ok": {
        "fr": "✅ <b>Parfait !</b> Ton nom d'utilisateur Telegram (@{username}) permettra à tes matchs de te contacter facilement. 🌸",
        "en": "✅ <b>Perfect!</b> Your Telegram username (@{username}) will let your matches contact you easily. 🌸",
        "ru": "✅ <b>Отлично!</b> Твоё имя пользователя Telegram (@{username}) позволит твоим совпадениям легко связаться с тобой. 🌸",
    },
    "rappel_username_manquant": {
        "fr": "⚠️ <b>Petit point important !</b>\n\nTu n'as pas encore de <b>nom d'utilisateur Telegram</b>. Sans lui, tes matchs ne pourront pas te contacter ! 😔\n\n<b>Comment en créer un (1 minute) :</b>\n1️⃣ Va dans les <b>Réglages</b> de Telegram\n2️⃣ Touche <b>« Nom d'utilisateur »</b>\n3️⃣ Choisis un nom (ex : @julie_paris)\n\nFais-le maintenant, puis reviens ici 🌸\n<i>C'est ce qui te permettra de rencontrer du monde !</i>",
        "en": "⚠️ <b>Important note!</b>\n\nYou don't have a <b>Telegram username</b> yet. Without it, your matches won't be able to contact you! 😔\n\n<b>How to create one (1 minute):</b>\n1️⃣ Go to Telegram <b>Settings</b>\n2️⃣ Tap <b>« Username »</b>\n3️⃣ Choose a name (e.g. @julie_paris)\n\nDo it now, then come back here 🌸\n<i>This is what will let you meet people!</i>",
        "ru": "⚠️ <b>Важный момент!</b>\n\nУ тебя ещё нет <b>имени пользователя Telegram</b>. Без него твои совпадения не смогут связаться с тобой! 😔\n\n<b>Как создать (1 минута):</b>\n1️⃣ Зайди в <b>Настройки</b> Telegram\n2️⃣ Нажми <b>« Имя пользователя »</b>\n3️⃣ Выбери имя (напр. @julie_paris)\n\nСделай это сейчас, затем вернись сюда 🌸\n<i>Именно это позволит тебе знакомиться!</i>",
    },


}





def t(user_id, cle, **kwargs):
    """Renvoie le texte traduit dans la langue de l'utilisateur."""
    langue = get_langue(user_id)
    textes = TRADUCTIONS.get(cle, {})
    texte = textes.get(langue) or textes.get("fr") or cle
    if kwargs:
        texte = texte.format(**kwargs)
    return texte