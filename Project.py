from collections import Counter
import math

# read from file


def wczytaj_dane(plik):
    with open(plik, 'r') as f:
        lines = f.readlines()

    # split lines
    dane = []
    for line in lines:
        attributes = [float(x.replace(',', '.'))
                      for x in line.split('\t')[:-1]]
        decision = line.strip().split('\t')[:-1]
        dane.append((attributes, decision))

    return dane


train_data = wczytaj_dane('iris_training.txt')
test_data = wczytaj_dane('iris_test.txt')


def odleglosc_euklidesowa(a, b):
    return math.sqrt(sum([(a[i]-b[i])**2 for i in range(len(a))]))


# znajdz najblizszych
def znajdz_najblizszych(dane, punkt, k):
    odleglosci = [(odleglosc_euklidesowa(x[0], punkt), x[1]) for x in dane]
    odleglosci.sort()
    return odleglosci[:k]


# klasyfikuj
def klasyfikuj(dane, punkt, k):
    sasiad = znajdz_najblizszych(dane, punkt, k)
    counts = {}
    for s in sasiad:
        if s[1] not in counts:
            counts[s[1]] = 0
        else:
            counts[s[1]] += 1
    max_count = max(counts.values())
    return [k for k, value in counts.items() if value == max_count][0]


# trenuj
def test(train, test, k):
    correct_count = 0
    for x in test:
        if klasyfikuj(train, x[0], k) == x[1]:
            correct_count += 1
    return correct_count / len(test) * 100


while True:
    k_str = input("Podaj k: ")
    if not k_str:
        break
    k = [float(x) for x in k_str.strip().split(',')]
    klasyfikacja = klasyfikuj(train_data, k, 3)
    print("Klasyfikacja: ", klasyfikacja)

# test
print("Dokladnosc: ", test(train_data, test_data, 3))
