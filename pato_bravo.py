from pato import Pato
from comportamentos_voo import VoarRaso
from comportamentos_danca import Danca_Tango
from padrao_pular import Pular  
from Apito import Apito 

class PatoBravo(Pato):
    def __init__(self):
        super().__init__(VoarRaso(), Danca_Tango(), Pular(), ) 
        self.grasnado = Apito.grasnar 
    def pular(self):
        return self.comportamento_pular.pular()

    def realizar_mostrar(self):
        return "Eu sou o Pato Bravo."

    def realizar_grasnar(self):
        return self.grasnado()