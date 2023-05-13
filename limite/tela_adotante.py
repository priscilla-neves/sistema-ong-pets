class TelaAdotante():
  
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
    print("-------- Adotantes ----------")
    print("Escolha a opcao")
    print("1 - Incluir Adotante Adotante")
    print("2 - Alterar Adotante")
    print("3 - Listar Adotantes")
    print("4 - Excluir Adotante")
    print("0 - Retornar")

    opcao = self.le_num_inteiro("Escolha a opcao:", [0,1,2,3,4])
    return opcao


  def pega_dados_adotante(self):
    print("-------- DADOS Adotante ----------")
    nome = input("Nome: ")
    cpf = input("CPF: ")
    dt_nasc = input ("Data de Nascimento: ")
    endereco = input("Endereço: ")
    tipoHab = input("Tipo de Habitação(casa ou apartamento): ")
    outros_animais = input("Possui outros animais?: ")
    
    return {"nome": nome, "cpf": cpf, "dt_nasc": dt_nasc, "endereco": endereco,"tipoHab": tipoHab,"outros_animais": outros_animais}

  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def mostra_Adotante(self, dados_Adotante):
    print ("-----------LISTA DE AdotanteS-----------")
    print("Nome: ", dados_Adotante["nome"])
    print("CPF: ", dados_Adotante["cpf"])
    print("Endereço: ", dados_Adotante["endereco"])
    print("Data de Nascimento: ", dados_Adotante["dt_nasc"])
    print("Tipo de Habitação ", dados_Adotante["tipoHab"])
    print("Possui outros animais? ", dados_Adotante["outros_animais"])
   
    print("\n")

  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def seleciona_Adotante(self):
    cpf = input("CPF do Adotante que deseja selecionar: ")
    return cpf

  def verifica_Adotante(self):
    cpf = input("Digite o CPF do Adotante: ")
    return cpf    

  def mostra_mensagem(self, msg):
    print(msg)