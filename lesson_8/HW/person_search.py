from log import search, error_enter


def person_search():
    name = input('Введите Фамилию: ')
    search(name)
    with open('Metro.csv', 'r', encoding='utf_8') as data:
        data_list = data.readlines()
        for i in range(1, len(data_list)):
            if name in data_list[i]:
                print(data_list[i])
                break
        else:
            error_enter()
            print('Ошибка')