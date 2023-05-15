from entidade.Usuario import Usuario

class Doador(Usuario):
  # fazer aqui tratamento dos dados, caso os parametros sejam diferentes do esperado
  def __init__(self,  nome: str, dt_nasc: str, cpf: int, endereco: str):
     super().__init__(nome, dt_nasc,  cpf, endereco)
