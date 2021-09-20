from behave import *

use_step_matcher("re")


@step("I see the login button")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert context.home_page.verificar_login_cta_existence(), 'El botón de login no existe'