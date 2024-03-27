from random import randint
vezes_jogadas = int(input("quantas vezes deseja jogar?: "))
player = 0
bot = 0
for i in range(vezes_jogadas):
    if vezes_jogadas  / 2 + 0.5 <= player or vezes_jogadas  / 2 + 0.5 <= bot:
        print("puts")
    else:
        player = int(input('impar(1) ou par(2)? '))
        bot = randint(0, 10)
        numero = int(input('qual numero deseja jogar?'))
        resultado = (numero + bot)
        print('bot escolheu {}'.format(bot))
        if player == 1:
            if resultado == 1 or resultado == 3 or resultado == 5 or resultado == 7 or resultado == 9 or resulatdo == 11 or resultado == 13 or resultado ==  15 or resultado == 17 or resultado == 19:
                print('player venceu')
                player = player + 1
            else:
                print('bot venceu')
                bot = bot + 1
        if player == 2:
            if resultado == 1 or resultado == 3 or resultado == 5 or resultado == 7 or resultado == 9 or reusltado == 11 or resultado == 13 or resultado ==  15 or resultado == 17 or resultado == 19:
                print('bot venceu')
                bot = bot + 1
            else:
                print('player venceu')
                player = player + 1
print('-' * 20)
print('o player tem {} pontos'.format(player))
print('bot tem {} pontos'.format(bot))
if player > bot:
    print('player ganhou')
else:
    print('bot ganhou')
print('-'*20)
