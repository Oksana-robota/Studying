from flask import Flask
from logging.config import dictConfig



app = Flask(__name__)

dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '%(levelname)s %(message)s',
    }}
})

from .views import *

