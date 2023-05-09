from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return f"ola"

@app.route("/user/<name>")
def index(name):
    return f"User {name}"

if __name__ == '__main__':
    app.run(debug=True)
