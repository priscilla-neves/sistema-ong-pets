class TelaCao():
  
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
    print("-------- Animais ----------")
    print("Escolha a opcao")
    print("1 - Incluir Cão")
    print("2 - Alterar Cão")
    print("3 - Listar Cão")
    print("4 - Excluir Cão")
    print("0 - Retornar")

    opcao = self.le_num_inteiro("Escolha a opcao:", [0,1,2,3,4])
    return opcao


  def pega_dados_animal(self):
    print("-------- DADOS CÃO ----------")
    nome = input("Nome: ")
    raca = input("Raça: ")
    chip = input ("Código do chip: ")
    tamanho = input ("Tamanho em cm: ")

    return {"nome": nome, "raca": raca, "chip": chip, "tamanho": tamanho}

  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
    
  def mostra_animal(self, dados_animal):
    print("-----------CÃO-----------")
    print("Nome: ", dados_animal["nome"])
    print("Raça: ", dados_animal["raca"])
    print("Tamanho: ", dados_animal["tamanho"])
    print("Chip: ", dados_animal["chip"])
  
    print("\n")

  # fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
  def seleciona_animal(self):
    chip = input("Chip do animal que deseja selecionar: ")
    return chip

  def verifica_animal(self):
    chip = input("Digite o Chip do animal: ")
    return chip    

  def mostra_mensagem(self, msg):
    print(msg)