import os

class Menu:
    def __init__(self):
        self.notDone = True

    def mainMenu(self):
        print("""######### Menu główne #########  
              \nCo chcesz zrobić?
              \n1. utworzyć nową listę zakupów
              \n2. zaktualizować istniejącą listę
              \n3. wyjść
               """)
        
    
        
    def logicChoice(self):
        info = input("Co wybierasz?")

        if info == "1":
            f = FirstChoice()
            while self.notDone:
                while True:
                    f.createNewCategory()
                    break   
                if True:
                    while self.notDone:
                        f.addProductToShoppingList()
                        if f.get_I == 2:
                            break
                        elif f.get_I == 0:
                            self.notDone = False

                
        elif info == "2":
            pass
        elif info == "3":
            pass
        elif info == None:
            pass


class FirstChoice():
    def __init__(self):
        self.shoppingList = {}
        self.categoryList = ["pieczywo", "warzywo", "owoc", "mięso", "wędlina", "napoje", "nabiał"]
        self.category = ""
        self.i = 0
    

    def createNewCategory(self):
        i = True
        while i:
            firstMenu =("""Wpisz kategorię, do której będziesz dodawał produkty. Do wyboru masz:
                                        \n- pieczywo,\n- warzywa,\n- owoce,\n- mięso,\n- wędlina,\n- napoje,\n- nabiał
                                        : """)
            print(firstMenu)
            choice = str(input().lower())
            
            if choice in self.categoryList:
                self.category = choice
                i = False
                
            else:
                print("UPS! wybrałeś błędną kategorię :(, spróbuj ponownie")
        
        return False
            

       
    
    def addProductToShoppingList(self):
        if self.category not in self.shoppingList:
                self.shoppingList[str(self.category)] = []
        

        if self.category in self.shoppingList:
            while True:
                pr = input("podaj nazwę produktu: ")
                val = input("podaj wagę/ ilość: ")
                product = f"Nazwa: {str(pr)}" +f" Waga/ Ilość: {str(val)}"
                self.shoppingList[self.category].append(product)
                print()
                con = input( "Chcesz dodać kolejny? wcisńij '1, Chcesz zmienić kategorię? wciśnij '2', jeśli natomiast chcesz zakończyć to wpisz '0': ")
                print("""\n


                    """)
                if con == "2":
                    self.set_I(2)
                    break
                if con == "0":
                    self.set_I(0)
                    self.exportListToTxtFile()
                    print("Lista wygenerowana. Dziękujemy za skorzystanie z naszej listy zakupów.")
                    break
        
        return False
       
    @property
    def get_I(self):
        return self.i
    
    
    def set_I(self, newI):
        if not isinstance(newI, int):
            raise ValueError("I musi być liczbą całkowitą")
        self.i = newI
        

    def exportListToTxtFile(self):
        scriptDir = os.path.dirname(__file__)
        os.chdir(scriptDir)

        fh = open("lista.txt", "w", encoding="utf-8")
        
        for category, product in self.shoppingList.items():
                fh.write(f" Kategoria: {category}\n")
                for p in product:
                    fh.write(f" - {p}\n")
        fh.close()

   

                    



        
            
            