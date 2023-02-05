# 1. Напишите программу, удаляющую из текста все слова, содержащие "абв". В тексте используется разделитель пробел.
# in
# Number of words: 10
#
# out
# авб абв бав абв вба бав вба абв абв абв
# авб бав вба бав вба
#
# in
# Number of words: 6
#
# out
# ваб вба абв ваб бва абв
# ваб вба ваб бва
#
# in
# Number of words: -1
#
# out
# The data is incorrect

from random import sample
def words(count: int, letter: str = 'а' 'б' 'в'):
    words_list = []
    for i in range(count):
        letters = sample(letter, 3)
        words_list.append("".join(letters))
    return " ".join(words_list)
def res(words: str) -> str:
    return " ".join(words.replace("абв", "").split())

all_list = words(int(input("Введите количество наборов букв абв: ")))
print(all_list)
print(res(all_list))