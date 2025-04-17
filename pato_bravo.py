from pato import Pato
from comportamentos_voo import VoarRaso
from comportamentos_danca import Danca_Tango
from padrao_pular import Pular  

class PatoBravo(Pato):
    def __init__(self):
        super().__init__(VoarRaso(), Danca_Tango(), Pular()) 

    def pular(self):
        return self.comportamento_pular.pular()

    def mostrar(self):
        return "Eu sou o Pato Bravo."

    def grasnar(self):
        return "Que-Que. Grrrrrrrrr."