import pytest
from unittest.mock import Mock
from traer import traer
import json

def test_traer(mocker):
    mock_traer_datos = mocker.patch('traer.traer')
    mock_traer_datos.return_value = '{"hits":{"hits":""}}'
    cantidad = 3
    resultado = traer(cantidad)
    res_dic = json.loads(resultado)
    assert isinstance(resultado, str)
    assert resultado[0] == '{'
    assert "hits" in res_dic.keys()
    assert len(res_dic["hits"]["hits"]) >= cantidad