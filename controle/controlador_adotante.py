from entidade.Adotante import Adotante
from limite.tela_adotante import TelaAdotante



class ControladorAdotante():
  
  def __init__(self, controlador_sistema):
    self.__usuarios = []
    self.__tela_usuario = TelaAdotante()
    self.__controlador_sistema = controlador_sistema

  def pega_usuario_por_cpf(self, cpf: int):
    for usuario in self.__usuarios:
      if(usuario.cpf == cpf):
        return usuario
    return None

  def incluir_usuario(self):  
    dados_usuario = self.__tela_usuario.pega_dados_usuario()
    usuario = Adotante(dados_usuario["nome"], dados_usuario["endereco"], dados_usuario["cpf"],dados_usuario["dt_nasc"],dados_usuario["tipoHab"], dados_usuario["outros_animais"])
    self.__usuarios.append(usuario)

  def alterar_usuario(self): 
    self.lista_usuarios()
    cpf_usuario = self.__tela_usuario.seleciona_usuario()
    usuario = self.pega_usuario_por_cpf(cpf_usuario)

    if(usuario is not None):
      novos_dados_usuario = self.__tela_usuario.pega_dados_usuario()
      usuario.nome = novos_dados_usuario["nome"]
      usuario.endereco = novos_dados_usuario["endereco"]
      usuario.cpf = novos_dados_usuario["cpf"]
      usuario.dt_nasc = novos_dados_usuario["dt_nasc"]
      usuario.tipoHab = novos_dados_usuario["tipoHab"]
      usuario.outros_animais = novos_dados_usuario["outros_animais"]
      
    
      self.lista_usuarios()
    else:
      self.__tela_usuario.mostra_mensagem("ATENCAO: Adotante não existente")

  # Sugestão: se a lista estiver vazia, mostrar a mensagem de lista vazia
  def lista_usuarios(self):
    for usuario in self.__usuarios:
      self.__tela_usuario.mostra_usuario({"nome": usuario.nome, "dt_nasc": usuario.dt_nasc, "endereco": usuario.endereco,"cpf": usuario.cpf, "tipoHab": usuario.tipoHab,"outros_animais": usuario.outros_animais, })

  def excluir_usuario(self):
    self.lista_usuarios()
    cpf_usuario = self.__tela_usuario.seleciona_usuario()
    usuario = self.pega_usuario_por_cpf(cpf_usuario)

    if(usuario is not None):
      self.__usuarios.remove(usuario)
      self.lista_usuarios()
      self.__tela_usuario.mostra_mensagem("Adotante excluído")
    else:
      self.__tela_usuario.mostra_mensagem("ATENCAO: Adotante não existente")

  def retornar(self):
    self.__controlador_sistema.abre_tela()

  def abre_tela(self):
    lista_opcoes = {1: self.incluir_usuario,  2: self.alterar_usuario, 3: self.lista_usuarios, 4: self.excluir_usuario, 0: self.retornar}
    continua = True
    while continua:
      lista_opcoes[self.__tela_usuario.tela_opcoes()]()

  def verifica_usuario(self):
    cpf_usuario = self.__tela_usuario.verifica_usuario()
    usuario = self.pega_usuario_por_cpf(cpf_usuario)
    if (usuario == None):
      self.__tela_usuario.mostra_mensagem("ATENCAO: Adotante não existente, realize o cadastro.")
      self.abre_tela()
    else :
      self.__controlador_sistema.abre_tela_opcoes()