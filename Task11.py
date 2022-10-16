# Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.

# numberN = int(input("Введите число N: "))
# if numberN <= 0:
#     print("Вы ввели неверное число")
#     exit()
# result = []
# sum = 0
# for i in range(1, numberN+1):
#     elementN = round((1+1/i)**i, 3)
#     sum += elementN
#     result.append(elementN)
# print(f"Сумма {numberN} чисел последовательности (1+1/N)^N: {result} равна {sum}")

numberN = int(input("Введите число N: "))
if numberN <= 0:
    print("Вы ввели неверное число")
    exit()
list_element = list(range(1,numberN+1))
result = list(map(lambda x: round((1+1/x)**x, 3), list_element))
sum = 0
for i in result:
    sum +=i
print(f"Сумма {numberN} чисел последовательности (1+1/N)^N: {result} равна {sum}")
