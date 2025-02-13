import os


class Product():
    def __init__(self):
        self.name = ""
        self.value =""
        self.categoryList = ["pieczywo", "warzywo", "owoc", "mięso", "wędlina", "napoje", "nabiał"]
        self.category = ""
        self.shoppingList ={}
        self.choice = False
        
        

    def choiceCategory(self):
        while True:
            choice = str(input("""Wpisz kategorię, do której będziesz dodawał produkty. Do wyboru masz:
                                    \n- pieczywo,\n- warzywa,\n- owoce,\n- mięso,\n- wędlina,\n- napoje,\n- nabiał \n- jeśli natomiast chcesz zakończyć to wpisz 'exit': """)).lower()
            if choice in self.categoryList:
                self.category = choice
                self.choice = True
                break
            elif choice == "exit":
                self.exportListToTxtFile()
                break
            else:
                print("UPS! wybrałeś błędną kategorię :(, spróbuj ponownie")
                self.choice = False
        
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
    def exportListToTxtFile(self):
        scriptDir = os.path.dirname(__file__)
        os.chdir(scriptDir)

        fh = open("lista.txt", "w", encoding="utf-8")
        
        for category, product in self.shoppingList.items():
                fh.write(f" Kategoria: {category}\n")
                for p in product:
                    fh.write(f" - {p}\n")
                    
        
       # for category, name,  in self.shoppingList.items():
        #    fh.write(f"\nKategoria:" + f"{category}\n Nazwa:{name}")
        fh.close()
        
    def addProductToList(self):
        while True:
            self.choiceCategory()
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

            
               
                


    



        
        


    
           
           
           
    
            


        


















        
    
           
    def categoryChoice(self):
            print()
            choice = str(input("""Wpisz kategorię produktu, który ma zostać dodany do listy zakupów. Do wyboru masz:
                                \n- pieczywo,\n- warzywo,\n- owoc,\n- mięso,\n- wędlina,\n- napoj,\n- nabiał \n: """)).lower()

            if choice in self.categoryList:
                self.category = choice
                print(self.category)
            else:
                print("UPS! wybrałeś błędną kategorię :(, spróbuj ponownie")
            
            while True:
                print()
                choice = str(input("""Wpisz kategorię produktu, który ma zostać dodany do listy zakupów. Do wyboru masz:
                                    \n- pieczywo,\n- warzywo,\n- owoc,\n- mięso,\n- wędlina,\n- napoj,\n- nabiał \n  : """)).lower()

                if choice in self.categoryList:
                    self.category = choice
                    print(self.category)
                elif choice == "x":
                    break
                else:
                    print("UPS! wybrałeś błędną kategorię :(, spróbuj ponownie")
                
                    
                
            