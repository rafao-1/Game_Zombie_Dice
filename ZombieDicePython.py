#Aluno: Rafael Carlos Calixto

import random


comeca_partida = False

#define dados
dado_verde = "C,P,C,T,P,C"  # 6 dados verdes
dado_amarelo = "T,P,C,T,P,C"  # 4 dados amarelos
dado_vermelho = "T,P,T,C,P,T"  # 3 dados vermelhos

copo = []


def adicionar_dados():    #adicionar os dados
    for i in range(0, 6):
        copo.append(dado_verde)
    for i in range(0, 4):
        copo.append(dado_amarelo)
    for i in range(0, 3):
        copo.append(dado_vermelho)


turno = 0

numero_jogadores = 0
while(numero_jogadores < 2):
    numero_jogadores = int(input("Digite o número de jogadores na partida: \n"))

    if (numero_jogadores < 2):
        print("AVISO: Precisa-se ao menos de 2 jogadores!\n")

lista_jogadores = []
for ind in range(0, numero_jogadores):
    nome = input("Qual o nome do jogador? \n")

if numero_jogadores >= 2:
    comeca_partida = True # iniciar a partida
    cerebros = 0
    tiros = 0
    adicionar_dados()
    i = 1
    while (i < numero_jogadores +1):
        player = dict({'jogador': i, 'cerebros': 0, 'tiros': 0})
        lista_jogadores.append(player)
        i = i + 1

        print("Partida iniciada! ")

        while comeca_partida == True:
            for player[i + 1] in lista_jogadores:
                try:
                    print("\n Olá", nome, "digite o que deseja fazer:".format(nome))
                    jogar = int(input("[1] - Jogar os dados, [2] Finalizar turno ou [3] Trocar de jogador: \n"))
                except:
                    print("valor inválido!")

                if jogar == 1:
                    for i in range(0, 3):
                        num_sorteado = int(random.randrange(0, len(copo)))
                        print("Dado sorteado {}: {} ".format((i + 1), num_sorteado))

                        dado_sorteado = copo[num_sorteado]  # 'lança' o dado e verifica qual a face sorteada
                        face_dado = int(random.randrange(0, 5))  # obtem a face do dado

                        if dado_sorteado[face_dado] == "C":  # tirou "cerebro no dado
                            print("Você comeu um cérebro!!")
                            cerebros = cerebros + 1


                        elif dado_sorteado[face_dado] == "T":  # tirou tiro no dado
                            print("Você levou um tiro!!")
                            tiros = tiros + 1


                        else:
                            print("A vítima escapou!!")


                elif jogar == 2:
                    pontos = cerebros
                    print("Turno finalizado! Fez", pontos, "pontos!")
                    print(lista_jogadores)
                    turno += 1
                    tiros = 0

                elif jogar == 3:
                    print("Próximo jogador!")
                    turno += 2
                    tiros <- 0;
                    cerebros <- 0;

        while comeca_partida == True:
            for player[i + 1] in lista_jogadores:
                try:
                    print("\n Olá,", nome,"digite o que deseja fazer:".format(nome))
                    jogar = int(input("[1] - Jogar os dados, [2] Finalizar turno ou [3] Trocar de jogador: \n"))
                except:
                    print("valor inválido!")

                if jogar == 1:
                    for i in range(0, 3):
                        num_sorteado = int(random.randrange(0, len(copo)))
                        print("Dado sorteado {}: {} ".format((i + 1), num_sorteado))

                        dado_sorteado = copo[num_sorteado]  # 'lança' o dado e verifica qual a face sorteada
                        face_dado = int(random.randrange(0, 5))  # obtem a face do dado

                        if dado_sorteado[face_dado] == "C":  # tirou "cerebro no dado
                            print("Você comeu um cérebro!!")
                            cerebros = cerebros + 1


                        elif dado_sorteado[face_dado] == "T":  # tirou tiro no dado
                            print("Você levou um tiro!!")
                            tiros = tiros + 1


                        else:
                            print("A vítima escapou!!")

