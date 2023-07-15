total = int(input())
remaining = 1000 - total

denominations = [500, 100, 50, 10, 5, 1]
num_of_notes = []

for denomination in denominations:
    num_of_notes.append(remaining // denomination)
    remaining = remaining % denomination

print(*num_of_notes, end="")