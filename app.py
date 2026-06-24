from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({
        "message": "Welcome to Joel's API"
    })


@app.route("/health")
def health():
    return jsonify({
        "status": "UP"
    })


@app.route("/info")
def info():
    return jsonify({
        "location": "Maryland"
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
