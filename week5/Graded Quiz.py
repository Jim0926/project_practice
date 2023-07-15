import math

def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

input_string = input() 

# map()是一個內建函數，它接受一個函數（如int）和一個可迭代對象（如列表、元組等），
# 並將該函數應用於可迭代對象中的每個元素。它返回一個新的可迭代對象，
# 其中包含應用函數後的結果。
n, p, d = map(int, input_string.split())  # 城鎮數，最多可設置基地台數，可覆蓋範圍

cityInfo = []
for i in range(0, n):
    input_string = input()  # 輸入城鎮座標及人口數
    cityInfo.append(input_string.split())

unVisited = [True] * n
best_cities = []

for _ in range(p):  # 迴圈執行 p 次，選擇 p 個城鎮設置基地台
    max_population = 0
    beat_city = 0
    for i, cityA in enumerate(cityInfo):  # 選擇要設在哪個城鎮
        if unVisited[i]:
            population = 0
            covered = []
            for j, cityB in enumerate(cityInfo):  # 計算設在此城鎮的覆蓋範圍
                if distance(int(cityA[0]), int(cityA[1]), int(cityB[0]), int(cityB[1])) <= d and unVisited[j]:
                    population += int(cityB[2])
                    covered.append(j+1)

            if population > max_population:  # 設定當前最適合設基地台的城鎮和其覆蓋範圍
                max_population = population
                beat_city = i + 1
                covered_cities = covered

    best_cities.append((beat_city, max_population))
    for k in covered_cities:
        unVisited[k-1] = False

total_population = 0
for city, population in best_cities:
    total_population += population
    print(city, end = " ")

print(total_population, end = "")