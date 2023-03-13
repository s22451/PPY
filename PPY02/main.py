# zadanie 1

# a = "Python 2023"
# b = "Python 2023"
# c = "Python 2023"
#
# print(id(a) == id(b))
# print(id(b) == id(c))
#
# print(hex(id(a)))
# print(type(a))
# print(hex(id(b)))
# print(type(b))
# print(hex(id(c)))
# print(type(c))
#
# c = "Java 11"
#
# print(id(a) == id(b))
# print(id(b) == id(c))
#
# print(hex(id(a)))
# print(type(a))
# print(hex(id(b)))
# print(type(b))
# print(hex(id(c)))
# print(type(c))

# zadanie 2

# i = int(input("Podaj pierwszą liczbe: "))
# j = int(input("Podaj drugą liczbe: "))
# z = input("podaj operator (+,-,/,*): ")
#
# if z == '+':
#     print(i+j)
# elif z == '-':
#     print(i-j)
# elif z == '/':
#     print(i/j)
# elif z == '*':
#     print(i*j)

# zadanie 3

Questions = {"Podaj imie i nazwisko ": [],
            "Jaki jest najczęstszy sposób spędzania wolnego czasu dla Ciebie: ": [],
            "W jakich okolicznościach czytasz książki najczęściej? ": [],
            "Jeżeli spędzasz czas wolny czytając książki, jaki jest główny powód takiego wyboru? ": [],
            "Po książki w jakiej formie sięgasz najczęściej? ": [],
            "Ile książek czytasz średnio w ciągu roku? ": [],
            "Jak często średnio czytasz książki? ": [],
            "Po jakie gatunki książek sięgasz najczęściej? ": []}

for x in Questions:
    print("pytanie: " + x, end="")
    ans = input()
    print("odpowiedź: " + ans)


