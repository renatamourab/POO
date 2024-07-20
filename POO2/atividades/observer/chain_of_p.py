class Cliente:
    def __init__(self):
        self.processador = ProcessadorUm()

    def processar_texto(self, texto):
        self.processador.processar(texto)

class Processador:
    def set_proximo(self, proximo):
        self.proximo = proximo

    def processar(self, texto):
        self._processar(texto)

    def _processar(self, texto):
        pass

class ProcessadorUm(Processador):
    def __init__(self):
        self.proximo = ProcessadorFinal()

    def _processar(self, texto):
        space_count = texto.count(' ')
        print(f"espaços: {space_count}")
        self.proximo.processar(texto)

class ProcessadorFinal(Processador):
    def _processar(self, texto):
        a_count = texto.lower().count('a')
        print(f"letras 'a': {a_count}")

        dot_count = texto.count('.')
        print(f"pontos: {dot_count}")

def main():
    texto = "Olá. Estou fazendo esse teste como exemplo para a atividade. Tomara que funcione."
    print(f"teste: {texto}\nresposta esperada: 8 vogais a, 3 '.', 12 espaços\n")

    cliente = Cliente()
    cliente.processar_texto(texto)

if __name__ == "__main__":
    main()