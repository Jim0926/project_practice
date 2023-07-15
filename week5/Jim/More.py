import math

def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

n, p, d = map(int, input().split())

cityInfo = []
for _ in range(n):
    city_x, city_y, population = map(int, input().split())
    cityInfo.append((city_x, city_y, population))

unVisited = [True] * n
best_cities = []

for _ in range(p):  # 迴圈執行 p 次，選擇 p 個城鎮設置基地台
    max_population = 0
    best_city = 0
    covered_cities = []
    for i, (x1, y1, _) in enumerate(cityInfo):
        if unVisited[i]:
            population = 0
            covered = []
            for j, (x2, y2, _) in enumerate(cityInfo):
                if distance(x1, y1, x2, y2) <= d and unVisited[j]:
                    population += cityInfo[j][2]
                    covered.append(j+1)

            if population > max_population:
                max_population = population
                best_city = i + 1
                covered_cities = covered

    best_cities.append((best_city, max_population))
    for k in covered_cities:
        unVisited[k-1] = False

total_population = sum(population for _, population in best_cities)
best_cities_str = ' '.join(str(city) for city, _ in best_cities)

print(best_cities_str, total_population, end="")
