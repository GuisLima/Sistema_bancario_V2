def extrato(saldo, /, *, extrato):
    if not extrato:
        print ('========= EXTRATO =========')
        print("Não houve operações.")
        print ('===========================')
    else:
        # Imprime cada operação registrada no extrato, seguida pelo valor
        print ('========= EXTRATO =========')
        for operacao, valor in extrato:
            print(f'{operacao} de R$ {valor:.2f}')

        print (f'Seu saldo é de R$ {saldo:.2f}')
        print ('===========================')
    
    return saldo, extrato

def deposito(saldo, valor_deposito, extrato, /):

    if valor_deposito > 0:
        # Adiciono uma tupla a lista criada, onde identifico se é um deposito e armazeno o valor digitado pelo usuário
        extrato.append(('Deposito',valor_deposito))
        print (f'O valor R$ {valor_deposito:.2f} foi depositado com sucesso!')
        # Soma-se o valor do deposito ao saldo do usuário.
        saldo += valor_deposito

    else:
        print ('Ops! Você digitou um número invalido!')
 
    return saldo, extrato 

def saque(* ,saldo, valor_saque, extrato, LIMITE_DE_OPERACAO=3):
        
    # No saque o usuário pode sacar até R$ 500,00 reais e possui um limite de 3 operações diárias
    if 0 < valor_saque <= 500:
        # Verifico também se o valor do saque, é maior que o saldo atual.
        if saldo >= valor_saque:
            if LIMITE_DE_OPERACAO > 0:
            # Adiciono uma tupla a lista criada, onde identifico se é um saque e armazeno o valor digitado pelo usuário
                 extrato.append(('Saque',valor_saque))
                 print(f"O valor R$ {valor_saque:.2f} foi sacado com sucesso!")
                 # Deduz o valor do saque do saldo do usuário
                 saldo -= valor_saque
                 # Deduz 1 a partir do limite de operação, que se inicializa com 3.
                 LIMITE_DE_OPERACAO -= 1
            else:
                 print("Você atingiu o limite de operações diárias.")
        else:
              print("Você não possui saldo suficiente.")
    else:
           print("O valor do saque deve estar entre R$ 0,00 e R$ 500,00.")

    return saldo, extrato 

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

def validar_cpf():
    while True:
        cpf = input (f'Digite aqui o seu CPF (sem pontos ou espaços): ')
        if cpf.isdigit() and len(cpf) == 11:
            return cpf
        else:
            print ('Por favor, digite o seu CPF com 11 digitos e sem pontos ou espaços')

def validar_endereco(validador):
    
        if validador == 'Logradouro, nro':
            while True:
                logradouro = input('Digite o logradouro, numero: ')
                partes_logradouro = logradouro.split(',')
                if len(partes_logradouro) != 2:
                    print ('Digite o endereço e o número separados por virgula')
                else:
                    return logradouro
        elif validador == 'Bairro':
            bairro = input ('Digite o Bairro: ')
            return bairro
        elif validador == 'Cidade':
            cidade = input ('Digite sua Cidade: ')
            return cidade
        elif validador == 'UF':
            while True:
                uf = input('Digite aqui a UF (dois caracteres): ')
                if len(uf) == 2:
                    return uf
                else:
                    print('Por favor, digite a UF com dois caracteres')
          
def criar_conta_corrente():
    conta_corrente = {}

    agencia = '0001'

    cpf = input('Digite o cpf: ')


    if cpf == filtras_usuarios():
        contador = 0
        while True:
            contador += 1
            converter = str(contador)
            conta_corrente[converter] = {'Agencia': agencia, 'Cpf': cpf}
            break
    else:
        print ('Não existe')

    return conta_corrente

def filtras_usuarios(cadastros_usuarios):
    for chave, _ in cadastros_usuarios.items():
        if chave.isdigit() and len(chave) == 11:
            return chave



