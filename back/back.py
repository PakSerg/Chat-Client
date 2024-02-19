import socket
import eel
import json


def try_get_connection(client: socket.socket, HOST: str, PORT: 5002):
    try:
        client.connect((HOST, PORT))
        print('Подключение к серверу прошло успешно')
    except:
        print('Ошибка подключения к серверу')



def get_and_load_new_message(client: socket.socket) -> None:
    message_data: dict = json.loads(client.recv(1024).decode('utf-8'))

    message_time = message_data.get('time')
    message_content = message_data.get('content')
    message_author = message_data.get('username')

    eel.addMessageToChat(message_content, message_time, message_author)


def get_and_load_chat_history(client: socket.socket) -> None:
    all_previous_messages: list[dict] = json.loads(client.recv(10000).decode('utf-8') )
    eel.loadChatHistory(all_previous_messages)


def try_get_connection(client: socket.socket, host: str, port: int) -> None:
    try:
        client.connect((host, port))
    except ConnectionRefusedError:
        print("Connection refused. Make sure the server is running.")
        exit(1)
    except Exception as e:
        print(f"An error occurred: {e}")
        exit(1)


def start_working(client: socket.socket) -> None:
    listen_to_get_user_id(client)
    get_and_load_chat_history(client)

    eel.toggleChatWindow()
    eel.toggleSignUpWindow()
    eel.toggleLogInWindow()

    while True:
        try:
            get_and_load_new_message(client)
        except:
            client.close()
            break


def listen_to_get_user_id(client: socket.socket):
    user_id = -1
    while user_id == -1:
        user_id = try_get_user_id(client)

    eel.loadUserID(user_id)


def try_get_user_id(client: socket.socket) -> int:
    try:
        user_id_str: str = client.recv(1024).decode('utf-8')
        user_id = int(user_id_str)
        return user_id
    except ConnectionRefusedError:
        print("Connection refused. Make sure the server is running.")
        exit(1)
    except Exception as e:
        print(f"An error occurred: {e}")
        exit(1)