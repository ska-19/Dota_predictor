from database.models import Users


async def set_user(tg_id:int, user_data: dict):
    Users.create_user(tg_id, user_data['username'])
    user = Users.get_user(tg_id)
    user.name = user_data['name']
    user.surname = user_data['surname']
    return user

async def get_user(tg_id:int):
    user = Users.get_user(tg_id)
    return user

async def reg_user(user_data: dict):
    user = Users.get_user(user_data['tg_id'])
    user.user_login = user_data['login']
    user.user_password = user_data['password']
    user.username = user_data['username']
    user.name = user_data['name']
    user.surname = user_data['surname']

    return user