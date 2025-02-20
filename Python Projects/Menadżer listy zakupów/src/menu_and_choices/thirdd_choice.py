import os
import psycopg2

class ThirdChoice():
    def __init__(self):
        self.user = "postgres"
        self.password = "admin123"
        self.host = "localhost"
        self.database = "MLZ"

    def getActualList(self):
        try:
            connection = psycopg2.connect(host = self.host, user= self.user, password = self.password, dbname =  self.database)
            print("--------")
            print("nawiązano połączenie z bazą")
            cursor = connection.cursor()
        
            showAll = "SELECT * FROM shopping_list_manager ORDER BY category ASC"

            cursor.execute(showAll)
            result = cursor.fetchall()
            
            scriptDir = os.path.dirname(__file__)
            os.chdir(scriptDir)

            fh = open("lista.txt", "w", encoding="utf-8")
        
            x = 0
            for i in result:
                shpList = i                
                print(x,". |NAZWA|: "+ shpList[1]+ " |WARTOŚĆ|: "+ shpList[2] + " |KATEGORIA|: " +  shpList[3] )
                fh.write(". |NAZWA|: "+ shpList[1]+ " |WARTOŚĆ|: "+ shpList[2] + " |KATEGORIA|: " +  shpList[3] + "\n")
                x +=1
                print()

            fh.close()
            

            connection.commit()
            print("--------")
           

        except(Exception,psycopg2.DatabaseError) as error:
            print("Błąd podczas aktualizacji listy", error)    
        finally:
            cursor.close()
            connection.close()
