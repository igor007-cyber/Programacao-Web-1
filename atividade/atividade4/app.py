from flask import Flask, render_template, request, redirect, url_for
from validacao import valida_cadastro

app = Flask(__name__,template_folder='template')

motorista = []
destino = []
tempo = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signup')
def signup():    
    aceito = request.args.get('aceito')
    if aceito:
        return render_template('adicionar-topik.html', aceito=aceito)
    
    erro = request.args.get('erro')
    if erro:
        return render_template('adicionar-topik.html', erro=erro)
    else:
        return render_template('adicionar-topik.html') 
    
       
        
@app.route('/register', methods=['POST'])
def register():
    motorista.append(request.form['nome'])
    destino.append(request.form['destino'])
    tempo.append(request.form['horario'])
    
    msg = valida_cadastro(motorista, destino, tempo)
    ok = 'Cadastro realizado'
    if msg is not None:
        return redirect(url_for('signup',erro=msg))
    
    return redirect(url_for('signup', aceito=ok))


@app.route('/lista')
def lista_topick():
    Mo = motorista
    De = destino
    Te = tempo
    tam = len(motorista)
    return render_template('listar-topik.html', Motorista=Mo,Destino=De,Tempo=Te,Tam=tam)

@app.route('/Atualizar_topik/<int:x>')
def editar_topik(x):
    return render_template('editar-topik.html', x=x, Motorista=motorista[x], Destino=destino[x], Tempo=tempo[x])



@app.route('/editar-topik/<int:x>', methods=['POST'])
def Editar(x):
    
    mo=request.form['motorista']  
    de=request.form['destino'] 
    te=request.form['horario'] 
    
    motorista[x] = mo
    tempo[x] = te
    destino[x] = de

    return redirect(url_for('lista_topick'))


@app.route('/excluir/<int:x>')
def excluir(x):
    
    del motorista[x]
    del destino[x]
    del tempo[x]
    return redirect(url_for('lista_topick'))
    
    

if __name__ == '__main__':
    app.run(debug=True)   