# 1 метод
fluffy = open("text_22.txt", "r", encoding="utf-8")
print(fluffy.read().split("\n")) # при использовании чтения возвращается 1 строка
fluffy.close()

# 2 метод
fluffy = open("text_22.txt", "r", encoding="utf-8")
print(fluffy.readline()) # считывание одной единственной строки
print(fluffy.readline()) # если необходимо считать другую строку то пишется еще раз и т.д.
fluffy.close()

# 3 метод
fluffy = open("text_22.txt", "r", encoding="utf-8")
print(fluffy.readlines()) # возвращает список без пустых строк
                          # (возвращает весь список, что есть в файле со всеми управляющими конструкциями внутри)
fluffy.close()

# 4 метод
fluffy = open("text_22.txt", "r", encoding="utf-8")

for i in fluffy: # цикл при работе с файлами становится итератором
    print(i, end="") # выведет все строки в фале без пустых строк

fluffy.close()