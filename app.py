from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Horizon Career is LIVE!</h1><p>Designed by Rocky Singh. Education in Russia starts here.</p>"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
