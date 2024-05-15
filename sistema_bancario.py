menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[nc] Nova Conta
[lc] Listar Contas
[nu] Novo Usuário
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
AGENCIA = "0001"
LIMITE_SAQUES = 3
usuarios = []
contas = []

def saque(*,saldo, valor, extrato, limite, numero_saques):
    if numero_saques >= LIMITE_SAQUES:
        print("Operação falhou! Você já atingiu o seu limite de saques diários")
    elif valor > limite:
        print(f"Operação falhou! O saque não pode exceder o seu limite de R$ {limite:.2f}")
    elif valor <= 0:
        print("Operração Falhou, você digitou um valor inválido")
    elif valor > saldo:
        print('Operação Falhou! Saldo Insuficiente')
    else:
        print('Saque Realizado com Sucesso')
        extrato += f"Saque de R$ {valor:.2f}\n"
        print(f"Saque de R$ {valor:.2f} realizado com sucesso \n\nSaldo Anterior: {saldo}")
        saldo -= valor
        print(f"Novo Saldo: {saldo}")
        numero_saques += 1

    return saldo, extrato

def depositar(saldo, deposito, extrato, /):
    if deposito > 0:
        print(f"Depósito de R$ {deposito:.2f} feito com sucesso \n\nSaldo Anterior: {saldo}")
        saldo += deposito
        print(f"Novo Saldo: {saldo}")
        extrato += f"Depósito de R$ {deposito:.2f}\n"
    else:
        print("Valor Inválido")
    return saldo, extrato

def mostra_extrato(saldo,/,*,extrato):
    print(extrato)
    print(f"Saldo: R$ {saldo:.2f}")

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n@@@ Já existe usuário com esse CPF! @@@")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("=== Usuário criado com sucesso! ===")


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")


def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(linha)

while True:

    opcao = input(menu)

    if opcao == "d":
      print('DEPOSITAR'.center(50,'='))
      deposito = float(input('Valor a ser depositado: R$'))
      saldo, extrato = depositar(saldo, deposito, extrato)

    elif opcao == "s":
        print('SACAR'.center(50,'='))
        valor = float(input('Valor do Saque: '))
        saldo, extrato = saque(saldo= saldo, valor = valor, extrato = extrato, limite = limite, numero_saques = numero_saques)
        
    elif opcao == "e":
        print('EXTRATO'.center(50,'='))
        mostra_extrato(saldo,extrato = extrato)

    elif opcao == "nc":
        numero_conta = len(contas) + 1

        conta = criar_conta(AGENCIA, numero_conta, usuarios)

        if conta:
            contas.append(conta)

    elif opcao == "lc":
        listar_contas(contas)

    elif opcao == "nu":
        criar_usuario(usuarios)

    elif opcao == "q":
        break
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")