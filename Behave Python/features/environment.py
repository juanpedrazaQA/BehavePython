from selenium import webdriver
import os


def before_all(context):

    context.timeout = 15

    options = webdriver.ChromeOptions()
    options.add_argument('--incognito')
    options.add_argument('--allow-running-insecure-content')
    options.add_argument('--disable-web-security')

    driver_path = os.environ.get('ChromeDriver')
    print(f'The driver path is {driver_path}')
    context.driver = webdriver.Chrome(driver_path, chrome_options=options)


def after_all(context):
    try:
        context.driver.quit()
    except:
        print("The connection wasn't done, so the driver was not even instanced")
