import random
import getpass

# zadanie 1

n = str(input())
n = n.split(",")
numbers = [int(i) for i in n]
result = numbers[0]
for i in numbers:
    if i > result:
        result = i
print(result)
result = numbers[0]
for i in numbers:
    if i < result:
        result = i
print(result)

# zadanie 2

cities = [
    "Warsaw",
    "Berlin",
    "Paris",
    "Vienna",
    "Praha",
    "Amsterdam",
    "Brussels",
    "Madrid",
    "Lisbona",
    "Rome"
]
do = 1

while do == 1:
    index = random.randint(0, 9)
    if type(cities[index]) == str:
        print(cities[index])
        cities[index] = 0
    if cities.__contains__(type(str)):
        continue

# zadanie 3

ilosc_rund = input("Ile rund? \n")
tryb = input("VS komputer (K), VS 2 gracz (G) \n")
ile_rund = int(ilosc_rund)

if tryb == "G":
    pierwszy_gracz = input("Podaj nazwę pierwszego gracza: ")
    drugi_gracz = input("Podaj nazwę drugiego gracza: ")
    wyniki = []
    while ile_rund > 0:
        print(pierwszy_gracz+": Wybierz swój ruch: Papier(P) || Kamień (K) || Nożyce (N) \n")
        p_wybor = getpass.getpass('wybór: ')
        print(drugi_gracz + ": Wybierz swój ruch: Papier(P) || Kamień (K) || Nożyce (N) \n")
        d_wybor = getpass.getpass('wybór: ')
        if p_wybor == "K":
            if d_wybor == "K":
                print(pierwszy_gracz + ": Kamień, " + drugi_gracz + ": Kamień")
                print("Remis")
                wyniki.append("Remis")
            if d_wybor == "P":
                print(pierwszy_gracz + ": Kamień, " + drugi_gracz + ": Papier")
                print(drugi_gracz +" wygrywa")
                wyniki.append(drugi_gracz)
            if d_wybor == "N":
                print(pierwszy_gracz + ": Kamień, " + drugi_gracz + ": Nożyce")
                print(pierwszy_gracz + " wygrywa")
                wyniki.append(pierwszy_gracz)
        if p_wybor == "P":
            if d_wybor == "K":
                print(pierwszy_gracz + ": Papier, " + drugi_gracz + ": Kamień")
                print(pierwszy_gracz + " wygrywa")
                wyniki.append(pierwszy_gracz)
            if d_wybor == "P":
                print(pierwszy_gracz + ": Papier, " + drugi_gracz + ": Papier")
                print("Remis")
                wyniki.append("Remis")
            if d_wybor == "N":
                print(pierwszy_gracz + ": Papier, " + drugi_gracz + ": Nożyce")
                print(drugi_gracz +" wygrywa")
                wyniki.append(drugi_gracz)
        if p_wybor == "N":
            if d_wybor == "K":
                print(pierwszy_gracz + ": Nożyce, " + drugi_gracz + ": Kamień")
                print(drugi_gracz +" wygrywa")
                wyniki.append(drugi_gracz)
            if d_wybor == "P":
                print(pierwszy_gracz + ": Nożyce, " + drugi_gracz + ": Papier")
                print(pierwszy_gracz + " wygrywa")
                wyniki.append(pierwszy_gracz)
            if d_wybor == "N":
                print(pierwszy_gracz + ": Nożyce, " + drugi_gracz + ": Nożyce")
                print("Remis")
                wyniki.append("Remis")
        ile_rund -= 1

    ostateczny_wynik_gracza_1 = wyniki.count(pierwszy_gracz)
    ostateczny_wynik_gracza_2 = wyniki.count(drugi_gracz)
    cnt = 1
    print(" === Historia gier === ")
    for i in wyniki:
        print(str(cnt) + ". " + i)
        cnt += 1

    if ostateczny_wynik_gracza_1 > ostateczny_wynik_gracza_2:
        print("Wygrał gracz: " + pierwszy_gracz)
    if ostateczny_wynik_gracza_1 == ostateczny_wynik_gracza_2:
        print("Remis wyników")
    if ostateczny_wynik_gracza_1 < ostateczny_wynik_gracza_2:
        print("Wygrał gracz: " + drugi_gracz)



if tryb == "K":
    pierwszy_gracz = input("Podaj nazwę pierwszego gracza: ")
    drugi_gracz = "Komputer"
    wyniki = []
    opcje_komputera = ['P', 'K', 'N']
    while ile_rund > 0:
        print("Wybierz swój ruch: Papier(P) || Kamień (K) || Nożyce (N) \n")
        wybor = input()
        index = random.randint(0, 2)
        wybor_komputera = opcje_komputera[index]

        if wybor == "K":
            if wybor_komputera == "K":
                print("1.gracz: Kamień, Komputer: Kamień")
                print("Remis")
                wyniki.append("Remis")
            if wybor_komputera == "P":
                print("1.gracz: Kamień, Komputer: Papier")
                print("Komputer wygrywa")
                wyniki.append("Komputer wygrał")
            if wybor_komputera == "N":
                print("1.gracz: Kamień, Komputer: Nożyce")
                print("Gracz wygrywa")
                wyniki.append("Gracz wygrał")
        if wybor == "P":
            if wybor_komputera == "K":
                print("1.gracz: Papier, Komputer: Kamień")
                print("Gracz wygrywa")
                wyniki.append("Gracz wygrał")
            if wybor_komputera == "P":
                print("1.gracz: Papier, Komputer: Papier")
                print("Remis")
                wyniki.append("Remis")
            if wybor_komputera == "N":
                print("1.gracz: Papier, Komputer: Nożyce")
                print("Komputer wygrywa")
                wyniki.append("Komputer wygrał")
        if wybor == "N":
            if wybor_komputera == "K":
                print("1.gracz: Nożyce, Komputer: Kamień")
                print("Komputer wygrywa")
                wyniki.append("Komputer wygrał")
            if wybor_komputera == "P":
                print("1.gracz: Nożyce, Komputer: Papier")
                print("Gracz wygrywa")
                wyniki.append("Gracz wygrał")
            if wybor_komputera == "N":
                print("1.gracz: Nożyce, Komputer: Nożyce")
                print("Remis")
                wyniki.append("Remis")
        ile_rund -= 1

    ostateczny_wynik_gracza = wyniki.count("Gracz wygrał")
    ostateczny_wynik_komputera = wyniki.count("Komputer wygrał")
    cnt = 1
    print(" === Historia gier === ")
    for i in wyniki:
        print(str(cnt) + ". " + i)
        cnt += 1

    if ostateczny_wynik_komputera > ostateczny_wynik_gracza:
        print("Wygrał komputer")
    if ostateczny_wynik_komputera == ostateczny_wynik_gracza:
        print("Remis wyników")
    if ostateczny_wynik_komputera < ostateczny_wynik_gracza:
        print("Wygrał gracz")


