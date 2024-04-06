N = int(input("Введите количество слов: "))
predloz = ""

for i in range(N):
    slovo = input("Введите слово: ")
    predloz += slovo
    predloz += " "

print("Результат:", predloz)
