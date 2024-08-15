import random
import time
from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class Twitch(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.twitch_icon = (By.XPATH, "//nav/a")
        self.search_icon = (By.XPATH, "//a[@href='/search']")
        self.search_input = (By.XPATH, "//input")
        self.tabs = {
            'Top': (By.XPATH, "//li/a/div[.='Top']"),
            'Channels' : (By.XPATH, "//li/a/div[.='Channels']"),
            'Categories': (By.XPATH, "//li/a/div[.='Categories']"),
            'Videos': (By.XPATH, "//li/a/div[.='Videos']")
        }
        self.channels_list = (By.XPATH, "//div[@role='list']")
        self.channels = (By.XPATH, "//div[@role='list']/div/a")
        self.video_loading_spinner = (By.XPATH, "//div[@class='ScLoadingSpinnerCircle-sc-bvzaq8-1 emCEDE']")

    def login_visibility(self):
        return self.is_visible_by_locator(self.twitch_icon)

    def click_search_icon(self):
        icon = self.find_element(self.search_icon)
        self.click_element(icon)

    def search_by_text(self, text):
        self.input_text(self.search_input, text)
        self.send_key_enter(self.search_input)

    def click_tab(self, text):
        tab_locator = self.tabs[text]
        tab = self.find_element(tab_locator)
        self.click_element(tab)

    def wait_for_list(self):
        return self.is_visible_by_locator(self.channels_list)

    def select_any_streamer(self):
        channels = self.find_elements(self.channels)
        channel = random.choice(channels)
        self.click_element(channel)

    def wait_channel_loading(self):
        try:
            if bool(self.is_visible_by_locator(self.video_loading_spinner)):
                time.sleep(1)
                self.wait_channel_loading()
        except:
            return False
