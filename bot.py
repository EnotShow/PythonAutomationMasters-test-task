from aiogram import Bot, Dispatcher, types

from config import _API_TOKEN, _CHANEL_ID, _base_site

bot = Bot(token=_API_TOKEN)
dp = Dispatcher(bot)


async def send_post(post_title, post_url):
    await bot.send_message(_CHANEL_ID, f"{post_title}\n\n{_base_site + post_url}")
