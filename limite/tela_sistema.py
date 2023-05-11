class TelaSistema:
    #fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
    
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
                    
    def tela_opcoes(self):
        print("-------- Sistema Doação e Adoção de Pets - Florianópolis ---------")
        print("Escolha sua opcao")
        print("1 - Cadastrar Usuário")
        print("2 - Login ")
        opcao = self.le_num_inteiro("Escolha a opcao:", [1,2])
        return opcao

    def tela_opcoes_principal(self):
        print("-------- Sistema Doação e Adoção de Pets - Florianópolis ---------")
        print("Escolha sua opcao")
        print("1 - Supermercado")
        print("2 - Categoria")
        print("3 - Produto")
        print("0 - Finalizar sistema")
        opcao = self.le_num_inteiro("Escolha a opcao:", [0,1,2,3])
        return opcao        