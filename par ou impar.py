from random import randint
repeticao = int(input('quantas vezes deseja jogar? '))
jogador = 0
maquina = 0
ganhou = 0
for i in range(repeticao):
    if ganhou == 0:
        if repeticao / 2 + 0.5 <= jogador or repeticao / 2 + 0.5 <= maquina:
            if jogador > maquina:
                print('Partida encerrada, pois o jogador venceu')
                ganhou = 1
            else:
                print("partida encerrada, pois a máquina venceu")
                ganhou = 1
        else:
            impopar = int(input('impar(1) ou par(2)? '))
            if impopar < 1 or impopar > 2:
                print("Escolha entre 1 e 2 apenas")
            else:
                pc = randint(0, 99)
                player = int(input('qual numero deseja jogar?'))
                soma = (player + pc)
                print(f'a maquina escolheu {pc}')
                if impopar == 1:
                    if soma % 2 != 0:
                        print('jogador venceu')
                        jogador = jogador + 1
                    else:
                        print('maquina venceu')
                        maquina = maquina + 1
                if impopar == 2:
                    if soma % 2 == 0:
                        print('maquina venceu')
                        maquina = maquina + 1
                    else:
                        print('jogador venceu')
                        jogador = jogador + 1
                print('-' * 20)
print(f'o jogador tem {jogador} pontos')
print(f'maquina tem {maquina} pontos')
if jogador == 0 and maquina == 0:
    print('seu danado fudido ')
else:
    if jogador > maquina:
        print('jogador ganhou')
    else:
        if jogador < maquina:
            print('maquina ganhou')
        else:
            print('empatou! ')
print('-'*20)

#while faz tudo que o for faz mas o for n faz tudo que o while faz
#usar depurador 