def validar_cpf():
    while True:
        cpf = input (f'Digite aqui o seu CPF (sem pontos ou espaços): ')
        if cpf.isdigit() and len(cpf) == 11:
            return cpf
        else:
            print ('Por favor, digite o seu CPF com 11 digitos e sem pontos ou espaços')

def validar_endereco(chave):
        
    
        if chave == 'Logradouro, nro':
            while True:
                logradouro = input('Digite o logradouro, numero: ')
                partes_logradouro = logradouro.split(',')
                if len(partes_logradouro) != 2:
                    print ('Digite o endereço e o número separados por virgula')
                else:
                    return logradouro
        elif chave == 'Bairro':
            bairro = input ('Digite o bairro: ')
            return bairro
        elif chave == 'Cidade':
            cidade = input ('Digite sua cidade: ')
            return cidade
        elif chave == 'UF':
            while True:
                uf = input('Digite aqui a UF (dois caracteres): ')
                if len(uf) == 2:
                    return uf
                else:
                    print('Por favor, digite a UF com dois caracteres')




def cadastro_usuario():

    cpf = validar_cpf()
    
    banco_dados_cadastro_usuario = {
        cpf: {
            'Nome': '',
            'Data de Nascimento': '',
            'Endereço': {
                'Logradouro, nro': '',
                'Bairro': '',
                'Cidade': '',
                'UF': '',
            }
        }
    }

    
    for chave in banco_dados_cadastro_usuario[cpf].keys():
        if chave == 'Nome':
            banco_dados_cadastro_usuario[cpf][chave] = input (f'Digite aqui o seu {chave}: ')
        elif chave == 'Data de Nascimento':
            banco_dados_cadastro_usuario[cpf][chave] = input (f'Digite aqui a sua {chave}: ')
        elif chave == 'Endereço':
            for sub_chave in banco_dados_cadastro_usuario[cpf][chave].keys():
                banco_dados_cadastro_usuario[cpf][chave][sub_chave] = validar_endereco(sub_chave)

    return banco_dados_cadastro_usuario

cadastro_usuario()


    