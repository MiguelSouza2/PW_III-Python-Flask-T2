# importando o flask e o render
from flask import Flask, render_template


# carregando o flask na variável app
app = Flask(__name__, template_folder='views')

# criando a primeira rota do site
@app.route('/')

# criando função no site
def home():
    # retornando a mensagem de boas vindas
    return render_template('index.html')

@app.route('/games')

def games():
    game = {
        'titulo': 'CS-GO',
        'ano': '2012',
        'categoria': 'FPS Online',
        'jogadores': ['miguel josé', 'miguel isack', 'leaf', 'aspax', 'quemario', 'trop', 'maxxdiego']

    }
    jogosFriv = ['Fireboy & Watergirl', "Papa's pizzaria", 'Motox3m', 'Bob the Robber', 'Temple Run 2', 'Dynamon']
    
    return render_template('games.html', 
                           game=game, 
                           jogosFriv = jogosFriv)

@app.route('/miguelisack')
def miguelisack():
    return render_template('miguelisack.html')
if __name__ == '__main__':
    # iniciando o servidor no localhost na porta 5000, modo de depuração ativado
    app.run(host='0.0.0.0', port=5000, debug=True)
