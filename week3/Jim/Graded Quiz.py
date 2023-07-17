'''
邱峻彥 陳芃睿 黃唯
依照使用者輸入0~1000的消費金額，算出若用1000元鈔票該怎麼找錢，找錢面額的優先順序為: 500 100 50 10 5 1，最後輸出結果的方式是依序印出500~1元面額的數量，且若某個面額的數量為0就不用輸出。
'''
total = int(input())
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

print(output)
