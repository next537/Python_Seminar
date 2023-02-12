import log
from person_search import person_search
from print_info import print_metro
from adding_info import adding
from model_update import read, update
from model_delete import delete_data
from exceptions import user_choice

def input_menu_choice():
    log.start_app()
    while True:
        print()
        print('1. Показать всё')
        print('2. Найти запись')
        print('3. Добавить запись')
        print('4. Редактировать запись')
        print('5. Удалить запись')
        print('0. Выход')
        choice_menu = user_choice()
        if choice_menu == 1:
            print_metro()
        elif choice_menu == 2:
            print('1. Поиск')
            print('0. Выход')
            choice1 = user_choice()
            if choice1 == 1:
                person_search()
            elif choice1 == 0:
                log.end_app()
                input_menu_choice()
            else:
                print('Ошибка')
                log.error_enter()
                input_menu_choice()
        elif choice_menu == 3:
            adding()
            log.add()
            print('Запись добавлена')
        elif choice_menu == 4:
            read()
            update()
            log.change()
        elif choice_menu == 5:
            read()
            delete_data()
            log.del_item()
        elif choice_menu == 0:
            log.end_app()
            return exit()
        else:
            print('Ошибка')
            log.error_enter()
            return input_menu_choice()

input_menu_choice()