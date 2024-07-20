from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List

class Sujeito(ABC):
    observadores: List[Observador] = []

    def __init__(self) -> None:
        pass
    
    def insere_observador(self, observador: Observador) -> None:
        Sujeito.observadores.append(observador)

    def notificar_observadores(self) -> None:
        for observador in Sujeito.observadores:
            observador.atualizar(self)

class Observador(ABC):
    def atualizar(self, Sujeito: Sujeito) -> None:
        pass

class Ex_Observador(Observador):
    def __init__(self, nome: str) -> None:
        self.nome = nome

    def atualizar(self, Sujeito: Sujeito) -> None:
        dados = {
            'pH': Sujeito.obter_ph(),
            'PA': Sujeito.obter_pressao_atmosferica(),
            'temperatura': Sujeito.obter_temperatura()
        }
        print(f"A {self.nome} recebeu dados da Sujeito: {dados}")

class Sujeito_Concreto(Sujeito):
    _ph: int = None
    _pressao_atmosferica: float = None
    _temperatura: float = None

    def setar_dados_ambientais(self, ph: int, pressao: float, temperatura: float) -> None:
        self._ph = ph
        self._pressao_atmosferica = pressao
        self._temperatura = temperatura
        self.notificar_observadores()

    def obter_ph(self) -> int:
        return self._ph

    def obter_pressao_atmosferica(self) -> float:
        return self._pressao_atmosferica

    def obter_temperatura(self) -> float:
        return self._temperatura

#exemplo
amazonia = Sujeito_Concreto()
unifesp = Ex_Observador("UNIFESP")
Observador2 = Ex_Observador("faculdade2")

amazonia.insere_observador(unifesp)
amazonia.insere_observador(Observador2)

#atualizar
print('\nPrimeira coleta de dados')
amazonia.setar_dados_ambientais(ph =6, pressao= 1102, temperatura=30)
print('\nSegunda coleta de dados')
amazonia.setar_dados_ambientais(ph=6, pressao=1000, temperatura=25)