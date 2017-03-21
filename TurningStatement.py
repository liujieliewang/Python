#python 3.5.2

def TurningStatement(st_in):
    result = [0]
    result[:] = st_in.split()
    result.reverse()
    result = ' '.join(result)
    return result

statement = input("请输入语句:")
print(TurningStatement(statement))
