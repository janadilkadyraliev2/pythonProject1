from decouple import config
from random import randint

attempts = int(config('ATTEMPTS'))
capital = int(config('CAPITAL'))

while attempts > 0:

    if capital <= 0:
        print('У вас не осталось денег. '
              '\nИгра завершена.')
        break
    print(f'Количество попыток: {attempts}')

    chance = randint(0, 13)
    number = int(input("Отгадайте число от 0 до 12: "))
    bets = int(input("Ваши ставки: "))

    if bets > capital:
        print(f'Baшa ставка превышают ваш капитал')

    elif bets <= capital:

        if chance == number:
            print(f'Вы выиграли: {bets * 2}')
            capital += bets
            print(f'ваш капитал: {capital}')


        elif chance != number:
            print(f'ответневерный, вы потерялисвою ставку')
            capital -= bets
            print(f'Ваш капитал {capital}')
            bets = 0

        else:
            print(f'Неправильное число')

        attempts -= 1

