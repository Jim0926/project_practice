def distance( x1, y1, x2, y2 ) :
    return ( ( x1 - x2 ) ** 2 + ( y1 - y2 ) ** 2 ) ** 0.5

npdStr = input( "npd: " )
n = int( npdStr.split()[0] )    # n個城鎮
p = int( npdStr.split()[1] )    # 挑選p個城鎮蓋基地台
d = int( npdStr.split()[2] )    # 基地台覆蓋範圍為d公里
print( n, p, d )

countryInfo = []
tempList = []
for i in range( n ) :    # 讀入城鎮資訊
    tempStr = input( "第" + str( i + 1 ) + "個城鎮: " )
    for j in tempStr.split() :
        tempList.append( int( j ) )
    
    countryInfo.append( list( tempList ) )
    tempList.clear()

bestCountry = int()
selectedCountry = []
totalCoveredPeople = int()
for i in range( p ) :
    bestCoveredPeople = int( 0 )
    for mainCountry in countryInfo :
        coveredPeople = mainCountry[2]
        for subCountry in countryInfo :
            if distance( mainCountry[0], mainCountry[1], subCountry[0], subCountry[1] ) <= d and subCountry != mainCountry :
                coveredPeople = coveredPeople + subCountry[2]
        
        if coveredPeople > bestCoveredPeople :
            bestCoveredPeople = coveredPeople
            bestCountry = countryInfo.index( mainCountry )
        
    selectedCountry.append( bestCountry )
    totalCoveredPeople = totalCoveredPeople + bestCoveredPeople
    for subCountry in countryInfo :
        if distance( countryInfo[bestCountry][0], countryInfo[bestCountry][1], subCountry[0], subCountry[1] ) <= d :
            subCountry[2] = 0

for i in range( p ) :
    print( selectedCountry[i] + 1, end = ' ' )

print( totalCoveredPeople )