class TelaDoador():
  
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
    print("-------- Doador ----------")
    print("Escolha a opcao")
    print("1 - Incluir Doador")
    print("2 - Alterar Doador")
    print("3 - Listar Doadores")
    print("4 - Excluir Doador")
    print("0 - Retornar")

    opcao = self.le_num_inteiro("Escolha a opcao:", [0,1,2,3,4])
    return opcao

  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def pega_dados_Doador(self):
    print("-------- DADOS Doador ----------")
    nome = input("Nome: ")
    cpf = input("CPF: ")
    dt_nasc = input ("Data de Nascimento: ")
    endereco = input("Endereço: ")
  

    return {"nome": nome, "cpf": cpf, "dt_nasc": dt_nasc, "endereco": endereco}
  
  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def mostra_Doador(self, dados_Doador):
    print ("-----------LISTA DE DOADOR-----------")
    print("Nome: ", dados_Doador["nome"])
    print("CPF: ", dados_Doador["cpf"])
    print("Endereço: ", dados_Doador["endereco"])
    print("Data de Nascimento: ", dados_Doador["dt_nasc"])
   
    print("\n")

  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def seleciona_Doador(self):
    cpf = input("CPF do doador que deseja selecionar: ")
    return cpf

  def verifica_Doador(self):
    cpf = input("Digite o CPF do Doador: ")
    return cpf    

  def mostra_mensagem(self, msg):
    print(msg)