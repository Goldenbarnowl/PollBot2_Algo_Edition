from typing import Optional, Any

from postgrest import APIResponse
from supabase import Client, create_client


class PupilDataRepository:
    def __init__(self, supabase: Client):
        self.supabase = supabase

    def insert_field(self, chat_id: int):
        """Вставить указанное значение в указанное поле в таблице UserData"""
        self.supabase.table("PupilData").insert({"chat_id": chat_id}).execute()

    def update_field(self, chat_id: int, field: str, value: str or list):
        """Обновить указанное значение в указанном поле в таблице UserData"""
        self.supabase.table("PupilData").update({field: value}).eq("chat_id", chat_id).execute()

    def get_user_by_chat_id(self, chat_id: int) -> APIResponse[Any]:
        """Получить данные пользователя по chat_id"""
        return self.supabase.table("PupilData").select("*").eq("chat_id", chat_id).execute()

    def delete_all_user_data(self, chat_id: int):
        """Удалить все данные пользователя по chat_id"""
        self.supabase.table("PupilData").delete().eq("chat_id", chat_id).execute()

    def get_all_users(self) -> APIResponse[Any]:
        """Получить список всех пользователей с нужными полями"""
        return self.supabase.table("PupilData").select("chat_id").execute()
