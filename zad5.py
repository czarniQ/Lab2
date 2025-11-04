# a)
with open(r"C:\Users\czarniQ\Desktop\Laboratorium_2\notowania_gieldowe.txt", "r", encoding="utf-8") as plik: # otwiera plik
    for linia in plik:
        print(linia.strip()) # wypisuje dane z pliku

# b)
with open(r"C:\Users\czarniQ\Desktop\Laboratorium_2\notowania_gieldowe.txt", "a", encoding="utf-8") as plik: #otwiera plik
    plik.write("\nALR, 113") # dopisuje w nowej lini dane

with open(r"C:\Users\czarniQ\Desktop\Laboratorium_2\notowania_gieldowe.txt", "r", encoding="utf-8") as plik: # otwiera plik
    for linia in plik:
        print(linia.strip()) # wypisuje dane z pliku


