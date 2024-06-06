import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# Configuration
TWITCH_NAME = 'twitch.tv/gweng1'
NUMBER_OF_VIEWERS = 5

if __name__ == "__main__":

    drivers = []
    
    for x in range(NUMBER_OF_VIEWERS):
        # Creates headless environment
        options = Options()
        #options.add_argument("--headless=new")

        # Sets up Chrome service
        service = Service('Driver/chromedriver.exe')

        # Creates Chrome driver and adds to the list
        driver = webdriver.Chrome(service=service, options=options)
        drivers.append(driver)

        # Gets web proxy
        driver.get('https://proxyium.com/')
        driver.implicitly_wait(2)

        # Finds input object
        input_box = driver.find_element(by=By.NAME, value='url')
        input_box.send_keys(TWITCH_NAME)

        # Clicks submit
        submit_button = driver.find_element(by=By.ID, value='unique-btn-blue')
        submit_button.click()

        driver.implicitly_wait(5)


        # DEBUG
        #print('')

    # Keep the script running to keep all browser windows open
    try:
        while True:
            time.sleep(1)    
    except KeyboardInterrupt:
        # Quit all drivers on exit
        for driver in drivers:
            driver.quit()