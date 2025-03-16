import math


def wczytaj_dane(plik):
    with open(plik, "r") as f:
        lines = f.readlines()

    dane = []
    for line in lines:
        attributes = line.strip().split(",")[:-1]
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
print("\n TRAINING DATA: \n")
for attributes, decision in training_data:
    print(f"Attributes: {attributes}, Decision: {decision}")
print("\n TEST DATA: \n")
for attributes, decision in test_data:
    print(f"Attributes: {attributes}, Decision: {decision}")


def Distance(a, b):
    if len(a) != len(b):
        raise ValueError(" errrr ")
    sum_sq = 0
    for i in range(len(a)):
        sum_sq += (a[i] - b[i]) ** 2
    return math.sqrt(sum_sq)
