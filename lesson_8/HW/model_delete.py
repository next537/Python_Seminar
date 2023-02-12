import csv
from log import error_enter

def read():
    with open('Metro.csv', 'r', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter=';')
        for rec in reader:
            print(rec)

def delete_data():
    with open('Metro.csv', 'r', newline='\n', encoding='utf-8') as f:
        try:
            n_id = input('Выберите ID для удаления записи :')
        except ValueError:
            error_enter()
        found = 0
        reader = csv.reader(f, delimiter=";")
        nrec = []
        for rec in reader:
            if rec[0] == n_id:
                print('Запись удалена:', rec)
                found = 1
            else:
                nrec.append(rec)

        if found == 0:
            print('Ошибка')
            f.close()
        else:
            with open('Metro.csv', 'w', newline='', encoding='utf-8') as f:
                w = csv.writer(f, delimiter=';')
                w.writerows(nrec)