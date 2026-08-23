import random

acertos = 0 
erros = 0
pontuacao = 0
tentativas = 0

animatronics = ["Freddy", "Toy Chica", "Foxy", "Withered Bonnie", "Toy Bonnie", "Puppet"]

while tentativas < 6:
    print("\n=====  MENU FNAF  =====")
    print("""
    1 - Colocar Máscara
    2 - Usar Lanterna
    3 - Dar Corda Na Caixa 
    4 - Sair
    """)

    escolhido = random.choice(animatronics)
    animatronics.remove(escolhido) #Aqui eu removi para que não haja repetição das escolhas

    op = int(input(f"CUIDADO! {escolhido} está quase na sua sala!! \nQual opção você vai tomar? Tome cuidado: "))

    if op == 4:
        print("Encerrando o sistema...")

    tentativas += 1

    #Se houvesse repetição dava para fazer colocando esses índices:

    # resposta_certa = (
    #     (escolhido == animatronics[0] and op == 2)
    #     or (escolhido == animatronics[1] and op == 1)
    #     or (escolhido == animatronics[2] and op == 2)
    #     or (escolhido == animatronics[3] and op == 1)
    #     or (escolhido == animatronics[4] and op == 1)
    #     or (escolhido == animatronics[5] and op == 3)
    # ) 

    resposta_certa = (
        (escolhido == "Freddy" and op == 2)
        or (escolhido == "Toy Chica" and op == 1)
        or (escolhido == "Foxy" and op == 2)
        or (escolhido == "Withered Bonnie" and op == 1)
        or (escolhido == "Toy Bonnie" and op == 1)
        or (escolhido == "Puppet" and op == 3)
    )

    if resposta_certa:
        acertos += 1
        pontuacao += 50
        print("UFA! Você escapou dessa...") 

    else:
        erros += 1
        pontuacao -= 50
        print(f"AAAAAAAAAAAAAAAAAAAAA... {escolhido} TE PEGOU. Você perdeu muita aura...")

print(f"""
\n======  RESULTADOS FINAIS  ======
\nAcertos: {acertos}
Erros: {erros}
\nPontuação Final: {pontuacao}
""")
