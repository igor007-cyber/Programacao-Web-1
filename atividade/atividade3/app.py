from flask import Flask, render_template

app = Flask(__name__,template_folder='template')

@app.route('/')

def index():
    return render_template('index.html',\
        titulo_pagina="Bem vindo ao Delyveri",\
        conteudo='Qual é o seu pedido?')

@app.route('/sobre')
def sobre():
    return render_template('sobre.html', titulo_pagina='Delivery Wigle')

@app.route('/menu')
def menu():
    return render_template('menu.html', titulo_pagina='Delivery Wigle')

@app.route('/cardapio')
def cardapio():
    return render_template('cardapio.html', titulo_pagina='Delivery Wigle')

@app.route('/pagamento')
def pagamento():
    return render_template('pagamento.html', titulo_pagina='Delivery Wigle')

@app.route('/rodape')
def rodape():
    return render_template('rodape.html', titulo_pagina='Delivery Wigle')



if __name__ == '__main__':
    app.run(debug=True)