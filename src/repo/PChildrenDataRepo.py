from typing import Optional, Any

from postgrest import APIResponse
from supabase import Client, create_client


class PChildrenDataRepository:
    def __init__(self, supabase: Client):
        self.supabase = supabase

    def insert_field(self, chat_id: int, field: str, value: str or list or bool):
        """Вставить указанное значение в указанное поле в таблице UserData"""
        self.supabase.table("PChildren").insert({"chat_id": chat_id, "check": False, field: value}).execute()

    def update_field(self, chat_id: int, field: str, value: str or list):
        """Обновить указанное значение в указанном поле в таблице UserData"""
        self.supabase.table("PChildren").update({field: value}).eq("chat_id", chat_id).eq("check", False).execute()

    def get_user_by_chat_id(self, chat_id: int) -> APIResponse[Any]:
        """Получить данные пользователя по chat_id"""
        return self.supabase.table("PChildren").select("*").eq("chat_id", chat_id).eq("check", False).execute()

    def get_user_by_chat_id_all(self, chat_id: int) -> APIResponse[Any]:
        """Получить данные пользователя по chat_id"""
        return self.supabase.table("PChildren").select("*").eq("chat_id", chat_id).execute()

    def delete_all_user_data(self, chat_id: int):
        """Удалить все данные пользователя по chat_id"""
        self.supabase.table("PChildren").delete().eq("chat_id", chat_id).eq("check", False).execute()

    def get_all_users(self) -> APIResponse[Any]:
        """Получить список всех пользователей с нужными полями"""
        return self.supabase.table("PChildren").select("chat_id").execute()
