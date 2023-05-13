from limite.tela_adotante import TelaAdotante
from entidade.Adotante import Adotante

class ControladorAdotante():
  
  def __init__(self, controlador_sistema):
    self.__Adotante = []
    self.adotante_logado = None
    self.__tela_adotante = TelaAdotante()
    self.__controlador_sistema = controlador_sistema

  def pega_adotante_por_cpf(self, cpf: int):
    for adotante in self.__Adotante:
      if(adotante.cpf == cpf):
        return adotante
    return None

  
  def incluir_adotante(self):
    dados_adotante = self.__tela_adotante.pega_dados_adotante()
    adotante = self.pega_adotante_por_cpf(dados_adotante["cpf"])
    try:
        if adotante is None:
            adotante = Adotante(dados_adotante["nome"],dados_adotante["dt_nasc"], dados_adotante["endereco"], dados_adotante["cpf"], dados_adotante["tipoHab"], dados_adotante["outros_animais"]  )
            self.__Adotante.append(adotante)
        else:
            raise KeyError
    except KeyError:
        self.__tela_adotante.mostra_mensagem("Adotante já existente!")

  def alterar_adotante(self):
    adotante_logado = self.__controlador_adotante.adotante_logado    
    self.lista_Adotante()
    cpf_adotante = self.__tela_adotante.seleciona_adotante()
    adotante = self.pega_adotante_por_cpf(cpf_adotante)

    if(adotante is not None):
      novos_dados_adotante = self.__tela_adotante.pega_dados_adotante()
      adotante.nome = novos_dados_adotante["nome"]
      adotante.endereco = novos_dados_adotante["endereco"]
      adotante.cpf = novos_dados_adotante["cpf"]
      adotante.dt_nasc = novos_dados_adotante["dt_nasc"]
      adotante.adotante = adotante_logado
    
      self.lista_Adotante()
    else:
      self.__tela_adotante.mostra_mensagem("ATENCAO: adotante não existente")

  # Sugestão: se a lista estiver vazia, mostrar a mensagem de lista vazia
  def lista_Adotante(self):
    if not self.__Adotante:
        self.__tela_adotante.mostra_mensagem("Lista de Adotantes vazia!")
    else:
        for adotante in self.__Adotante:
            self.__tela_adotante.mostra_adotante({"nome": adotante.nome, "dt_nasc": adotante.dt_nasc, "endereco": adotante.endereco, "cpf": adotante.cpf})

  def excluir_adotante(self):
    self.lista_Adotante()
    cpf_adotante = self.__tela_adotante.seleciona_adotante()
    adotante = self.pega_adotante_por_cpf(cpf_adotante)

    if(adotante is not None):
      self.__Adotante.remove(adotante)
      self.lista_Adotante()
      self.__tela_adotante.mostra_mensagem("adotante excluído")
    else:
      self.__tela_adotante.mostra_mensagem("ATENCAO: adotante não existente")

  def retornar(self):
    self.__controlador_sistema.abre_tela()

  def abre_tela(self):
    lista_opcoes = {1: self.incluir_adotante,  2: self.alterar_adotante, 3: self.lista_Adotante, 4: self.excluir_adotante, 0: self.retornar}
    continua = True
    while continua:
      lista_opcoes[self.__tela_adotante.tela_opcoes()]()

  def verifica_adotante(self):
    cpf_adotante = self.__tela_adotante.verifica_adotante()
    adotante = self.pega_adotante_por_cpf(cpf_adotante)
    if (adotante == None):
      self.__tela_adotante.mostra_mensagem("ATENCAO: adotante não existente, realize o cadastro.")
      self.abre_tela()
    else :
      self.__tela_adotante.mostra_mensagem("Login Realizado com sucesso!")
      self.adotante_logado = adotante.cpf
      self.__controlador_sistema.abre_tela_opcoes()