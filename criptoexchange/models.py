import requests
from config import api_key

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