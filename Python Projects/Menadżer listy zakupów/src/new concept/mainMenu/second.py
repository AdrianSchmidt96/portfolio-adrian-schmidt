import psycopg2
class secondChoice():
    def __init__(self):
        self.user = "postgres"
        self.password = "admin123"
        self.host = "localhost"
        self.database = "MLZ"
        self.gettingShoppingList = []


    def showCurrentList(self):
        try:
            connection = psycopg2.connect(host = self.host, user= self.user, password = self.password, dbname =  self.database)
            print("--------")
            print("""nawiązano połączenie z bazą\n 
                O to lista Twoich zakupów:
                  """)
            
            cursor = connection.cursor()
            showAll = "SELECT * FROM shopping_list_manager"

            cursor.execute(showAll)
            result = cursor.fetchall()
            shoppingList = []
            nList = 0
            n = 1
            for i in result:
                
                shpList = i                
                print(n,". ","|ID|: ", shpList[0]," |NAZWA|: "+ shpList[1]+ " |WARTOŚĆ|: "+ shpList[2] + " |KATEGORIA|: " +  shpList[3] )
                n+=1
                shoppingList.append(i)
                nList +=1
                print()
            self.gettingShoppingList = shoppingList

            return self.gettingShoppingList
            
        except(Exception,psycopg2.DatabaseError) as error:
            print("Błąd podczas wyświetlania listy", error)    
        finally:
            connection.close()
            cursor.close()
            print("--------")
            print("Zamknięto połączenie z bazą danych")
            print()
    
    def updateData(self):
        self.showCurrentList()

        basicInfo =input("Podaj nr ID do zmiany: ")
        num = int(basicInfo)
        
        if num and num in self.gettingShoppingList:
            getChose = self.gettingShoppingList[num-1]
            print(getChose)
            num +1
        else:
            print("Podałeś błędne ID")

        nextInfo = input(("""Co chcesz zmienić?
                          \n1.Nazwę
                          \n2.Wartość
                          \n3.Kategrię
                          \n: """))
        choseNum = int(nextInfo)
        choseNum -=1

        if choseNum == 0:
            update = """
                UPDATE shopping_list_manager
                SET name = %s
                WHERE id = %s
            """
            n = 4 #musze miec ID z listy sql 
            info = input('podaj nową nazwę: ')
            self.update(info,n, update)




        



    def update(self,name,id,update):     
        try:
            connection = psycopg2.connect(host = self.host, user= self.user, password = self.password, dbname =  self.database)
            print("--------")
            print("nawiązano połączenie z bazą")
            cursor = connection.cursor()
           
            cursor.execute(update,(name,id))
           # product = f"Nazwa: {str(pr)}" +f" Waga/ Ilość: {str(val)}"
           # self.shoppingList[self.category].append(product) jak to rozwiązać?
            
            connection.commit()
            print("--------")
            print("Dodano produkt do bazy")

        except(Exception,psycopg2.DatabaseError) as error:
            print("Błąd podczas aktualizacji listy", error)    
        finally:
            cursor.close()
            connection.close()
            
            print("--------")
            print("Zamknięto połączenie z bazą danych")




sec = secondChoice()
sec.updateData()