'''
11027147邱峻彥 11027140陳芃睿 11027250黃唯
題目說明:
你經營一家報攤專賣一份日報，今天下午你得在報社關門前下訂單，告訴報社你要為明天訂購幾
份報紙，隔天清晨你就會收到訂購的報紙並且付款。每份報紙的進貨價格是 c 元，賣給客人的零
售價則是 r 元。每天會來多少個客人想買報紙是件不確定的事，也就是說單日需求量 D 是隨機
的。根據過往經驗，你估計明天的單日需求量會落在 0 和 N 之間，並且符合如下的機率分佈：
Pr(D = i) = pi，i = 0, 1, . . . , N。
意思是說，有 0 個人來買報紙的機率是 P0、有 1 個人來買報紙的機率是 P1，依此類推，最後是賣
出 N 份報紙的機率是 PN 。你想要決定你的訂貨量 q* 去最大化你的期望利潤（expected profit）
π(q) = rE[ min{q, D}] − cq，
其中 min{q, D} 是明天的銷售量（訂貨量和需求量中比較小的那個數字）、 E[min{q, D}] 是
預期銷售量（也就是銷售量取期望值）、 rE[ min{q, D}] 是預期銷售收益、cq 則是必須付給報
社的進貨成本。這是一個作業管理（operations management）領域的經典存貨問題（inventory
problem），因為是很多存貨管理方法的基礎，被特別給予一個名稱叫「報童問題」（newsvendo
problem）。
在每筆測試資料中，會有 N+5 列，每一列都有一個數字。第一列的整數是單位進貨成本 c、第二列的整
數是單位零售價格 r、第三列的整數是需求的可能個數 N、第四列是訂貨量 q、第五列開始的小數則依序是
賣出零份、一份直到 N 份報紙的機率（也就是說對於i=4,5,...,N+4，第 i 列記錄的是賣出 i−4 份
報紙的機率）。已知 c 會落在 1 到 100 之間（包含 1 跟 100）、 r 會落在 1 到 100 之間（包含 1
跟 100）、 r 不會比 c 小、 N 一定會是 8。此外，對於 = 0 , 1 , . . . , i=0,1,...,N， pi 會
介於 0 到 1 之間（包含 0 跟 1）、最多只有兩位小數。
讀入這些資料之後，你會計算並輸出在給定訂購量下的預期利潤無條件捨去到整數⌊π(q)⌋。
'''
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
