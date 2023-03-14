# zadanie 1

a = "Python 2023"
b = "Python 2023"
c = "Python 2023"

print(id(a) == id(b))
print(id(b) == id(c))

print(hex(id(a)))
print(type(a))
print(hex(id(b)))
print(type(b))
print(hex(id(c)))
print(type(c))

c = "Java 11"

print(id(a) == id(b))
print(id(b) == id(c))

print(hex(id(a)))
print(type(a))
print(hex(id(b)))
print(type(b))
print(hex(id(c)))
print(type(c))

# zadanie 2

i = int(input("Podaj pierwszą liczbe: "))
j = int(input("Podaj drugą liczbe: "))
z = input("podaj operator (+,-,/,*): ")

if z == '+':
    print(i+j)
elif z == '-':
    print(i-j)
elif z == '/':
    print(i/j)
elif z == '*':
    print(i*j)

# zadanie 3

Questions = {"Podaj imie i nazwisko ": [],
            "Jaki jest najczęstszy sposób spędzania wolnego czasu dla Ciebie: ": ["oglądanie telewizji/filmów/seriali","czytanie książek/czasopism","uprawianie sportu"],
            "W jakich okolicznościach czytasz książki najczęściej? ": ["podczas podróży","w czasie wolnym (po pracy, na urlopie)","w ogóle nie czytam"],
            "Jeżeli spędzasz czas wolny czytając książki, jaki jest główny powód takiego wyboru? ": ["chęć poszerzenia wiedzy","czytanie to moje hobby","konieczność nauki w związku z wykonywaną pracą/studiami"],
            "Po książki w jakiej formie sięgasz najczęściej? ": ["papierowej (tradycyjnej)","e-booki na tablecie/telefonie","e-booki na specjalnym czytniku (np. Kindle)"],
            "Ile książek czytasz średnio w ciągu roku? ": ["żadnej w całości - jedynie fragmenty","2 lub 3","4-10"],
            "Jak często średnio czytasz książki? ": ["codziennie","raz w miesiącu","raz na rok"],
            "Po jakie gatunki książek sięgasz najczęściej? ": ["kryminały/thrillery","naukowe","fantastykę"]}


ind = 1
for k, v in Questions.items():
    print(ind, "pytanie: ", k)
    tmpind = 1
    for values in Questions.get(k):
        print('\t', tmpind, values)
        tmpind = tmpind + 1
    if ind == 1:
      print("odpowiedź: ", input())
    elif 1 < ind < 8:
        inp = list(map(int,input().split()))
        print("odpowiedź: ")
        for ans in inp:
            tmp = 1
            for values in Questions.get(k):
                if ans == tmp:
                    print('\t', tmp, values)
                tmp = tmp + 1
    elif ind == 8:
        ans = input()
        while len(ans) != 1:
            print("Wybierz jedną odpowiedź!")
            ans = input()
        tmp = 1
        print("odpowiedź: ")
        for values in Questions.get(k):
            if int(ans) == tmp:
                print('\t', tmp, values)
            tmp = tmp + 1
    ind = ind + 1

print("dziękujemy za wypełnienie ankiety")



