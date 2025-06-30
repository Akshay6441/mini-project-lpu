# filepath: c:\Users\Lenovo\Desktop\mini-project-lpu-1\app.py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Mini Project!"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')