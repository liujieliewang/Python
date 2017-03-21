#python 3.3
x = 6
y = 4
a = [1] * x
p = [1/y] * y

i = 0
listp = [0]*(x*y+1)
while i == 0:
    pi = [0] * y
    for ax in range(0, x):
        for ix in range(0, y):
            if a[ax] == ix+1:
                pi[ix] += 1
    Probability = 1
    for b in range(0, y):
        Probability = Probability * (p[b] ** pi[b])
    s = sum(a)
    for num in range(x, x*y+1):
        if num == s:
            listp[num] += Probability
    a[x-1] += 1
    for add in range(1, x):
        if a[-add] == y+1:
            a[-add] = 1
            a[-add-1] += 1
        if a[0] == y+1:
            a[0] = 1
            i += 1
for num2 in range(x, x*y+1):
    print(num2, listp[num2])
print("sum", sum(listp))
