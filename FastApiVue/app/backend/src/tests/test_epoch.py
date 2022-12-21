# test = [[1,1,1,0],
#         [1,0,0,0],
#         [0,0,0,0],
#         [0,0,0,0],]
import pytest

@pytest.mark.asyncio
async def test_epoch_1(world_object):
    expected = [[1, 1, 0, 1],
                [1, 0, 0, 1],
                [0, 0, 0, 0],
                [0, 1, 0, 0], ]

    await world_object.live_an_epoch()
    assert world_object.cur_epoch_desk == expected

    expected = [[0, 1, 0, 1],
                [0, 1, 1, 1],
                [1, 0, 0, 0],
                [0, 1, 1, 0], ]

    await world_object.live_an_epoch()
    assert world_object.cur_epoch_desk == expected


def test_neighbours_count(world_object):
    expected_values = [[2, 3, 1, 3],
                       [2, 4, 2, 3],
                       [1, 1, 0, 1],
                       [2, 3, 2, 2],]
    test_counter = []
    [test_counter.append([(world_object._check_neighbours(j, i)) for i in range(4)]) for j in range(4)]
    assert test_counter == expected_values
