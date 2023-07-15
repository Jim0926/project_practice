c = int(input())  # 單位進貨成本
r = int(input())  # 單位零售價格
N = int(input())  # 需求的可能個數
q = int(input())  # 訂貨量

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

print(int(profit))