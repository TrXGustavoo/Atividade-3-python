from interfaces import PadraoDancar

class Danca_Tango(PadraoDancar):
    def __init__(self):
        self.estilo = "Tango"

    def dancar(self):
        return f"Dançando no estilo {self.estilo}! 💃"

class Danca_Samba(PadraoDancar):
    def __init__(self):
        self.estilo = "Samba"

    def dancar(self):
        return f"Mandando ver na {self.estilo}! 🕺"

class NaoDanca(PadraoDancar):
    def dancar(self):
        return "Prefiro não dançar. 🦆"
