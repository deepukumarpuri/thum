
from os


class Var(object):
    API_ID = int(os.environ.get('API_ID'))
    API_HASH = os.environ.get('API_HASH'))
    BOT_TOKEN = os.environ.get('BOT_TOKEN'))
    SESSION_NAME = os.environ.get('SESSION_NAME', 'F2LxBot'))
    BIN_CHANNEL = int(os.environ.get('BIN_CHANNEL'))
    DATABASE_URL = int(os.environ.get('DATABASE_URL'))
    UPDATES_CHANNEL = int(os.environ.get('UPDATES_CHANNEL', None))
