
predloz = ""

while True:
    slovo = input("Введите слово: ")
    if slovo == "стоп":
        break
    else:
        predloz += slovo
        predloz += " "


print("Результат:", predloz)
