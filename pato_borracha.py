from pato import Pato
from comportamentos_voo import NaoVoa
from comportamentos_danca import NaoDanca

class PatoBorracha(Pato):
    def __init__(self):
        super().__init__(NaoVoa(), NaoDanca())

    def mostrar(self):
        return "Olá, eu sou de Borracha."
