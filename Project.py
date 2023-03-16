from collections import Counter
from math import sqrt


def wczytaj_dane(plik):
    with open(plik, 'r') as f:
        dane = [line.strip().split(',') for line in f.readlines()]
    X = [[float(x.replace(' ', '').replace('\t', ''))
          for x in wiersz[:-1]] for wiersz in dane]
    y = [wiersz[-1].strip() for wiersz in dane]
    return X, y


def odleglosc_euklidesowa(a, b):
    sum_sq = 0.0
    for i in range(len(a)-1):
        sum_sq += (a[i] - b[i]) ** 2
    return sqrt(sum_sq)


# Locate the most similar neighbors
def get_neighbors(train, test_row, num_neighbors):
    distances = list()
    for train_row in train:
    dist = odleglosc_euklidesowa(test_row, train_row)
    distances.append((train_row, dist))
    distances.sort(key=lambda tup: tup[1])
    neighbors = list()
    for i in range(num_neighbors):
    neighbors.append(distances[i][0])
    return neighbors

# Make a prediction with neighbors


def predict_classification(train, test_row, num_neighbors):
    neighbors = get_neighbors(train, test_row, num_neighbors)
    output_values = [row[-1] for row in neighbors]
    prediction = max(set(output_values), key=output_values.count)
    return prediction

# kNN Algorithm


def k_nearest_neighbors(train, test, num_neighbors):
    predictions = list()
    for row in test:
    output = predict_classification(train, row, num_neighbors)
    predictions.append(output)
    return (predictions)


# Test the kNN on the Iris Flowers dataset
seed(1)
filename = 'iris.csv'
dataset = wczytaj_dane(filename)
for i in range(len(dataset[0])-1):
    str_column_to_float(dataset, i)
# convert class column to integers
str_column_to_int(dataset, len(dataset[0])-1)
# evaluate algorithm
n_folds = 5
num_neighbors = 5
scores = evaluate_algorithm(
    dataset, k_nearest_neighbors, n_folds, num_neighbors)
print('Scores: %s' % scores)
print('Mean Accuracy: %.3f%%' % (sum(scores)/float(len(scores))))
