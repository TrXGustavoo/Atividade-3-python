# from abc import ABC, abstractmethod

class Pato() :
    def __init__(self, comportamento_voar, comportamento_dancar):
        self.comportamento_voar = comportamento_voar
        self.comportamento_dancar = comportamento_dancar

    def nadar(self):
        return "Pato Nadando."

    def realizar_voo(self):
        return self.comportamento_voar.voar()

    def realizar_danca(self):
        return self.comportamento_dancar.dancar()

    # @abstractmethod
    def mostrar(self):
        pass