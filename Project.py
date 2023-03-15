import math

# Funkcja obliczająca odległość euklidesową między dwoma punktami


def euclidean_distance(point1, point2):
    distance = 0.0
    for i in range(len(point1)):
        distance += (point1[i] - point2[i]) ** 2
    return math.sqrt(distance)


# Wczytanie danych treningowych z pliku
train_data = []
with open('iris_training.txt', 'r') as f:
    for line in f:
        train_data.append(list(map(float, line.strip().split(','))))


# Wczytanie danych testowych z pliku
test_data = []
with open('iris_test.txt', 'r') as f:
    for line in f:
        test_data.append(list(map(float, line.strip().split(','))))


# Funkcja znajdująca k najbliższych sąsiadów dla danego wektora testowego
def get_neighbors(train_data, test_vector, k):
    distances = []
    for train_vector in train_data:
        dist = euclidean_distance(train_vector, test_vector)
        distances.append((train_vector, dist))
    distances.sort(key=lambda x: x[1])
    neighbors = [distances[i][0] for i in range(k)]
    return neighbors
