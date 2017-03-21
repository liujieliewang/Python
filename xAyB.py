#Python 3.5.2
import random
def split_num(n_num):
    a = n_num//1000
    b = (n_num - a*1000)//100
    c = (n_num - a*1000 - b*100)//10
    d = n_num - a*1000 - b*100 - c*10
    r_num =[a,b,c,d] 
    return r_num
num = input ("作为测试先输入一个4位数字试试吧：")
num = int(num)
answer_num = split_num(num)
x = 1
while 1:
    a = 0
    b = 0
    in_num = input ("猜一个数字吧：")
    in_num = int(in_num)
    guess_num = split_num(in_num)
    for i in range(4):
        if guess_num[i] == answer_num[i]:
            a += 1
            if a == 4:
                print("猜对了，答案就是",in_num)
                x = 0
        elif guess_num[i] in answer_num:
            b += 1
    if x == 0:
        break
    print(a,"A",b,"B")
