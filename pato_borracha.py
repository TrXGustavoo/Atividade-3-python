from pato import Pato
from comportamentos_voo import NaoVoa
from comportamentos_danca import NaoDanca
from padrao_pular import Pular  # Changed from comportamentos_pulo to padrao_pular

class PatoBorracha(Pato):
    def __init__(self):
        super().__init__(NaoVoa(), NaoDanca(), Pular())

    def mostrar(self):
        return "Olá, eu sou de Borracha."