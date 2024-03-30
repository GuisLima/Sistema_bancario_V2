# Menu de apresentação ao usuário

menu = """
============ MENU ============
       [1] - DEPOSITO
       [2] - SACAR
       [3] - EXTRATO
       [0] - SAIR
===============================       
"""

# CONSTANTE DE LIMITE
LIMITE_DE_OPERACAO = 3

# LISTA PARA ARMAZENAR OPERAÇÕES
extrato = []

# Inicialização do saldo
saldo = 0

# Apresentação
print ('Olá! Seja bem vindo, nesse sistema você conseguirá realizar operações bancárias.')

# Loop operacional do usuário
while True:

    print (menu)

    # Efetuando validação da entrada  do usuário, para as opções desejadas
    try:
     escolha_usuario = int(input('Digite a opção desejada: '))

    except ValueError:
     print ('Você digitou uma opção invalida, tente novamente!')
     continue

    if escolha_usuario == 0:
        print ('Obrigado por utilizar nosso sistema!')
        break

    # O usuário irá depositar o valor, onde a única condição necessária é que o valor seja maior que 0.
    if escolha_usuario == 1:
        valor_deposito = float(input('Digite o valor que deseja depositar: '))

        if valor_deposito > 0:
            # Adiciono uma tupla a lista criada, onde identifico se é um deposito e armazeno o valor digitado pelo usuário
            extrato.append(('Deposito',valor_deposito))
            print (f'O valor R$ {valor_deposito:.2f} foi depositado com sucesso!')
            # Soma-se o valor do deposito ao saldo do usuário.
            saldo += valor_deposito

        else:
            print ('Ops! Você digitou um número invalido!')

    if escolha_usuario == 2:
        valor_saque = float(input('Digite o valor que deseja sacar: '))

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

    if escolha_usuario == 3:
    # Verifica se há operações no extrato
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