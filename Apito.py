import random

class Apito:
    @staticmethod
    def grasnar():
        quacks = [
            "QUACK QUACK!!",
            "quack...",
            "QUAAAACK!",
            "quack quack quack!",
            "QUACK!",
            "quack?",
            "QUAAAAAACK QUACK!",
            "quack-quack!",
            "Qua-Quack!"
        ]
        return random.choice(quacks)