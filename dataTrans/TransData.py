#Python 3.5.2
txtardss = input("请输入文件全路径：")
day_num = input("请输入要处理的天数：")
day_num = int(day_num)
file_object = open(txtardss,'r',encoding= 'utf-8')
file_object_w = open('output.txt', 'w+')
list_of_all_the_lines = file_object.readlines()
for x in range(day_num):
    a = []
    for i in range(6):
        a.append(list_of_all_the_lines[i+x*6].split(':',2)[1].replace("\n",""))
        file_object_w.write(a[i]+"\t")
    file_object_w.write("\n")
file_object_w.close( )
file_object.close()
