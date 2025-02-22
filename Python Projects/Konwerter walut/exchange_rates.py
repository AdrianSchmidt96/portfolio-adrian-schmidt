from getApi import *

class ShowRates():
    def __init__(self):
        self.getApi = GetApi()

    def x(self):
        currencyList = ["PLN"]
            
        for rate in self.getApi.getCurrencyValue()[0]['rates']:
            code = rate['code']
            currencyList.append(code)
        
        print(currencyList)
        i = 1
        while i:
            setFirstCurrency = input("Podaj walutę(kod): ").upper()
            if setFirstCurrency in currencyList:
                    self.firstCurrency = setFirstCurrency
                    print()
                    while i:
                        getValue = input("Podaj kwotę do wymiany: ")
                        getValue = float(getValue)
                        if getValue > 0:
                            self.firstValue = getValue
                            print()
                            while i:
                                setSecondCurrency = input("Podaj walutę, na którą chcesz wymienić swoje środki: ").upper()
                                if setSecondCurrency in currencyList and setSecondCurrency is not self.firstCurrency:
                                    self.secondCurrency = setSecondCurrency
                                    print()
                                    i = 0
                                    break
                                else:
                                    print("podałeś błędny kod waluty, lub próbujesz wymienić na tę samą walutę... spróbuj ponownie")
                                    self.secondCurrency = None
                        else:
                            print("podałeś kwotę mniejszą od zera.. spróbuj ponownie")
                            self.firstValue = None
            else:
                print("podałeś błędny kod waluty... spróbuj ponownie")
                self.firstCurrency = None
        self.calculation()