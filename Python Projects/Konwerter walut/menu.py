from getApi import *
from cantor import *

class Menu:
    def __init__(self):
        self.getApi = GetApi()
        self.cantor = Cantor()

    def Logic(self):
        print("""Witaj w kantorze by Adrian Schmidt!
              \nCo chcesz zrobić?
              \n1.Wymienić walutę
              \n2.Sprawdzić aktualne kursy walut w stosunku do PLN
              \n3.Wyjść

              """)

        print()
        info = input(":")
        x = 1
        while x:
            
