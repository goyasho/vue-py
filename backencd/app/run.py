from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/', methods=['GET'])
@app.route("/<path>", methods=['GET'])
def hello(path: str = '') -> str:
    return "Hello World! {}".format(path)


if __name__ == "__main__":
    print("## main ##")
    app.run(host='0.0.0.0', port=5000, debug=True)
