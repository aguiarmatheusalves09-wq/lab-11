from q1 import *
entregas = []

while True:
    print("\nEntregas")
    print("1) Criar entrega\n2) Listar entregas\n3) Sair")
    resposta = input("Escolha uma das opções acima: ")

    if resposta == "1":
        print("1) Entrega terrestre\n2) Entrega aérea")
        tipo = input("Selecione o tipo de entrega: ")
        endereco = input("Digite o endereço de destino: ")
        peso = float(input("Digite o peso da entrega: "))

        if tipo == "1":
            distancia = float(input("Digite a distância em km: "))
            entrega = EntregaTerrestre(endereco, peso, distancia)
        elif tipo == "2":
            taxa_despacho = float(input("Digite a taxa de despacho: "))
            entrega = EntregaAerea(endereco, peso, taxa_despacho)
        else:
            print("Tipo de entrega inválido.")
            continue

            entregas.append(entrega)
            print("Entrega adicionada com sucesso.")

    elif resposta == "2":
        if not entregas:
            print("Nenhuma entrega cadastrada.")
        else:
            for numero, entrega in enumerate(entregas, start=1):
                print(f"\nEntrega {numero}")
                print(entrega.imprimir_dados())

    elif resposta == "3":
        break
    else:
        print("Opção inválida.")