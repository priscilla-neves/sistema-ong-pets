from entidade.Usuario import Usuario

class Adotante(Usuario):
  # fazer aqui tratamento dos dados, caso os parametros sejam diferentes do esperado
  def __init__(self,  nome: str, dt_nasc: str, cpf: int, endereco: str, tipoHab: str, outros_animais:str):
     super().__init__(nome, dt_nasc,  cpf, endereco)
     if isinstance(tipoHab, str):
      self.tipoHab = tipoHab
     if isinstance(outros_animais, str):
      self.outros_animais = outros_animais
    

@property
def tipoHab(self):
    return self.__tipoHab

@tipoHab.setter
def tipoHab(self, tipoHab: str):
     if (isinstance(tipoHab, str)):  
        self.__tipoHab = tipoHab
    
@property
def outros_animais(self):
    return self.__outros_animais

@outros_animais.setter
def outros_animais(self, outros_animais: str):
    if (isinstance(outros_animais, str)):  
        self.__outros_animais = outros_animais