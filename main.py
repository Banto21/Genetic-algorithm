import random

# Plecak — zestaw 12

zestaw = [
    {'waga': 7, 'wartosc': 14},
    {'waga': 12, 'wartosc': 2},
    {'waga': 3, 'wartosc': 12},
    {'waga': 4, 'wartosc': 14},
    {'waga': 9, 'wartosc': 8},
    {'waga': 6, 'wartosc': 3},
    {'waga': 11, 'wartosc': 10},
    {'waga': 15, 'wartosc': 2},
    {'waga': 6, 'wartosc': 8},
    {'waga': 1, 'wartosc': 9}
]

# Dopuszczalny ciężar plecaka, prawdopodobieństwo mutacji, prawdopodobieństwo krzyżowania
waga_max = 52
p_mutacji = 0.1
p_krzyzowania = 0.8

# Populacja początkowa — 20 osobników w postaci list 0-1 długości 10.
generacja_0 = [[random.randrange(0,2) for k in range(10)] for i in range(20)]



#Funkcja przystosowania dla generacji 0

def funkcja_przystosowania(generacja, zestaw):
    wyniki = []
    for osobnik in generacja:
        waga = 0
        wartosc = 0
        for indeks in range(10):
            waga += zestaw[indeks]['waga'] * osobnik[indeks]
            wartosc += zestaw[indeks]['wartosc'] * osobnik[indeks]
        wyniki.append({'waga': waga, 'wartosc': wartosc})

    return wyniki

wartosc_i_waga_generacja_0 = funkcja_przystosowania(generacja_0, zestaw)
#print(wartosc_i_waga_generacja_0)


# Generacja 0 po wygnięciu osobników o zbyt dużej wadze

def eliminacja(generacja, wartosc_i_waga):
        for osobnik in generacja:
            if wartosc_i_waga[generacja.index(osobnik)]['waga'] > waga_max:
                generacja.remove(osobnik)

eliminacja(generacja_0, wartosc_i_waga_generacja_0)

# Wartość i waga osobników, które przeżyły
wartosc_i_waga_generacja_0_2 = funkcja_przystosowania(generacja_0, zestaw)

# Najlepiej przystosowany osobnik generacji 0
def najlepszy_osobnik(generacja, wartosc_i_waga):
    generacja_max_wartosc = 0
    najlepszy_osobnik = 0
    for i in range(len(wartosc_i_waga)):
        if wartosc_i_waga[i]['wartosc'] > generacja_max_wartosc:
            generacja_max_wartosc = wartosc_i_waga[i]['wartosc']
            najlepszy_osobnik = generacja[i]
    return [najlepszy_osobnik, generacja_max_wartosc]

najlepszy_osobnik_gen_0 = najlepszy_osobnik(generacja_0, wartosc_i_waga_generacja_0_2)
print("Najlepszy osobnik generacji 0")
print(najlepszy_osobnik_gen_0)


# Przedziały procentowe do ruletki
def przedzialy_procentowe(generacja, wartosc_i_waga):

    n = len(generacja)
    suma_wartosci_plecakow = sum([wartosc_i_waga[i]['wartosc'] for i in range(n)])
    ruletka_przedziały = []

    for i in range(n):
        przedzial = 0
        for j in range(i+1):
            przedzial += wartosc_i_waga[j]['wartosc']
        ruletka_przedziały.append(przedzial/suma_wartosci_plecakow)

    return ruletka_przedziały

ruletka_przedzialy_gen_0 = przedzialy_procentowe(generacja_0, wartosc_i_waga_generacja_0_2)

# Losowanie generacji 1.
def losowanie(ruletka_przedzialy, generacja_poprzednia):
    generacja = []
    for i in range(20):
        wylosowana_liczba = random.random()
        for przedzial in ruletka_przedzialy:
            if wylosowana_liczba < przedzial:
                generacja.append(generacja_poprzednia[ruletka_przedzialy.index(przedzial)])
                break
    return generacja

generacja_1 = losowanie(ruletka_przedzialy_gen_0, generacja_0)

#print(generacja_1)

# Mutacje
def mutacje(generacja):

    for osobnik in generacja:
        if random.random() <= p_mutacji:
            gen_zmutowany = random.randint(0, 9)
            osobnik[gen_zmutowany] = abs(osobnik[gen_zmutowany] - 1)

mutacje(generacja_1)
#print(generacja_1)

# Krzyżowanie

def krzyzowanie(generacja):

    for i in range(10):
        if random.random() <= p_krzyzowania:
            poczatek_krzyzowania = random.randint(0, 9)
            for j in range(poczatek_krzyzowania, 10):
                generacja[2*i][j], generacja[2*i+1][j] = generacja[2*i+1][j], generacja[2*i][j]

krzyzowanie(generacja_1)
#print(generacja_1)


# Funkcja przystosowania dla generacji 1

wartosc_i_waga_generacja_1 = funkcja_przystosowania(generacja_1, zestaw)
#print(wartosc_i_waga_generacja_1)

# Osobniki, które przeżyły w generacji 1
eliminacja(generacja_1, wartosc_i_waga_generacja_1)

# Wartość i waga osobników, które przeżyły
wartosc_i_waga_generacja_1_2 = funkcja_przystosowania(generacja_1, zestaw)
# Najlepiej przystosowany osobnik generacji 1

najlepszy_osobnik_gen_1 = najlepszy_osobnik(generacja_1, wartosc_i_waga_generacja_1_2)

print("Najlepszy osobnik generacji 1")
print(najlepszy_osobnik_gen_1)

#Przedziały i ruletka dla generacji 1

ruletka_przedzialy_gen_1 = przedzialy_procentowe(generacja_1, wartosc_i_waga_generacja_1_2)
generacja_2 = losowanie(ruletka_przedzialy_gen_1, generacja_1)

#Mutacje i krzyżowanie
mutacje(generacja_2)
krzyzowanie(generacja_2)

# Funkcja przystosowania dla generacji 2

wartosc_i_waga_generacja_2 = funkcja_przystosowania(generacja_2, zestaw)
#print(wartosc_i_waga_generacja_1)

# Osobniki, które przeżyły w generacji 2
eliminacja(generacja_2, wartosc_i_waga_generacja_2)

# Wartość i waga osobników, które przeżyły
wartosc_i_waga_generacja_2_2 = funkcja_przystosowania(generacja_2, zestaw)
# Najlepiej przystosowany osobnik generacji 2

najlepszy_osobnik_gen_2 = najlepszy_osobnik(generacja_2, wartosc_i_waga_generacja_2_2)

print("Najlepszy osobnik generacji 2")
print(najlepszy_osobnik_gen_2)