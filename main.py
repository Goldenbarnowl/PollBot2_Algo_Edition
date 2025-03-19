import asyncio
import logging
import sys

from aiogram.methods import DeleteWebhook

from config import dp, bot
from src.routers.last_stand import last_stand_router
from src.routers.parent_handlers import parent_router
from src.routers.pupil_handlers import pupil_router
from src.routers.teacher_handlers import teacher_router
from src.routers.user_handlers import user_router


async def start():
    dp.include_router(user_router)
    dp.include_router(pupil_router)
    dp.include_router(parent_router)
    dp.include_router(teacher_router)
    dp.include_router(last_stand_router)
    try:
        await bot(DeleteWebhook(drop_pending_updates=True))
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(start())
