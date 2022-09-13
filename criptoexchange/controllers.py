from criptoexchange.models import Cambio, TodoCoinApiIO, ModelError
from config import api_key
from criptoexchange.views import mostrarError, mostrarTipoCambio, pideCripto

class Exchanger:
    def ejecuta(self):
        todas = TodoCoinApiIO()
        todas.trae(api_key)

        cripto = pideCripto()

        while cripto != "":
            if cripto in todas.criptos:
                tipoCambio = Cambio(cripto)
                try:
                    tipoCambio.actualiza(api_key)
                    mostrarTipoCambio(tipoCambio.tasa)
                except ModelError as mensaje:
                    mostrarError(mensaje)

            cripto = pideCripto()