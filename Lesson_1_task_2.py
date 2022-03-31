print("Hello, let's start")
sec = int(input("Введите время в секундах"))
hour = sec // 3600
sec_2 = sec - hour * 3600
minute = sec_2 // 60
sec_3 = sec_2 - minute * 60
print(hour, "Часов", minute, "Минут", sec_3, "секунд")
