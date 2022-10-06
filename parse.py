from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()


def auth():
    driver.get(_login_page)

    email_field = driver.find_element(by=By.ID, value='customer_email')
    email_field.send_keys(_user_email)

    password_field = driver.find_element(by=By.ID, value='customer_password')
    password_field.send_keys(_user_password)
    password_field.send_keys(Keys.ENTER)

    # Here we can use captcha solve service or captcha handle input
    while True:

        # if driver.current_url == _captcha_page:
        #     solve_captcha()

        # In this case we are waiting for user input
        if driver.current_url == 'https://www.tesmanian.com/account':
            return None


def get_post():
    if driver.current_url != _base_site:
        driver.get(_base_site)
    else:
        driver.refresh()

    post = driver.find_element(by=By.CLASS_NAME, value='article').find_element(by=By.CLASS_NAME, value='sub_title')

    post_title = post.text

    post_link = post.find_element(by=By.CSS_SELECTOR, value='a').get_attribute('href')
    print(post_link, 'post link!')
    return post_title, post_link
