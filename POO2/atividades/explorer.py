from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List

class Sujeito(ABC):
    observadores: List[Observador] = []

    def __init__(self) -> None:
        pass
    
    def insere(self, observador: Observador) -> None:
        Sujeito.observadores.append(observador)

    def Notificar(self) -> None:
        for observador in Sujeito.observadores:
            observador.atualizar(self)

class Observador(ABC):
    def atualizar(self, sujeito: Sujeito) -> None:
        pass

class EX1_Observador(Observador):
    def atualizar(self, sujeito: Sujeito) -> None:
        print(f"sujeito: {sujeito}")

class Sujeito_Concreto(Sujeito):
    _state: int = None

    def setar_Dados(self, myData: int) -> None:
        self._state = myData
        self.Notificar()

    def pegar_Dados(self) -> int:
        return self._state

#exemplo
s = Sujeito_Concreto()
obs2 = EX1_Observador()
s.insere(obs2)
