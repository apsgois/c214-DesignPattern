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
    def update(self, palavras):
        lista_palavras = palavras.split()
        todas_palavras = len(lista_palavras)
        contagem_caracter = sum(1 for caracter in lista_palavras if len(caracter) % 2 == 0)
        contagem_maiuscula = sum(1 for caracter in lista_palavras if caracter[0].isupper())

        print("Contagem de todas as palavras:", todas_palavras)
        print("Contagem de palavras com quantidade par de caracteres:", contagem_caracter)
        print("Contagem de palavras começadas com maiúsculas:", contagem_maiuscula)



app = Contador()
observer = ContadorObserver()
app.attach(observer)

frase = input("Digite uma frase: ")
app.set_frase(frase)
