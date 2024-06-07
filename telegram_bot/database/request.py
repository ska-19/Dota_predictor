from database.models import Users
import joblib
import pandas as pd
import xgboost as xgb


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


async def get_prediction(req_data: dict):
    model_file_path = './database/xgboost_model_pipeline.joblib'
    loaded_model_pipeline = joblib.load(model_file_path)
    new_data = {}
    for key, value in req_data.items():
        new_data[str(int(str(key)[1:])-1)] = value
    new_data_df = pd.DataFrame([new_data])
    prediction = loaded_model_pipeline.predict_proba(new_data_df)[:, 1]
    return prediction