import pytest

from .schemas import GameOptions
from .calculation import World

@pytest.fixture
def world_object():
    test_data = {'shape': {'len': '4', 'width': '4'},
                     'alive_mols': ['0-0', '0-1', '1-0', '0-2'],
                 'interrupt': False,
                 'speed': 1}
    return World(GameOptions(**test_data))


@pytest.fixture
def test_data_without_mols():
    return {'shape': {'len': '4', 'width': '4'},
            'interrupt': False,
            'speed': 1}

