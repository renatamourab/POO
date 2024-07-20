from INotificador import INotificador  

class NotificadorEmail(INotificador):
  def enviar(self, mensagem, destinatario):
    print(f"Enviando Email para: {destinatario}: {mensagem}\n")