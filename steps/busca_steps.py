from behave import given, then, when
from utils import Utils
import requests
from nose.tools import assert_equal


utils = Utils()

nome = 'Everton'
# ----------Execução----------#
@given(u'que acesso a pagina principal')
def step_impl(context):
    # abrindo o navegador e acessando a url
    utils.navegar('https://bookstore.toolsqa.com/swagger/index.html#/')

@given(u'acesso get/user/username')
def step_impl(context):
    # clicando no botão get
    utils.clk_get()
    # clicando no botão try it out
    utils.clk_try()


@when(u'preencho o campo de busca com um nome que não esta no BD')
def step_impl(context):
    # Preenchendo o campo de pesquisa
    utils.preenche_nome(nome)
    # clicando no botão execute
    utils.clk_execute()

# ----------Verificações----------#
@then(u'o resultado sera mostrado')
def step_impl(context):
    # criando um elemento da página
    resposta = utils.resposta()
    # fazendo um get da url
    r = requests.get(resposta)
    # passando para um formato .json
    r = r.json()
    # fazendo comparação
    assert_equal(resposta, f'https://petstore.swagger.io/v2/user/{nome}')
    assert_equal(r['message'], 'User not found')
    utils.driver.quit()
