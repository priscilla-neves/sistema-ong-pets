


from entidade.Animal import Animal


class Gato(Animal):
  # fazer aqui tratamento dos dados, caso os parametros sejam diferentes do esperado
  def __init__(self, nome: str, raca: str, chip: int):
    super().__init__(nome, raca, chip)
   
    #if isinstance(tamanho, str):    
  