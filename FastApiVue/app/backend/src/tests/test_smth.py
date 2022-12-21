from ..calculation import *

test_world = [[0, 0, 0, 0],
              [0, 0, 0, 0],
              [0, 0, 0, 0],
              [0, 0, 0, 0]]


# [0, 0, 0]
# [0, 1, 0]
# [0, 0, c]
#############################
def test_right_downside_default_position_with(test_data_without_mols):
    # schema = [[0, 0, 0, 0],
    #           [0, 1, 0, 0],
    #           [0, 0, 1, 0],
    #           [0, 0, 0, 0]]
    test_data_without_mols['alive_mols'] = {'1-1', '2-2'}
    obj = World(GameOptions(**test_data_without_mols))
    assert obj._check_right_downside(1, 1) == 1
def test_right_downside_default_position_without(test_data_without_mols):
    # schema = [[0, 0, 0, 0],
    #           [0, 1, 0, 0],
    #           [0, 0, n, 0],
    #           [0, 0, 0, 0]]

    test_data_without_mols['alive_mols'] = {'1-1'}
    obj = World(GameOptions(**test_data_without_mols))
    assert obj._check_right_downside(1, 1) == 0
def test_right_downside_left_position_with(test_data_without_mols):
    # schema = [[0, 0, 0, 0],
    #           [0, 0, 0, 1],
    #           [1, 0, 0, 0],
    #           [0, 0, 0, 0]]
    test_data_without_mols['alive_mols'] = {'1-3', '2-0'}
    obj = World(GameOptions(**test_data_without_mols))

    assert obj._check_right_downside(1, 3) == 1
def test_right_downside_left_position_without(test_data_without_mols):
    # schema = [[0, 0, 0, 0],
    #           [0, 0, 0, 1],
    #           [n, 0, 0, 0],
    #           [0, 0, 0, 0]]
    test_data_without_mols['alive_mols'] = {'1-3'}
    obj = World(GameOptions(**test_data_without_mols))

    assert obj._check_right_downside(1, 3) == 0
def test_right_downside_bottom_position_with(test_data_without_mols):
    # schema = [[0, 0, 1, 0],
    #           [0, 0, 0, 0],
    #           [0, 0, 0, 0],
    #           [0, 1, 0, 0]]
    test_data_without_mols['alive_mols'] = {'3-1', '0-2'}
    obj = World(GameOptions(**test_data_without_mols))

    assert obj._check_right_downside(3, 1) == 1
def test_right_downside_bottom_position_without(test_data_without_mols):
    # schema = [[0, 0, n, 0],
    #           [0, 0, 0, 0],
    #           [0, 0, 0, 0],
    #           [0, 1, 0, 0]]
    test_data_without_mols['alive_mols'] = {'3-1'}
    obj = World(GameOptions(**test_data_without_mols))

    assert obj._check_right_downside(3, 1) == 0
def test_right_downside_corner_position_with(test_data_without_mols):
    # schema = [[1, 0, 0, 0],
    #           [0, 0, 0, 0],
    #           [0, 0, 0, 0],
    #           [0, 0, 0, 1]]
    test_data_without_mols['alive_mols'] = {'3-3', '0-0'}
    obj = World(GameOptions(**test_data_without_mols))

    assert obj._check_right_downside(3, 3) == 1
    
def test_right_downside_corner_position_without(test_data_without_mols):
    # schema = [[n, 0, 0, 0],
    #           [0, 0, 0, 0],
    #           [0, 0, 0, 0],
    #           [0, 0, 0, 1]]
    test_data_without_mols['alive_mols'] = {'3-3'}
    obj = World(GameOptions(**test_data_without_mols))

    assert obj._check_right_downside(3, 3) == 0

# [0, 0, 0]
# [0, 1, 0]
# [0, c, 0]
#############################
def test_downside_default_position_with(test_data_without_mols):
    # schema = [[0, 0, 0, 0],
    #           [0, 1, 0, 0],
    #           [0, 1, 0, 0],
    #           [0, 0, 0, 0]]
    test_data_without_mols['alive_mols'] = {'1-1', '2-1'}
    obj = World(GameOptions(**test_data_without_mols))

    assert obj._check_downside(1, 1) == 1
def test_downside_default_position_without(test_data_without_mols):
    # schema = [[0, 0, 0, 0],
    #           [0, 1, 0, 0],
    #           [0, 1, 0, 0],
    #           [0, 0, 0, 0]]
    test_data_without_mols['alive_mols'] = {'1-1'}
    obj = World(GameOptions(**test_data_without_mols))
    assert obj._check_downside(1, 1) == 0
