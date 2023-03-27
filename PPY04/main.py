# zadanie 1
import math


def calculate_needed_panels(floor_length, floor_width,panel_length,panel_width, panel_count):
    floor_field = floor_length * floor_width * 1.1
    panel_field = panel_length * panel_width
    number_of_panel_packages_needed = math.ceil((floor_field/panel_field)/panel_count)

    print("Potrzeba " + str(number_of_panel_packages_needed) + " paczek paneli")

calculate_needed_panels(4,4,0.20,1,10)

# zadanie 2
def are_numbers_prime(*args):
    dividers = [2,3,5,7]
    for arg in args:
        if arg == 0 or arg == 1:
            print(str(arg) + " is not prime number")
            continue
        is_Prime = True
        for d in dividers:
            if arg == d:
                break
            if int(arg%d) == 0:
                is_Prime = False
                break
        if is_Prime is True:
                print(str(arg) + " is prime number")
        else:
                print(str(arg) + " is not prime number")

are_numbers_prime(2,3,4,5,6,7,8,9,10,11,12,13)

def cipher_with_ceasar(text, key):
    #97 - 122 a-z
    #65 - 90 A-Z
    #48 - 57 0-9
    #32 spacja
    text_as_list = list(text)
    for c in text_as_list:
        if ord(c) == 32:
            continue
        if ord(c) >= 97 and ord(c) <= 122:
            c = chr(ord(c) + key)
            if ord(c) > 122:
                c = chr(ord(c) - 35)
        if (ord(c) >= 48 and ord(c) <= 57):


