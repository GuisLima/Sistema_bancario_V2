def validar_cpf(cpf):
    # Valida o CPF na Função de Cadastro de Usuários
    if cpf.isdigit() and len(cpf) == 11:
        return True
    else:
        return False
    
def validar_data_nascimento(data):
    # Valida a data de nascimento na função de Cadastro de Usuários
    if data.isdigit() and len(data) == 8:
        return True
    else:
        return False

def cadastros_usuarios():
    # Inicializa um dicionário vazio
    usuario = {}
    
    # Efetua um looping de verificação da digitação do CPF, através da função de validar CPF
    while True:
        cpf = input('Digite seu CPF (Sem espaços ou pontos): ')
        if validar_cpf(cpf):
            break
        else:
            print('O CPF está inválido, digite sem espaços ou pontos')
    
    # Solicita a digitação do nome completo do usuário
    nome = input('Digite seu nome: ')

    # Efetua um looping de verificação através da função de validação de data de nascimento
    while True:
        data_nascimento = input('Digite sua data de nascimento (Formato: DDMMAAAA): ')
        if validar_data_nascimento(data_nascimento):
            break
        else:
            print ('A data de nascimento encontra-se invalida! Utilize o (Formato: DDMMAAAA)')
     
    # Solicita o endereço do usuário
    endereco = input ('Digite o seu endereço completo (Formato: logradouro, nro - bairro - cidade/siga estado): ')

    # Adiciona ao dicionário uma chave de CPF, impedindo assim que o mesmo usuário possa cadastrar o mesmo CPF
    # Cria um dicionário aninhado com as informações complementares
    usuario[cpf] = {
        'Nome': nome,
        'Data de Nascimento': data_nascimento,
        'Endereço': endereco
    }

    print ('Cadastro finalizado com sucesso!')

    # Retorna o dicionário com as informações inclusas acima
    return usuario

def filtragem_cpfs(cpf, lista):
    for usuario in lista:
        if cpf in usuario:
            return True
    return False

def criar_conta_corrente(bd_usuario, numero_conta):
    # Inicializa o dicionário vazio
    contas_corrente = {} 
    # Define uma constante para a agência que será sempre a mesma
    AGENCIA = '0001'


    while True:
        digitacao_cpf = input('Digite o seu CPF: ')

        # Verifica se o CPF consta na lista da função filtragem CPFS
        if filtragem_cpfs(digitacao_cpf, bd_usuario):
            # Adiciona informações ao dicionário vazio
            contas_corrente[digitacao_cpf] = {'Agencia': AGENCIA, 'C/C': numero_conta}
            print ('Conta cadastrado com sucesso!')
            break
        else:
            print ('Este CPF não encontra-se cadastrado! ')


    return contas_corrente
   
def deposito(saldo, valor_deposito, extrato, /):
    if valor_deposito > 0:
        # Adiciono uma tupla a lista criada, onde identifico se é um deposito e armazeno o valor digitado pelo usuário
        extrato.append(('Deposito',valor_deposito))
        print (f'O valor R$ {valor_deposito:.2f} foi depositado com sucesso!')
        # Soma-se o valor do deposito ao saldo do usuário.
        saldo = saldo + valor_deposito

    else:
        print ('Ops! Você digitou um número invalido!')
 
    return saldo, extrato

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

def saque(* , saldo, valor_saque, extrato, limite_de_operacao):
        
    # No saque o usuário pode sacar até R$ 500,00 reais e possui um limite de 3 operações diárias
    if 0 < valor_saque <= 500:
        # Verifico também se o valor do saque, é maior que o saldo atual.
        if saldo >= valor_saque:
            if limite_de_operacao > 0:
            # Adiciono uma tupla a lista criada, onde identifico se é um saque e armazeno o valor digitado pelo usuário
                 extrato.append(('Saque',valor_saque))
                 print(f"O valor R$ {valor_saque:.2f} foi sacado com sucesso!")
                 # Deduz o valor do saque do saldo do usuário
                 saldo -= valor_saque
                 # Deduz 1 a partir do limite de operação, que se inicializa com 3.
                 limite_de_operacao -= 1
            else:
                 print("Você atingiu o limite de operações diárias.")
        else:
              print("Você não possui saldo suficiente.")
    else:
           print("O limite de valor por operação é de R$ 500,00 reais")

    return saldo, extrato, limite_de_operacao

def menu():
    menu = f'''
    ========== MENU ==========
     [1] - Cadastrar Usuário
     [2] - Cadastrar Conta
     [3] - Deposito
     [4] - Saque
     [5] - Extrato
     [6] - Listar Contas
     [0] - Sair
    ==========================
    '''

    print(menu)

def main():
    # Inicialização de listas
    bd_usuarios = []
    operacoes = []
    bd_contas_correntes = []

    # Inicialização de variáveis e constantes
    LIMITE_DE_OPERACAO = 3
    saldo = 0
    numero_conta = 0

    # Apresentação 
    print ('Olá! Seja bem vindo, nesse sistema você conseguirá realizar operações bancárias.')

    while True:

        menu()

        # Efetuando validação da entrada  do usuário, para as opções desejadas
        try:
            escolha_usuario = int(input('Digite a opção desejada: '))

        except ValueError:
            print ('Você digitou uma opção invalida, tente novamente!')
            continue

        if escolha_usuario == 0:
            print ('Obrigado por utilizar o sistema, volte sempre!')
            break

        elif escolha_usuario == 1:
            cadastro_usuario = cadastros_usuarios()
            bd_usuarios.append(cadastro_usuario)
            
            
        elif escolha_usuario == 2:   
            numero_conta = len(bd_contas_correntes) + 1     
            cadastro_conta_corrente = criar_conta_corrente(bd_usuarios, numero_conta)
            bd_contas_correntes.append(cadastro_conta_corrente)
        
        elif escolha_usuario == 3:
            valor_deposito = float(input('Digite o valor que deseja depositar: '))

            saldo, operacoes = deposito(saldo, valor_deposito, operacoes)

        elif escolha_usuario == 4:
            valor_saque = float(input('Digite o valor que deseja sacar: '))

            saldo, operacoes, LIMITE_DE_OPERACAO = saque(saldo=saldo, valor_saque=valor_saque, extrato=operacoes, limite_de_operacao=LIMITE_DE_OPERACAO)

        elif escolha_usuario == 5:
            saldo, operacoes = extrato(saldo, extrato=operacoes)

        elif escolha_usuario == 6:
            print (bd_contas_correntes)

main()