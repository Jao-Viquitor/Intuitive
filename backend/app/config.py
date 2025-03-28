from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
from decimal import Decimal

load_dotenv()
app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

def decimal_default(obj):
    if isinstance(obj, Decimal):
        return float(obj)
    raise TypeError