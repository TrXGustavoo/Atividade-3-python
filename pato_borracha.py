from pato import Pato
from comportamentos_voo import NaoVoa
from comportamentos_danca import NaoDanca
from padrao_pular import Pular  

class PatoBorracha(Pato):
    def __init__(self):
        super().__init__(NaoVoa(), NaoDanca(), Pular())
        self.comportamento_voar = NaoVoa()
        self.comportamento_dancar = NaoDanca()

    def realizar_mostrar(self):
        return "Olá, eu sou de Borracha."
    
    # def mostrar(self):
    #     return "Eu sou um Pato de Borracha!"
    
    def realizar_grasnar(self):
        return self.grasnado()