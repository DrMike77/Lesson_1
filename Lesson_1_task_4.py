print("Задание № 3")
num = int(input("Введите число:"))
count = 0
maxnum = -1
while num > 0:
    count = count + 1
    n = num % 10
    if n > maxnum:
        maxnum = n
    num = num // 10
print("Количество цифр", count)
print(" Наибольшая цифра", maxnum)
