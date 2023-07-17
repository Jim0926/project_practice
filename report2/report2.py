import math

def week3_1() :
    x1 = int(input( "x1: " ))
    x2 = int(input( "x2: " ))
    y  = int(input( "y: " ))

    if x1 > y :
        x1 = x1 - y
        x2 = x2 + y
    else :
        x2 = x2 + x1
        x1 = 0
    
    print( "ANS: ", end = '' )
    print(x1, x2)

def week3_2() :
    total = int(input( "多少錢: " ))
    remaining = 1000 - total

    denominations = {500: 0, 100: 0, 50: 0, 10: 0, 5: 0, 1: 0}

    for denomination in denominations:
        denominations[denomination] = remaining // denomination
        remaining = remaining % denomination

    output = ""
    for denomination, num_of_note in denominations.items():
        if num_of_note != 0:
            output += f"{denomination}, {num_of_note}; "

    output = output.rstrip("; ") # 刪除 output 字串末尾的分號和空格
    
    print( "ANS: ", end = '' )
    print(output)

def week4_1() :
    c = int(input("單位進貨成本: "))  # 單位進貨成本
    r = int(input("單位零售價格: "))  # 單位零售價格
    N = int(input("需求的可能個數: "))  # 需求的可能個數
    q = int(input("訂貨量: "))  # 訂貨量

    pi = []
    for i in range(0, N+1) :
      probability = float(input())
      pi.append(probability)

    profit = float()
    numOfCustomers = int()
    remaining = 1
    for probability in pi :
      if numOfCustomers + 1 <= q :
        profit = profit + (r * numOfCustomers - c * q) * probability
        remaining = remaining - probability
      else :
        profit = profit + (r * numOfCustomers - c * q) * remaining
        break
      
      numOfCustomers += 1
    
    print( "ANS: ", end = '' )
    print(int(profit))

def week4_2() :
    c = float(input("單位進貨成本: "))  # 單位進貨成本
    r = float(input("單位零售價格: "))  # 單位零售價格
    N = int(input("需求的可能個數: "))  # 需求的可能個數

    pi = [float(input()) for _ in range(N+1)]

    max_profit = 0.0

    for q in range(N+1):
        profit = 0.0
        numOfCustomers = 0
        remaining = 1.0

        for probability in pi: 
            if numOfCustomers == q: 
                profit += (r * numOfCustomers - c * q) * remaining
                break
            else:
                profit += (r * numOfCustomers - c * q) * probability
                remaining -= probability 

            numOfCustomers += 1

        if (max_profit < profit and abs(max_profit - profit) > 0.001) or q == 0  :
            max_profit = profit
            best_q = q
        else:
            break
    
    print( "ANS: ", end = '' )
    print(best_q, int(max_profit))

def week5_1() :
    c = float(input("單位進貨成本: "))  # 單位進貨成本
    r = float(input("單位零售價格: "))  # 單位零售價格
    N = int(input("需求的可能個數: "))  # 需求的可能個數
    s = int(input("殘值: "))  # 殘值

    pi = [float(input()) for _ in range(N+1)]

    max_profit = 0.0

    for q in range(N+1):
        profit = 0.0
        numOfCustomers = 0
        remaining = 1.0

        for probability in pi: 
            if numOfCustomers == q: 
                profit += (r * numOfCustomers - c * q) * remaining
                break
            else:
                profit += (r * numOfCustomers - c * q + s * (q - numOfCustomers)) * probability
                remaining -= probability 

            numOfCustomers += 1

        if (max_profit < profit and abs(max_profit - profit) > 0.001) or q == 0  :
            max_profit = profit
            best_q = q
        else:
            break
    
    print( "ANS: ", end = '' )
    print(best_q, int(max_profit))

def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def week5_2() :
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
    
    print( "ANS: ", end = '' )
    for city, population in best_cities:
        total_population += population
        print(city, end = " ")

    print(total_population, end = "")

command = -1
while command != 0 :
    print( "\n0: 結束" )
    print( "1: week3 Q1" )
    print( "2: week3 Q2" )
    print( "3: week4 Q1" )
    print( "4: week4 Q2" )
    print( "5: week5 Q1" )
    print( "6: week5 Q2" )
    command = int( input( "輸入指令:" ) )
    if command == 1 :
        for i in range( 5 ) :
            print()
            week3_1()
    elif command == 2 :
        for i in range( 5 ) :
            print()
            week3_2()
    elif command == 3 :
        for i in range( 5 ) :
            print()
            week4_1()
    elif command == 4 :
        for i in range( 5 ) :
            print()
            week4_2()
    elif command == 5 :
        for i in range( 5 ) :
            print()
            week5_1()
    elif command == 6 :
        for i in range( 5 ) :
            print()
            week5_2()
            print()
    elif command != 0 :
        print( "no command" )