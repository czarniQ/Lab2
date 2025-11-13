# a)
with open("notowania_gieldowe.txt", "r") as plik: # otwiera plik
    print(plik.read()) # wypisuje dane z pliku

# b)
with open("notowania_gieldowe.txt", "a") as plik: # otwiera plik
    plik.write("\nALR, 113") # dopisuje w nowej lini dane

with open("notowania_gieldowe.txt", "r") as plik: # otwiera plik
        print(plik.read()) # wypisuje dane z pliku


