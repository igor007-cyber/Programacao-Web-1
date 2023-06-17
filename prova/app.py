from flask import Flask, render_template, request, redirect, url_for
from confirmar import validar

app = Flask(__name__,template_folder='template')

nome = []
senha = []
email = []
confSenha = []

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/cadastro')
def cadastro():
    sucesso = request.args.get('sucesso')
    if sucesso:
        return render_template('cadastro.html', sucesso=sucesso)
    
    view = request.args.get('view')
    if view:
        return render_template('cadastro.html',view=view)
    else:
        return render_template('cadastro.html')  


@app.route('/cadastrar_funcionarios', methods=['POST'])
def cadastrar_funcionarios():
    x = 0
    tam = len(nome)
    nome.append(request.form['nome'])
    senha.append(request.form['senha'])
    email.append(request.form['email'])
    confSenha.append(request.form['confsenha'])
    
    for a in range(0,tam):
        x = a
    
    msg = validar(nome[x], senha[x], email[x], confSenha[x])
    ok = 'Cadastro realizado com sucesso'
    if msg is not None:
        return redirect(url_for('cadastro',view=msg))
                
    return redirect(url_for('cadastro',sucesso=ok))

@app.route('/listar')
def listar():
    no = nome
    em = email
    se = senha
    tam = len(nome)
    
    return render_template('lista.html', nome=no, email=em, senha=se, tam=tam)

@app.route('/atualizar/<int:x>')
def atualizar(x):
    return render_template('editar.html', x=x, nome=nome[x], email=email[x], senha=senha[x], confSenha=confSenha[x])


@app.route('/editar/<int:x>', methods=['POST'])
def editar(x):
    
    no = request.form['nome']
    em = request.form['email']  
    se = request.form['senha'] 
    conf = request.form['confSenha'] 
    
    nome[x] = no
    email[x] = em
    senha[x] = se
    confSenha[x] = conf
   
    return redirect(url_for('listar'))

    
@app.route('/excluir/<int:x>')
def excluir(x):
     
    del nome[x]   
    del senha[x]
    del email[x]
    del confSenha[x]
    return redirect(url_for('listar'))

if __name__ == '__main__':
    app.run(debug=True) 