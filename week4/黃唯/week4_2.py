c = int( input( "單位進貨成本: " ) )
r = int( input( "單位零售價格: " ) )
N = int( input( "可能需求: " ) )
probabilityList = []

for i in range( N + 1 ) :
    probabilityList.append( float( input( "賣掉" + str( i ) + "份報紙的機率: " ) ) )

expectedprofit = float( 0.0 )
best = int( 0 )
for q in range( N + 1 ) :
    j = int( 0 )
    tempExpectedSaleValue = float( 0.0 )
    p = float( 1.0 )
    for i in probabilityList :
        if j < q :
            tempExpectedSaleValue = tempExpectedSaleValue + j * i
            p = p - i
            j = j + 1
        else :
            tempExpectedSaleValue = tempExpectedSaleValue + q * p
            break
    
    if expectedprofit <= tempExpectedSaleValue * r - q * c :
        expectedprofit = tempExpectedSaleValue * r - q * c
        best = q
    else :
        break

print( best, int( expectedprofit ) )