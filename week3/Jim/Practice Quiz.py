'''
11027147邱峻彥 11027140陳芃睿 11027250黃唯
題目敘述:
在兩個戶頭之間轉帳，是非常普通的一個金融交易。假設我們現在有兩個帳戶，戶頭金額各為 x1 和
x2，而我們想要從第一個戶頭轉 y 元到第二個戶頭，則一般情況下兩個戶頭的金額各會變成 x1 − y
和 x2 + y 。但如果第一個戶頭錢不夠的話，我們就把第一個戶頭的錢扣到變成 0，然後把第二個戶
頭的錢變成 x2 + x1。舉例來說，如果原本兩個戶頭各有 1000 和 2000 元，而我們要轉 500 元，那
就會變成 500 和 2500，但如果要轉 1200 元，就會變成 0 和 3000。
請寫一個程式，讀入 x1 、 x2 和 y 之後，判斷兩個戶頭各應該變成多少錢。
輸入輸出格式
在每筆測試資料中，第一行會有一個整數 x1 ，第二行會有一個整數 x2 ，第三行會有一個整數 y 。已
知 x1 、 x2 和 y 都介於 0 和 100000 之間。讀入三個整數之後，請依照題目指定的規則，決定兩個戶
頭的餘額各會變成多少，先印出第一個戶頭的餘額，再印出第二個戶頭的餘額，兩個整數之間用一
個空白字元隔開。
'''
x1 = int(input())
x2 = int(input())
y  = int(input())

if x1 > y :
    x1 = x1 - y
    x2 = x2 + y
else :
    x2 = x2 + x1
    x1 = 0

print(x1, x2)
