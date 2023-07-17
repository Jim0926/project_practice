'''
邱峻彥 陳芃睿 黃唯
題目描述:
有兩個帳戶的戶頭金額各為x1和x2，需求出從帳戶一轉帳y元到帳戶二的結果，若帳戶一的存款不足，也就是 x1 < y 的時候，就把x1變為0，x2變為x2 + x1。
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
