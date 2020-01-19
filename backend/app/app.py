import sys
from flask import Flask, render_template
from lib import create_message

app = Flask(__name__,
            static_url_path='',
            static_folder='../../dist',
            template_folder='../../dist')

sys.dont_write_bytecode = True


@app.route('/')
def web():
    print('#web')
    return render_template('index.html')


@app.route("/api/<path>", methods=['GET'])
def api(path: str = '') -> str:
    print('#api')
    return create_message(path)


if __name__ == "__main__":
    print("## main ##")
    app.run(host='0.0.0.0', port=5000, debug=True)
