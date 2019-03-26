from flask import Flask
from config import Configuration

from posts.afisha import afisha
from posts.cursy import cursy

app = Flask(__name__)
app.config.from_object(Configuration)

app.register_blueprint(afisha, url_prefix='/afisha')

app.register_blueprint(cursy, url_prefix='/cursy')
