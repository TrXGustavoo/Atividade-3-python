from pato import Pato
from comportamentos_voo import VoarRaso
from comportamentos_danca import Danca_Samba

class PatoRuivo(Pato):
    def __init__(self):
        super().__init__(VoarRaso(), Danca_Samba())

    def mostrar(self):
        return "Eu sou o Pato Ruivo."

    def grasnar(self):
        return "Que-Que."
