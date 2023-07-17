'''
11027147邱峻彥 11027140陳芃睿 11027250黃唯
題目描述:
在本題中，我們承接第一題的報童問題，但現在我們不想根據給定的一個存貨量去計算預期利
潤；我們想要找出能最大化預期利潤的最佳訂貨量 q* ，以及在此訂貨量之下能得到的預期利潤
π(q )無條件捨去到整數位。以第一題的例子而言，就是 4 跟 18（請自己試著算算看）。如果有
數個訂貨量會導致一模一樣的預期利潤（是預期利潤一樣，不是無條件捨去之後一樣！），請用
比較小的那一個當最佳訂貨量。
輸入輸出格式:
在每筆測試資料中，會有 N+4 列，每一列都有一個數字。第一列的整數是單位進貨成本 c 、第
二列的整數是單位零售價格 r 、第三列的整數是需求的可能個數 N 、第四列開始的小數則依序是
賣出零份、一份直到 N 份報紙的機率（也就是說對於 i = 4, 5, ..., N + 4 ，第 i 列記錄的是賣出
i -4份報紙的機率）。已知 c 會落在 1 到 100 之間（包含 1 跟 100）、 r 會落在 1 到 100 之間（包
含 1 跟 100）、 r 不會比 c 小、 N 一定會是 8。此外，對於i = 0, 1, ..., N ，pi會介於 0 到 1 之間
（包含 0 跟 1）、最多只有兩位小數。
讀入這些資料之後，你會計算最佳訂購量 q∗ ，以及在此訂購量下的預期利潤無條件捨去到整數
⌊π(q )⌋，並且在兩者中間用一個空格隔開。

'''
c = float(input())  # 單位進貨成本
r = float(input())  # 單位零售價格
N = int(input())  # 需求的可能個數

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

print(best_q, int(max_profit))
