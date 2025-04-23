from aiogram import Bot
from aiogram import Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.fsm.storage.redis import RedisStorage
from pydantic_settings import BaseSettings
from supabase import Client, create_client

from src.repo.PChildrenDataRepo import PChildrenDataRepository
from src.repo.ParentDataRepo import ParentDataRepository
from src.repo.PupilDataRepo import PupilDataRepository
from src.repo.TeacherDataRepo import TeacherDataDataRepository
from src.repo.UserDataRepo import UserDataRepository


class Secrets(BaseSettings):
    token: str
    admin_id: int
    supabase_url: str
    supabase_key: str
    redis_url: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


secrets = Secrets()

channel_id = -1002500913902  # -1002406861510  # Канал для проверки
admin_group = -1002500913902  # Группа админов
pupil_thread = 2
parent_thread = 3
teacher_thread = 0

# Инициализация подключения к базе данных Supabase
url: str = secrets.supabase_url
key: str = secrets.supabase_key

# Создание клиента Supabase
supabase: Client = create_client(url, key)

users_data_repo = UserDataRepository(supabase)
pupil_data_repo = PupilDataRepository(supabase)
parent_data_repo = ParentDataRepository(supabase)
pchildren_data_repo = PChildrenDataRepository(supabase)
teacher_data_repo = TeacherDataDataRepository(supabase)

# Инициализация бота
default = DefaultBotProperties(parse_mode='HTML', protect_content=False)
bot = Bot(token=secrets.token, default=default)
#storage = RedisStorage.from_url(secrets.redis_url)
dp = Dispatcher()#storage=storage)
