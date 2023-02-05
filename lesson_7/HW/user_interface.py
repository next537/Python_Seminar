import compl
import model_div
import model_sum
import model_pow
import model_sub
import model_mult
import excep
import logg

def menu():
    while True:
        print("\nГЛАВНОЕ МЕНЮ")
        print("1. Работа с рациональными числами")
        print("2. Работа с комплексными числами")
        print("0. Выход")
        logg.start_app()
        try:
            choice1 = int(input("Выберете раздел: "))
        except ValueError:
            print('Это не число')
            logg.error_enter()
            return menu()

        if choice1 == 1:
            print("\nРАЦИОНАЛЬНЫЕ ЧИСЛА")
            print("1. Сложение")
            print("2. Вычитание")
            print("3. Умножение")
            print("4. Деление")
            print("5. Возведение в степень")
            print("0. Вернуться в главное меню")
            try:
                choice2 = int(input("Выберете операцию: "))
            except ValueError:
                print('Это не число')
                logg.error_enter()
                return menu()

            if choice2 == 1:
                r1 = excep.take_number()
                r2 = excep.take_number()
                model_sum.init(r1, r2)
                result = model_sum.do_it()
                logg.sum_log(r1, r2, result)
                print(result)
                return result


            elif choice2 == 2:
                r1 = excep.take_number()
                r2 = excep.take_number()
                model_sub.init(r1, r2)
                result = model_sub.do_it()
                logg.sub_log(r1, r2, result)
                print(result)
                return result

            elif choice2 == 3:
                r1 = excep.take_number()
                r2 = excep.take_number()
                model_mult.init(r1, r2)
                result = model_mult.do_it()
                logg.mult_log(r1, r2, result)
                print(result)
                return result

            elif choice2 == 4:
                r1 = excep.take_number()
                r2 = excep.take_number()
                model_div.init(r1, r2)
                try:
                    result = model_div.do_it()
                    logg.div_log(r1, r2, result)
                    print(result)
                    return result
                except ZeroDivisionError:
                    print('Делить на ноль нельзя')
                    logg.error_enter()
                    return menu()

            elif choice2 == 5:
                r1 = excep.take_number()
                r2 = excep.take_number()
                model_pow.init(r1, r2)
                result = model_pow.do_it()
                logg.pow_log(r1, r2, result)
                print(result)
                return result

            elif choice2 == 0:
                menu()

            else:
                print("Ошибка")
                logg.error_enter()
                menu()

        if choice1 == 2:
            print("\nКОМПЛЕКСНЫЕ ЧИСЛА")
            print("1. Сложение")
            print("2. Вычитание")
            print("3. Умножение")
            print("4. Деление")
            print("5. Возведение в степень")
            print("0. Вернуться в главное меню")
            try:
                choice2 = int(input("Выберете операцию: "))
            except ValueError:
                print('Это не целое число')
                logg.error_enter()
                return menu()

            if choice2 == 1:
                c1 = compl.make_complex()
                c2 = compl.make_complex()
                model_sum.init(c1, c2)
                result = model_sum.do_it()
                logg.sum_log(c1, c2, result)
                print(result)
                return result

            elif choice2 == 2:
                c1 = compl.make_complex()
                c2 = compl.make_complex()
                model_sub.init(c1, c2)
                result = model_sub.do_it()
                logg.sub_log(c1, c2, result)
                print(result)
                return result

            elif choice2 == 3:
                c1 = compl.make_complex()
                c2 = compl.make_complex()
                model_mult.init(c1, c2)
                result = model_mult.do_it()
                logg.mult_log(c1, c2, result)
                print(result)
                return result

            elif choice2 == 4:
                c1 = compl.make_complex()
                c2 = compl.make_complex()
                model_div.init(c1, c2)
                try:
                    result = model_div.do_it()
                    logg.div_log(c1, c2, result)
                    print(result)
                    return result
                except ZeroDivisionError:
                    print('Делить на ноль нельзя!')
                    logg.error_enter()
                    return menu()

            elif choice2 == 5:

                c1 = compl.make_complex()
                c2 = compl.make_complex()
                model_pow.init(c1, c2)
                result = model_pow.do_it()
                logg.pow_log(c1, c2, result)
                print(result)
                return result

            elif choice2 == 0:
                menu()

            else:
                print("Ошибка")
                logg.error_enter()
                menu()

        if choice1 == 0:
            quit()
menu()