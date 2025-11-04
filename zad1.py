podaj = float(input("Podaj liczbę zdobytych punktów: ")) # uzytkownik podaje liczbe
liczba_punktów = podaj
if liczba_punktów <80: # sprawdza czy liczba wieksza/mniejsza
    print("Nie zdajesz egzaminu.")
    if liczba_punktów >50:
        print("Możesz poprawić egzamin") # wypisuje ze mozna poprawic

elif liczba_punktów >80:
    print("Zdajesz egzamin") # wypisuje ze zdajesz egzamin