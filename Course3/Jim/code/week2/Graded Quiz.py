'''
--------------------------------------------------------------------------------------------------------------------------------
組員名單:
    11027147 邱峻彥 11027140 陳芃睿 11027250 黃唯
    
程式撰寫者:
    11027147 邱峻彥
--------------------------------------------------------------------------------------------------------------------------------
YouBike 租借記錄視覺化（一）
題目敘述:
在「Resources」的「資料檔」區，有「ubike.csv」這個檔案，這是在 2015 年 9 月 7 日到 10 月 8
日之間從網路上爬下來的大安區 YouBike 站的每小時即時資訊。每個站點有 743 列，因此大安區的
30 個站點合計有 22290 列。
你會發現其中有 16 個欄位：
. time：爬取資料的時間，包含年月日時分。
. id：站點的編號，共 30 個不同的數字。
. station、address、latitude、longitude：站點的名稱、地址、緯度與經度。
. location：站點所屬的行政區。在這個檔案裡，通通都是「Daan Dist.」。
. status：該站點在當下的狀態，1 表示正常運作中，0 表示整個站點暫停營運（例如維修中）。
. lot：該站點共有幾個停車格。
. bike：爬取資料的當下該站點有幾臺可以借的車。
. empty：爬取資料的該站點有幾個空位。除非 status 欄位是 0，否則 ，而且
會是當下故障中的車位。
. weather：「Rain」表示爬取資料的當下正在下雨，「No Rain」表示沒有下雨。
. temp：爬取資料的當下的氣溫，以 Kelvin 度數表示。
. pressure：爬取資料當下的氣壓，以 hPa 表示。
. humidity：爬取資料當下的濕度，以百分比表示。
. wind：爬取資料當下的風速，以每秒幾公尺表示。
談到影響「可借車數」的因子，時間顯然是其中之一。讓我們來試著對「捷運公館站二號出口」
（Roosevelt & Xinsheng S. Intersection）這一站做這個分析。如果我們把一天分成 0 am 到 1 am、
1 am 到 2 am 等共 24 個時段，則在給定的資料中，我們在每個時段中都抓取恰好一次資料。如果
把給定的那批資料中的可借車數依照時段計算各時段的平均數，並且把這些平均數和總車位數畫成
兩條折線，放在一個折線圖上，就能感受時間對可借車數的影響。

下方的範例程式可以計算出各時段的平均可借車數與總車位數：
import matplotlib.pyplot as py
import csv, datetime

# open the file
f = open("ubike.csv", "r")
bike = {}
capacity = {}
count = {}

# processing the data
for row in csv.DictReader(f):
    if row["station"] == "Roosevelt & Xinsheng S. Intersection":
        time = datetime.datetime.strptime(row["time"], "%Y/%m/%d %H:%M")
        hour = time.hour
        if hour not in bike:
            bike[hour] = int(row["bike"])
            capacity[hour] = int(row["lot"])
            count[hour] = 1
        else:
            bike[hour] += int(row["bike"])
            capacity[hour] += int(row["lot"])
            count[hour] += 1 
f.close()

# preparing for plotting
time_seq = bike.keys()
time_seq = sorted(time_seq)
avg = []
lot = []
for k in time_seq:
    avg.append(float(bike[k]) / count[k])
    lot.append(float(capacity[k]) / count[k])
    
# plotting the data in avg and lot
--------------------------------------------------------------------------------------------------------------------------------
任務
你的朋友接著上面的程式，寫了一段用 matplotlib 畫圖的程式，畫出了(圖一)。
你也嘗試著這麼做，因此寫了如下的程式，但結果卻不如預期（請執行看看這段程式，看看差在哪
裡）：
py.plot(time_seq, lot, label = "Average")
py.plot(time_seq, avg, label = "Capacity")
py.title("Bikes at Roosevelt & Xinsheng S. Intersection")
py.xlabel("Time(hr)")
py.ylabel("Bike")
py.show()
--------------------------------------------------------------------------------------------------------------------------------
YouBike 租借記錄視覺化（二）
題目敘述:
有了經緯度資訊，當然就可以把各站點的位置畫在一個散佈圖上。不過如果這張散佈圖只呈現出位
置資訊就太可惜了。舉例來說，我們可以用不同顏色的點來表現不同的可借車輛佔總車位數的比例
（稱為「可借比例」）。舉例來說，如果我們想視覺化呈現 5 pm 到 7 pm 各站點的平均可借比例，
我們可以把平均可借比例低於 20%（不包含20\%）的站點標為紅色、介於 20% 到 30%（不包含
30%）的標為黃色，介於 30% 到 40%（不包含 40%）的標為綠色，40% 以上的則標為藍色，如(圖
二)所示。請注意經緯度之間的比例關係並沒有被嚴謹地設定。

下方你朋友寫的程式可以計算出各站點的可借比例：
import csv, os, datetime 
import matplotlib.pyplot as py 

f = open("ubike.csv", "r")

station = {} 
count = {} 
lat = {} 
lon = {} 
capacity = {} 
for row in csv.DictReader(f):
    time = datetime.datetime.strptime(row["time"], "%Y/%m/%d %H:%M")
    time = time.hour
    if time == 17 or time == 18:
        id = int(row["id"])
        if id not in station:
            lat[id] = float(row["latitude"])
            lon[id] = float(row["longitude"])
            capacity[id] = int(row["lot"])
            station[id] = int(row["bike"])
            count[id] = 1
        else:
            station[id] += int(row["bike"])
            capacity[id] += int(row["lot"])
            count[id] += 1
f.close()

id_seq = station.keys()
id_seq = sorted(id_seq)
redlat = [] 
redlon = [] 
yellowlat = [] 
yellowlon = [] 
greenlat = [] 
greenlon = [] 
bluelat = [] 
bluelon = [] 

for k in id_seq:
    capacity[k] = float(capacity[k]) / count[k]
    station[k] = (float(station[k]) / count[k]) / capacity[k]
    if station[k] < 0.2:
        redlat.append(lat[k])
        redlon.append(lon[k])
    elif 0.2 <= station[k] < 0.3:
        yellowlat.append(lat[k])
        yellowlon.append(lon[k])
    elif 0.3 <= station[k] < 0.4:
        greenlat.append(lat[k])
        greenlon.append(lon[k])
    else:
        bluelat.append(lat[k])
        bluelon.append(lon[k])
--------------------------------------------------------------------------------------------------------------------------------
任務
你的朋友接著上面的程式，寫了一段用 matplotlib 畫圖的程式，畫出了你剛剛看到的圖。你也嘗試
著這麼做，因此寫了如下的程式，但結果卻不如預期（請執行看看這段程式，看看差在哪裡）：
py.xlabel("latitude")
py.ylabel("longitude")
py.title("Bike Distribution")
py.plot(redlat, redlon)
py.plot(yellowlat, yellowlon)
py.plot(greenlat, greenlon)
py.plot(bluelat, bluelon)
py.axis([25.01,25.05,121.52,121.56])
py.legend(loc = "lower right")
py.show()
--------------------------------------------------------------------------------------------------------------------------------
'''