def test_downside_bottom_position_with(test_data_without_mols):
    # schema = [[0, 1, 0, 0],
    #           [0, 0, 0, 0],
    #           [0, 0, 0, 0],
    #           [0, 1, 0, 0]]
    test_data_without_mols['alive_mols'] = {'3-1', '0-1'}
    obj = World(GameOptions(**test_data_without_mols))

    assert obj._check_downside(3, 1) == 1
def test_downside_bottom_position_without(test_data_without_mols):
    # schema = [[0, 1, 0, 0],
    #           [0, 0, 0, 0],
    #           [0, 0, 0, 0],
    #           [0, 1, 0, 0]]
    test_data_without_mols['alive_mols'] = {'3-1'}
    obj = World(GameOptions(**test_data_without_mols))

    assert obj._check_downside(3, 1) == 0

# [0, 0, 0]
# [0, 1, 0]
# [c, 0, 0]
#############################
def test_left_downside_default_position_with(test_data_without_mols):
    # schema = [[0, 0, 0, 0],
    #           [0, 1, 0, 0],
    #           [1, 0, 0, 0],
    #           [0, 0, 0, 0]]
    test_data_without_mols['alive_mols'] = {'1-1', '2-0'}
    obj = World(GameOptions(**test_data_without_mols))

    assert obj._check_left_downside(1, 1) == 1
def test_left_downside_default_position_without(test_data_without_mols):
    # schema = [[0, 0, 0, 0],
    #           [0, 1, 0, 0],
    #           [n, 0, 0, 0],
    #           [0, 0, 0, 0]]

    test_data_without_mols['alive_mols'] = {'1-1'}
    obj = World(GameOptions(**test_data_without_mols))

    assert obj._check_left_downside(1, 1) == 0
def test_left_downside_left_position_with(test_data_without_mols):
    # schema = [[0, 0, 0, 0],
    #           [1, 0, 0, 0],
    #           [0, 0, 0, 1],
    #           [0, 0, 0, 0]]
    test_data_without_mols['alive_mols'] = {'1-0', '2-3'}
    obj = World(GameOptions(**test_data_without_mols))

    assert obj._check_left_downside(1, 0) == 1
def test_left_downside_left_position_without(test_data_without_mols):
    # schema = [[0, 0, 0, 0],
    #           [1, 0, 0, 0],
    #           [0, 0, 0, n],
    #           [0, 0, 0, 0]]
    test_data_without_mols['alive_mols'] = {'1-0'}
    obj = World(GameOptions(**test_data_without_mols))

    assert obj._check_left_downside(1, 0) == 0
def test_left_downside_bot_position_with(test_data_without_mols):
    # schema = [[1, 0, 0, 0],
    #           [0, 0, 0, 0],
    #           [0, 0, 0, 0],
    #           [0, 1, 0, 0]]
    test_data_without_mols['alive_mols'] = {'3-1', '0-0'}
    obj = World(GameOptions(**test_data_without_mols))

    assert obj._check_left_downside(3, 1) == 1
def test_left_downside_corner_position_with(test_data_without_mols):
    # schema = [[0, 0, 0, 1],
    #           [0, 0, 0, 0],
    #           [0, 0, 0, 0],
    #           [1, 0, 0, 0]]
    test_data_without_mols['alive_mols'] = {'3-0', '0-3'}
    obj = World(GameOptions(**test_data_without_mols))

    assert obj._check_left_downside(3, 0) == 1
def test_left_downside_corner_position_without(test_data_without_mols):
    # schema = [[0, 0, 0, n],
    #           [0, 0, 0, 0],
    #           [0, 0, 0, 0],
    #           [1, 0, 0, 0]]
    test_data_without_mols['alive_mols'] = {'3-0'}
    obj = World(GameOptions(**test_data_without_mols))

    assert obj._check_left_downside(3, 0) == 0


# [0, 0, 0]
# [c, 1, 0]
# [0, 0, 0]
#############################
def test_left_side_default_position_with(test_data_without_mols):
    # schema = [[0, 0, 0, 0],
    #           [1, 1, 0, 0],
    #           [0, 0, 0, 0],
    #           [0, 0, 0, 0]]
    test_data_without_mols['alive_mols'] = {'1-1', '1-0'}
    obj = World(GameOptions(**test_data_without_mols))
    assert obj._check_left_side(1, 1) == 1

def test_left_side_default_position_without(test_data_without_mols):
    # schema = [[0, 0, 0, 0],
    #           [n, 1, 0, 0],
    #           [0, 0, 0, 0],
    #           [0, 0, 0, 0]]
    test_data_without_mols['alive_mols'] = {'1-1'}
    obj = World(GameOptions(**test_data_without_mols))
    assert obj._check_left_side(1, 1) == 0

def test_left_side_left_position_with(test_data_without_mols):
    # schema = [[0, 0, 0, 0],
    #           [1, 0, 0, 1],
    #           [0, 0, 0, 0],
    #           [0, 0, 0, 0]]
    test_data_without_mols['alive_mols'] = {'1-0', '1-3'}
    obj = World(GameOptions(**test_data_without_mols))

    assert obj._check_left_side(1, 1) == 1
