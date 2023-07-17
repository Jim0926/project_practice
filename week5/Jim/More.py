'''
11027147邱峻彥 11027140陳芃睿 11027250黃唯
題目敘述:
有一家電信公司正在研擬一個新服務區域的無線基地臺設置計畫。在這個區域裡，一共有 n 個城
鎮，編號為 1、2 直到 n ，而城鎮 i 的人口數是 Pi 。公司將此區域以一公里為單位，畫出了一個二
維座標系，並且以 (xi, yi) 表示城鎮 i 的位置。換句話說，城鎮 i1 跟城鎮 i2 之間的距離是
( ( x1 - x2 ) ** 2 + ( y1 - y2 ) ** 2 ) ** 0.5
公里。如果一個基地臺跟一個城鎮的距離在 d 公里以內，我們就說這個基地臺可以「覆蓋」這個
城鎮，也就是這個城鎮的人可以收得到強度足夠的從該基地臺發出的訊號。公司預計在此區域的
個城鎮中挑選 p 個城鎮設置基地臺，以求能覆蓋最多的人口數。
你在這家電信公司工作，負責挑出這 p 個城鎮。為此，你設計了一個貪婪演算法。首先在所有城
鎮中，你找出「如果蓋在這裡，將可以覆蓋最多人」的城鎮，然後設一個基地臺在那裡。現在你
還能再設置 p-1 個基地臺，所以如法泡製，在所有還沒有基地臺的城鎮中，找出「如果蓋在這
裡，將可以覆蓋最多還沒被覆蓋的人」的城鎮，設一個基地臺在那裡，然後繼續如此直到挑出 p
個城鎮去設置基地臺為止。如果在任一時刻遇到有兩個以上的城鎮可以被選，就選編號較小的那
個。
輸入輸出格式:
在每筆測試資料中，第一列存放三個整數 n 、 p 跟 d ；在第二列至第 n+1 列中，第 i 列存放三個整
數 Xi-1 、 yi-1 與 Pi-1 ，分別表示第 i-1 個城鎮的 x 座標、 y 座標和人口數。在任意一列中，兩個
數字之間都以一個空白隔開。已知2 ≤ n ≤ 1000 、 2 ≤ p ≤ n 、 −100 ≤ xi ≤ 100、
−100 ≤ yi ≤ 100 、 1 ≤ Pi ≤ 100。不會有兩個城鎮落在同一個地點。
讀入這些資料之後，請根據題目指定的演算法，求出應該在哪 p 個城鎮設置基地臺，然後依照選擇
的先後順序由先而後印出這些城鎮的編號，最後輸出被覆蓋的總人數。任兩個城鎮編號間，用一個
空白隔開。
'''
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
