import os
from dotenv import load_dotenv 


load_dotenv() 


HOST = os.environ.get('HOST')
PORT = int(os.environ.get('PORT'))

MSG_SIZE = int(os.environ.get('MSG_SIZE'))