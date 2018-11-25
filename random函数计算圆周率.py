#CalPiV1.py
from random import random
from time import perf_counter
DARTS = 1000*1000
hits = 0.0
start = perf_counter()
for i in range(1,DARTS+1):
    x, y = random(), random()
    dist = pow(x ** 2 + y ** 2, 0.5)
    if dist <= 1.0:
        hits = hits + 1
pi = 4 * (hits/DARTS)
print("圆周率值是: {}".format(pi))
print("运行时间是:{:.5f}s".format(perf_counter() - start))




#CalPiV2.py
pi = 0
N = 100
for k in range(N):
    pi += 1/pow(16,k)*(4/(8*k+1) - 2/(8*k+4) - \
                       1/(8*k+5) - 1/(8*k+6))
print("圆周率值是：{}".format(pi))




#CalBMIV1.py
height, weight = eval(input("请输入身高（米）和体重（公斤）[逗号隔开]: "))
bmi = weight / pow(height, 2)
print("BMI 数值为:{:.2f}".format(bmi))
who = ""
if bmi < 18.5:
    who = "偏瘦"
elif 18.5 <= bmi < 25:
    who = "正常"
elif 25 <= bmi < 30:
    who = "偏胖"
else:
    who = "偏胖"
print("BMI 指标为:国际'{0}'".format(who))




#CalBMIV2.py
height, weight = eval(input("请输入身高（米）和体重\(公斤）[逗号隔开]:"))
bmi = weight / pow(height,2)
print("BMI 数值为:{:.2f}".format(bmi))
nat = ""
if bmi < 18.5:
    nat = "偏瘦"
elif 18.5 <= bmi < 24:
    nat = "正常"
elif 24 <= bmi < 28:
    nat = "偏胖"
else:
    nat = "肥胖"
print("BMI 指标为:国内'{0}'".format(who))




#pi,py
from random import random
from time import perf_counter
DARTS = 1000*1000
hits = 0.0
start = perf_counter()
for i in range(1,DARTS+1):
    x,y = random(),random()
    dist = pow(x ** 2 + y ** 2, 0.5)
    if dist <= 1.0:
        hits = hits + 1
pi = 4 * (hits/DARTS)
print("圆周率值是:{}".format(pi))
print("运行时间是:{:.5f}s".format(perf_counter() - start))




#整数加减和H1.py
m = 0
for i in range(1,967):
    if i % 2 in [0]:
        n = -i
    else:
        n = i
    m = n + m
print(m)



#整数加减和H2.py
s = 0
count = 1
while count <=966:
    if count%2 == 0:
        s -= count
    else:
        s += count
    count += 1
print(s)




# 三位水仙花数S1.py
s = ""
for i in range(100, 1000):
    m = i // 100
    n = (i // 10) % 10
    q = i % 10
    m = m ** 3
    n = n ** 3
    q = q ** 3
    num = m + n + q
    if i in [num]:
        s += "{},".format(i)
print(s[:-1])


#三位水仙花S2.py
s = ""
for i in range(100, 1000):
    t = str(i)
    if pow(eval(t[0]),3) + pow(eval(t[1]),3) + pow(eval(t[2]),3) == i :
        s += "{},".format(i)
print(s[:-1])





#用户登录N1.py
username = input()
password = input()
if username == 'Kate' and  password == '666666':
    print("登录成功！")
else:
    username = input()
    password = input()
    if username == 'Kate' and  password == '666666':
        print("登录成功！")
    else:
        username = input()
        password = input()
        if username == 'Kate'  and   password == '666666':
            print("登录成功！")
        else:
            print("3次用户名或者密码均有误！退出程序。")
pass




#用户登录N2.py
count = 0
while count < 3:
    name = input()
    password = input()
    if name == 'Kate'and password == '666666':
        print("登录成功！")
        break
    else:
        count += 1
        if count == 3:
            print("3次用户名或者密码均有误！退出程序。")
pass


