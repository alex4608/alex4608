# 2. Напишите функцию, которая возвращает True,
# если введенный текст читается одинаково слева-направо и справа-налево. Иначе – False.

def text(a):
    if a[::1] == a[::-1]:
        print('True')
    else:
        print('False')
text(input("Введите текст: "))