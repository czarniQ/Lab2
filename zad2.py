a = float(input("Podaj pierwszą liczbę:")) # uzytkownik podaje liczby
b = float(input("Podaj liczbę drugą:"))
c = float(input("Podaj liczbę trzecią:"))

def zad2(a, b, c): # jest to zbior liczb podanych przez uzytkownika
    if a >= b and a >= c: # sprawdza ktore liczby sa wieksze od sibie
        if b >= c:
            print(c, b, a)
        else:
            print(b,c,a)
    elif b >= a and b >= c:
        if a >= c:
            print(c, a, b)
        else:
            print(a, c, b)
    elif c >= a and c >= b:
        if a >= b:
            print(b,a,c)
        else:
            print(a,b,c)

print (zad2(a, b, c)) # wypisuje poprawna odpowiedz
