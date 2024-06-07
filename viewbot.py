import time
import random

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# Configuration
TWITCH_NAME = 'twitch.tv/gweng1'
NUMBER_OF_VIEWERS = 30

def create_driver():
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
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
    servers = ['https://www.croxyproxy.com/','https://proxyium.com/', 'https://www.croxy.org/', 'https://www.blockaway.net/']
    return random.choice(servers)

if __name__ == "__main__":

    driver = create_driver()

    for x in range(NUMBER_OF_VIEWERS):
        driver.switch_to.new_window('window')
        driver.get(randomize_server())
        driver.implicitly_wait(2)

        input_box = driver.find_element(by=By.NAME, value='url')
        input_box.send_keys(TWITCH_NAME)
        input_box.send_keys(Keys.RETURN)
        driver.implicitly_wait(2)

    # Keep the script running to keep all browser windows open
    try:
        while True:
            time.sleep(60)    
    except KeyboardInterrupt:
       # Close all drivers on exit
        print("All browser windows have been closed.")
        driver.quit()