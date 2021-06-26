#language: pt

  Funcionalidade: acessar o swagger e obter o retorno do status

    @test404
    Cenario: obter o retorno 404
      Dado que acesso a pagina principal
      E acesso get/user/username
      Quando preencho o campo de busca com um nome que não esta no BD
      Então o resultado sera mostrado


    @test200
    Cenario: obter o retorno 200
      Dado que acesso a pagina principal para post
      E acesso POST/user/createWithList
      #Quando preencho o campo com dados
      #Então o usuário será cadastrado
