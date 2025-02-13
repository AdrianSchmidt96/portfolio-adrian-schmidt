import os
import json

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
                                    \n- pieczywo,\n- warzywa,\n- owoce,\n- mięso,\n- wędlina,\n- napoje,\n- nabiał \n: """)).lower()
            if choice in self.categoryList:
                self.category = choice
                self.choice = True
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
        
    def addProductToList(self):
        if not self.choice:
           raise TypeError("Nie wybrano kategorii!")
       
        if self.category not in self.shoppingList:
           self.shoppingList[self.category] = []

        if self.name and self.value != None:
            product = {"nazwa: " + str(self.name) +  ", waga/ ilość: " + self.value}
            self.shoppingList[self.category].append(product)

        print(self.shoppingList)
        print()
        print()
        print()
        print()
        print()


    def exportListToTxtFile(self):
        scriptDir = os.path.dirname(__file__)
        os.chdir(scriptDir)
        fh = open("ListaZakupów.json", "w", encoding="utf-8")
        fh.write(json.dumps(str(self.shoppingList)))

        fh.close()


    
           
           
           
    
            


        


















        
    
           
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
                
                    
                
            