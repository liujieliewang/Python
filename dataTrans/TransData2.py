#Python 3.5.2
txtardss = input("请输入文件全路径：")
file_object = open(txtardss,'r',encoding= 'utf-8')
file_object_w = open('output2.txt', 'w+')
list_of_all_the_lines = file_object.readlines()

for i in range(len(list_of_all_the_lines)):
    a = []
    type_num = list_of_all_the_lines[i].split('\t',3)[1]
    lo_value = list_of_all_the_lines[i].split('\t',3)[2].replace("\n","")
    if int(type_num) < 6:
        a.append(lo_value)
        file_object_w.write(a[-1]+"\t")
        if int(type_num) == 5:
            file_object_w.write("\n")
file_object_w.close( )
file_object.close()
