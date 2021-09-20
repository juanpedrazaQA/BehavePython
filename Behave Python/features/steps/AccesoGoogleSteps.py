from behave import *
from page_objects.main_page import MainPage

use_step_matcher("re")


@given("I navigate to Google Home Page")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.home_page = MainPage(context)
    context.driver.get("http://www.google.com")


@then('I see the page title as "(?P<title>.+)"')
def step_impl(context, title):
    """
    :param title:
    :type context: behave.runner.Context
    """
    assert context.home_page.get_current_page_title() == title, 'El titulo es incorrecto'
