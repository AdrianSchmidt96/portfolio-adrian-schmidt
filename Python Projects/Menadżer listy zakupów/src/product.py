class Product():
    def __init__(self):
        self.name = ""
        self.value =""
        self.categoryList = ["pieczywo", "warzywo", "owoc", "mięso", "wędlina", "napoje", "nabiał"]
        self.category = ""
        self.shoppingList ={}
        

    def choiceCategory(self):
        choice = str(input("""Wpisz kategorię, do której będziesz dodawał produkty. Do wyboru masz:
                                \n- pieczywo,\n- warzywa,\n- owoce,\n- mięso,\n- wędlina,\n- napoje,\n- nabiał \n: """)).lower()
        if choice in self.categoryList:
            self.category = choice
            return True
        else:
            print("UPS! wybrałeś błędną kategorię :(, spróbuj ponownie")
            return False
        
    def addProduct(self):
        self.name = input()
    
    def addValue(self):
        self.value = input()

    def get_Product(self):
        return self.name

    def get_Value(self):
        return self.value
        
    def addProductToList(self):
        if Product.choiceCategory == True:
            if self.shoppingList[self.category] in self.shoppingList:
                if self.name != None and self.category in self.categoryList:
                    self.shoppingList[self.category]= [{"nazwa produktu: " + str(self.name) + "waga/ ilość: " + str(self.value)}+","]
                else:
                    print("nie dodano produktu, spróbuj ponownie")
            else:
                self.shoppingList = {str(self.category) + ": " + ["\n",{"nazwa produktu: " + str(self.name) + "waga/ ilość: " + str(self.value)},]}
        else:
            return TypeError("brak produktu na liście")
    
            


        


















        
    
           
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
                
                    
                
            