from behave import *
from expects import *
from tools.credentials import Credentials
from tools.page_factory import PageFactory


@step('Access to a browser.')
def step_impl(context,):
    context.driver.implicitly_wait(10)


@step('The user navigates to "{env}".')
def step_impl(context, env):
    context.env = env
    context.env_settings = Credentials().get_credentials(context.env)
    context.driver.get(context.env_settings['URL'])
    context.page = PageFactory(context.driver).create_page(env)
    expect(context.page.login_visibility()).to(be_true)


@step('The user searches "{text}"')
def step_impl(context, text):
    context.page.click_search_icon()
    context.page.search_by_text(text)


@step('The user click the tab "{tab}"')
def step_impl(context, tab):
    context.page.click_tab(tab)
    expect(context.page.wait_for_list()).to(be_true)


# direction = up, down, left, right
@step('The user scrolls "{direction}".')
def step_impl(context, direction):
    context.page.scroll(direction.lower())


@step('The user selects any streamer.')
def step_impl(context):
    context.page.select_any_streamer()


@step('A screenshot is taken and saved.')
def step_impl(context):
    context.page.wait_channel_loading()
    context.page.take_screenshot()