import matplotlib.pyplot as py
import csv, datetime

# open the file
f = open("ubike.csv", "r")
bike = {}
capacity = {}
count = {}

# processing the data
for row in csv.DictReader(f):
    if row["station"] == "Roosevelt & Xinsheng S. Intersection":
        time = datetime.datetime.strptime(row["time"], "%Y/%m/%d %H:%M")
        hour = time.hour
        if hour not in bike:
            bike[hour] = int(row["bike"])
            capacity[hour] = int(row["lot"])
            count[hour] = 1
        else:
            bike[hour] += int(row["bike"])
            capacity[hour] += int(row["lot"])
            count[hour] += 1 
f.close()

# preparing for plotting
time_seq = bike.keys()
time_seq = sorted(time_seq)
avg = []
lot = []
for k in time_seq:
    avg.append(float(bike[k]) / count[k])
    lot.append(float(capacity[k]) / count[k])
    
# plotting the data in avg and lot
py.plot(time_seq, lot, label = "Average")
py.plot(time_seq, avg, label = "Capacity")
py.title("Bikes at Roosevelt & Xinsheng S. Intersection")
py.xlabel("Time(hr)")
py.ylabel("Bike")
py.legend()
py.ylim(0, max(lot)*1.2)
values = list(range(0,24))
py.xticks(values)
py.show()

################################################################################################

import csv, os, datetime 
import matplotlib.pyplot as py 

f = open("ubike.csv", "r")

station = {} 
count = {} 
lat = {} 
lon = {} 
capacity = {} 
for row in csv.DictReader(f):
    time = datetime.datetime.strptime(row["time"], "%Y/%m/%d %H:%M")
    time = time.hour
    if time == 17 or time == 18:
        id = int(row["id"])
        if id not in station:
            lat[id] = float(row["latitude"])
            lon[id] = float(row["longitude"])
            capacity[id] = int(row["lot"])
            station[id] = int(row["bike"])
            count[id] = 1
        else:
            station[id] += int(row["bike"])
            capacity[id] += int(row["lot"])
            count[id] += 1
f.close()

id_seq = station.keys()
id_seq = sorted(id_seq)
redlat = [] 
redlon = [] 
yellowlat = [] 
yellowlon = [] 
greenlat = [] 
greenlon = [] 
bluelat = [] 
bluelon = [] 

for k in id_seq:
    capacity[k] = float(capacity[k]) / count[k]
    station[k] = (float(station[k]) / count[k]) / capacity[k]
    if station[k] < 0.2:
        redlat.append(lat[k])
        redlon.append(lon[k])
    elif 0.2 <= station[k] < 0.3:
        yellowlat.append(lat[k])
        yellowlon.append(lon[k])
    elif 0.3 <= station[k] < 0.4:
        greenlat.append(lat[k])
        greenlon.append(lon[k])
    else:
        bluelat.append(lat[k])
        bluelon.append(lon[k])

py.xlabel("latitude")
py.ylabel("longitude")
py.title("Bike Distribution")
py.plot(redlat, redlon, "ro", label = "<20%")
py.plot(yellowlat, yellowlon, "yo", label = "20%~30%")
py.plot(greenlat, greenlon, "go", label = "30%~40%")
py.plot(bluelat, bluelon, "bo", label = ">=40%")
py.axis([25.01,25.05,121.52,121.56])
py.legend(loc = "lower right")
py.show()
