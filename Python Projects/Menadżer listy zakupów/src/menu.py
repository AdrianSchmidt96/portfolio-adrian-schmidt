class Menu():
    def __init__(self):
        self.welcome ="Witamy! \n.\n.\n.\n.\n.\nstwórz swoją listę zakupów, a wyeksportuję ją do pliku txt :)"
        self.FirstProduct = ""

    def welcomePrint(self):
        print(self.welcome)
        product = str(input("wpisz nazwę produktu: "))
        self.FirstProduct = product

    def get_product(self):
        return self.FirstProduct