import io
from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message, CallbackQuery, BufferedInputFile

from bot_instance import bot
from keyboards.user_keyboards import get_main_ikb, get_back_button
from database import request as rq

router = Router()


class RegUeser(StatesGroup):
    enter_login = State()
    enter_password = State()


@router.callback_query(F.data == "reg_user")
async def cmd_reg_user(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer(
        text="🎩 <b>Укажите логин:</b>\n",
        reply_markup=get_back_button()
    )
    await state.set_state(RegUeser.enter_login)
    await callback.message.delete()


@router.message(RegUeser.enter_login)
async def cmd_enter_login(message: Message, state: FSMContext):
    await state.update_data(login=message.text)
    await message.answer(
        text="🔑 <b>Укажите пароль:</b>\n",
        reply_markup=get_back_button()
    )
    await state.set_state(RegUeser.enter_password)
    await message.delete()


@router.message(RegUeser.enter_password)
async def cmd_enter_password(message: Message, state: FSMContext):
    await state.update_data(password=message.text)
    user_data = await state.get_data()
    user_data['tg_id'] = message.from_user.id
    user_data['username'] = message.from_user.username
    user_data['name'] = message.from_user.first_name
    user_data['surname'] = message.from_user.last_name
    await rq.reg_user(user_data)
    await message.answer(
        text="🎉 <b>Регистрация прошла успешно!</b>",
        reply_markup=get_main_ikb(user_data)
    )
    await state.clear()

@router.callback_query(F.data == "back")
async def cmd_back(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer(
        text="<b>Вы прервали создание клуба</b>",
        reply_markup=get_main_ikb({'tg_id': callback.from_user.id})
    )
    await state.clear()