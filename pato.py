from abc import ABC, abstractmethod

class Pato(ABC) :
    
    def __init__(self, comportamento_voar, comportamento_dancar, comportamento_pular):
        self.comportamento_voar = comportamento_voar
        self.comportamento_dancar = comportamento_dancar
        self.comportamento_pular= comportamento_pular

    def realizar_nadar(self):
        return "Pato Nadando."

    def realizar_voo(self):
        return self.comportamento_voar.voar()

    def realizar_danca(self):
        return self.comportamento_dancar.dancar()
    
    def realizar_pulo(self):
        return self.comportamento_pular.pular()

    @abstractmethod
    def realizar_mostrar(self):
        pass