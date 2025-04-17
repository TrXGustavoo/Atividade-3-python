from padrao_voaveis import PadraoVoaveis

class VoarFoguete(PadraoVoaveis):
    def __init__(self):
        self.velocidade = 1000

    def voar(self):
        return f"Voando como um foguete. Velocidade: {self.velocidade}"

class VoarRaso(PadraoVoaveis):
    def voar(self):
        return "Voando baixo."

class NaoVoa(PadraoVoaveis):
    
    def voar(self):
        return "Não sei voar!"
