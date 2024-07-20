from INotificador import INotificador

def enviarSMS(numero, mensagem):
  print(f"Enviando SMS para: {numero}: {mensagem}\n")

class AdaptadorSMS(INotificador):
  def enviar(self, mensagem, destinatario):
    enviarSMS(destinatario, mensagem)