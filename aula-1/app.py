# importando o flask
from flask import Flask

# carregando o flask na variável app
app = Flask(__name__)

# criando a primeira rota do site
@app.route('/')

# criando função no site
def home():
    # retornando a mensagem de boas vindas
    return '<h1>Bem-vindo ao site do Miguel Isack </h1>'

if __name__ == '__main__':
    # iniciando o servidor no localhost na porta 5000, modo de depuração ativado
    app.run(host='localhost', port=5000, debug=True)
