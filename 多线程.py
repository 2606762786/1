#面包
import threading
import time
bread = 0
class b(threading.Thread):
    baker = "" #面包师
    customersname = "" #顾客
    money = "" #顾客的钱
    count = 0

    def run(self) -> None:
        global bread
        while True:
            if bread < 500:
                    b = bread+1
                    print("厨师", self.baker, "做了", bread, "个面包")
            elif bread == 500:
                    print("满了")
                    time.sleep(2)
            elif self.customersname:
                if bread >= 1:
                    if self.money > 1:
                        self.money = self.money - 3
                        self.count = self.count + 1
                        bread = bread - 1
                        print(self.customersname, "一共买了", self.count, "个面包！")
                    elif self.money <= 1:
                        break
                elif bread == 0:
                    print("稍等片刻")
                    time.sleep(2)


b1 = b()
b2 = b()
b3 = b()
b4 = b()
b5 = b()
b6 = b()
b1.Baker = "c001"
b2.Baker = "c002"
b3.Baker= "c003"
b1.customersname = "g001"
b1.money = 3000
b2.customersname = "g002"
b2.money = 3000
b3.customersname = "g003"
b3.money = 3000
b4.customersname = "g004"
b4.money = 3000
b5.customersname = "g005"
b5.money = 3000
b6.customersname = "g006"
b6.money = 3000
b1.start()
b2.start()
b3.start()
b4.start()
b5.start()
b6.start()















