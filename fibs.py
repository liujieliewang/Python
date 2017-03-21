#Python 3.5.2

fibs = [0,1]
n = input("请输入求第几位数：")
n = int(n)
for i in range(n-1):
    fibs.append(fibs[-1]+fibs[-2])
print(fibs)
print(fibs[-1])
