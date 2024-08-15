import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def is_visible_by_locator(self, locator):
        try:
            element = WebDriverWait(self.driver, 10, poll_frequency=1).until(EC.visibility_of_element_located(locator))
            return bool(element)
        except:
            return False

    def find_element(self, locator):
        element = self.driver.find_element(*locator)
        return element

    def find_elements(self, locator):
        elements = self.driver.find_elements(*locator)
        return elements

    def click_element(self, element):
        element.click()

    def input_text(self, locator, text):
        self.find_element(locator).send_keys(text)

    def send_key_enter(self, locator):
        self.find_element(locator).send_keys(Keys.ENTER)

    def scroll(self, direction):
        action = ActionChains(self.driver)
        if direction == 'up':
            action.move_by_offset(0, -100)
        elif direction == 'down':
            action.move_by_offset(0, 100)
        elif direction == 'left':
            action.move_by_offset(-100, 0)
        elif direction == 'right':
            action.move_by_offset(100, 0)
        else:
            return Exception(f"Invalid direction to scroll: '{direction}'")

    def take_screenshot(self):
        self.driver.save_screenshot('Screenshots/twitch.png')
