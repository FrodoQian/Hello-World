
#DayDayUpQ1.py
dayup =pow(1.001,365)
daydown =pow(0.999,365)
print("向上: {:.2f}, 向下：{:.2f}".format(dayup,daydown))


#DayDayUpQ2.py
dayfactor = 0.005
dayup = pow(1+dayfactor,365)
daydown = pow(1-dayfactor,365)
print("向上:{:.2f},向下:{:.2f}".format(dayup,daydown))


#DayDayUpQ3.py
dayup = 1.0
dayfactor = 0.01
for i in range(365):
    if i % 7 in [6,0]:
        dayup = dayup*(1-dayfactor)
    else:
        dayup = dayup*(1+dayfactor)
print("工作日的力量：{:.2f}".format(dayup))


#DayDayUpQ4.py
def dayUp(df):
    dayup = 1
    for i in range(365):
        if i % 7 in [6,0]:
            dayup = dayup * (1 - 0.01)
        else:
            dayup = dayup * (1 + df)
    return dayup
dayfactor = 0.01
while dayUp(dayfactor) < 37.78:
    dayfactor += 0.001
print("工作日的努力参数是:{:.3f}".format(dayfactor))



#WeekNamePritV1.py
weekStr = "星期一星期二星期三星期四星期五星期六星期日"
weekId = eval(input("请输入星期数字（1-7):"))
pos = (weekId -1) * 3
print(weekStr[pos:pos+3])



#星座V2.py
for i in range(12):
    print(chr(9800 + i) ,end="")


#TextProBarV3.py
import time
for i in range(101):
    print("\r{:3}%".format(i),end=" ")
    time.sleep(0.1)


#TextProBarV4.py
import time
scale = 50
print("执行开始".center(scale//2,"-"))
start = time.perf_counter()
for i in range(scale+1):
    a = '*' * i
    b = '-' * (scale - 1)
    c = (i/scale)*100
    dur = time.perf_counter() - start
    print("\r{:^3.0f}%[{}->{}]{:.2f}s".format(c,a,b,dur),end='')
    time.sleep(0.1)
print("\n"+"执行结束".center(scale//2,'-'))



#TextProBarV5.py
import time
scale = 50
print("执行开始".center(scale//2,"-"))
start = time.perf_counter()
for i in range(scale+1):
    a = '*' * i
    b = '.' * (scale+1)
    c = (i/scale)*100
    dur = time.perf_counter() - start
    print("\r{:^3.0f}%[{}->{}]{:.2f}s".format(c,a,b,dur),end='')
    time.sleep(0.1)
print("\n"+"执行结束".center(scale//2,'-'))



#三次方格式化V6.py
num = eval(input("请输入数字:"))
x = num **3
scale = 20
print("{:.^}".format(x).center(scale,'-'))



#星号三角形V7.py
num = eval(input(""))  #输入的数字
scale = num   #一行有多少个字符
n = num // 2    #一共有多少行
for i in range(scale+1):              #如果i是基数，那么就输出i个*号，
    if i % 2 in [1]:
        a = '*' * i
        print("\r"+"{}".format(a).center(scale,'-'))
    else:
        print("\b")
    pass# 如果i是偶数，呢么久继续继续下一个


#星号三角形V7.py
num = eval(input(""))  #输入的数字
scale = num   #一行有多少个字符
n = num // 2    #一共有多少行
for i in range(scale+1):
    x = i + 1    #如果i是基数，那么就输出i个*号，
    if x % 2 in [1]:
        a = '*' * i
        print("\r"+"{}".format(a).center(scale,' '),end='')
    else:
        print("",end='')


#星号三角形V7.py
num = eval(input(""))
scale = num
for i in range(scale+1):
    if i % 2 in [1]:
        a = '*' * i
        print("{}".format(a).center(scale,' '))
    else:
        print("",end='')
    pass




#凯撒密码V8.py
s = input()
t = ""
for c in s:
    if 'a' <= c <= 'z':
        t += chr( ord('a') + ((ord(c)-ord('a')) + 3 )%26 )
    elif 'A'<=c<='Z':
        t += chr( ord('A') + ((ord(c)-ord('A')) + 3 )%26 )
    else:
        t += c
print(t)














