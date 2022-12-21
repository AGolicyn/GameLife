import pytest
from ..schemas import *

def test_molecules_schema_correct_data():
    test_data = ['12-5', '4-3', '2-8']

    result = AliveMolecules(alive_mols=test_data)

    assert result.molecules == [Molecule(row=12, col=5),
                                Molecule(row=4, col=3),
                                Molecule(row=2, col=8)]

def test_molecules_schema_data_without_separator():
    test_data = ['12-5', '43', '2-8']

    with pytest.raises(ValueError, match='Coords must be separated by "-"'):
        AliveMolecules(alive_mols=test_data)

def test_molecules_schema_separator_only_without_data():
    test_data = ['12-5', '-', '2-8']

    with pytest.raises(ValueError, match='Coords must be integers'):
        AliveMolecules(alive_mols=test_data)


def test_molecules_schema_data_invalid_types():
    test_data = ['12.-5', '2-9', '2-8']

    with pytest.raises(ValueError, match='Coords must be integers'):
        AliveMolecules(alive_mols=test_data)

def test_molecules_schema_data_negative_integers():
    # If separator will be changed :)
    test_data = ['-12-5', '2-9', '2-8']

    with pytest.raises(ValueError, match='Coords must be integers'):
        AliveMolecules(alive_mols=test_data)

def test_playground_with_correct_data():
    test_data = {
        'len': '10',
        'width': 15,
    }
    result = PlayGround(**test_data)

    assert result.row_num == 15
    assert result.col_num == 10

def test_playground_with_negative_data():
    test_data = {
        'len': '-10',
        'width': 15,
    }
    with pytest.raises(ValueError, match='Shape values must be greater then zero'):
        PlayGround(**test_data)

def test_playground_with_zero_data():
    test_data = {
        'len': '0',
        'width': 15,
    }
    with pytest.raises(ValueError, match='Shape values must be greater then zero'):
        PlayGround(**test_data)


def test_speed_with_negative_data():
    test_data = {'speed': -2.5}

    result = EpochSpeed(**test_data)

    assert result.speed > 0


def test_full_input():
    test_data = {'shape': {'len': '6', 'width': '10'},
                 'alive_mols': ['3-3', '3-5', '5-4', '2-5', '0-5', '1-4', '4-4'],
                 'interrupt': False,
                 'speed': 1}

    obj = GameOptions(**test_data)
    assert obj == {
        'molecules': [Molecule(row=3, col=3), Molecule(row=3, col=5),
                      Molecule(row=5, col=4), Molecule(row=2, col=5),
                      Molecule(row=0, col=5), Molecule(row=1, col=4),
                      Molecule(row=4, col=4)],
        'shape': PlayGround(width=10, len=6),
        'interrupt': False,
        'speed': 1,
    }
