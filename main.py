import asyncio
from os import getenv

from mistralai import Mistral
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message

TOKEN = getenv("TOKEN")
api_key = getenv("MISTRAL_API_KEY")

model = "mistral-large-latest"

client = Mistral(api_key=api_key)

dp = Dispatcher()


# Command handler
@dp.message(Command("start"))
async def command_start_handler(message: Message) -> None:
    await message.answer("Я AI бот, который работает 24/7.")


@dp.message(lambda msg: msg.text)
async def mistral_ai(message: Message) -> None:
    chat_response = client.chat.complete(
        model=model,
        messages=[
            {
                "role": "system",
                "content": "",
            },
            {
                "role": "user",
                "content": message.text,
            },
        ]
    )
    await message.answer(chat_response.choices[0].message.content, parse_mode="Markdown")


# Run the bot
async def main() -> None:
    bot = Bot(token=TOKEN)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
