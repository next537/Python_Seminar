import logging


def menu():
    while True:
        type_num = input("Choice\n"
                         "1 - rat\n"
                         "2 - com\n"
                         "3 - exit\n")
        match type_num:
            case "1":
                pass
            case "2":
                pass
            case "3":
                break
            case _:
                logging.error('Stop programm')
                print("Err")

menu()