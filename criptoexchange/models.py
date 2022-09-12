import requests
from config import api_key

class ModelError(Exception):
    pass

class TodoCoinApiIO:
    def __init__(self):
        self.criptos = []
        self.no_criptos = []

    def trae(self, api_key):
        r = requests.get("https://rest.coinapi.io/v1/assets?apikey={}".format(api_key))
        if r.status_code != 200:
            raise Exception("Error en consulta de assets: {}".format(r.status_code))
        lista_candidatas = r.json()
        for candidata in lista_candidatas:
            if candidata["type_is_crypto"]:
                self.criptos.append(candidata["asset_id"])
            else:
                self.no_criptos.append(candidata["asset_id"])

class Cambio:
    def __init__(self, cripto):
        self.cripto = cripto
        self.tasa = None
        self.horafecha = None

    def actualiza(self, api_key):
        r = requests.get("https://rest.coinapi.io/v1/exchangerate/{}/EUR?apikey={}".format(self.cripto, api_key))
        resultado = r.json()
        if r.status_code == 200:
            self.tasa = resultado['rate']
            self.horafecha = resultado['time']
        else:
            raise ModelError("{}: {}".format(r.status_code, resultado["error"]))