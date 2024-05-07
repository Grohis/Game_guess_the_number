print('*' * 30)
print('Игра - угадай число. Играем?', '1 ==> "Да"', '2 ==> "Нет"', sep='\n')
print('*' * 40)

def Game_guess_the_number():
    import random
    random_digit = random.randint(1, 30)  # диапозон числа
    count = 3  # кол-во попыток
    total = 0
    while count != 0:
        if count != 0:
            if total == 0:
                print('*' * 40)
                print('Поехали!')
                print(f'Я загадал число от 0 до 30')
                print(f"У тебя есть {count} попыток")
                user_digit = int(input('Угадаешь с 1 раза? Введи число -->'))
                count -= 1  # нужно тут что бы цикл сдвинулся
                print('-' * 40)
            elif total > 0:
                print('-' * 40)
                print(f'Осталось {count} попыток')
                user_digit = int(input('Введи число -->'))
                count -= 1
                print('-' * 40)
        if user_digit == random_digit:
            total += 1
            print(f'***Правильно!*** число {random_digit}')
            print(f'Ты угадас с {total} попытки!')
            print('Игра закончена')
            break
        if user_digit > random_digit:
            print(f"Ваше число {user_digit} слишком большое")
            total += 1
        else:
            print(f'Ваше число {user_digit} слишком маленькое')
            total += 1
    print('*' * 40)
    print('Game Over. Попыток не осталось')
    print('*' * 40)
    print()


chek = int(input('"число" -->'))
while chek != 2:
    Game_guess_the_number()
    print('Сыграем еще раз?', '1 --> "Да"', '2 --> "Нет"', sep='\n')
    chek = int(input('"число" -->'))
    