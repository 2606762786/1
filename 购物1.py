import random
answer=input("是否抽取优惠券：")
d = {"是","yes"}
b = {"否","no"}
if answer in d:
    print("----商品优惠券----")
    coupon = [
        ["机械革命", 10, 0.5],
        ["卫龙辣条", 20, 0.3],
        ["HUA WEI WATCH", 15, 0.8],
    ]
    for key, value in enumerate(coupon):
        print(key, value)
    chose = random.randint(0, len(coupon) - 1)
    print("恭喜您抽到：", coupon[chose][2] * 10, "折", coupon[chose][0], "的优惠券")
    dd=0
    coupon[chose][1] = coupon[chose][1] - 1
    if coupon[chose][1] == 0:
        coupon.pop(chose)
    print(coupon)
elif answer in b:
    print("放弃优惠券，请直接购买！")



shop=[
    ["lenovo PC",5600],
    ["HUA WEI WATCH",1200],
    ["Mac pro",12000],
    ["洗衣机",3000],
    ["机械革命",5000],
    ["卫龙辣条",4.5],
    ["老干妈辣酱",20],
]
money=input("请输入您的初始金额：")
money=int(money)
mycart=[]
i=0
c = {"不买了"}
while i<20:
    print("----全部商品----")
    for key,value in enumerate(shop):
        print(key,value)
    number=input("请输入您要购买的商品号：")
    if number.isdigit():
        number=int(number)
        if number>=0 and number<len(shop):
            if money>=shop[number][1]:
                money=money-shop[number][1]
                mycart.append(shop[number])
                print("恭喜，商品添加成功！您的余额为：￥", money)
            else:
                print("温馨提示：您的银行卡余额不足，穷鬼！请买其他商品！")
        else:
            print("该商品不存在！别瞎弄！")
    elif number in c:
        print("欢迎下次光临！")
        break
    else:
        print("对不起，别瞎弄！重新输入！")
i=i+1

print("以下是您的购物小条，请拿好！")
print("".center(30,"-"))
for key,value in enumerate(mycart):
    print(key,value)
print("".center(30,"-"))
