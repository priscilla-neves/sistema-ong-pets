


from entidade.Animal import Animal


class Cao(Animal):
  # fazer aqui tratamento dos dados, caso os parametros sejam diferentes do esperado
  def __init__(self, nome: str, raca: str, chip: int, tamanho: int):
    super().__init__(nome, raca, chip)
    self.__tamanho = tamanho
    #if isinstance(tamanho, str):    
  
  
  @property
  def tamanho(self):
    return self.__tamanho

  @tamanho.setter
  def tamanho(self, tamanho: str):
    self.__tamanho = tamanho

 