from flask import Flask

app = Flask(__name__)

def greet():
    return "Welcome to DVP Week 12 CI/CD Assignment!"

def add(a, b):
    return a + b

@app.route('/')
def home():
    return greet()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
