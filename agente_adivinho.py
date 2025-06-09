def agente_adivinho(numero_secreto):
    baixo = 1
    alto = 100
    tentativas = 0

    while baixo <= alto:
        tentativas += 1
        meio = (baixo + alto) // 2
        print(f"Chute: {meio}")

        if meio == numero_secreto:
            print(f"Acertei em {tentativas} tentativas!")
            return
        elif meio < numero_secreto:
            print("É maior...")
            baixo = meio + 1
        else:
            print("É menor...")
            alto = meio - 1

agente_adivinho(13);
