from collections import Counter
import math


def wczytaj_dane(plik):
    with open(plik, 'r') as f:
        dane = [line.strip().split(',') for line in f.readlines()]
    X = [[float(x.replace(' ', '').replace('\t', ''))
          for x in wiersz[:-1]] for wiersz in dane]
    y = [wiersz[-1].strip() for wiersz in dane]
    return X, y


def odleglosc_euklidesowa(a, b):
    sum_sq = 0.0
    for i in range(len(a)):
        sum_sq += (a[i] - b[i]) ** 2
    return math.sqrt(sum_sq)


# def k_nn(X, y, wektor, k):
#    odleglosci = [odleglosc_euklidesowa(wektor, x) for x in X]
#    indeksy_k_sasiadow = sorted(
#        range(len(odleglosci)), key=lambda i: odleglosci[i])[:k]
#    k_sasiadow = [y[i] for i in indeksy_k_sasiadow]
#    licznik = Counter(k_sasiadow)
#    return licznik.most_common(1)[0][0]

def k_nn(X_train, y_train, X_test, k):
    """Predict the class of each sample in X_test using the k-nearest neighbors algorithm."""
    predictions = []
    for x_test in X_test:
        # Calculate the distances between x_test and all training samples
        distances = []
        for i, x_train in enumerate(X_train):
            distance = odleglosc_euklidesowa(x_test, x_train)
            distances.append((i, distance))
        # Sort the distances in ascending order and select the k nearest neighbors
        distances.sort(key=lambda x: x[1])
        neighbors = []
        for i in range(k):
            index = distances[i][0]
            neighbors.append(y_train[index])
        # Make a prediction based on the majority class of the nearest neighbors
        counts = {}
        for neighbor in neighbors:
            if neighbor in counts:
                counts[neighbor] += 1
            else:
                counts[neighbor] = 1
        prediction = max(counts, key=counts.get)
        predictions.append(prediction)
    return predictions


def main():
    iris_training = 'iris_training.txt'
    iris_test = 'iris_test.txt'
    X_train, y_train = wczytaj_dane(iris_training)
    X_test, y_test = wczytaj_dane(iris_test)

    k = int(input("Podaj wartość parametru k: "))

    poprawne = 0
    for i in range(len(X_test)):
        predykcja = k_nn(X_train, y_train, X_test[i], k)
        if predykcja == y_test[i]:
            poprawne += 1

    dokladnosc = poprawne / len(X_test) * 100
    print(f"Liczba poprawnie zaklasyfikowanych przykładów: {poprawne}")
    print(f"Dokładność eksperymentu: {dokladnosc:.2f}%")

    while True:
        wektor = input(
            "Wpisz wektor atrybutów oddzielony przecinkami (lub wpisz 'q' aby zakończyć): ")
        if wektor == 'q':
            break
        wektor = [float(x) for x in wektor.split(',')]
        wynik = k_nn(X_train, y_train, wektor, k)
        print(f"Wynik klasyfikacji k-NN dla wektora: {wynik}")


if __name__ == "__main__":
    main()
