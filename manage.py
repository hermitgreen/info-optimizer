from main import create_app
from flask import Flask


flask = Flask(__name__)
app = create_app(flask)

if __name__ == '__main__':
    app.run()
