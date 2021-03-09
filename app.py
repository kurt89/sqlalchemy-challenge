from flask import Flask, jsonify


app = Flask(__name__)

Unfortunately, I ran out of time to complete the second part of the homework this week. I did invest 20 hours on it.


@app.route("/")
def home():
    return "Hi"


@app.route("/normal")
def normal():
    return hello_dict


@app.route("/jsonified")
def jsonified():
    return jsonify(hello_dict)


if __name__ == "__main__":
    app.run(debug=True)
