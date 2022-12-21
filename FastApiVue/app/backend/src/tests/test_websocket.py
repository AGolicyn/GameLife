import pytest
from fastapi.testclient import TestClient

from ..app import app


@pytest.mark.skip(reason='Endless loop websocket')
def test_websocket():
    client = TestClient(app)
    send_data = {'shape': {'len': 60, 'width': 30},
                 'alive_mols': ['3-48', '6-50', '6-47', '7-46', '8-46', '8-47', '8-48', '7-47', '6-45', '5-45', '4-45',
                                '4-46',
                                '4-47', '4-49', '5-50', '5-51', '6-51', '7-51', '8-52', '8-50'],
                 'interrupt': False,
                 'speed': 1}

    receive_data = ["3-46", "3-47", "3-48", "4-45", "4-46", "4-47", "4-48", "4-49", "4-50", "5-44",
                    "5-45", "5-47", "5-48", "5-49", "5-51", "6-45", "6-47", "6-52", "7-45", "7-49",
                    "7-52", "8-46", "8-48", "8-51", "9-47"]

    with client.websocket_connect('/ws') as websocket:
        websocket.send_json(send_data)
        data = websocket.receive_json()
        print('Inside')
    print('Outside')

    assert receive_data == data
