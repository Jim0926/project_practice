c = int( input( "單位進貨成本: " ) )
r = int( input( "單位零售價格: " ) )
N = int( input( "可能需求: " ) )
q = int( input( "訂貨量: " ) )
probabilityList = []

for i in range( N + 1 ) :
    probabilityList.append( float( input( "賣掉" + str( i ) + "份報紙的機率: " ) ) )

j = int( 0 )
expectedSaleValue = float( 0.0 )
p = float( 1.0 )
for i in probabilityList :
    if j < q :
        expectedSaleValue = expectedSaleValue + j * i
        p = p - i
        j = j + 1
    else :
        expectedSaleValue = expectedSaleValue + q * p
        break

print( int( expectedSaleValue * r - q * c ) )
