from num2words import num2words

#трансформируем числа в буквы
def format_money(total):
    rub = int(total)
    rub_words = num2words(rub, lang='ru').capitalize()

    rub_str = str(rub)
    number = int(rub_str[-1])
    two_numbers = int(rub_str[-2:]) if len(rub_str) >= 2 else None

    if two_numbers in [11, 12, 13, 14] or number in [0, 5, 6, 7, 8, 9]:
        rub_word = 'рублей'
    elif number == 1:
        rub_word = 'рубль'
    else:
        rub_word = 'рубля'
    return f'{rub_words} {rub_word}'

def sum_min(N, distances, tariffs):
    taxi = [0] * N
    sorted_tariffs = sorted(enumerate(tariffs), key=lambda x: x[1], reverse=True)

    for i, distance in enumerate(distances):  #в минимальном по стоимости такси поедет
        taxi_index, _ = sorted_tariffs[0]     #человек с максимальным расстояние, и наоборот
        taxi[i] = taxi_index

        sorted_tariffs.pop(0) #удаляем такси в котором уже едут

    total_expenses = sum(tariffs[taxi[i]] * distances[i] for i in range(N)) #считаем общие траты

    return taxi, total_expenses

def main():
    N = int(input("Введите количество сотрудников: "))     #вводим необходимую инфу
    while N < 1:
        print("Минимальное количество сотрудников: 1")
        N = int(input("Введите количество сотрудников: "))
    distances = []
    tariffs = []

    print("Введите расстояния до домов сотрудников: ")
    for _ in range(N):
        distance = int(input())
        distances.append(distance)

    print("Введите цену за единицу расстояния в такси: ")
    for _ in range(N):
        tariff = int(input())
        tariffs.append(tariff)

    taxi, total = sum_min(N, distances, tariffs) #высчитываем минимальную сумму проездов

    print("Рассадка сотрудников по такси:")
    for i, taxi_index in enumerate(taxi):
        print(f"Сотрудник {i + 1} - Такси {taxi_index + 1}")

    formatt_money = format_money(total)
    print("Сумма затрат:", formatt_money, "(", total, ")")

if True:
    main()