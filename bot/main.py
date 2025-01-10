from aiogram import Bot, Dispatcher, types,F
from aiogram.types import Message
from buttons import button
from aiogram.filters import CommandStart
from api import create_user,create_feedback
from states  import FeedboksStates
from aiogram.fsm.context import FSMContext
from aiogram.filters import StateFilter


BOT_TOKEN = "7150380677:AAHOQ-WwfPN1Xd-W4_-KOhLXJPT0aWLgh0M"

from aiogram.fsm.storage.memory import MemoryStorage

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(storage=MemoryStorage())


@dp.message(CommandStart())
async def start_command(message: Message):
     await message.answer("Assalomu alaykum",reply_markup=button)
     print(create_user(message.from_user.username, message.from_user.first_name, message.from_user.id))


@dp.message(F.text == "Savol va takliflar")
async def feedbock_1(message: types.Message, state: FSMContext):
    await message.answer("Xabar yuboring")
    await state.set_state(FeedboksStates.body)


@dp.message(StateFilter(FeedboksStates.body))
async def feedbock_2(message: types.Message, state: FSMContext):
    await message.answer(create_feedback(message.from_user.id, message.text))
    await state.clear()


# @dp.message()
# async def echo_message(message: Message):
#     await message.reply(message.text)



# Botni ishga tushirish
async def main():
    print("Bot ishga tushdi!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
