from behave import fixture, use_fixture
from selenium import webdriver


@fixture
def selenium_webdriver_chrome(context):
    mobile_emulation = {"deviceName": "Samsung Galaxy S8+"}
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--lang=en")
    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    context.driver = webdriver.Chrome(options=chrome_options)
    yield context.driver


def before_scenario(context, scenario):
    use_fixture(selenium_webdriver_chrome, context)
