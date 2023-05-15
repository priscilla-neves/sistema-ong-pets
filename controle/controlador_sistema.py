from controle.controlador_adotante import ControladorAdotante
from controle.controlador_cao import ControladorCao
from controle.controlador_doador import ControladorDoador
from controle.controlador_gato import ControladorGato
from limite.tela_sistema import TelaSistema


class ControladorSistema:


    def __init__(self):
        self.__controlador_adotante = ControladorAdotante(self)
        self.__controlador_gato = ControladorGato(self)
        self.__controlador_cao = ControladorCao(self)
        self.__controlador_doador = ControladorDoador(self)
        
        self.__tela_sistema = TelaSistema()

    @property
    def controlador_adotante(self):
        return self.__controlador_adotante
    @property
    def controlador_doador(self):
        return self.__controlador_doador
    @property
    def controlador_gato(self):
        return self.__controlador_gato
    @property
    def controlador_cao(self):
        return self.__controlador_cao

    def inicializa_sistema(self):
        self.abre_tela()

    def cadastra_adotante(self):
        # Chama o controlador de Usuarios
        self.__controlador_adotante.abre_tela()
    
    def cadastra_doador(self):
        # Chama o controlador de Usuarios
        self.__controlador_doador.abre_tela()
    
    def cadastra_gato(self):
        # Chama o controlador de Usuarios
        self.__controlador_gato.abre_tela()
    def cadastra_cao(self):
        # Chama o controlador de Usuarios
        self.__controlador_cao.abre_tela()

    def login(self):
        # Chama o controlador de Usuarios
        self.__controlador_adotante.verifica_usuario()

    def encerra_sistema(self):
        exit(0)

    def abre_tela(self):
        lista_opcoes = {1: self.cadastra_doador, 2: self.cadastra_adotante,3: self.cadastra_gato, 4: self.cadastra_cao}
        while True:
            opcao_escolhida = self.__tela_sistema.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()

