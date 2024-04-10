### Sistema de Operações Bancárias

Este é um sistema de operações bancárias básico desenvolvido em Python. Ele permite que os usuários realizem diversas operações, como cadastro de usuário, cadastro de conta corrente, depósito, saque, e visualização de extrato.

#### Funcionalidades

1. **Cadastro de Usuário**
    - Solicita ao usuário que insira seu CPF, nome completo, data de nascimento e endereço.
    - Realiza validações nos dados inseridos, como CPF e data de nascimento.
    - Evita o cadastro de múltiplos usuários com o mesmo CPF.

2. **Cadastro de Conta Corrente**
    - Permite ao usuário criar uma conta corrente associada ao seu CPF.
    - A agência é definida como '0001'.
    - Verifica se o CPF fornecido está cadastrado no sistema.

3. **Depósito**
    - Permite que o usuário deposite um valor em sua conta corrente.
    - Atualiza o saldo da conta e registra a operação no extrato.

4. **Saque**
    - Permite ao usuário sacar um valor da sua conta corrente.
    - Verifica se o valor do saque não excede o saldo disponível e se o limite de operações diárias não foi ultrapassado.
    - Atualiza o saldo da conta, registra a operação no extrato e atualiza o limite de operações.

5. **Extrato**
    - Exibe o extrato da conta corrente, mostrando todas as operações realizadas e o saldo atual.
    - Caso não haja operações, informa que não houve atividades.

6. **Listar Contas**
    - Lista todas as contas correntes cadastradas no sistema.

#### Utilização
1. Ao iniciar o programa, o usuário é apresentado a um menu com as opções disponíveis.
2. O usuário pode escolher a operação desejada digitando o número correspondente ao menu.
3. O sistema solicitará as informações necessárias para cada operação e fornecerá feedback sobre o resultado.

#### Observações
- O sistema controla o limite de operações diárias para saques.
- As operações são registradas em um extrato, permitindo ao usuário visualizar o histórico de transações.
- O CPF é utilizado como identificador único para cada usuário.
- A implementação assume que as entradas do usuário são válidas e realiza validações básicas nos dados inseridos.
