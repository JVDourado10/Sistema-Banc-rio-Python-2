menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3


while True:

    opcao = input(menu)

    if opcao == "d":
      print('DEPOSITAR'.center(50,'='))
      deposito = float(input('Valor a ser depositado: R$'))
      if deposito > 0:
          print(f"Depósito de R$ {deposito:.2f} feito com sucesso \n\nSaldo Anterior: {saldo}")
          saldo += deposito
          print(f"Novo Saldo: {saldo}")
          extrato += f"Depósito de R$ {deposito:.2f}\n"
      else:
          print("Valor Inválido")
    elif opcao == "s":
        print('SACAR'.center(50,'='))
        saque = float(input('Valor do Saque: '))
        
        if numero_saques >= LIMITE_SAQUES:
            print("Operação falhou! Você já atingiu o seu limite de saques diários")
        elif saque > limite:
            print(f"Operação falhou! O saque não pode exceder o seu limite de R$ {limite:.2f}")
        elif saque <= 0:
            print("Operração Falhou, você digitou um valor inválido")
        elif saque > saldo:
            print('Operação Falhou! Saldo Insuficiente')
        else:
            print('Saque Realizado com Sucesso')
            extrato += f"Saque de R$ {saque:.2f}\n"
            print(f"Saque de R$ {saque:.2f} realizado com sucesso \n\n Saldo Anterior: {saldo}")
            saldo -= saque
            print(f"Novo Saldo: {saldo}")
            numero_saques += 1


    elif opcao == "e":
        print('EXTRATO'.center(50,'='))
        print(extrato)

    elif opcao == "q":
        break
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")