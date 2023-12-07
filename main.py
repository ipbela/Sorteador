import random
import time


def fase_Facil():
    round = 1
    totalVida = 100
    primo = 10

    while primo > 0:
        if primo % 2 == 0 or primo % 3 == 0 or primo % 5 == 0 or primo % 7 == 0:  # Verificando números que não são primos
            primo = random.randint(1, 100)  # sorteador
            totalVida = 100  # Inicializando a variável totalVida aqui fora do loop
            break
        else:
            continue

    while totalVida > 0:  # Enquanto totalVida for maior que 0 ele continua no jogo
        num_sorteado = float(input("Qual número foi sorteado? "))
        if num_sorteado == primo:  # se o numero que o usuario digitar for igual ao primo, o programa termina
            print(f"Parabéns você acertou! O número sorteado foi: {primo}")
            break
        else:
            # verificação para nao fazer conta com numero negativo
            if primo > num_sorteado:
                dif_vida = primo - num_sorteado
            else:
                dif_vida = num_sorteado - primo

            totalVida -= dif_vida  # atualiza a variavel totalVida a cada round, igual: totalVida = dif_vida - totalVida

            if totalVida > 0:  # se totalVida for maior que 0 , ele faz a condição para continuar rodando, com a determinada frase
                print("Você errou. Tente novamente!")

                round += 1

                print(f"Pontos de vida ao final do {round}º round: {totalVida}")

            else:  # se não, ele conta o numero do round e mostra a frase de término
                print(f"Suas vidas acabaram! Você chegou até o round {round}. Parabéns!")
                break


# if __name__ == "__main__":
#     fase_Facil()


def fase_Media():
    round = 1
    totalVida = 100
    primo = 10
    chutes = 1
    tempo_inicial = time.time();
    tempo = 10

    while primo > 0:
        if primo % 2 == 0 or primo % 3 == 0 or primo % 5 == 0 or primo % 7 == 0:  # Verificando números que não são primos
            primo = random.randint(1, 100)  # sorteador
            totalVida = 100  # Inicializando a variável totalVida aqui fora do loop
            break
        else:
            continue

    while totalVida > 0 or chutes <=3 or time <=10:  # Enquanto totalVida for maior que 0 ele continua no jogo
        num_sorteado = float(input("Qual número foi sorteado? "))
        if num_sorteado == primo:  # se o numero que o usuario digitar for igual ao primo, o programa termina
            print(f"Parabéns você acertou! O número sorteado foi: {primo}")
            break
        else:
            # verificação para nao fazer conta com numero negativo
            if primo > num_sorteado:
                dif_vida = primo - num_sorteado
            else:
                dif_vida = num_sorteado - primo

            totalVida -= dif_vida  # atualiza a variavel totalVida a cada round, igual: totalVida = dif_vida - totalVida

            if totalVida > 0:  # se totalVida for maior que 0 , ele faz a condição para continuar rodando, com a determinada frase
                print("Você errou. Tente novamente!")

                round += 1
                chutes += 1

                print(f"Pontos de vida ao final do {round}º round: {totalVida}")

            else:  # se não, ele conta o numero do round e mostra a frase de término
                tempo_final = time.time();
                tempo_total = tempo_final - tempo_inicial


                if tempo_total >= tempo:
                    print("Seu tempo acabou!")
                    break

                print(f"Suas vidas e\ou chances acabaram! Você chegou até o round {round}. Parabéns!")
                break


# if __name__ == "__main__":
#     fase_Media()

def fase_Dificil():
    round = 1
    totalVida = 100
    primo = 10
    chutes = 1
    tempo_inicial = time.time();
    tempo = 10

    while primo > 0:
        if primo % 2 == 0 or primo % 3 == 0 or primo % 5 == 0 or primo % 7 == 0:  # Verificando números que não são primos
            primo = random.randint(1, 100)  # sorteador
            totalVida = 100  # Inicializando a variável totalVida aqui fora do loop
            break
        else:
            continue

    while totalVida > 0 or chutes <=3 or time <=10:  # Enquanto totalVida for maior que 0 ele continua no jogo
        num_sorteado = float(input("Qual número foi sorteado? "))
        if num_sorteado == primo:  # se o numero que o usuario digitar for igual ao primo, o programa termina
            print(f"Parabéns você acertou! O número sorteado foi: {primo}")
            break
        else:
            # verificação para nao fazer conta com numero negativo
            if primo > num_sorteado:
                dif_vida = primo - num_sorteado
            else:
                dif_vida = num_sorteado - primo

            totalVida -= dif_vida  # atualiza a variavel totalVida a cada round, igual: totalVida = dif_vida - totalVida

            if totalVida > 0:  # se totalVida for maior que 0 , ele faz a condição para continuar rodando, com a determinada frase
                print("Você errou. Tente novamente!")

                round += 1
                chutes += 1

                print(f"Pontos de vida ao final do {round}º round: {totalVida}")

            else:  # se não, ele conta o numero do round e mostra a frase de término
                tempo_final = time.time();
                tempo_total = tempo_final - tempo_inicial


                if tempo_total >= tempo:
                    print("Seu tempo acabou!")
                    break

                print(f"Suas vidas e\ou chances acabaram! Você chegou até o round {round}. Parabéns!")
                break


if __name__ == "__main__":
    fase_Dificil()