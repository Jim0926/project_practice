c = int( input( "單位進貨成本: " ) )
r = int( input( "單位零售價格: " ) )
N = int( input( "可能需求: " ) )
s = int( input( "殘值: " ) )
probabilityList = []

for i in range( N + 1 ) :
    probabilityList.append( float( input( "賣掉" + str( i ) + "份報紙的機率: " ) ) )

expectedProfit = float( 0.0 )    #預期收益
best = int( 0 )    #最佳收益的數量
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
    
    if expectedProfit <= tempExpectedSaleValue * r - q * c + ( q - tempExpectedSaleValue ) * s :
        expectedProfit = tempExpectedSaleValue * r - q * c + ( q - tempExpectedSaleValue ) * s
        best = q
    else :
        break

print( best, int( expectedProfit ) )
