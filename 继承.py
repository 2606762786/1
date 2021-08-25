import time
class OldPhone():
    __brand = ""
    __number =""
    __ring =""

    def getbrand(self,brand):
        self.__brand=brand
    def setbrand(self):
        return self.__brand
    def getnumber(self,number):
        self.__number=number
    def setbrand(self):
        return self.__brand
    def getring(self, ring):
        self.__ring = ring
    def setring(self):
        return self.__ring

    def call(self, number):
        print(self.__number, "正在给", number, "打电话，正在响铃", self.__ring)
        for i in range(8):
            print(".", end="")
            time.sleep(1)
        print("已接通")



class NewPhone(OldPhone):
    __address = ""
    __background = ""

    def __init__(self, address, background):
        self.__address = address
        self.__background = background

    def call(self, number):
        print("语音拨通中")
        super().call(number)
        print("来电号码归属于", self.__address, "显示背景为：", self.__background)

    def describe(self):
        print("品牌为:", super().setbrand(), "的手机真好用")

class Test_phone():
    phone = NewPhone("北京","人民币")
    phone.getnumber("16619986837")
    phone.getring("红豆")
    phone.getbrand("华为")
    phone.call("15076227534")
    phone.describe()


class ChefClass():
    __uesrname = ""
    __age = 0

    def getusername(self, username):
        self.__username = username

    def setusername(self):
        return self.__username

    def getage(self, cookage):
        self.__age = cookage

    def setage(self):
        return self.__age

    def Steamedrice(self):
        print("厨师",self.__username,"正在蒸饭")

class Cook(ChefClass):
    def Stir(self):
        print("厨师",self.setusername(),"正在炒菜")

class Stir_try(Cook):
    def Steamedrice(self):
        print("厨师", self.setusername(), "正在蒸饭")

    def Stir(self):
        print("厨师", self.setusername(), "正在炒菜")

class Test_cook:
    cook = Stir_try()
    cook.getusername("张三")
    cook.getage(39)
    print("厨师",cook.setusername(),"今年",cook.setage())
    cook.Steamedrice()
    cook.Stir()


class person():
    __age = 0
    __sex = ""
    __name = ""

    def setPerson(self,age,sex,name):
        self.setAge(age)
        self.setSex(sex)
        self.setName(name)

    def setAge(self,age):
        if age > 0 and age <= 120:
            self.__age = age
        else:
            print("年龄设置有误")

    def getAge(self):
        return self.__age

    def setSex(self,sex):
        if sex == "男" or sex == "女":
            self.__sex = sex
        else:
            print("性别设置有误")

    def getSex(self):
        return self.__sex

    def setName(self,name):
        self.__name = name

    def getName(self):
        return self.__name


class worker(person):
    def work(self):
        print(super().getName(),"干活")

class student(person):
    __s_id = ""

    def setStudent(self,age,sex,name,s_id):
        super().setPerson(age,sex,name)
        self.setS_id(s_id)

    def setS_id(self,s_id):
        self.__s_id = s_id

    def getS_id(self):
        return self.__s_id

    def learn(self):
        print(super().getName(),"学习")

    def sing(self):
        print(super().getName(),"唱歌")


s = student()
s.setStudent(18,"男","小明",123456)
s.learn()
s.sing()

w = worker()
w.setPerson(18,"男","小光")
w.work()





