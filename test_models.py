
from criptoexchange.models import TodoCoinApiIO
from config import api_key

def test_todocoinapiio():
    todas = TodoCoinApiIO()
    assert isinstance(todas, TodoCoinApiIO)
    todas.trae(api_key)
    assert len(todas.criptos) == 15913
    assert len(todas.no_criptos) == 219