from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'I was taught to start developing from backend to frontend '

if __name__ == '__main__':
    app.run(debug=True)
