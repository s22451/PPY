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

q1 = "Podaj imie i nazwisko "
q2 = "Jaki jest najczęstszy sposób spędzania wolnego czasu dla Ciebie: "
q3 = "W jakich okolicznościach czytasz książki najczęściej? "
q4 = "Jeżeli spędzasz czas wolny czytając książki, jaki jest główny powód takiego wyboru? "
q5 = "Po książki w jakiej formie sięgasz najczęściej? "
q6 = "Ile książek czytasz średnio w ciągu roku? "
q7 = "Jak często średnio czytasz książki? "
q8 = "Po jakie gatunki książek sięgasz najczęściej? "

Questions = [q1,q2,q3,q4,q5,q6,q7,q8]

for x in Questions:
    print("pytanie: " + x, end="")
    ans = input()
    print("odpowiedź: " + ans)


