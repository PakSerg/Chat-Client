import socket
import eel

from back.utilities import *


def start_working(client: socket.socket) -> None:
    listen_to_get_user_id(client) 
    eel.switchToChat()
    get_and_load_chat_history(client)

    print('История чата успешно загрузилась')

    while True:
        try:
            data: dict = get_json_from_server(client)
            print('the data has been received')

            print(data)
            action = data.get('header')

            if action == 'new_message':
                print('новое сообщение')
                load_new_message(data) 

            elif action == 'new_chat':
                print('Новый чат')
                load_new_chat(data)
                
        except Exception as ex:
            client.close() 
            print(ex)
            print('ЧТо-то пошло не так\n')
            break


def load_new_message(message_data: dict) -> None: 
    print('load_new_message начала работу')
    
    time = message_data.get('time')
    content = message_data.get('content')
    sender_name = message_data.get('username')
    chat_id = message_data.get('chat_id')

    eel.addNewMessage(chat_id, time, content, sender_name)

def load_new_chat(chat_data: dict) -> None: 

    print('передаём данные по новому чату в eel')
    
    chat_id = chat_data.get('chat_id')
    chat_name = chat_data.get('chat_name')

    eel.addNewChat(chat_id, chat_name)


def get_and_load_chat_history(client: socket.socket) -> None: #TODO 
    chat_history: list[dict] = get_json_from_server(client, 10000)

    eel.loadChatHistory(chat_history)


def try_get_connection(client: socket.socket, host: str, port: int) -> None:
    try:
        client.connect((host, port))
    except ConnectionRefusedError:
        print("Connection refused. Make sure the server is running.")
        exit(1)
    except Exception as e:
        print(f"An error occurred: {e}")
        exit(1)


def listen_to_get_user_id(client: socket.socket) -> None:
    user_id = -1
    while user_id == -1:
        user_id = try_get_user_id(client)

    eel.loadUserID(user_id)


def try_get_user_id(client: socket.socket) -> int:
    try:
        user_id_str: str = get_string_from_server(client)
        user_id = int(user_id_str)
        return user_id
    except ConnectionRefusedError:
        print("Connection refused. Make sure the server is running.")
        exit(1)
    except Exception as e:
        print(f"An error occurred: {e}")
        exit(1)