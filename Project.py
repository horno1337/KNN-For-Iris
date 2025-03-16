import math
from collections import Counter


def wczytaj_dane(plik):
    with open(plik, "r") as f:
        lines = f.readlines()

    dane = []
    for line in lines:
        attributes = list(map(float, line.strip().split(",")[:-1]))
        decision = line.strip().split(",")[-1].strip()
        dane.append((attributes, decision))

    return dane


def dziel_dane(data, training_data, test_data):

    count = 0
    for attributes, decision in data:
        if count % 4 == 0:
            test_data.append((attributes, decision))
        else:
            training_data.append((attributes, decision))
        count += 1

    return training_data, test_data


training_data = []
test_data = []
data = wczytaj_dane("iris.txt")
training_data, test_data = dziel_dane(data, training_data, test_data)

print("Training Data:")
for attributes, decision in training_data:
    print(f"Attributes: {attributes}, Decision: {decision}")

print("Test Data:")
for attributes, decision in test_data:
    print(f"Attributes: {attributes}, Decision: {decision}")


def Distance(a, b):
    if len(a) != len(b):
        raise ValueError(" errrr ")
    sum_sq = 0
    for i in range(len(a)):
        sum_sq += (a[i] - b[i]) ** 2
    return math.sqrt(sum_sq)


def classify_knn(training_data, test, k):
    distances = [(Distance(test, train), label) for train, label in training_data]
    distances.sort()
    nearest_neighbors = [label for _, label in distances[:k]]
    return Counter(nearest_neighbors).most_common(1)[0][0]


def oblicz_celnosc(training_data, test_data, k):
    poprawne = 0
    for attributes, decision in test_data:
        predicted = classify_knn(training_data, attributes, k)
        if predicted == decision:
            poprawne += 1
    return (poprawne / len(test_data)) * 100


k = int(input("Podaj wartość k dla kNN: "))
celnosc = oblicz_celnosc(training_data, test_data, k)
print(f"Celność klasyfikatora k-NN dla k={k}: {celnosc:.2f}%")
