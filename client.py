import eel
import socket
import threading
import middle.mid
import subprocess

from back import back
from config import HOST, PORT
    

# Функция для перезапуска приложения
# @eel.expose
# def restart_app():
#     print('Функция работает')
#     subprocess.run("venv/Scripts/python.exe client.py")



if __name__ == "__main__":
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    back.try_get_connection(client, HOST, PORT)

    middle.mid.client = client

    thread = threading.Thread(target=back.start_working, daemon=True, args=(client,))
    thread.start()  

    eel.init('interface')
    eel.start('index.html', size=(1300, 800), mode='chrome')
