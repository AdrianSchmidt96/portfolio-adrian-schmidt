from product import *

class Menu:
    
    def __init__(self):
        self.welcome ="Witamy! \n.\n.\n.\n.\n.\nstwórz swoją listę zakupów, a wyeksportuję ją do pliku txt :)"
        self.p = Product()
    
    def welcomePrint(self):
        print(self.welcome)

    def menu(self):
        print("""Wybierz z menu co chcesz zrobić:\n
              1. utworzyć nową listę zakupów\n
              2. zaktualizować istniejącą listę\n
              3. wyjść\n
              :
              """)
        info = input()
        if info == "1":
            decision = True
            while decision:
                self.p.addProductToList()
                decision = self.p.get_SelfDec
        elif info == 2:
            pass
        elif info == 3:
            pass

        



