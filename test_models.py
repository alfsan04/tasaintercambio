import pytest
from criptoexchange.models import TodoCoinApiIO, Cambio, ModelError
from config import api_key

def test_todocoinapiio():
    todas = TodoCoinApiIO()
    assert isinstance(todas, TodoCoinApiIO)
    todas.trae(api_key)
    assert len(todas.criptos) == 15913
    assert len(todas.no_criptos) == 220

def test_cambio_OK():
    btcEur = Cambio('BTC')
    assert btcEur.tasa is None
    assert btcEur.horafecha is None
    btcEur.actualiza(api_key)
    assert btcEur.tasa > 0
    assert isinstance(btcEur.horafecha, str)

def test_cambio_no_OK():
    noOK = Cambio("KKTUA")
    assert noOK.tasa is None
    assert noOK.horafecha is None
    #noOK.actualiza(api_key) hacer cuando da error, mirar en romanos

    with pytest.raises(ModelError) as exceptionInfo:
        noOK.actualiza(api_key)

    assert str(exceptionInfo.value) == "550: You requested specific single item that we don't have at this moment."
