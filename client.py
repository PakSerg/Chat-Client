import eel
import socket
import threading
import json
from back import back
from back import utilities


HOST = '127.0.0.1'
PORT = 5002


@eel.expose
def send_message_to_server(message: str, user_id: int) -> None:
    time_now: str = utilities.get_current_time()

    message_data = {
        'time': time_now, 
        'content': message, 
        'user_id': user_id
    }
    print(message_data)
    client.send(json.dumps(message_data).encode('utf-8'))


@eel.expose
def sign_up(name: str, password: str) -> None:
    hashed_password = utilities.hash(password)
    sign_up_data = json.dumps({
        'sign_up': True, 
        'name': name, 
        'hashed_password': hashed_password
    })
    client.sendall(sign_up_data.encode('utf-8'))


@eel.expose 
def log_in(name: str, password: str) -> None:
    hashed_password = utilities.hash(password)
    log_in_data = json.dumps({
        'log_in': True, 
        'name': name, 
        'hashed_password': hashed_password
    })
    client.sendall(log_in_data.encode('utf-8'))


if __name__ == "__main__":
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    back.try_get_connection(client, HOST, PORT)

    thread = threading.Thread(target=back.start_working, daemon=True, args=(client,))
    thread.start()  

    eel.init('front')
    eel.start('index.html', size=(500, 600), mode='chrome')
