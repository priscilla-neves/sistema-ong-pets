from entidade.Usuario import Usuario

class Adotante(Usuario):
  # fazer aqui tratamento dos dados, caso os parametros sejam diferentes do esperado
  def __init__(self,  nome: str, dt_nasc: str, cpf: int, endereco: str, tipoHab: str, outros_animais:str,  usuario: str):
     super().__init__(nome, dt_nasc,  cpf, endereco,tipoHab,outros_animais, usuario)

@property
def tipoHab(self):
    return self.__tipoHab

@tipoHab.setter
def nome(self, tipoHab: str):
    self.__tipoHab = tipoHab
    
@property
def outros_animais(self):
    return self.__outros_animais

@tipoHab.setter
def outros_animais(self, outros_animais: str):
    self.__outros_animais = outros_animais