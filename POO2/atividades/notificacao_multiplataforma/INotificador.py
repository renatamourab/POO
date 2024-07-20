from abc import ABC, abstractmethod
@abstractmethod

class INotificador(ABC):
  def enviar(self, mensagem, destinatario):
    pass