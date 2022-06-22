from unittest import result
from behave import step
from calc import soma

result = None

@step('somar "{val_0:d}" com "{val_1:d}"')
def test_soma(context, val_0, val_1):
    global result
    result = soma(val_0, val_1)

@step('O resultado deve ser "{resultado:d}"')
def test_soma_result(context, resultado):
    assert result == resultado