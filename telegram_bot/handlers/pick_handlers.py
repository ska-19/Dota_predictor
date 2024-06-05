import io
from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message, CallbackQuery, BufferedInputFile

from bot_instance import bot
from keyboards.user_keyboards import get_main_ikb, get_back_button
from database import request as rq

router = Router()

dota_heroes = ['abaddon', 'alchemist', 'ancient_apparition', 'anti_mage', 'arc_warden', 'axe', 'bane', 'batrider',
               'beastmaster', 'bloodseeker', 'bounty_hunter', 'brewmaster', 'bristleback', 'broodmother',
               'centaur_warrunner', 'chaos_knight', 'chen', 'clinkz', 'clockwerk', 'crystal_maiden', 'dark_seer',
               'dazzle', 'death_prophet', 'disruptor', 'doom', 'dragon_knight', 'drow_ranger', 'earth_spirit',
               'earthshaker', 'elder_titan', 'ember_spirit', 'enchantress', 'enigma', 'faceless_void', 'gyrocopter',
               'huskar', 'invoker', 'io', 'jakiro', 'juggernaut', 'keeper_of_the_light', 'kunkka', 'legion_commander',
               'leshrac', 'lich', 'lifestealer', 'lina', 'lion', 'lone_druid', 'luna', 'lycan', 'magnus', 'medusa',
               'meepo', 'mirana', 'morphling', 'naga_siren', 'natures_prophet', 'necrophos', 'night_stalker',
               'nyx_assassin', 'ogre_magi', 'omniknight', 'oracle', 'outworld_devourer', 'phantom_assassin',
               'phantom_lancer', 'phoenix', 'puck', 'pudge', 'pugna', 'queen_of_pain', 'razor', 'riki', 'rubick',
               'sand_king', 'shadow_demon', 'shadow_fiend', 'shadow_shaman', 'silencer', 'skywrath_mage', 'slardar',
               'slark', 'sniper', 'spectre', 'spirit_breaker', 'storm_spirit', 'sven', 'techies', 'templar_assassin',
               'terrorblade', 'tidehunter', 'timbersaw', 'tinker', 'tiny', 'treant_protector', 'troll_warlord', 'tusk',
               'underlord', 'undying', 'ursa', 'vengeful_spirit', 'venomancer', 'viper', 'visage', 'warlock', 'weaver',
               'windranger', 'winter_wyvern', 'witch_doctor', 'wraith_king', 'zeus']


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
        await state.clear()
        await message.answer(
            text=f"Вероятность победы команды света: 50%\n\n"
                 f"{req_data}",
        )
    else:
        await message.answer(
            text="Персонаж не найден, попробуйте еще раз"
        )