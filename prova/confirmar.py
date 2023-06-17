def validar(nome, email ,senha, consenha):
    if nome == "":
        print('Falta prencher o campo nome')
    elif len(nome) <= 3:
        print('O nome tem que ser maior que 3')  
    elif email == "":
        print('Falta prencher o campo Email')
    elif senha == "":
        print('Falta prencher o campo senha')
    elif consenha == "":
        print('Falta prencher o campo confirmar senha')
    elif senha != consenha:
        print('Campos senha e confirmar senha, eles não são iguais')
    else:
        return None