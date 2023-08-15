import csv

input_file = "C:\\Users\\ASUS\\Desktop\\midterm2.csv"
f = open( input_file, 'r' ) 
cols = 5
rows = 4
problem = [[0 for _ in range(cols)] for _ in range(rows)] #建立一個4*5的list

l = f.readline()
print( l )
line_now = csv.reader( f, delimiter='\t' ) #讀檔

b = str(input())
e = str(input()) #輸入時間限制

begintime = int( b.replace( ":", "" ) )
endtime = int( e.replace( ":", "" ) ) #把時間限制改為可以比對的數字

for l in line_now :
    l = list( l ) 
    l = l[0].split( ',' ) #逐筆取出資料並且轉換成list
    print(l[6])
    if int( l[6].replace( ":", "" ) ) >= begintime and int( l[6].replace( ":", "" ) ) <= endtime :
        if l[3] == "Accepted" :
            problem[int(l[2])-1][0] = problem[int(l[2])-1][0] + 1
        elif  l[3] == "Compile Error" :
            problem[int(l[2])-1][1] = problem[int(l[2])-1][1] + 1
        elif  l[3] == "Runtime Error" :
            problem[int(l[2])-1][2] = problem[int(l[2])-1][2] + 1
        elif  l[3] == "Time Limit Exceed" :
            problem[int(l[2])-1][3] = problem[int(l[2])-1][3] + 1
        elif  l[3] == "Wrong Answer" :
            problem[int(l[2])-1][4] = problem[int(l[2])-1][4] + 1 #確認是否在限制時間內後插入對應的位置

print( problem )
