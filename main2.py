from q2 import *

while True:
    print("\n1) - Cartão\n2) - PIX\n3) - Boleto\n4) - Sair")
    metodo = input("Escolha uma opção: ")

    if metodo == "1":
        numero_cartao = input("Digite o número do cartão: ")
        pagamento = CartaoCredito("pendente", numero_cartao)
    elif metodo == "2":
        chave_pix = input("Digite a chave Pix: ")
        pagamento = Pix("pendente", chave_pix)
    elif metodo == "3":
        codigo_de_barras = input("Digite o código de barras: ")
        pagamento = Boleto("pendente", codigo_de_barras)
    elif metodo == "4":
        break
    else:
        print("Método de pagamento inválido.")
        continue

    while True:
        print("\n1) Processar pagamento\n2) Cancelar pagamento")
        print("3) Gerar comprovante\n4) Escolher outro método")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            resultado = pagamento.processar_pagamento()
        elif opcao == "2":
            resultado = pagamento.cancelar_pagamento()
        elif opcao == "3":
            resultado = pagamento.gerar_comprovante()
        elif opcao == "4":
            break
        else:
            print("Opção inválida.")
            continue

        if resultado is not None:
            print(resultado)
