'''
11027147邱峻彥 11027140陳芃睿 11027250黃唯
--------------------------------------------------------------------------------------------------------------------------------
題目敘述:
如果你在一家零售店幫消費的客人結帳，你可能需要快速地挑出合適且數量正確的鈔票與零錢。假
設客人的消費金額 a 一定是 1 到 1000 之間的整數，而你有無限量的 500、100、50、10、5、1 這
些面額的鈔票和零錢，我們希望你能依照下面的規則找錢：
. 你找的錢的總額要是 1000 − a 。
. 與其給客人五張 100 元，不如給他一張 500 元；與其給客人兩個 50 元，不如給他一張 100 元……
依此類推。

以下是一些範例：
. 如果客人消費 200 元，你應該找給他 1 張 500 元和 3 張 100 元。
. 如果客人消費 286 元，你應該找給他 1 張 500 元、2 張 100 元、1 個 10 元和 4 個一元。
. 如果客人消費 925 元，你應該找給他 1 個 50 元、2 個 10 元和 1 個 5 元。
在本題中，你將會被給予上述的整數 ，而你要找出符合上述規則的唯一找錢方式。

輸入輸出格式:
在每筆測試資料中，會有一個整數 a 代表客人的消費金額， a 會介於 1 到 999 之間（包含 1 跟
999）。讀入 a 之後，你會依照題目指定的規則找出每種面額的鈔票或銅板應該要給幾張或幾個，
然後由面額大至面額小依序輸出所需鈔票張數或銅板個數，但如果不應該找給客人某個面額的鈔票
或銅板，就跳過該面額不要輸出。因為這樣一來可能只輸出少於 6 個數字，會不知道怎麼對應到面
額，因此現在要把面額與所需張數（個數）成對地輸出，中間用一個逗點和一個空格隔開，而面額
與面額之間用一個分號和一個空格隔開。
--------------------------------------------------------------------------------------------------------------------------------
根據題目規定，給定客人的消費金額 total（介於1到999之間），程式會計算並找出滿足以下條件的唯一找錢方式：
找的錢的總額要是 1000 - total。
需要找給客人的鈔票或銅板數量盡量少，並且遵循面額由大到小的順序。

程式碼的執行流程如下：

1. 首先，讀取一個整數 total 作為客人的消費金額。

2. 接著，計算 remaining，即找錢的總額，公式為 remaining = 1000 - total。

3. 建立一個字典 denominations，用來保存各種面額的鈔票或銅板需要的數量。初始時，每種面額的數量都設置為0。

4. 接下來的迴圈中，程式會依序處理每種面額的鈔票或銅板，並計算需要的數量。計算方式為：用 remaining 整除面額，
   得到這種面額需要的張數或個數，然後更新 remaining 為 remaining 除以面額的餘數，以便處理下一個面額。

5. 計算完成後，程式會將找錢的結果以字串 output 的形式儲存起來。這個字串包含了找錢的面額和對應的張數，並以分號和空格隔開。

6. 最後，輸出 output 字串，即顯示找錢的結果。
   (程式碼已經考慮了不需要找給客人某個面額的鈔票或銅板的情況，因此只會輸出需要找錢的面額及其對應的數量)
--------------------------------------------------------------------------------------------------------------------------------
'''

total = int(input())
remaining = 1000 - total

denominations = {500: 0, 100: 0, 50: 0, 10: 0, 5: 0, 1: 0}

for denomination in denominations:
    denominations[denomination] = remaining // denomination
    remaining = remaining % denomination

output = ""
for denomination, num_of_note in denominations.items():
    if num_of_note != 0:
        output += f"{denomination}, {num_of_note}; "

output = output.rstrip("; ") # 刪除 output 字串末尾的分號和空格

print(output)
