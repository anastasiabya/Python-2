def conversion(number, from_num, to_num):
    try:
        # Проверка на знак числа
        flag = False
        if number[0] == '-':
            number = number[1:]
            flag = True
        # Проверка на соответствие числа данной системе счисления
        alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        for i in range(len(number)):
            if alphabet.index(str(number[i])) >= from_num:
                return 'Число не соответствует системе счисления'
        # Перевод числа в десятичную систему счисления
        rev_num = number[::-1]
        result10 = 0
        for i in range(len(rev_num)):
            result10 += (from_num ** i) * alphabet.index(str(rev_num[i]))
        # Перевод числа из десятичной системы счисления в заданную
        result = ''
        if to_num == 10:
            return result10
        while result10:
            result10, y = divmod(result10, to_num)
            result = alphabet[y] + result
        # Возвращение результата
        if flag:
            return '-' + result
        else:
            return result
    except ValueError:
        return 'Неверно введенное число или система счисления'


def numerals():
    print("Введите число:")
    number = input()
    try:
        print("Введите систему счисления данного числа:")
        from_num = int(input())
        print("Введите систему счисления для перевода:")
        to_num = int(input())
        print(conversion(number, from_num, to_num))
    except ValueError:
        print("Не числовые данные")


numerals()
