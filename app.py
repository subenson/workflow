from flask import Flask

app = Flask(__name__)

@app.route("/")
def workflow():
    return {'app': 'workflow'}

if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0', port=5001)
