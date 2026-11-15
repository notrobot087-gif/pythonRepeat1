char = input("Введите символ: ")

if len(char) == 1:
    a = ord(char)
    print("Код ASCII:")
    print(a)

    if 'A' <= char <= 'Z':
        print("Это заглавная латинская буква.")
    else:
        print("Это не заглавная латинская буква.")
else:
    print("Введите один символ")