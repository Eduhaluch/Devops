from src.main import *
from unittest.mock import patch


def test_funcao_teste():
    with patch('random.randint', return_value=12345):
        result = funcao_teste()

    assert result == {"teste": True, "num_aleatorio": 12345}



def root_test():
    assert root() == {"message": "Hello World"}



def deucerto_test():
    assert deucerto() == {"teste": "se viu é pq deu certo!"}