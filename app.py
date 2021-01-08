from flask import Flask

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "Welcome to Home Page"


if __name__ == "__main__":
    app.secret_key = "123456789qwerty"
    app.run("localhost", 5000, debug=True)
