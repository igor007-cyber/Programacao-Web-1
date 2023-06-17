def validar(nome, email ,senha, consenha):
    if nome == "":
        return 'Falta prencher o campo nome'
    elif len(nome) <= 3:
        return 'O nome tem que ser maior que 3'  
    elif email == "":
        return 'Falta prencher o campo Email'
    elif senha == "":
        return 'Falta prencher o campo senha'
    elif consenha == "":
        return'Falta prencher o campo confirmar senha'
    elif senha != consenha:
        return 'Campos senha e confirmar senha, eles não são iguais'
    else:
        return None