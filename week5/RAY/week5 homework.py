def count( a, b, c ,d ):
    return (a-b)*(a-b)+(c-d)*(c-d)


l = input().split()
l = [int(element) for element in l] 
totalcity = l[0]
totalstation = l[1]
dis = l[2]
citydata = []

for i in range(totalcity):
    l = input().split()
    l = [int(element) for element in l]
    citydata.append(l)


beadd = []
cover = 0 
totalcover = 0 
mostcover = 0 
cityset = 0

for i in range(0, totalstation):
    mostcover = 0
    cityset = 0
    for j in range(totalcity):
        if beadd.count(j) == 0 :
            cover = citydata[j][2]
        else :
            cover = 0 

        for k in range(totalcity):
            #print( j, " ", k, " ", count( citydata[j][0], citydata[k][0], citydata[j][1], citydata[k][1] ) )
            if count( citydata[j][0], citydata[k][0], citydata[j][1], citydata[k][1] ) <= dis*dis and beadd.count(k) == 0 and k != j:
                cover = cover+citydata[k][2]
        
        #print( mostcover, " ",cover )
        if mostcover < cover:
            mostcover = cover
            cityset = j

    # find best city
    print(cityset)

    for x in range(totalcity):
        if count( citydata[cityset][0], citydata[x][0], citydata[cityset][1], citydata[x][1] ) <= dis*dis and beadd.count(x) == 0:
            beadd.append( x )
    totalcover += mostcover 
    #print(beadd)

print(totalcover)
    
