from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)
#print('O computador escolheu {}'. format(itens[computador]))
print("""Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA""")
jogador = int(input('Qual é sua jogada?'))
print('JO')
sleep (1)
print('KEN')
sleep (1)
print('PO!!!')
sleep (1)
print('-=-' * 20)
print('O computador jogou {}'. format(itens[computador]))
print('O jogador jogou {}'. format(itens[jogador]))
print('-=-' * 20)
if computador == 0: #computador jogou PEDRA
    if jogador == 0:
         print('EMPATE')
    elif jogador == 1:
         print('JOGADOR VENCE')
    elif jogador == 2:
         print('COMPUTADOR VENCE')
elif computador == 1: #computador jogou PAPEL
    if jogador == 0:
        print('COMPUTADOR VENCE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCE')
elif computador == 2: #computador jogou TESOURA
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('COMPUTADOR VENCE')
    elif jogador == 2:
        print('EMPATE')
