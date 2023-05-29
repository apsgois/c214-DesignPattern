import unittest
from q2 import Contador, ContadorObserver


class Testes_Q2(unittest.TestCase):
    print("*******Inicio dos testes******* \n")


    def test_01_vazio(self):
        aux = Contador()
        observer = ContadorObserver()
        aux.attach(observer)
        frase = ""
        aux.set_frase(frase)
        self.assertEqual(observer.todas_palavras, 0)
        print("Teste 01 - OK \n")


    def test_02_qtd_palavra(self):
        aux = Contador()
        observer = ContadorObserver()
        aux.attach(observer)
        frase = "Frase para validar o teste dois"
        aux.set_frase(frase)
        self.assertEqual(observer.todas_palavras, 6)
        print("Teste 02 - OK \n")


    def test_03_qtd_maiuscula(self):
        aux = Contador()
        observer = ContadorObserver()
        aux.attach(observer)
        frase = "Frase para Validar o teste tres"
        aux.set_frase(frase)
        self.assertEqual(observer.contagem_maiuscula, 2)
        print("Teste 03 - OK \n")


    def test_04_qtd_caracter_par(self):
        aux = Contador()
        observer = ContadorObserver()
        aux.attach(observer)
        frase = "Frase para validar o teste quatro"
        aux.set_frase(frase)
        self.assertEqual(observer.contagem_caracter, 2)
        print("Teste 04 - OK \n")


if __name__ == '__main__':
    unittest.main()
