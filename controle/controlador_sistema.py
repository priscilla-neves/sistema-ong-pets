from limite.tela_sistema import TelaSistema
from controle.controlador_doador import ControladorDoador
from controle.controlador_adotante import ControladorAdotante

class ControladorSistema:


    def __init__(self):
        self.__controlador_adotante = ControladorAdotante(self)
        self.__controlador_doador = ControladorDoador(self)
        self.__tela_sistema = TelaSistema()

    @property
    def controlador_adotante(self):
        return self.__controlador_adotante

    @property
    def controlador_doador(self):
        return self.__controlador_doador


    def inicializa_sistema(self):
        self.abre_tela()

    def cadastra_doador(self):
        # Chama o controlador de doador
        self.__controlador_doador.abre_tela()
    
    def cadastra_adotante(self):
        # Chama o controlador de Usuarios
        self.__controlador_adotante.abre_tela()

    def login(self):
        # Chama o controlador de Usuarios
        self.__controlador_adotante.verifica_adotante()
        

    def encerra_sistema(self):
        exit(0)

    def abre_tela(self):
        lista_opcoes = {1: self.cadastra_doador, 2: self.cadastra_adotante, 3: self.login}
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