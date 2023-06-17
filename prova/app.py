from flask import Flask, render_template, request, redirect, url_for
from confirmar import validar

app = Flask(__name__,template_folder='template')

nome = []
senha = []
email = []
confSenha = []
tam = len(nome)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/cadastro_funcionarios')
def cadastro_funcionarios():
    sucesso = request.args.get('sucesso')
    if sucesso:
        return render_template('cadastor.html',sucesso=sucesso)
    
    view = request.args.get('view')
    if view:
        return render_template('cadastor.html',view=view)
    else:
        return render_template('adicionar-topik.html')  


@app.route('/cadastrar_funcionarios', methods=['POST'])
def cadastrar_funcionarios():
    x = 0
    nome.append(request.form['nome'])
    senha.append(request.form['senha'])
    email.append(request.form['email'])
    confSenha.append(request.form['confsenha'])
    
    for a in range(0,tam):
        x = a
    
    msg = validar(nome[x], senha[x], email[x], confSenha[x])
    ok = 'Cadastro realizado com sucesso'
    if msg is not None:
        return redirect(url_for('cadastro_funcionarios',view=msg))
                
    return redirect(url_for('cadastro_funcionarios',sucesso=ok))

@app.route('/listar')
def listar():
    return render_template('lista.html', nome=nome, senha=senha, email=email, tam=tam)

@app.route('/editar')
def editar():
    

@app.route('/excluir')
def excluir():
    
