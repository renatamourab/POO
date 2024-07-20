from abc import ABC, abstractmethod

class Sujeito(ABC):
    @abstractmethod
    def operacao(self):
        pass

class SujeitoReal(Sujeito):
    def operacao(self):
        return "testee"

class Intermediario(Sujeito):
    def __init__(self, real: SujeitoReal):
        self._real = real

    def operacao(self):
        return self._real.operacao()

class Fabrica:
    @staticmethod
    def get_sujeito():
        return SujeitoReal()

class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.sujeito = Fabrica.get_sujeito()

    def operacao(self):
        return self.sujeito.operacao()

#testee
renata = Cliente("Renata")
print(f"{renata.nome} está executando a operação: {renata.operacao()}")

intermediario = Intermediario(SujeitoReal())
print("Executando operação com o intermediário:", intermediario.operacao())
