import asyncio

import config
from traductions import t
from database import (
    profils_a_relancer,
    noter_rappel,
    a_match_non_ouvert,
    likes_recus_en_attente,
)


async def boucle_rappels(bot):
    """Tâche de fond : envoie des rappels aux utilisateurs inactifs."""
    # petite attente au démarrage pour laisser le bot s'initialiser
    await asyncio.sleep(10)

    while True:
        try:
            a_relancer = profils_a_relancer(
                config.RAPPEL_INACTIF_APRES,
                config.RAPPEL_PAS_AVANT,
            )
            for uid, profil in a_relancer:
                # On choisit le message le plus accrocheur selon la situation
                nb_likes = likes_recus_en_attente(uid)
                if nb_likes > 0:
                    # Priorité : des gens l'ont liké → ça donne envie de revenir
                    texte = t(uid, "rappel_likes_attente", n=nb_likes)
                elif a_match_non_ouvert(uid):
                    texte = t(uid, "rappel_match_attente_simple")
                else:
                    texte = t(uid, "rappel_inactif_simple")
                try:
                    await bot.send_message(int(uid), texte)
                    noter_rappel(uid)
                except Exception:
                    # l'utilisateur a peut-être bloqué le bot : on ignore
                    pass
                # petite pause entre chaque envoi pour ne pas saturer
                await asyncio.sleep(0.3)
        except Exception:
            pass

        # On attend l'intervalle avant la prochaine vérification
        await asyncio.sleep(config.RAPPEL_INTERVALLE_VERIF * 3600)