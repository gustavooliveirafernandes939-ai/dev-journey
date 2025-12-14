from random import randint
sorteado = randint(1, 10)
vidas = 3

while True:
    palpite = int(input("Digite um número "))
    if palpite == sorteado:
        print("Você acertou")
        break
    if palpite < sorteado:
        print("Errou por menos")
    elif palpite > sorteado:
        print("Errou por mais") 

    vidas = vidas-1

    if vidas == 0:
      print ("Game Over")