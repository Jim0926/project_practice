c = int(input())  # 單位進貨成本
r = int(input())  # 單位零售價格
N = int(input())  # 需求的可能個數

pi = []
for i in range(0, N+1) :
  probability = float(input())
  pi.append(probability)

max_profit = 0.0

for q in range(0, N+1) :
  profit = 0.0
  numOfCustomers = 0
  remaining = 1.0
  for probability in pi :
    if numOfCustomers + 1 <= q :
      profit = profit + (r * numOfCustomers - c * q) * probability
      remaining = remaining - probability
    else :
      profit = profit + (r * numOfCustomers - c * q) * remaining
      break
  
    numOfCustomers += 1

  if max_profit < profit or q == 0 :
    max_profit = profit
    if q == N :
      print(q, int(max_profit))
  else :
    print(q-1, int(max_profit))
    break

