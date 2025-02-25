from flask import render_template

def init_app(app):
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
