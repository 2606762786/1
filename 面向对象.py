#水杯
class cup:
    __height = ""
    __volume = ""
    __color = ""
    __texture = ""

    def setheight(self,height):
        self.__height = height

    def getheight(self):
        return self.__height

    def setvolume(self,volume):
        self.__volume = volume

    def getvolume(self):
        return self.__volume

    def setcolor(self,color):
        self.__color = color

    def getcolor(self):
        return self.__color

    def settexture(self, texture):
        self.__texture = texture

    def gettexture(self):
        return self.__texture

    def a(self):
        print(self.__height,"是杯子的高度",self.__volume,"是杯子的容积",self.__color,"是杯子的颜色",self.__texture,"是杯子的材质。")

    def use(self):
        print("能盛",self.__volume,"的水")

c = cup()

c.setheight(20)
c.setvolume(400)
c.setcolor("black")
c.settexture("glass")

c.a()
c.use()

print(c.getheight(),c.getvolume(),c.getcolor(),c.gettexture())

#笔记本电脑
class computer():
    __name = ""
    __size =0  #屏幕尺寸
    __price =0
    __cpu = ""
    __memory =""
    __time =0  #待机时长

    def computer_name(self,name):
        self.__name=name

    def size(self,size):
        if size>0:
            self.__size=size
        else:
            print("输入非法")

    def price(self,price):
        if price>0:
            self.__price=price
        else:
            print("输入非法")

    def cpu(self,cpu):
        self.__cpu=cpu

    def memory(self,memory):
        self.__memory=memory

    def time(self,time):
        if time>0:
            self.__time=time
        else:
            print("输入非法")

    def mode(self):
        print("这台电脑的显示尺寸是",self.__size,"英寸,价格是",self.__price,"cpu是",self.cpu,
              "内存是",self.__memory,"待机时长",self.__time,"秒")


    def type(self):
        print("我正在用", self.__name, "打字")

    def play(self, game):
        print("我正在用", self.__name, "玩", game)

    def watch(self, watching):
        print("我正在用", self.__name, "看", watching)

c = computer()
c.computer_name("mac")
c.size(17)
c.price(18000)
c.cpu("AMD5900X")
c.time(60)
c.mode()
c.type()
c.play("巫师三")
c.watch("权利的游戏")





