from entidade.AbstractUsuario import AbstractUsuario


class Usuario(AbstractUsuario):
  # fazer aqui tratamento dos dados, caso os parametros sejam diferentes do esperado
  def __init__(self, nome: str, dt_nasc: str, cpf: int, endereco: str):
    #if isinstance(nome, str):    
      self.__nome = nome
    #if isinstance(dt_nasc, str):  
      self.__dt_nasc = dt_nasc
      self.__cpf = cpf
      self.__endereco =endereco
    

  @property
  def nome(self):
    return self.__nome

  @nome.setter
  def nome(self, nome: str):
    self.__nome = nome

  @property
  def dt_nasc(self):
    return self.__dt_nasc

  @dt_nasc.setter
  def dt_nasc(self, dt_nasc: str):
    self.__dt_nasc = dt_nasc

  @property
  def cpf(self):
    return self.__cpf

  @cpf.setter
  def cpf(self, cpf: int):
    self.__cpf = cpf

  @property
  def endereco(self):
    return self.__endereco

  @endereco.setter
  def endereco(self, endereco: str):
    self.__endereco = endereco

