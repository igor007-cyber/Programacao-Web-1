from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Pagina Inicial'

@app.route('/sobre')
def sobre():
    return 'Ola meu nome é igor, sou estudante em Sistema de informação na area da T.I'

@app.route('/experiencia')
def experiencia():
    return 'Ja trabalhei no banco do nordete | Fiz estagio na area de tecnologia em desenvolvedor web'

@app.route('/formacao')
def formacao():
    return 'Formação: Superior incompleto'

@app.route('/contato')
def contato():
    return 'Email: igor-ramalho@hotmail.com'

if __name__ == '__main__':
    app.run(debug=True)

