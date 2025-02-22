import requests


class GetApi():
    def __init__(self):
        self.currencyValueList = {}
        


    def getCurrencyValue(self):

        url ="https://api.nbp.pl/api/exchangerates/tables/a?format=json"

        try:
            response = requests.get(url)
            response.raise_for_status()
                 
            self.currencyValueList = response.json()
            
            #$print("Aktualne kursy walut pobrane")
            #print("----------------------------")

            #for rate in self.currencyValueList[0]['rates']:
            #    currency = rate['currency']
            #    code = rate['code']
            #    mid = rate['mid']
            #    print(f"{currency}: {code} : {mid}")
            #    print()
                               
        except requests.exceptions.HTTPError as error:
            print("Błąd pobrania api", error)
        finally:
            return self.currencyValueList
