import random

# zadanie 1

# n = str(input())
# n = n.split(",")
# numbers = [int(i) for i in n]
# result = numbers[0]
# for i in numbers:
#     if i > result:
#         result = i
# print(result)
# result = numbers[0]
# for i in numbers:
#     if i < result:
#         result = i
# print(result)

# zadanie 2

# cities = [
#     "Warsaw",
#     "Berlin",
#     "Paris",
#     "Vienna",
#     "Praha",
#     "Amsterdam",
#     "Brussels",
#     "Madrid",
#     "Lisbona",
#     "Rome"
# ]
# do = 1
#
# while do == 1:
#     index = random.randint(0, 9)
#     if type(cities[index]) == str:
#         print(cities[index])
#         cities[index] = 0
#     if cities.__contains__(type(str)):
#         continue

# zadanie 3

ilosc_rund = input("Ile rund? \n")
tryb = input("VS komputer (K), VS 2 gracz (G) \n")


if tryb == "K":
    pierwszy_gracz = input("Podaj nazwę pierwszego gracza: ")
    drugi_gracz = "Komputer"
    wyniki = list
    opcje_komputera = list["P","K","N"]
    while ilosc_rund > 0:
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

        ostateczny_wynik_gracza = wyniki.count("Gracz wygrał")
        ostateczny_wynik_komputera = wyniki.count("Komputer wygrał")

        for i in wyniki:
            print(i + ". " + wyniki[i])

        if  ostateczny_wynik_komputera > ostateczny_wynik_gracza:
            print("Wygrał komputer")
        else:
            print("Wygrał gracz")






