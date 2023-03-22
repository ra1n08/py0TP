from flask import Flask
from main import generate_hash
from colorama import Fore, Back, Style
import threading

app = Flask(__name__)

@app.route('/')
def index():
    # print(generate_hash())
    print(Fore.GREEN + generate_hash() + Fore.RESET)
    return generate_hash()


if __name__ == '__main__':
    app.run(debug=True)
    