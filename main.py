from flask import Flask, request
from apps.test import Test
from apps.example import Example

app = Flask(__name__)


@app.route("/test", methods=['POST'])
def test():
    return Test().run(request)


@app.route("/example", methods=['POST'])
def example():
    return Example().run(request)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8080)
