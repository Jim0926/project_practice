c = float(input())  # 單位進貨成本
r = float(input())  # 單位零售價格
N = int(input())  # 需求的可能個數
s = int(input())  # 殘值

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

print(best_q, int(max_profit))
