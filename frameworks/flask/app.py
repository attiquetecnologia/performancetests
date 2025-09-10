from flask import Flask, jsonify

app = Flask(__name__)

app.secret_key = "123"

@app.route('/', methods=['GET'])
def index():
    return "Hello World"


@app.route("/api", methods=['GET'])
def api():
    dados = [
        {'id': 1, 'name': 'Ronald'},
        {'id': 2, 'name': 'Ronald'},
        {'id': 3, 'name': 'Ronald'},
        {'id': 4, 'name': 'Ronald'},
        {'id': 5, 'name': 'Ronald'},
        {'id': 6, 'name': 'Ronald'},
        {'id': 7, 'name': 'Ronald'},
        {'id': 8, 'name': 'Ronald'},
        {'id': 9, 'name': 'Ronald'},
        {'id': 10, 'name': 'Ronald'},
    ]
    return jsonify(dados)

if __name__ == "__main__":
    app.run()
    