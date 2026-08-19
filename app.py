from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>🚀 Application Python Khddama b Docker + Jenkins!</h1>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

