import os


class Product:
    def __init__(self):
        self.name = ""
        self.value =""
        self.categoryList = ["pieczywo", "warzywo", "owoc", "mięso", "wędlina", "napoje", "nabiał"]
        self.category = ""
        self.shoppingList ={}
        self.choice = False
        self.dec = True
        
        

    def choiceCategory(self):
        d = True
        while d:
            choice = str(input("""Wpisz kategorię, do której będziesz dodawał produkty. Do wyboru masz:
                                    \n- pieczywo,\n- warzywa,\n- owoce,\n- mięso,\n- wędlina,\n- napoje,\n- nabiał \n- jeśli natomiast chcesz zakończyć to wpisz 'exit': """)).lower()
            if choice in self.categoryList:
                self.category = choice
                self.choice = True
                break
            elif choice == "exit":
                self.exportListToTxtFile()
                d = False
            else:
                print("UPS! wybrałeś błędną kategorię :(, spróbuj ponownie")
                self.choice = False

        return choice
        
    def addProduct(self):
        pr = input("podaj nazwę produktu: ")
        self.name = pr
    
    def addValue(self):
        val = input("podaj wagę/ ilość: ")
        self.value = val

    def get_Product(self):
        return self.name
    def get_Value(self):
        return self.value

    def get_SelfDec(self):
        return self.dec

    def exportListToTxtFile(self):
        scriptDir = os.path.dirname(__file__)
        os.chdir(scriptDir)

        fh = open("lista.txt", "w", encoding="utf-8")
        
        for category, product in self.shoppingList.items():
                fh.write(f" Kategoria: {category}\n")
                for p in product:
                    fh.write(f" - {p}\n")

        fh.close()
        
    def addProductToList(self):
        self.dec = True
        if self.dec:
            self.choiceCategory()# trzeba wyjść z tego jakoś zeby podstawiała się po decyzji
            if self.choiceCategory == "exit":
                self.dec = False
                return self.dec
            else:
                self.addProduct()
                self.addValue()
            

            if not self.choice:
                raise TypeError("Nie wybrano kategorii!")
            if self.category not in self.shoppingList:
                self.shoppingList[str(self.category)] = []
            
            if self.category in self.shoppingList and  self.name and self.value != None:
                product = f"Nazwa: {str(self.name)}" +f" Waga/ Ilość: {str(self.value)}"
                self.shoppingList[self.category].append(product)

            for category, product in self.shoppingList.items():
                print(f"Kategoria: {category}")
                for p in product:
                    print(f" - {p}")
                


            
        

            
               
          