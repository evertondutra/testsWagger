from behave import given, then, when
from utils_cadastro import UtilsCadastro
import requests
from nose.tools import assert_equal


utils = UtilsCadastro()


@given(u'que acesso a pagina principal para post')
def step_impl(context):
    utils.navegar('https://bookstore.toolsqa.com/swagger/index.html#/')


@given(u'acesso POST/user/createWithList')
def step_impl(context):
    utils.clk_post()
    utils.clk_try()


@when(u'preencho o campo com dados')
def step_impl(context):
    raise NotImplementedError(u'STEP: When preencho o campo com dados')


@then(u'o usuário será cadastrado')
def step_impl(context):
    utils.preenche_username('Tone')

'''


@given(u'acesso POST/user/createWithList')
def step_impl(context):
    


@when(u'preencho o campo com dados')
def step_impl(context):
    


@then(u'o usuário será cadastrado')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then o usuário será cadastrado')
'''