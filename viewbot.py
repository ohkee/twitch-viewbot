from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import random

def create_driver():
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_argument("--window-size=100,50")
    options.add_argument('--headless')
    options.add_argument('--disable-logging')
    options.add_argument('--disable-gpu') 
    options.add_argument('--log-level=3')
    options.add_argument("--mute-audio")
    options.add_argument('--disable-extensions')
    options.add_argument('--disable-plugins')
    options.add_argument('--disable-dev-shm-usage')
    service = Service('Driver/chromedriver.exe')
    return webdriver.Chrome(service=service, options=options)

def randomize_server(): 
    servers = ['https://www.croxyproxy.com/','https://proxyium.com/', 'https://www.croxy.org/', 'https://www.blockaway.net/', 'https://www.youtubeunblocked.live/']
    return random.choice(servers)

def start_viewbot(stop_flag, platform, channel_name, number_of_viewers):
    driver = create_driver()
    viewbot_running = False

    while not stop_flag.is_set():
        if not viewbot_running:
            viewbot_running = True

            for _ in range(number_of_viewers):
                if stop_flag.is_set():  
                    break
                driver.switch_to.new_window('window')
                driver.get(randomize_server())
                driver.implicitly_wait(2)

                input_box = driver.find_element(by=By.NAME, value='url')
                input_box.send_keys(f'{platform}.tv/{channel_name}')
                input_box.send_keys(Keys.RETURN)

                driver.implicitly_wait(5)