from flask import Flask
from config import Configuration

from posts.blueprint import afisha, cursy

app = Flask(__name__)
app.config.from_object(Configuration)

app.register_blueprint(afisha, url_prefix='/afisha')

# app.register_blueprint(kursy, url_prefix='/kursy')
