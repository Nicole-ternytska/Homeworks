def sym_dif(str1, str2):
    """

    :param str1: рядок з будь-якими символами, будь-який формат. Наприклад: "abcd12345"
    :param str2: рядок з будь-якими символами,будь-який формат. Наприклад: "abcd9876"
    :return: рядок-симетрична різниця str1 i str2, формат відповідно до вхідного. Наприклад: "123459876"
    """
    str3 = ''
    for el1 in str1:
        counter = 0
        for el2 in str2:
            if el1 == el2:
                counter += 1
        if counter == 0:
            str3 += el1
    return str3

str3 = ''
print("Введіть рядок 1: ")
str1 = input()
print("Введіть рядок 2: ")
str2 = input()
str3 += sym_dif(str1, str2)
str3 += sym_dif(str2, str1)
print(str3)
