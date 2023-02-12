import csv
from log import error_enter

def read():
    with open('Metro.csv', 'r', newline='\n', encoding='utf-8') as f:
        r = csv.reader(f, delimiter=";")
        for rec in r:
            print(rec)

def update():
    with open('Metro.csv', 'r', newline='\n', encoding='utf-8') as f:
        n_id = input('Введите ID для изменения:')
        print('1. Изменение Фамилии')
        print('2. Изменение Имени')
        print('3. Изменение Отчества')
        print('4. Изменение Службы')
        print('5. Изменение Отдела')
        print('6. Изменение Должности')
        try:
            n = int(input('Выберите запись для изменения:'))
        except ValueError:
            error_enter()
        found = 0
        r = csv.reader(f, delimiter=";")
        nrec = []
        for rec in r:
            if rec[0] == n_id:
                if n == 1:
                    print('Текущая запись:', rec)
                    rec[1] = input("Введите новую Фамилию:")
                    print('Измененная запись:', rec)
                    found = 1
                elif n == 2:
                    print('Текущая запись:', rec)
                    rec[2] = input("Введите новое Имя:")
                    print('Измененная запись:', rec)
                    found = 1
                elif n == 3:
                    print('Текущая запись:', rec)
                    rec[3] = input("Введите новое Отчество:")
                    print('Измененная запись:', rec)
                    found = 1
                elif n == 4:
                    print('Текущая запись:', rec)
                    rec[4] = input("Введите новую Службу:")
                    print('Измененная запись:', rec)
                    found = 1
                elif n == 5:
                    print('Текущая запись:', rec)
                    rec[5] = input("Введите новый Отдел:")
                    print('Измененная запись:', rec)
                    found = 1
                elif n == 6:
                    print('Текущая запись:', rec)
                    rec[5] = input("Введите новую Должность:")
                    print('Измененная запись:', rec)
                    found = 1
            nrec.append(rec)

        if found == 0:
            print('Ошибка')
            error_enter()
            f.close()
        else:
            with open('Metro.csv', 'w', newline='', encoding='utf-8') as f:
                w = csv.writer(f, delimiter=';')
                w.writerows(nrec)