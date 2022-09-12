import requests
from config import api_key

r = requests.get("https://rest.coinapi.io/v1/assets?apikey={}".format(api_key))
if r.status_code != 200:
    raise Exception("Error en consulta de assets: {}".format(r.status_code))

lista_candidatas = r.json()
lista_definitiva = []
for candidata in lista_candidatas:
    if candidata["type_is_crypto"]:
        lista_definitiva.append(candidata["asset_id"])

cripto = input("Introduzca una cripto conocida: ").upper()
while cripto != "":
    if cripto in lista_definitiva:
        r = requests.get("https://rest.coinapi.io/v1/exchangerate/{}/EUR?apikey={}".format(cripto, api_key))
        resultado = r.json()
        if r.status_code == 200:
            print("El precio en euros de un {} es {:.2f} €".format(cripto, resultado['rate']))
        else:
            print(resultado["error"])

    cripto = input("Introduzca una cripto conocida: ").upper()