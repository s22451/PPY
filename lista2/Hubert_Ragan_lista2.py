import ssl
import pandas as pd
from sklearn import preprocessing

ssl._create_default_https_context = ssl._create_unverified_context

#Wczytaj dane z adresu podanego w pliku tekstowym: pliktextowy.txt
# do ramki danych.
#Użyj reszty wierszy jako nagłówków ramki danych.
#Uwaga! Zobacz która zmienna jest zmienną objaśnianą, będzie to potrzebne do dalszych zadań.

with open('/content/pliktextowy.txt', 'r') as file:
    url = file.readline()

url = url.replace('\n', '')

df_tmp = pd.read_csv(url, header=None)

with open('/content/pliktextowy.txt', 'r') as file:
    headers = [line.strip() for line in file.readlines()[1:]]
df_tmp.columns = headers

df = df_tmp
#Zadanie1 przypisz nazwy kolumn z df w jednej linii:   (2pkt)

wynik1 = ', '.join(df.columns)
print(wynik1)

#Zadanie 2: Wypisz liczbę wierszy oraz kolumn ramki danych w jednej linii.  (2pkt)
wynik2 = f"Liczba wierszy: {df.shape[0]}, Liczba kolumn: {df.shape[1]}"
print(wynik2)


#Zadanie Utwórz klasę Wine na podstawie wczytanego zbioru:
#wszystkie zmienne objaśniające powinny być w liscie.
#Zmienna objaśniana jako odrębne pole.
# metoda __init__ powinna posiadać 2 parametry:
#listę (zmienne objaśniające) oraz liczbę(zmienna objaśniana).
#nazwy mogą być dowolne.

# Klasa powinna umożliwiać stworzenie nowego obiektu na podstawie
# już istniejącego obiektu jak w pdf z lekcji lab6.
# podpowiedź: metoda magiczna __repr__
#Nie pisz metody __str__.

class Wine:
    def __init__(self, variables, typeOf):
        self.variables = variables
        self.typeOf = typeOf

    def __repr__(self):
        return f"Wine(variables={self.variables}, target={self.typeOf})"

#Zadanie 3 Utwórz przykładowy obiekt:   (3pkt)
wynik3 = Wine(variables=['zmienna1', 'zmienna2', 'zmienna3'], typeOf=3)
#do podmiany. Pamiętaj - ilość elementów, jak w zbiorze danych.
#Uwaga! Pamiętaj, która zmienna jest zmienną objaśnianą
print(wynik3)

#Zadanie 4.                             (3pkt)
#Zapisz wszystkie dane z ramki danych do listy obiektów typu Wine.
#Nie podmieniaj listy, dodawaj elementy.
#Uwaga! zobacz w jakiej kolejności podawane są zmienne objaśniane i objąśniająca.
# Podpowiedź zobacz w pliktextowy.txt
wineList = []

for index, row in df.iterrows():
    variables = row.tolist()
    target = variables.pop(0)
    wine = Wine(variables, target)
    wineList.append(wine)

wynik4 = len(wineList)
print(wynik4)


#Zadanie5 - Weź ostatni element z listy i na podstawie         (3pkt)
#wyniku funkcji repr utwórz nowy obiekt - eval(repr(obiekt))
#do wyniku przypisz zmienną objaśnianą z tego obiektu:
new_object = eval(repr(wineList[-1]))
wynik5 = new_object.typeOf
# last_element = wineList[-1]
# new = eval(repr(last_element))
# wynik5 = new.typeOf
print(wynik5)


#Zadanie 6:                                                          (3pkt)
#Zapisz ramkę danych  do bazy SQLite nazwa bazy(dopisz swoje imię i nazwisko):
# wines_imie_nazwisko, nazwa tabeli: wines.
#Następnie wczytaj dane z tabeli wybierając z bazy danych tylko wiersze z typem wina nr 3
# i zapisz je do nowego data frame:
wynik6 = "W następnej linijce podmień na nowy  data frame z winami tylko klasy trzeciej:"
wynik6 = pd.DataFrame() #tutaj do podmiany

print(wynik6.shape)


#Zadanie 7                                                          (1pkt)
#Utwórz model regresji Logistycznej z domyślnymi ustawieniami:

model = "tu wstaw kod inicjalizujacy model"


wynik7 = model.__class__.__name__
print(wynik7)

# Zadanie 8:                                                        (3pkt)
#Dokonaj podziału ramki danych na dane objaśniające i  do klasyfikacji.
#Znormalizuj dane objaśniające za pomocą:
#preprocessing.normalize(X)
# Wytenuj model na wszystkich danych bez podziału na zbiór treningowy i testowy.
# Wykonaj sprawdzian krzyżowy, używając LeaveOneOut() zamiast KFold (Parametr cv)
#  Podaj średnią dokładność (accuracy)

wynik8 = "tu wstaw średnią dokładność"
print(wynik8)