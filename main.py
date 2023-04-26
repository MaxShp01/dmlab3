# Задаємо матрицю відстаней між містами
distances = [
    [0, 35, 40, 54, 69, 87],
    [35, 0, 0, 89, 43, 0],
    [40, 0, 0, 79, 0, 54],
    [54, 89, 79, 0, 16, 0],
    [69, 43, 0, 16, 0, 0],
    [87, 0, 54, 0, 0, 0]
]

# Знаходимо мінімальну вартість для кожної вершини графа
min_distances = []
for i in range(len(distances)):
    min_distance = float('inf')
    for j in range(len(distances[i])):
        if distances[i][j] != 0 and distances[i][j] < min_distance:
            min_distance = distances[i][j]
    min_distances.append(min_distance)


# Рекурсивно розгалужуємось на всі можливі маршрути між містами
def tsp_branch_and_bound(distances, path, bound):
    if len(path) == len(distances):
        # Якщо пройдено всі міста, повертаємо вартість маршруту
        return bound + distances[path[-1]][path[0]]

    min_distance = float('inf')
    for i in range(len(distances)):
        if i not in path:
            # Знаходимо верхню межу для нової гілки
            new_bound = bound + distances[path[-1]][i] + min_distances[i]
            if new_bound < min_distance:
                # Якщо верхня межа менша за поточний найкращий результат,
                # рекурсивно розгалужуємось на нову гілку
                new_path = path + [i]
                distance = tsp_branch_and_bound(distances, new_path, new_bound)
                if distance < min_distance:
                    min_distance = distance

    return min_distance


# Викликаємо алгоритм для пошуку мінімального маршруту
min_distance = tsp_branch_and_bound(distances, [0], 0)
print(min_distance)
