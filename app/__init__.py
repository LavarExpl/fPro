from flask import Flask
app = Flask(__name__)
# Import routes (views) after initializing the app to avoid circular imports
from app import routes