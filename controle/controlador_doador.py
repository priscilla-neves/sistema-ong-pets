from limite.tela_doador import TelaDoador
from entidade.Doador import Doador

class ControladorDoador():
  
  def __init__(self, controlador_sistema):
    self.__Doador = []
    self.doador_logado = None
    self.__tela_doador = TelaDoador()
    self.__controlador_sistema = controlador_sistema

  def pega_doador_por_cpf(self, cpf: int):
    for doador in self.__Doador:
      if(doador.cpf == cpf):
        return doador
    return None

  def incluir_doador(self):
    dados_doador = self.__tela_doador.pega_dados_doador()
    doador = self.pega_doador_por_cpf(dados_doador["cpf"])
    try:
        if doador is None:
            doador = Doador(dados_doador["nome"], dados_doador["endereco"], dados_doador["cpf"],dados_doador["dt_nasc"])
            self.__Doador.append(doador)
        else:
            raise KeyError
    except KeyError:
        self.__tela_doador.mostra_mensagem("Usuário já existente!")
  

  def alterar_doador(self):
    doador_logado = self.__controlador_doador.doador_logado    
    self.lista_Doador()
    cpf_doador = self.__tela_doador.seleciona_doador()
    doador = self.pega_doador_por_cpf(cpf_doador)

    if(doador is not None):
      novos_dados_doador = self.__tela_doador.pega_dados_doador()
      doador.nome = novos_dados_doador["nome"]
      doador.endereco = novos_dados_doador["endereco"]
      doador.cpf = novos_dados_doador["cpf"]
      doador.dt_nasc = novos_dados_doador["dt_nasc"]
      doador.doador = doador_logado
    
      self.lista_Doador()
    else:
      self.__tela_doador.mostra_mensagem("ATENCAO: doador não existente")

  # Sugestão: se a lista estiver vazia, mostrar a mensagem de lista vazia
  def lista_Doador(self):
    if not self.__Doador:
        self.__tela_doador.mostra_mensagem("Lista de usuários vazia!")
    else:
        for doador in self.__Doador:
            self.__tela_doador.mostra_doador({"nome": doador.nome, "dt_nasc": doador.dt_nasc, "endereco": doador.endereco, "cpf": doador.cpf})

  def excluir_doador(self):
    self.lista_Doador()
    cpf_doador = self.__tela_doador.seleciona_doador()
    doador = self.pega_doador_por_cpf(cpf_doador)

    if(doador is not None):
      self.__Doador.remove(doador)
      self.lista_Doador()
      self.__tela_doador.mostra_mensagem("doador excluído")
    else:
      self.__tela_doador.mostra_mensagem("ATENCAO: doador não existente")

  def retornar(self):
    self.__controlador_sistema.abre_tela()

  def abre_tela(self):
    lista_opcoes = {1: self.incluir_doador,  2: self.alterar_doador, 3: self.lista_Doador, 4: self.excluir_doador, 0: self.retornar}
    continua = True
    while continua:
      lista_opcoes[self.__tela_doador.tela_opcoes()]()

  def verifica_doador(self):
    cpf_doador = self.__tela_doador.verifica_doador()
    doador = self.pega_doador_por_cpf(cpf_doador)
    if (doador == None):
      self.__tela_doador.mostra_mensagem("ATENCAO: doador não existente, realize o cadastro.")
      self.abre_tela()
    else :
      self.__tela_doador.mostra_mensagem("Login Realizado com sucesso!")
      self.doador_logado = doador.cpf
      self.__controlador_sistema.abre_tela_opcoes()