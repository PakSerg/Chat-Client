import eel
from back.utilities import * 


client = None


@eel.expose
def send_message_to_server(content: str, sender_id: int, chat_id: int) -> None:
    message_data = {
        'header': 'new_message',

        'content': content, 
        'sender_id': sender_id, 
        'chat_id': chat_id
    }
    send_json_to_server(client, message_data)
    print('Сообщение отправлено на сервер')


@eel.expose
def sign_up(name: str, password: str) -> None:
    sign_up_data = {
        'header': 'sign_up',

        'name': name, 
        'hashed_password': hash(password)
    }
    send_json_to_server(client, sign_up_data)


@eel.expose 
def log_in(name: str, password: str) -> None:
    log_in_data = {
        'header': 'log_in',

        'name': name, 
        'hashed_password': hash(password)
    }
    send_json_to_server(client, log_in_data)


@eel.expose
def create_new_chat(chat_name: str) -> None:
    new_chat_data = {
        'header': 'new_chat', 

        'chat_name': chat_name
    }
    send_json_to_server(client, new_chat_data)


@eel.expose
def create_new_chat_member(chat_id: int, member_id: int):
    new_member_data = {
        'header': 'new_member', 

        'chat_id': chat_id, 
        'member_id': member_id
    }
    send_json_to_server(client, new_member_data)