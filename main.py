from random import randint


def is_valid(n):
    if 0 < n < num + 1:
        return True
    else:
        return False


again = 'игра'
while again.lower() == 'игра':
    print('Добро пожаловать в числовую угадайку')
    num = int(input('Введите число которое будет правой границей угадываемого числа \n'))
    target = randint(1, num)
    print(f'Число от 1 до {num} сгенерировано, попробуйте его отгадать')
    trying = int(input('Введите ваше число \n'))
    count = 1

    while is_valid(trying) is False:
        trying = int(input('А может быть все-таки введем целое число от 1 до 100?'))
    while True:
        if trying < target:
            trying = int(input('Ваше число меньше загаданного, попробуйте еще разок \n'))
            count += 1
        elif trying > target:
            trying = int(input('Ваше число больше загаданного, попробуйте еще разок \n'))
            count += 1
        elif trying == target:
            print(f'Вы угадали, поздравляем! Количество ваших попыток: {count}')
            break

    print('Спасибо, что играли в числовую угадайку')
    again = input('Чтобы сыграть еще раз, введите слово "игра" \n')
