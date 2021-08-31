def getDate():
    file = open(file=r"baidu_x_system.log",mode="r+",encoding="utf-8")
    dates = file.readlines()
    list1 = []
    for i in dates:
        list1.append(i.split(" ")[0])
    file.close()
    return date

list2 = set(list1)
s = 0
ip = ""
    for i in list2:
        print(ip,"最多出现了",s,"次".format(i,list1.count(i))
