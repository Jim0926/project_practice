'''
--------------------------------------------------------------------------------------------------------------------------------
組員名單:
    11027147 邱峻彥 11027140 陳芃睿 11027250 黃唯
    
程式撰寫者:
    11027147 邱峻彥
--------------------------------------------------------------------------------------------------------------------------------
題目敘述:
你經營一家報攤專賣一份日報，今天下午你得在報社關門前下訂單，告訴報社你要為明天訂購幾
份報紙，隔天清晨你就會收到訂購的報紙並且付款。每份報紙的進貨價格是 c 元，賣給客人的零
售價則是 r 元，而每一份沒賣出去的報紙，在明天結束時可以被以一份 s 元的殘值（salvage
value）當作廢紙賣掉。每天會來多少個客人想買報紙是件不確定的事，也就是說單日需求量 D 是
隨機的。根據過往經驗，你估計明天的單日需求量會落在 0 和 N 之間，並且符合如下的機率分
佈：
Pr(D = i) = pi，i = 0, 1, . . . , N。
意思是說，有 0 個人來買報紙的機率是 P0 、有 1 個人來買報紙的機率是 P1 ，依此類推，最後是賣
出 N 份報紙的機率是 PN 。你想要決定你的訂貨量 q∗ 去最大化你的期望利潤（expected profit）
π(q) = rE[ min{q, D}] − cq + sE[ max{q − D, 0}]，
其中 min{q, D} 是明天的銷售量（訂貨量和需求量中比較小的那個數字）、 E[min{q, D}] 是
預期銷售量（也就是銷售量取期望值）、 rE[ min{q, D}] 是預期銷售收益、 cq 是必須付給報社
的進貨成本、$\max\{q - D, 0\}$ 是沒賣掉的份數（$D \geq q$ 表示沒有剩），因此 $s\mathbb{E}
[\max\{q - D, 0\}]$ 是預期總殘值。這是一個作業管理（operations management）領域的經典存貨
問題（inventory problem），因為是很多存貨管理方法的基礎，被特別給予一個名稱叫「報童問
題」（newsvendor problem）。

輸入輸出格式:
在每筆測試資料中，會有 N+4 列，每一列都有一個數字。第一列的整數是單位進貨成本 c 、第二列
的整數是單位零售價格 r 、第三列的整數是需求的可能個數 N 、第四列是殘值 s 、第五列開始的小數則依序是
賣出零份、一份直到 N 份報紙的機率（也就是說對於 i = 4, 5, ..., N + 4 ，第 i 列記錄的是賣出
i -4份報紙的機率）。已知 c 會落在 1 到 100 之間（包含 1 跟 100）、 r 會落在 1 到 100 之間（包
含 1 跟 100）且不會比c小、s 會落在 1 到 100 之間（包含 1 跟 100）且不會比c大、 N 會落在 1 到 1000 
之間（包含 1 跟 1000）。此外，對於i = 0, 1, ..., N ，pi會介於 0 到 1 之間（包含 0 跟 1）、最多只有兩位小數。
讀入這些資料之後，你會計算並輸出此訂購量下的預期利潤無條件捨去到整數⌊π(q )⌋。
--------------------------------------------------------------------------------------------------------------------------------
根據題目規定，需在給定進貨成本 c、零售價格 r、需求的可能個數 N 以及殘值 s 的情況下，找出最佳的訂貨量 q，以使期望利潤最大化。

程式碼的執行流程如下：

1. 首先，讀取單位進貨成本 c、單位零售價格 r、需求的可能個數 N、以及殘值 s。

2. 接著，使用迴圈讀取每個需求量的機率 pi，並將這些資訊存入 pi 列表中。

3. 初始化 max_profit 變數為 0，用來儲存最大的期望利潤。

4. 接下來的迴圈中，程式會計算每種訂購量 q 下的預期利潤 profit。利用變數 numOfCustomers 跟踪已經購買報紙的客人數量，remaining 變數
   來追蹤未考慮到的機率（即購買量大於訂購量的機率之和）。

5. 在迴圈中，程式會檢查若現有的客人數量加上一個客人後是否小於等於訂購量。如果是，代表現有的訂購量可以滿足這一類需求，計算並累加這一類需求的預期利潤。
   並將對應機率 probability 從 remaining 減去。

6. 如果現有的客人數量加上一個客人後大於訂購量，代表部分需求的購買量會超過訂購量，這時程式會計算並累加這部分需求的預期利潤，並且停止迴圈計算。

7. 在每種訂購量 q 的迴圈中，程式會比較此訂購量下的預期利潤 profit 是否大於已知的最大預期利潤 max_profit。如果大於，則更新最大預期利潤 max_profit，
   並記錄最佳訂貨量 q*。否則代表當前的 max_profit 為最終的最大預期利潤。另外在迴圈過程中，如果 q 等於 N，代表是最大值，直接輸出。

8. 最後，在所有訂購量 q 的迴圈結束後，輸出最佳訂貨量 q* 和對應的最大預期利潤 max_profit。
   (如果有多個訂購量對應的預期利潤相同，則程式會選擇比較小的那一個作為最佳訂貨量，由第7步驟的程式邏輯可得)
--------------------------------------------------------------------------------------------------------------------------------
'''

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