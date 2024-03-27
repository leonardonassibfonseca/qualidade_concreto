from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Bem-vindo à API do meu aplicativo!'

if __name__ == '__main__':
    app.run()