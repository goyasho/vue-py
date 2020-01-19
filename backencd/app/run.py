import sys
from flask import Flask, jsonify, request
from app.lib import create_message


app = Flask(__name__)

sys.dont_write_bytecode = True


@app.route('/', methods=['GET'])
@app.route("/<path>", methods=['GET'])
def hello(path: str = '') -> str:
    return create_message(path)


if __name__ == "__main__":
    print("## main ##")
    app.run(host='0.0.0.0', port=5000, debug=True)
