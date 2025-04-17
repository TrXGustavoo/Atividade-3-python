from pato import Pato
from comportamentos_voo import VoarRaso
from comportamentos_danca import Danca_Tango

class PatoBravo(Pato):
    def __init__(self):
        super().__init__(VoarRaso(), Danca_Tango())

    def mostrar(self):
        return "Eu sou o Pato Bravo."

    def grasnar(self):
        return "Que-Que. Grrrrrrrrr."
