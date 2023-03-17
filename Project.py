from collections import Counter
import math
# read from file


def wczytaj_dane(plik):
    with open(plik, 'r') as f:
        lines = f.readlines()

    # split lines
    dane = []
    for line in lines:
        attributes = [float(x.replace(',', '.')) for x in line.split()[:-1]]
        decision = line.strip().split('\t')[-1].strip()
        dane.append((attributes, decision))

    return dane


train_data = wczytaj_dane('iris_training.txt')
test_data = wczytaj_dane('iris_test.txt')


def odleglosc_euklidesowa(a, b):
    if len(a) != len(b):
        raise ValueError("a and b must have the same length")
    sum_sq = 0
    for i in range(len(a)):
        sum_sq += (a[i]-b[i])**2
    return math.sqrt(sum_sq)


# znajdz najblizszych
def znajdz_najblizszych(dane, punkt, k):
    odleglosci = [(odleglosc_euklidesowa(punkt, x[0]), x[1]) for x in dane]
    odleglosci.sort()
    return odleglosci[:k]


# klasyfikuj
def klasyfikuj(dane, punkt, k):
    sasiedzi = znajdz_najblizszych(dane, punkt, k)
    counts = Counter([s[-1] for s in sasiedzi])
    max_count = counts.most_common(1)[0][1]

    tied_classes = [cls for cls, count in counts.items() if count == max_count]

    # Find the class with the shortest distance among the tied classes
    shortest_distance_class = None
    shortest_distance = float('inf')
    for s in sasiedzi:
        if s[-1] in tied_classes and s[0] < shortest_distance:
            shortest_distance = s[0]
            shortest_distance_class = s[-1]

    return shortest_distance_class

# trenuj2


def test(train, test, k):
    correct_count = 0
    for x in test:
        if klasyfikuj(train, x[0], k) == x[-1]:
            correct_count += 1
    return correct_count / len(test)


while True:
    k_str = input("Podaj k: ")
    if not k_str:
        break
    k = int(k_str)
    accuracy = test(train_data, test_data, k)
    print("Dokladnosc: ", accuracy)
