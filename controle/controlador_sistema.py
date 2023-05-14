from limite.tela_sistema import TelaSistema
from controle.controlador_usuarios import ControladorUsuarios

class ControladorSistema:


    def __init__(self):
        self.__controlador_usuarios = ControladorUsuarios(self)
        self.__tela_sistema = TelaSistema()

    @property
    def controlador_usuarios(self):
        return self.__controlador_usuarios

    def inicializa_sistema(self):
        self.abre_tela()

    def cadastra_usuarios(self):
        # Chama o controlador de Usuarios
        self.__controlador_usuarios.abre_tela()

    def login(self):
        # Chama o controlador de Usuarios
        self.__controlador_usuarios.verifica_usuario()

    def encerra_sistema(self):
        exit(0)

    def abre_tela(self):
        lista_opcoes = {1: self.cadastra_usuarios, 2: self.login}
        while True:
            opcao_escolhida = self.__tela_sistema.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()

    def abre_tela_opcoes(self):
        lista_opcoes = {1: self.cadastra_supermercado, 2: self.cadastra_categoria, 3: self.cadastra_produtos , 0: self.encerra_sistema}
        while True:
            opcao_escolhida = self.__tela_sistema.tela_opcoes_principal()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()  