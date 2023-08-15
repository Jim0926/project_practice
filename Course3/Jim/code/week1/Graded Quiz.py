'''
--------------------------------------------------------------------------------------------------------------------------------
組員名單:
    11027147 邱峻彥 11027140 陳芃睿 11027250 黃唯

程式撰寫者:
    11027147 邱峻彥
--------------------------------------------------------------------------------------------------------------------------------
題目敘述:
當我們在臺大開設「商管程式設計」的實體課程時，我們使用一個自動批改系統，學生們在寫作業
或考試的時候，是去系統上傳自己的程式碼，然後系統會直譯並且執行此程式碼，並且輸入若干筆
測試資料，讓程式計算並輸出結果，再跟正確答案比對。在一次上傳後，會有至少以下五種批改結
果：
. Accepted：在全部的測試資料都得到了正確答案。
. Compile Error：程式中有 syntax error。
. Runtime Error：程式在某幾筆測試資料發生了 run-time error。
. Wrong Answer：程式在某幾筆測試資料輸出了錯誤的答案（亦即發生了 logic error）。
. Time Limit Exceed：程式在某幾筆測試資料執行過久，在時限前沒有輸出答案。
在「Resource」裡面的「資料檔」區，大家可以看到「midterm2.csv」這個檔案。在這個檔案中，
我們記錄了本門課在臺大的實體課某學期第二次期中考（共有四題）的所有繳交記錄。檔案共有七
個欄位，「SubmissionID」是每次提交程式碼時系統給定的唯一編號、「StudentID」是那次提交程
式碼的學生編號（一個學號對應到一個學生編號，但我們已經處理過編號了，因此你從學生編號看
不出學號）、「Problem」是提交的題號（1 到 4 的整數）、「Status」是提交後的狀態
（Accepted、Compile Error、Runtime Error、Time Limit Exceed、Wrong Answer 五種）、
「Score」是該題的得分（第一題到第四題的滿分各是 30、40、30、30，考試總分 130 分）、
「CodeLength」是該次提交的程式碼的長度、「SubmissionTime」是提交的時間。請注意這個檔案
中的資料列是依提交時間由晚到早排序的。

輸入輸出格式
在每筆測試資料中會包含兩個字串，依序代表指定的開始時間與結束時間（所以前者早於後者），
時間的格式為 hh:mm:ss，例如九點十八分零六秒表示為 09:18:06。兩個時間字串之間被一個空白隔
開。
讀入資料後，請按照題目的規定計算出每一題在兩個時間（含）之間的五種狀態的提交次數，接著
以一列印出，先印出第一題的五個數字，接著印出一個分號，再印出第二題的五個數字，依此類
推。在每一題中，請依序印出該題 Accepted、Compile Error、Runtime Error、Time Limit
Exceed、Wrong Answer 的次數。一題中每兩個數字之間用一個空白鍵隔開。最後一個數字後面不
可以有空格。分號前後不應該有空格。第四題的五個數字最後也應該有一個分號。
--------------------------------------------------------------------------------------------------------------------------------
請針對上述任務寫一個 Python 程式，在給定輸入的資料後，按照指定格式輸出運算結果。就以下五
題，請將你的程式輸出的結果貼到答案欄，若與正確解答一字不差則算正確，反之則算不正確。
雖然沒有人會檢查你的程式碼，但你當然應該試著用 class 來寫這個程式。一個很合理的作法是讓
每次 submission 都在系統中被存成一個物件。當然，你也可以有自己的設計。
--------------------------------------------------------------------------------------------------------------------------------
'''

from datetime import datetime, time

# 判斷一時間點是否在給定的區段時間內
def is_time_within_range(input_time, start_time, end_time):
    input_time = datetime.strptime(input_time, '%H:%M:%S').time()
    start_time = time(*map(int, start_time.split(':')))
    end_time = time(*map(int, end_time.split(':')))
    
    return start_time <= input_time <= end_time

# 開啟檔案並回傳內容
def read_file(file_path):
    data = []  # 用來存放讀取的資料
    
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()  # 讀取所有行
            
            for line in lines[1:]:  # 跳過首行（標題行）
                line = line.strip()  # 去除行尾的換行符
                elements = line.split(',')  # 用逗號分割每個元素
                data.append(elements)  # 將元素加入資料列表
    except FileNotFoundError:
        print("找不到指定的檔案。")
    
    return data


class Automatic_correction_system:
    def findDatas(self, start_time, end_time):
        datas = []
        for submission in self.file_data:
            if( is_time_within_range(submission[6], start_time, end_time) ):
                datas.append(submission)

        return datas

    def showResult(self, datas):
        result = {'1':[0]*5, '2':[0]*5, '3':[0]*5, '4':[0]*5}
        for submission in datas:
            if ( submission[2] == '1' ):
                self.updateStatesNum(submission, result['1'])
            elif ( submission[2] == '2' ):
                self.updateStatesNum(submission, result['2'])
            elif ( submission[2] == '3' ):
                self.updateStatesNum(submission, result['3'])
            elif ( submission[2] == '4' ):
                self.updateStatesNum(submission, result['4'])

        for State in result.values():
            output_string = " ".join(map(str, State))  # 將列表轉換為空格分隔的字串
            print(output_string, end=";")

    def updateStatesNum(self, submission, result):
        if( submission[3] == 'Accepted' ):
            result[0] = result[0] + 1
        elif( submission[3] == 'Compile Error'):
            result[1] = result[1] + 1
        elif( submission[3] == 'Runtime Error'):
            result[2] = result[2] + 1
        elif( submission[3] == 'Time Limit Exceed'):
            result[3] = result[3] + 1
        elif( submission[3] == 'Wrong Answer'):
            result[4] = result[4] + 1
        
        

file_path = 'C:\\Users\\jim97\\Desktop\\project\\course3\\week1\\input.csv'  # 替換成你的檔案路徑
ACS = Automatic_correction_system()
ACS.file_data = read_file(file_path)

start_time = input('Please enter a start time : ')
end_time = input('Please enter a end time : ')
ACS.range_data = ACS.findDatas(start_time, end_time)
ACS.showResult(ACS.range_data)
