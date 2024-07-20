#Exercício: Sistema de Notificações Multiplataforma
# Alunos: 
  # Renata Moura Barreto - 163983
  # Guiherme de Almeida Ferracini - 163784

from NotificadorEmail import NotificadorEmail
from AdaptadorPush import AdaptadorPush
from AdaptadorSMS import AdaptadorSMS
  
class Main:
    NotificadorEmail().enviar("Oi, estou enviando um email pra você!", "gui@gmai.com")
    AdaptadorSMS().enviar("Oi, estou enviando um SMS pra você!", "123456789")
    AdaptadorPush().enviar("Oi, estou enviando um Push pra você!", "idDispositivo")

