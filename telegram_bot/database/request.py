from database.models import Users
import joblib
import pandas as pd
import xgboost as xgb

from  handlers.pick_handlers import dota_heroes
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
    encoder_file_path = './database/onehot_encoder.joblib'
    loaded_model_pipeline = joblib.load(model_file_path)
    loaded_encoder = joblib.load(encoder_file_path)
    first_five_cols = ['0', '1', '2', '3', '4']
    last_five_cols = ['5', '6', '7', '8', '9']

    new_data = {}
    for key, value in req_data.items():
        new_data[str(int(str(key)[1:])-1)] = value
    new_data_df = pd.DataFrame([new_data])

    new_first_five_encoded = loaded_encoder.transform(new_data_df[first_five_cols].values.reshape(-1, 1)).reshape(
        new_data_df.shape[0], -1, len(loaded_encoder.categories_[0])).sum(axis=1)
    new_last_five_encoded = loaded_encoder.transform(new_data_df[last_five_cols].values.reshape(-1, 1)).reshape(
        new_data_df.shape[0], -1, len(loaded_encoder.categories_[0])).sum(axis=1)

    new_combined_encoded = new_first_five_encoded - new_last_five_encoded

    encoded_columns = [f'hero_{cat}' for cat in dota_heroes]
    new_encoded_df = pd.DataFrame(new_combined_encoded, columns=encoded_columns)

    prediction = loaded_model_pipeline.predict_proba(new_encoded_df)[:, 1]
    return prediction