def test_left_side_left_position_without(test_data_without_mols):
    # schema = [[0, 0, 0, 0],
    #           [1, 0, 0, n],
    #           [0, 0, 0, 0],
    #           [0, 0, 0, 0]]
    test_data_without_mols['alive_mols'] = {'1-0'}
    obj = World(GameOptions(**test_data_without_mols))

    assert obj._check_left_side(1, 0) == 0

# [c, 0, 0]
# [0, 1, 0]
# [0, 0, 0]
#############################
def test_left_upside_default_position_with(test_data_without_mols):
    # schema = [[1, 0, 0, 0],
    #           [0, 1, 0, 0],
    #           [0, 0, 0, 0],
    #           [0, 0, 0, 0]]
    test_data_without_mols['alive_mols'] = {'1-1', '0-0'}
    obj = World(GameOptions(**test_data_without_mols))

    assert obj._check_left_upside(1, 1) == 1
def test_left_upside_default_position_without(test_data_without_mols):
    # schema = [[n, 0, 0, 0],
    #           [0, 1, 0, 0],
    #           [0, 0, 0, 0],
    #           [0, 0, 0, 0]]
    test_data_without_mols['alive_mols'] = {'1-1'}
    obj = World(GameOptions(**test_data_without_mols))

    assert obj._check_left_upside(1, 1) == 0
def test_left_upside_left_position_with(test_data_without_mols):
    # schema = [[0, 0, 0, 1],
    #           [1, 0, 0, 0],
    #           [0, 0, 0, 0],
    #           [0, 0, 0, 0]]

    test_data_without_mols['alive_mols'] = {'0-1', '0-3'}
    obj = World(GameOptions(**test_data_without_mols))

    assert obj._check_left_upside(1, 0) == 1
def test_left_upside_left_position_without(test_data_without_mols):
    # schema = [[0, 0, 0, n],
    #           [1, 0, 0, 0],
    #           [0, 0, 0, 0],
    #           [0, 0, 0, 0]]

    test_data_without_mols['alive_mols'] = {'0-1'}
    obj = World(GameOptions(**test_data_without_mols))

    assert obj._check_left_upside(1, 0) == 0
def test_left_upside_left_corner_position_with(test_data_without_mols):
    # schema = [[1, 0, 0, 0],
    #           [0, 0, 0, 0],
    #           [0, 0, 0, 0],
    #           [0, 0, 0, 1]]

    test_data_without_mols['alive_mols'] = {'0-0', '3-3'}
    obj = World(GameOptions(**test_data_without_mols))

    assert obj._check_left_upside(0, 0) == 1
def test_left_upside_left_corner_position_without(test_data_without_mols):
    # schema = [[1, 0, 0, 0],
    #           [0, 0, 0, 0],
    #           [0, 0, 0, 0],
    #           [0, 0, 0, n]]

    test_data_without_mols['alive_mols'] = {'0-0'}
    obj = World(GameOptions(**test_data_without_mols))
    assert obj._check_left_upside(0, 0) == 0

# [0, c, 0]
# [0, 1, 0]
# [0, 0, 0]
#############################
def test_upside_default_position_with(test_data_without_mols):
    # schema = [[0, 1, 0, 0],
    #           [0, 1, 0, 0],
    #           [0, 0, 0, 0],
    #           [0, 0, 0, 0]]
    test_data_without_mols['alive_mols'] = {'1-1', '0-1'}
    obj = World(GameOptions(**test_data_without_mols))
    assert obj._check_upside(1, 1) == 1
def test_upside_default_position_without(test_data_without_mols):
    # schema = [[0, n, 0, 0],
    #           [0, 1, 0, 0],
    #           [0, 0, 0, 0],
    #           [0, 0, 0, 0]]
    test_data_without_mols['alive_mols'] = {'1-1'}
    obj = World(GameOptions(**test_data_without_mols))

    assert obj._check_upside(1, 1) == 0
def test_upside_top_position_with(test_data_without_mols):
    # schema = [[0, 1, 0, 0],
    #           [0, 0, 0, 0],
    #           [0, 0, 0, 0],
    #           [0, 1, 0, 0]]
    test_data_without_mols['alive_mols'] = {'0-1', '3-1'}
    obj = World(GameOptions(**test_data_without_mols))
    assert obj._check_upside(0, 1) == 1

def test_upside_top_position_without(test_data_without_mols):
    # schema = [[0, 1, 0, 0],
    #           [0, 0, 0, 0],
    #           [0, 0, 0, 0],
    #           [0, n, 0, 0]]
    test_data_without_mols['alive_mols'] = {'0-1'}
    obj = World(GameOptions(**test_data_without_mols))
    assert obj._check_upside(0, 1) == 0

