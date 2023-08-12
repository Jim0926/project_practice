import csv

def timeCompare( time1, time2 ) :    # 若t1比t2小就回傳-1，比較大就回傳1，相等就回傳0
  time1 = time1.replace( ":", "" )
  time2 = time2.replace( ":", "" )
  t1 = int( time1 )
  t2 = int( time2 )
  
  if t2 > t1 :
    return -1
  elif t2 < t1 :
    return 1
  else :
    return 0

str = str( input( "開始結束: " ) )
start = str.split( " " )[0]
end = str.split( " " )[1]

q1 = { "Accepted" : 0, "Compile Error" : 0, "Runtime Error" : 0, "Time Limit Exceed" : 0, "Wrong Answer" : 0 }
q2 = { "Accepted" : 0, "Compile Error" : 0, "Runtime Error" : 0, "Time Limit Exceed" : 0, "Wrong Answer" : 0 }
q3 = { "Accepted" : 0, "Compile Error" : 0, "Runtime Error" : 0, "Time Limit Exceed" : 0, "Wrong Answer" : 0 }
q4 = { "Accepted" : 0, "Compile Error" : 0, "Runtime Error" : 0, "Time Limit Exceed" : 0, "Wrong Answer" : 0 }
info = { "1" : q1, "2" : q2, "3" : q3, "4" : q4 }

with open('C:\\class\\python\\summer\\3week1\\midterm2.csv') as csvfile:

  # 讀取 CSV 檔案內容
  rows = csv.reader(csvfile)
  
  # 以迴圈輸出每一列
  for row in rows:
    if( row[6] != "SubmissionTime" and timeCompare( row[6], start ) >= 0 and timeCompare( row[6], end ) <= 0 ) :
      info[ row[2] ][ row[3] ] = info[ row[2] ][ row[3] ] + 1
      
  
  print( info["1"]["Accepted"], info["1"]["Compile Error"], info["1"]["Runtime Error"], info["1"]["Time Limit Exceed"], info["1"]["Wrong Answer"], end = "" )
  print( ";", end = "" )
  print( info["2"]["Accepted"], info["2"]["Compile Error"], info["2"]["Runtime Error"], info["2"]["Time Limit Exceed"], info["2"]["Wrong Answer"], end = "" )
  print( ";", end = "" )
  print( info["3"]["Accepted"], info["3"]["Compile Error"], info["3"]["Runtime Error"], info["3"]["Time Limit Exceed"], info["3"]["Wrong Answer"], end = "" )
  print( ";", end = "" )
  print( info["4"]["Accepted"], info["4"]["Compile Error"], info["4"]["Runtime Error"], info["4"]["Time Limit Exceed"], info["4"]["Wrong Answer"], end = "" )
  print( ";" )