from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List

class Mediador(ABC):
    def enviar_dados(self, ph: int, pressao: float, temperatura: float) -> None:
        pass

class Sujeito(ABC):
    def __init__(self, mediador: Mediador) -> None:
        self._mediador = mediador
    
    def insere_observador(self, observador: Observador) -> None:
        self._mediador.adicionar_observador(observador)

    def notificar_observadores(self, ph: int, pressao: float, temperatura: float) -> None:
        self._mediador.enviar_dados(ph, pressao, temperatura)

class Observador(ABC):
    def atualizar(self, ph: int, pressao: float, temperatura: float) -> None:
        pass

class Ex_Observador(Observador):
    def __init__(self, nome: str) -> None:
        self.nome = nome

    def atualizar(self, ph: int, pressao: float, temperatura: float) -> None:
        dados = {
            'pH': ph,
            'PA': pressao,
            'temperatura': temperatura
        }
        print(f"A {self.nome} recebeu dados: {dados}")

class Sujeito_Concreto(Sujeito):
    def setar_dados_ambientais(self, ph: int, pressao: float, temperatura: float) -> None:
        self.notificar_observadores(ph, pressao, temperatura)

class MediadorConcreto(Mediador):
    def __init__(self) -> None:
        self._observadores: List[Observador] = []

    def adicionar_observador(self, observador: Observador) -> None:
        self._observadores.append(observador)

    def enviar_dados(self, ph: int, pressao: float, temperatura: float) -> None:
        for observador in self._observadores:
            observador.atualizar(ph, pressao, temperatura)

# Exemplo de uso
mediador = MediadorConcreto()
amazonia = Sujeito_Concreto(mediador)
unifesp = Ex_Observador("UNIFESP")
observador2 = Ex_Observador("Faculdade2")

amazonia.insere_observador(unifesp)
amazonia.insere_observador(observador2)

# Atualização dos dados
print('\nPrimeira coleta de dados')
amazonia.setar_dados_ambientais(ph=6, pressao=1102, temperatura=30)
print('\nSegunda coleta de dados')
amazonia.setar_dados_ambientais(ph=6, pressao=1000, temperatura=25)
