a = int( input() )
a = 1000 - a
r500 = 0
r100 = 0
r50 = 0
r10 = 0
r5 = 0
r1 = 0

while a >= 500 :
    a = a - 500
    r500 = r500 + 1

while a >= 100 :
    a = a - 100
    r100 = r100 + 1

while a >= 50 :
    a = a - 50
    r50 = r50 + 1

while a >= 10 :
    a = a - 10
    r10 = r10 + 1

while a >= 5 :
    a = a - 5
    r5 = r5 + 1

while a >= 1 :
    a = a - 1
    r1 = r1 + 1

print( r500, r100, r50, r10, r5, r1 )