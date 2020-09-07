import requests

class Peticiones:

    monedas=()
    monedas_dict={}

    def __init__(self):
        COINMARKET_API_KEY = "2448e9c9-b938-4f0e-85f1-9878a7b41c87"
        headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': COINMARKET_API_KEY
        }

        data = requests.get("https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest",headers=headers).json()
        for cripto in data["data"]:
            self.monedas_dict[cripto["symbol"]]=cripto["name"]
        
        self.monedas = self.monedas_dict.keys()

    def esmoneda(self, cripto):
        return cripto in self.monedas

peticion = Peticiones()

moneda = input("Indique el nombre de la moneda a verificar: ")
while not peticion.esmoneda(moneda):
        print("Moneda Invalida.")
        moneda=input("Ingrese el nombre de la moneda: ")
else:
    print("La moneda con symbol:",moneda,"y nombre:",peticion.monedas_dict.get(moneda),
          "es valida porque existe en coimnmarketcap.com")
