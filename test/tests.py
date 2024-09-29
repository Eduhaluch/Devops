from src.main import *
from unittest.mock import patch


def test_funcao_teste():
    with patch('random.randint', return_value=12345):
        result = test_funcao_teste()
        yield result
    assert result == {"teste": True, "num_aleatorio": 12345}



def root_test():
    result = root_test()
    yield result
    assert result == {"message": "Hello World"}



def deucerto_test():
    result = deucerto_test()
    yield result
    assert result == {"teste": "se viu é pq deu certo!"}