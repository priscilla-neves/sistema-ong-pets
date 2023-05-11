class TelaUsuario():
  
  def le_num_inteiro(self, mensagem=" ", ints_validos = None):
        while True:
            valor_lido = input(mensagem)
            try:
                valor_int = int(valor_lido) #tenta transformar o valor lido em inteiro.
                if ints_validos and valor_int not in ints_validos:
                    raise ValueError #será lançada apenas se o número não é o esperado
                return valor_int
            except ValueError: #aqui cai se não for int ou se não for valido
                print("Valor incorreto!")
                if ints_validos:
                    print("Valores válidos: ", ints_validos)
  
  
  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def tela_opcoes(self):
    print("-------- USUARIOS ----------")
    print("Escolha a opcao")
    print("1 - Incluir Usuario Doador")
    print("2 - Incluir Usuario Adotante")
    print("3 - Alterar Usuario")
    print("4 - Listar Usuarios")
    print("5 - Excluir Usuario")
    print("0 - Retornar")

    opcao = self.le_num_inteiro("Escolha a opcao:", [0,1,2,3,4,5])
    return opcao

  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def pega_dados_usuario(self):
    print("-------- DADOS USUARIO ----------")
    nome = input("Nome: ")
    cpf = input("CPF: ")
    dt_nasc = input ("Data de Nascimento: ")
    endereco = input("Endereço: ")
  

    return {"nome": nome, "cpf": cpf, "dt_nasc": dt_nasc, "endereco": endereco}

  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def mostra_usuario(self, dados_usuario):
    print ("-----------LISTA DE USUÁRIOS-----------")
    print("Nome: ", dados_usuario["nome"])
    print("CPF: ", dados_usuario["cpf"])
    print("Endereço: ", dados_usuario["endereco"])
    print("Data de Nascimento: ", dados_usuario["dt_nasc"])
   
    print("\n")

  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def seleciona_usuario(self):
    cpf = input("CPF do usuário que deseja selecionar: ")
    return cpf

  def verifica_usuario(self):
    cpf = input("Digite o CPF do usuario: ")
    return cpf    

  def mostra_mensagem(self, msg):
    print(msg)