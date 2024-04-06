import random
prav = 0
neprav = 0
while neprav < 3:
    chislo1 = random.randint(1, 9)
    chislo2 = random.randint(1, 9)
    result = chislo2 + chislo1
    print(str(chislo1) + " + " + str(chislo2) + ": ")
    chislo = input()

    if int(chislo) == result:
        print("Правильно!")
        prav += 1
    else:
        print("Ответ неверный")
        neprav += 1

print("Игра окончена. Правильных ответов: " + str(prav))
