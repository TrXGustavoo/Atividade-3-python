from abc import ABC, abstractmethod

class PadraoVoaveis(ABC):
    @abstractmethod
    def voar(self):
        pass

class PadraoDancar(ABC):
    @abstractmethod
    def dancar(self):
        pass
