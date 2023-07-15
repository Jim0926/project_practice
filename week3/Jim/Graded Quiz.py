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
