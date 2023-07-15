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

if r500 != 0 :
    print( "500, " + str( r500 ), end = '' )
    if not ( r100 == 0 and r50 == 0 and r10 == 0 and r5 == 0 and r1 == 0 ) :
        print( "; ", end = '' )

if r100 != 0 :
    print( "100, " + str( r100 ), end = '' )
    if not ( r50 == 0 and r10 == 0 and r5 == 0 and r1 == 0 ) :
        print( "; ", end = '' )

if r50 != 0 :
    print( "50, " + str( r50 ), end = '' )
    if not ( r10 == 0 and r5 == 0 and r1 == 0 ) :
        print( "; ", end = '' )

if r10 != 0 :
    print( "10, " + str( r10 ), end = '' )
    if not ( r5 == 0 and r1 == 0 ) :
        print( "; ", end = '' )

if r5 != 0 :
    print( "5, " + str( r5 ), end = '' )
    if not ( r1 == 0 ) :
        print( "; ", end = '' )

if r1 != 0 :
    print( "1, " + str( r1 ), end = '' )