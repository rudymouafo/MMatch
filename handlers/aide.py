from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command

import config
from traductions import t

router = Router()


async def envoyer_aide(message, user_id):
    texte = (
        t(user_id, "aide_titre") + "\n\n"
        + t(user_id, "aide_q1") + "\n\n"
        + t(user_id, "aide_q2") + "\n\n"
        + t(user_id, "aide_q3") + "\n\n"
        + t(user_id, "aide_q4") + "\n\n"
        + t(user_id, "aide_q5") + "\n\n"
        + t(user_id, "aide_contact", contact=config.CONTACT_SUPPORT)
    )
    await message.answer(texte)


@router.message(Command("aide", "help"))
async def cmd_aide(message: Message):
    await envoyer_aide(message, message.from_user.id)


@router.message(F.text == "❓ Aide")
async def raccourci_aide(message: Message):
    await envoyer_aide(message, message.from_user.id)