import eel
import socket
import threading
import json

from back.chatting import get_current_time


HOST = '127.0.0.1'
PORT = 5002

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    client.connect((HOST, PORT))
except:
    print('Ошибка подключения к серверу')


def receive_messages_from_server(client: socket.socket) -> None:
    while True:
        try:
            message = client.recv(1024).decode('utf-8') #TODO: принимать от сервера не строку, а словарь
            print(message)
            eel.addMessageToChat(message) #TODO: переделать эту функцию в JavaScript под словарь
        except:
            print("Ошибка")
            client.close()
            break


@eel.expose
def send_message(message: str, user_id: int) -> None:

    time_now: str = get_current_time()

    message_data = {
        'time': time_now, 
        'content': message, 
        'user_id': user_id
    }
    serialized_message_data = json.dumps(message_data)

    client.send(serialized_message_data.encode('utf-8'))


if __name__ == "__main__":
    eel.init('front')
    eel.start('index.html', size=(500, 600), mode='chrome')

    thread = threading.Thread(target=receive_messages_from_server, daemon=True, args=(client,))
    thread.start()