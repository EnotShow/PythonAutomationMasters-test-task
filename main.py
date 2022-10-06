import time

from aiogram.utils import executor

from bot import send_post, dp
from config import _user_email, _user_password, _base_site, _captcha_page, _login_page
from parse import auth, get_post


async def on_startup(_):
    auth()
    current_post = get_post()[0]
    while True:
        time.sleep(5)
        post_title, post_link = get_post()
        if current_post == post_title:
            await send_post(post_title, post_link)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
