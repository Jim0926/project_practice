wallsInfo = {}
input_string = input() 
numOfWalls, numOfPaint = map(int, input_string.split())

for i in range(1, numOfWalls + 1):
    wallsInfo[i] = 1

paintInfo = []
for _ in range(numOfPaint):
    init, dest, number = map(int, input().split())
    paintInfo.append((init, dest, number))

for init, dest, number in paintInfo:
    for i in range(init, dest + 1):
        wallsInfo[i] = number

results = []
for _, _, number in paintInfo:
    count = 0
    for v in wallsInfo.values():
        if v == number:
            count += 1
    results.append((number, count))

output_str = ';'.join([f"{count} {value}" for value, count in results])
print(output_str)
