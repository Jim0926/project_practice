import matplotlib.pyplot as plt

def CournotEq(a, b, c1, c2, n):
    # iteration 0: entering the market
    q1 = list()
    q1.append((a + c1) / 2)
    q2 = list()
    q2.append((a + b * q1[0] + c2) / 2)

    # in each iteration, respond once
    for i in range(n):
        q1Next = (a + b * q2[i] + c1) / 2
        q1.append(q1Next)
        q2Next = (a + b * q1Next + c2) / 2
        q2.append(q2Next)

    return q1[n], q2[n]

input_string = input("請輸入各資訊並以逗點分隔：")
values = input_string.split(',')
a = int(values[0])
b = float(values[1])
c1 = int(values[2])
c2 = int(values[3])
n = int(values[4])
p1Eq, p2Eq = CournotEq(a, b, c1, c2, n)
print("%0.2f %0.2f" % (p1Eq, p2Eq))
