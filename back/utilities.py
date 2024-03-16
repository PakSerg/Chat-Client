import datetime
from hashlib import sha256
import socket
import json

from config import *


def get_current_time() -> str:
    dt = datetime.datetime.now()

    hours_str =  f'0{dt.hour}' if len(str(dt.hour)) == 1 else dt.hour
    minutes_str = f'0{dt.minute}' if len(str(dt.minute)) == 1 else dt.minute
    time_now = f'{hours_str}:{minutes_str}'

    return time_now


def hash(string: str) -> str:
    hashed_string: str = sha256(string.encode()).hexdigest()
    return hashed_string[:16]


def send_json_to_server(client: socket.socket, data: dict) -> None:
    client.sendall(json.dumps(data).encode('utf-8'))


def get_json_from_server(client: socket.socket, data_size: int = MSG_SIZE) -> dict:
    data = json.loads(client.recv(data_size).decode('utf-8'))
    return data


def get_string_from_server(client: socket.socket, data_size: int = MSG_SIZE) -> str:
    string = client.recv(data_size).decode('utf-8')
    return string