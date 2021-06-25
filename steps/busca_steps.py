from behave import given, then, when
from utils import Utils
from time import sleep


utils = Utils()


@given(u'que acesso a pagina principal')
def step_impl(context):
    utils.navegar('https://bookstore.toolsqa.com/swagger/index.html#/')
    sleep(5)

@given(u'acesso get/user/username')
def step_impl(context):
    utils.clk_get()
    utils.clk_try()


@when(u'preencho o campo de busca com um nome que não esta no BD')
def step_impl(context):
    utils.preenche_nome('Everton')
    utils.clk_execute()


@then(u'o resultado sera mostrado')
def step_impl(context):
    resposta = utils.driver.find_element_by_xpath(
        '//*[@id="operations-user-getUserByName"]/div[2]/div/div[3]/div[2]/div/div/div[2]/div/pre').text
    return resposta
