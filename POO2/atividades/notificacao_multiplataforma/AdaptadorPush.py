from INotificador import INotificador

def enviarPush(idDispositivo, mensagem):
  print(f"Enviando Push para: {idDispositivo}: {mensagem}\n")  

class AdaptadorPush(INotificador):
  def enviar(self, mensagem, destinatario):
    enviarPush(destinatario, mensagem)