cost = int(input())
price = int(input())
N = int(input())
left = int(input())

pb = []
for i in range(N+1):
    pb.append(float(input()))
    
temp1 = 0.0
temp2 = 0.0 
profit = 0.0
sell = 0

for i in range(N+1):
    temp2 = 0.0
    for j in range(N+1):
        temp1 = 0.0 
        if i >= j :
            temp1 = j*( price-cost ) + ( i-j )*left - ( i-j )*cost
        else:
            temp1 = i*( price-cost )
            
        temp2 = temp2 + temp1*pb[j]


    if temp2 > profit:
        profit = temp2 
        sell = i 
        
out = int(profit)
print( sell, out )
