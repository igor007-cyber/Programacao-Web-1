def valida_cadastro(nome, tempo, destino):
    if nome == '':
        return 'O campo nome é obrigatório'
    elif len(nome) < 3:
        return 'O nome deve ter pelo menos 3 caracteres'
    elif tempo == '':
        return 'O campo Horario é obrigatório'
    elif destino == '':
        return 'O campo destino é obrigatório'
    else:
        return None