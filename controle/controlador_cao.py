from entidade.Cao import Cao
from entidade.Cao import Cao
from limite.tela_cao import TelaCao

class ControladorCao():
  
  def __init__(self, controlador_sistema):
    self.__animais = []
    self.__tela_animal = TelaCao()
    self.__controlador_sistema = controlador_sistema

  def pega_animal_por_chip(self, chip: int):
    for animal in self.__animais:
      if(animal.chip == chip):
        return animal
    return None
  
  def incluir_animal(self):
    dados_animal = self.__tela_animal.pega_dados_animal()
    animal = Cao(dados_animal["nome"], dados_animal["raca"], dados_animal["chip"], dados_animal["tamanho"])
    self.__animais.append(animal)
  

  def alterar_animal(self):
    self.lista_animais()
    chip_animal = self.__tela_animal.seleciona_animal()
    animal = self.pega_animal_por_chip(chip_animal)

    if(animal is not None):
      novos_dados_animal = self.__tela_animal.pega_dados_animal()
      animal.nome = novos_dados_animal["nome"]
      animal.raca = novos_dados_animal["raca"]
      animal.chip = novos_dados_animal["chip"]
      animal.tamanho = novos_dados_animal["tamanho"]
    
      self.lista_animais()
    else:
      self.__tela_animal.mostra_mensagem("ATENCAO: Cão não existente")

  # Sugestão: se a lista estiver vazia, mostrar a mensagem de lista vazia

  def lista_animais(self):
    for animal in self.__animais:
      self.__tela_animal.mostra_animal({"nome": animal.nome, "tamanho": animal.tamanho, "raca": animal.raca, "chip": animal.chip})

  def excluir_animal(self):
    self.lista_animais()
    chip_animal = self.__tela_animal.seleciona_animal()
    animal = self.pega_animal_por_chip(chip_animal)

    if(animal is not None):
      self.__animais.remove(animal)
      self.lista_animais()
      self.__tela_animal.mostra_mensagem("Cão excluído")
    else:
      self.__tela_animal.mostra_mensagem("ATENCAO: Cão não existente")

  def retornar(self):
    self.__controlador_sistema.abre_tela()

  def abre_tela(self):
    lista_opcoes = {1: self.incluir_animal, 2: self.alterar_animal, 3: self.lista_animais, 4: self.excluir_animal, 0: self.retornar}
    continua = True
    while continua:
      lista_opcoes[self.__tela_animal.tela_opcoes()]()

  def verifica_animal(self):
    chip_animal = self.__tela_animal.verifica_animal()
    animal = self.pega_animal_por_chip(chip_animal)
    if (animal == None):
      self.__tela_animal.mostra_mensagem("ATENCAO: Usuario não existente, realize o cadastro.")
      self.abre_tela()
    else :
      self.__tela_animal.mostra_mensagem("Login Realizado com sucesso!")
      self.usuario_logado = animal.chip
      self.__controlador_sistema.abre_tela_opcoes()