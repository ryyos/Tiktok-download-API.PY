from libs import blueprint
from flask import Flask

app = Flask(__name__)

app.register_blueprint(blueprint=blueprint)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port = 8888)