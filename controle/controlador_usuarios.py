from limite.tela_usuario import TelaUsuario
from entidade.Doador import Doador
from entidade.Adotante import Adotante

class ControladorUsuarios():
  
  def __init__(self, controlador_sistema):
    self.__usuarios = []
    self.usuario_logado = None
    self.__tela_usuario = TelaUsuario()
    self.__controlador_sistema = controlador_sistema

  def pega_usuario_por_cpf(self, cpf: int):
    for usuario in self.__usuarios:
      if(usuario.cpf == cpf):
        return usuario
    return None

  def incluir_usuario_doador(self):
    dados_usuario = self.__tela_usuario.pega_dados_usuario()
    usuario = Doador(dados_usuario["nome"], dados_usuario["endereco"], dados_usuario["cpf"], "CPF", "")
    self.__usuarios.append(usuario)
  
  def incluir_usuario_adotante(self):  
    dados_usuario = self.__tela_usuario.pega_dados_usuario()
    usuario = Adotante(dados_usuario["nome"], dados_usuario["endereco"], dados_usuario["cpf"], "CPF", "")
    self.__usuarios.append(usuario)

  def alterar_usuario(self):
    usuario_logado = self.__controlador_usuario.usuario_logado    
    self.lista_usuarios()
    cpf_usuario = self.__tela_usuario.seleciona_usuario()
    usuario = self.pega_usuario_por_cpf(cpf_usuario)

    if(usuario is not None):
      novos_dados_usuario = self.__tela_usuario.pega_dados_usuario()
      usuario.nome = novos_dados_usuario["nome"]
      usuario.endereco = novos_dados_usuario["endereco"]
      usuario.cpf = novos_dados_usuario["cpf"]
      usuario.dt_nasc = novos_dados_usuario["dt_nasc"]
      usuario.usuario = usuario_logado
    
      self.lista_usuarios()
    else:
      self.__tela_usuario.mostra_mensagem("ATENCAO: Usuario não existente")

  # Sugestão: se a lista estiver vazia, mostrar a mensagem de lista vazia
  def lista_usuarios(self):
    for usuario in self.__usuarios:
      self.__tela_usuario.mostra_usuario({"nome": usuario.nome, "dt_nasc": usuario.dt_nasc, "endereco": usuario.endereco, "cpf": usuario.cpf})

  def excluir_usuario(self):
    self.lista_usuarios()
    cpf_usuario = self.__tela_usuario.seleciona_usuario()
    usuario = self.pega_usuario_por_cpf(cpf_usuario)

    if(usuario is not None):
      self.__usuarios.remove(usuario)
      self.lista_usuarios()
      self.__tela_usuario.mostra_mensagem("Usuario excluído")
    else:
      self.__tela_usuario.mostra_mensagem("ATENCAO: Usuario não existente")

  def retornar(self):
    self.__controlador_sistema.abre_tela()

  def abre_tela(self):
    lista_opcoes = {1: self.incluir_usuario_doador,2: self.incluir_usuario_adotante,  3: self.alterar_usuario, 4: self.lista_usuarios, 5: self.excluir_usuario, 0: self.retornar}
    continua = True
    while continua:
      lista_opcoes[self.__tela_usuario.tela_opcoes()]()

  def verifica_usuario(self):
    cpf_usuario = self.__tela_usuario.verifica_usuario()
    usuario = self.pega_usuario_por_cpf(cpf_usuario)
    if (usuario == None):
      self.__tela_usuario.mostra_mensagem("ATENCAO: Usuario não existente, realize o cadastro.")
      self.abre_tela()
    else :
      self.__tela_usuario.mostra_mensagem("Login Realizado com sucesso!")
      self.usuario_logado = usuario.cpf
      self.__controlador_sistema.abre_tela_opcoes()