# [0, 0, c]
# [0, 1, 0]
# [0, 0, 0]
#############################
def test_right_upside_default_position_with(test_data_without_mols):
    # schema = [[0, 0, 1, 0],
    #           [0, 1, 0, 0],
    #           [0, 0, 0, 0],
    #           [0, 0, 0, 0]]
    test_data_without_mols['alive_mols'] = {'1-1', '0-2'}
    obj = World(GameOptions(**test_data_without_mols))
    assert obj._check_right_upside(1, 1) == 1
def test_right_upside_default_position_without(test_data_without_mols):
    # schema = [[0, 0, n, 0],
    #           [0, 1, 0, 0],
    #           [0, 0, 0, 0],
    #           [0, 0, 0, 0]]
    test_data_without_mols['alive_mols'] = {'1-1'}
    obj = World(GameOptions(**test_data_without_mols))
    assert obj._check_right_upside(1, 1) == 0
def test_right_upside_right_position_with(test_data_without_mols):
    # schema = [[1, 0, 0, 0],
    #           [0, 0, 0, 1],
    #           [0, 0, 0, 0],
    #           [0, 0, 0, 0]]

    test_data_without_mols['alive_mols'] = {'1-3', '0-0'}
    obj = World(GameOptions(**test_data_without_mols))
    assert obj._check_right_upside(1, 3) == 1
def test_right_upside_right_position_without(test_data_without_mols):
    # schema = [[n, 0, 0, 0],
    #           [0, 0, 0, 1],
    #           [0, 0, 0, 0],
    #           [0, 0, 0, 0]]

    test_data_without_mols['alive_mols'] = {'1-3'}
    obj = World(GameOptions(**test_data_without_mols))
    assert obj._check_right_upside(1, 3) == 0
def test_right_upside_top_position_with(test_data_without_mols):
    # schema = [[0, 0, 1, 0],
    #           [0, 0, 0, 0],
    #           [0, 0, 0, 0],
    #           [0, 0, 0, 1]]
    test_data_without_mols['alive_mols'] = {'0-2', '3-3'}
    obj = World(GameOptions(**test_data_without_mols))
    assert obj._check_right_upside(0, 2) == 1
def test_right_upside_right_corner_position_with(test_data_without_mols):
    # schema = [[0, 0, 0, 1],
    #           [0, 0, 0, 0],
    #           [0, 0, 0, 0],
    #           [1, 0, 0, 0]]

    test_data_without_mols['alive_mols'] = {'0-3', '3-0'}
    obj = World(GameOptions(**test_data_without_mols))
    assert obj._check_right_upside(0, 3) == 1
def test_right_upside_right_corner_position_without(test_data_without_mols):
    # schema = [[0, 0, 0, 1],
    #           [0, 0, 0, 0],
    #           [0, 0, 0, 0],
    #           [n, 0, 0, 0]]

    test_data_without_mols['alive_mols'] = {'0-3'}
    obj = World(GameOptions(**test_data_without_mols))
    assert obj._check_right_upside(0, 3) == 0
##############################
# [0, 0, 0]
# [0, 1, c]
# [0, 0, 0]
def test_right_side_default_position_with(test_data_without_mols):
    # schema = [[0, 0, 0, 0],
    #           [0, 1, 1, 0],
    #           [0, 0, 0, 0],
    #           [0, 0, 0, 0]]
    test_data_without_mols['alive_mols'] = {'1-1', '1-2'}
    obj = World(GameOptions(**test_data_without_mols))
    assert obj._check_right_side(1, 1) == 1
def test_right_side_default_position_without(test_data_without_mols):
    # schema = [[0, 0, 0, 0],
    #           [0, 1, n, 0],
    #           [0, 0, 0, 0],
    #           [0, 0, 0, 0]]
    test_data_without_mols['alive_mols'] = {'1-1'}
    obj = World(GameOptions(**test_data_without_mols))
    assert obj._check_right_side(1, 1) == 0
def test_right_side_right_position_with(test_data_without_mols):
    # schema = [[0, 0, 0, 0],
    #           [1, 0, 0, 1],
    #           [0, 0, 0, 0],
    #           [0, 0, 0, 0]]
    test_data_without_mols['alive_mols'] = {'1-3', '1-0'}
    obj = World(GameOptions(**test_data_without_mols))

    assert obj._check_right_side(1, 3) == 1
def test_right_side_right_position_without(test_data_without_mols):
    # schema = [[0, 0, 0, 0],
    #           [n, 0, 0, 1],
    #           [0, 0, 0, 0],
    #           [0, 0, 0, 0]]
    test_data_without_mols['alive_mols'] = {'1-3'}
    obj = World(GameOptions(**test_data_without_mols))

    assert obj._check_right_side(1, 3) == 0

