from src.main import funcao_teste, root, deucerto
from unittest.mock import patch
import pytest

@pytest.mark.asyncio
async def test_funcao_teste():

    with patch('random.randint', return_value=12345):
        result = await funcao_teste()


    assert result == {"teste": True, "num_aleatorio": 12345}

@pytest.mark.asyncio
async def test_root():

    result = await root()

    assert result == {"message": "Hello World"}

@pytest.mark.asyncio
async def test_deucerto():

    result = await deucerto()

    assert result == {"teste": "se viu é pq deu certo!"}