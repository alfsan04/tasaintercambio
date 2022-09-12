from criptoexchange.models import Cambio, TodoCoinApiIO, ModelError
from config import api_key

todas = TodoCoinApiIO()
todas.trae(api_key)

print("{} de {}".format(len(todas.criptos),len(todas.criptos) + len(todas.no_criptos)))

cripto = input("Introduzca una cripto conocida: ").upper()
while cripto != "":
    if cripto in todas.criptos:
        tipoCambio = Cambio(cripto)
        try:
            tipoCambio.actualiza(api_key)
            print("{:.2f} €".format(tipoCambio.tasa))
        except ModelError as mensaje:
            print("Se ha producido el error {}".format(mensaje))

    cripto = input("Introduzca una cripto conocida: ").upper()