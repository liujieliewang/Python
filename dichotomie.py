#Python 3.5.2

def FindIndex(data,value):
    result = -1
    left = 0
    right = len(data) - 1
    while(left<right):
        mid = int((left + right)/2)
        if(data[mid] == value):
            result = mid
            break
        elif(data[mid] > value):
            right -= 1
        else:
            left += 1
    print(data[mid])
    return result

a = [1,2,4,6,8,12,33,41,56,78,99]

#print(a)
print(FindIndex(a,33))
