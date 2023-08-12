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