from pato import Pato
from comportamentos_voo import VoarRaso
from comportamentos_danca import Danca_Samba
from padrao_pular import Pular  
from Apito import Apito 

class PatoRuivo(Pato):
    def __init__(self):
        super().__init__(VoarRaso(), Danca_Samba(), Pular())
        self.comportamento_grasnar = Apito()
    def realizar_mostrar(self):
        return "Eu sou o Pato Ruivo."

    def realizar_grasnar(self):
         return self.comportamento_grasnar.grasnar()