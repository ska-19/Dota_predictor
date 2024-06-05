from sqlalchemy.orm import DeclarativeBase, mapped_column
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncAttrs

class Base(AsyncAttrs, DeclarativeBase):
    pass

class User:
    def __init__(self, tg_id: int, username: str = ' '):
        self.id = tg_id
        self.username = username
        self.name = 'name'
        self.surname = 'username'
        self.user_login = None
        self.user_password = None

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "name": self.name,
            "surname": self.surname,
            "user_login": self.user_login,
            "user_password": self.user_password
        }
    def __repr__(self):
        return f"User_r {self.username}"

    def __str__(self):
        return f"User_s {self.username}"

    def __eq__(self, other):
        return self.id == other.id

    def get_login(self):
        return self.user_login


class UsersC:
    def __init__(self):
        self.dict = {}

    def add_user(self, user: User):
        self.dict[user.id] = user
    def create_user(self, tg_id: int, username: str = ' '):
        self.dict[tg_id] = User(tg_id, username)

    def get_user(self, tg_id:int):
        user: User = self.dict[tg_id]
        return user

Users = UsersC()
