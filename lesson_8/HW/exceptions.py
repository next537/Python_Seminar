from log import error_enter


def user_choice():
    choice1 = input('Выберите: ')
    try:
        choice1 = int(choice1)
        if (choice1 > 5) and (choice1 < 0):
            print('Ошибка')
            return user_choice()
        else:
            return choice1
    except ValueError:
        print('Ошибка')
        error_enter()
        return user_choice()