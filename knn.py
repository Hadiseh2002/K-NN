from collections import Counter
import math

# نمونه‌ها
samples = [
    [1, 2, 3, 'A'],
    [4, 5, 6, 'A'],
    [7, 8, 9, 'B'],
    [10, 11, 12, 'B'],
    [4, 5, 6, 'C'],
    [7, 6, 5, 'C'],
    [10, 9, 8, 'D'],
    [13, 12, 11, 'D'],
    [4, 3, 2, 'A'],
    [7, 6, 5, 'B']
]

# ویژگی‌ها
def manhattan_distance(x, y):
    return sum(abs(a - b) for a, b in zip(x, y))

# تابع k-NN
def knn(k, new_sample):
    distances = [(manhattan_distance(new_sample[:-1], old_sample[:-1]), old_sample[-1]) for old_sample in samples]
    distances.sort(key=lambda pair: pair[0])
    nearest_neighbors = [label for _, label in distances[:k]]
    most_common = Counter(nearest_neighbors).most_common(1)
    return most_common[0][0]

# تست الگوریتم
new_data = [[5, 6, 7, '']]
k_value = 3
predicted_class = knn(k_value, new_data[0])
print(f'نمونه‌ی {new_data[0][:-1]} با k={k_value} بهترین کلاس تشخیص داده شده: {predicted_class}')
