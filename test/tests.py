from src.main import *
from unittest.mock import patch

import pytest
import pytest_asyncio

@pytest.mark.asyncio
async def test_funcao_teste():
    with patch('random.randint', return_value=12345):
        result = await funcao_teste()

    assert result == {"teste": True, "num_aleatorio": 12345}


@pytest.mark.asyncio
async def root_test():
    result = await root_test()

    assert result == {"message": "Hello World"}


@pytest.mark.asyncio
async def deucerto_test():
    result = await deucerto_test()
    assert result == {"teste": "se viu é pq deu certo!"}