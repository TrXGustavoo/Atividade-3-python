import random

# Define the base class first
class PadraoPular:
    """Interface base para comportamentos de pulo."""
    def pular(self):
        pass

class Pular(PadraoPular):
    """
    Implementação concreta de um comportamento de pulo básico.
    
    Esta classe implementa um comportamento de pulo padrão para patos,
    com altura moderada e aleatória.
    """
    
    def __init__(self):
        """
        Construtor que inicializa o comportamento de pulo básico.
        A altura do pulo é definida aleatoriamente entre 5 e 20 centímetros.
        """
        self.altura = random.randint(5, 20)
    
    def pular(self):
        """
        Implementa o comportamento de pulo básico.
        A cada chamada gera uma nova altura aleatória para o pulo.
        
        Returns:
            str: Uma string descrevendo o pulo e sua altura.
        """
        # Atualiza a altura com um novo valor aleatório a cada pulo
        self.altura = random.randint(5, 20)
        return f"Pulando! Altura: {self.get_altura()}cm 🦆"
    
    def get_altura(self):
        """
        Retorna a altura atual do pulo.
        
        Returns:
            int: A altura do pulo em centímetros.
        """
        return self.altura