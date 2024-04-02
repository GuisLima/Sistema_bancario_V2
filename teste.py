def cadastros_de_usuarios():

    menu_cadastros_usuario = f'''
        [1] - Novo Cadastro
        [2] - Sair
    '''

    # inicialização do dicionário vazio
    banco_cadastros_usuarios = {}
    
     
    # Digitação e verificação do cpf
    while True:

        print (menu_cadastros_usuario)

        try:
            escolha_usuario = int(input('Escolha a sua opção: '))

        except ValueError:
            print ('Valor incorreto, tente novamente')

        if escolha_usuario == 1:
            digitacao_cpf = input ('Digite o seu CPF: ')
            # Verificação se a entrada do usuário contém apenas digitos e se o tamanho é de 11 caracteres
            if digitacao_cpf.isdigit() and len(digitacao_cpf) == 11:
                # Verifação se o CPF já encontra-se no dicionário
                if digitacao_cpf in banco_cadastros_usuarios.keys():
                    print ('Este cpf já encontra-se cadastrado')
                else:
                    banco_cadastros_usuarios[digitacao_cpf] = {
                    'Nome': input('Digite o seu nome: '),
                    'Data de Nascimento': input('Digite a sua Data de Nascimento: '),
                    'Endereço': input('Digite o endereço: ')
                 }
                    print (banco_cadastros_usuarios)
                    print ('Cadastro Concluído com sucesso')
                
            else:
                print ('CPF inválido')

        elif escolha_usuario == 2:
            print ('Programa encerrado, obrigado!')
            break

        else:
            print ('Alternativa incorreta, tente 1 ou 2')
    
    return banco_cadastros_usuarios

