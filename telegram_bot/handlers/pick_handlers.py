import io
from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message, CallbackQuery, BufferedInputFile

from bot_instance import bot
from keyboards.user_keyboards import get_main_ikb, get_back_button
from database import request as rq
from database.models import dota_heroes

router = Router()

class PickState(StatesGroup):
    p1 = State()
    p2 = State()
    p3 = State()
    p4 = State()
    p5 = State()
    p6 = State()
    p7 = State()
    p8 = State()
    p9 = State()
    p10 = State()

@router.callback_query(F.data == "get_prediction")
async def cmd_reg_user(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer(
        text="Укажите первого персонажа команды света в формате:\n"
             "/+имя персонажа на английском, вместо пробелов используйте '_'",
    )
    await state.set_state(PickState.p1)

# comadn /+hero_name
@router.message(PickState.p1)
async def cmd_p1(message: Message, state: FSMContext):
    hero = message.text[1:]
    if hero in dota_heroes:
        await state.update_data(p1=hero)
        await message.answer(
            text="Укажите второго персонажа команды света:\n"
        )
        await state.set_state(PickState.p2)
    else:
        await message.answer(
            text="Персонаж не найден, попробуйте еще раз"
        )

@router.message(PickState.p2)
async def cmd_p2(message: Message, state: FSMContext):
    hero = message.text[1:]
    if hero in dota_heroes:
        await state.update_data(p2=hero)
        await message.answer(
            text="Укажите третьего персонажа команды света:\n"
        )
        await state.set_state(PickState.p3)
    else:
        await message.answer(
            text="Персонаж не найден, попробуйте еще раз"
        )

@router.message(PickState.p3)
async def cmd_p3(message: Message, state: FSMContext):
    hero = message.text[1:]
    if hero in dota_heroes:
        await state.update_data(p3=hero)
        await message.answer(
            text="Укажите четвертого персонажа команды света:\n"
        )
        await state.set_state(PickState.p4)
    else:
        await message.answer(
            text="Персонаж не найден, попробуйте еще раз"
        )

@router.message(PickState.p4)
async def cmd_p4(message: Message, state: FSMContext):
    hero = message.text[1:]
    if hero in dota_heroes:
        await state.update_data(p4=hero)
        await message.answer(
            text="Укажите пятого персонажа команды света:\n"
        )
        await state.set_state(PickState.p5)
    else:
        await message.answer(
            text="Персонаж не найден, попробуйте еще раз"
        )

@router.message(PickState.p5)
async def cmd_p5(message: Message, state: FSMContext):
    hero = message.text[1:]
    if hero in dota_heroes:
        await state.update_data(p5=hero)
        await message.answer(
            text="Укажите первого персонажа команды тьмы",
        )
        await state.set_state(PickState.p6)
    else:
        await message.answer(
            text="Персонаж не найден, попробуйте еще раз"
        )

@router.message(PickState.p6)
async def cmd_p6(message: Message, state: FSMContext):
    hero = message.text[1:]
    if hero in dota_heroes:
        await state.update_data(p6=hero)
        await message.answer(
            text="Укажите второго персонажа команды тьмы",
        )
        await state.set_state(PickState.p7)
    else:
        await message.answer(
            text="Персонаж не найден, попробуйте еще раз"
        )


@router.message(PickState.p7)
async def cmd_p7(message: Message, state: FSMContext):
    hero = message.text[1:]
    if hero in dota_heroes:
        await state.update_data(p7=hero)
        await message.answer(
            text="Укажите третьего персонажа команды тьмы",
        )
        await state.set_state(PickState.p8)
    else:
        await message.answer(
            text="Персонаж не найден, попробуйте еще раз"
        )

@router.message(PickState.p8)
async def cmd_p8(message: Message, state: FSMContext):
    hero = message.text[1:]
    if hero in dota_heroes:
        await state.update_data(p8=hero)
        await message.answer(
            text="Укажите четвертого персонажа команды тьмы",
        )
        await state.set_state(PickState.p9)
    else:
        await message.answer(
            text="Персонаж не найден, попробуйте еще раз"
        )


@router.message(PickState.p9)
async def cmd_p9(message: Message, state: FSMContext):
    hero = message.text[1:]
    if hero in dota_heroes:
        await state.update_data(p9=hero)
        await message.answer(
            text="Укажите пятого персонажа команды тьмы",
        )
        await state.set_state(PickState.p10)
    else:
        await message.answer(
            text="Персонаж не найден, попробуйте еще раз"
        )


@router.message(PickState.p10)
async def cmd_p10(message: Message, state: FSMContext):
    hero = message.text[1:]
    if hero in dota_heroes:
        await state.update_data(p10=hero)
        await message.answer(
            text="Отлично, ожидайте результатов",
        )
        req_data = await state.get_data()
        prediction = await rq.get_prediction(req_data)
        await state.clear()
        await message.answer(
            text=f"Вероятность победы команды света: {str(prediction * 100)[1:-1]}%\n\n"
                    f"Персонажи команды света:\n"
                    f"{req_data['p1']}\n"
                    f"{req_data['p2']}\n"
                    f"{req_data['p3']}\n"
                    f"{req_data['p4']}\n"
                    f"{req_data['p5']}\n\n"
                    f"Персонажи команды тьмы:\n"
                    f"{req_data['p6']}\n"
                    f"{req_data['p7']}\n"
                    f"{req_data['p8']}\n"
                    f"{req_data['p9']}\n"
                    f"{req_data['p10']}\n",
        reply_markup = get_main_ikb()
        )
    else:
        await message.answer(
            text="Персонаж не найден, попробуйте еще раз"
        )