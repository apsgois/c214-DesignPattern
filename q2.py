from abc import ABC, abstractmethod



class Observer(ABC):
    @abstractmethod
    def update(self, words):
        pass


class Subject:
    def __init__(self):
        self.observers = []

    def attach(self, observer):
        self.observers.append(observer)

    def detach(self, observer):
        self.observers.remove(observer)

    def notify(self, words):
        for observer in self.observers:
            observer.update(words)

class Contador(Subject):
    def __init__(self):
        super().__init__()
        self.frase = ""

    def set_frase(self, frase):
        self.frase = frase
        self.notify(self.frase)



class ContadorObserver(Observer):
    def __init__(self):
        self.todas_palavras = 0
        self.contagem_caracter = 0
        self.contagem_maiuscula = 0

    def update(self, palavras):
        lista_palavras = palavras.split()
        self.todas_palavras = len(lista_palavras)
        self.contagem_caracter = sum(1 for palavra in lista_palavras if len(palavra) % 2 == 0)
        self.contagem_maiuscula = sum(1 for palavra in lista_palavras if palavra[0].isupper())

        print("Contagem de todas as palavras:", self.todas_palavras)
        print("Contagem de palavras com quantidade par de caracteres:", self.contagem_caracter)
        print("Contagem de palavras começadas com maiúsculas:", self.contagem_maiuscula)



app = Contador()
observer = ContadorObserver()
app.attach(observer)

frase = input("Digite uma frase: ")
app.set_frase(frase)
