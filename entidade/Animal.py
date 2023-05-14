
from entidade.AbstractAnimal import AbstractAnimal


class Animal (AbstractAnimal):
  # fazer aqui tratamento dos dados, caso os parametros sejam diferentes do esperado
  def __init__(self, nome: str, raca: str, chip: int):
    #if isinstance(nome, str):    
      self.__nome = nome
    #if isinstance(raca, str):  
      self.__raca = raca
      self.__chip = chip

  
  @property
  def nome(self):
    return self.__nome

  @nome.setter
  def nome(self, nome: str):
    self.__nome = nome

  @property
  def raca(self):
    return self.__raca

  @raca.setter
  def raca(self, raca: str):
    self.__raca = raca

  @property
  def chip(self):
    return self.__chip

  @chip.setter
  def chip(self, chip: int):
    self.__chip = chip

