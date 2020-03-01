import random

lunch = ['中餐','西餐','甜点']
chinese_food = ['鱼香肉丝','青椒肉丝','鱼香茄子','红烧鱼块','香干回锅肉','粉蒸肉','干锅花菜','玉米排骨','小白菜','小炒黄牛肉']
western_food = ['巨无霸汉堡','墨西哥鸡肉卷','薯条','嫩牛五方','板烧鸡腿堡','黑椒牛排','通心粉','双层皇堡']
dessert = ['三明治','蛋糕','龟苓膏','奶茶','冰淇淋','麦片']

def PrintList(self):
    global lunch,chinese_food,western_food,dessert
    if self == '中餐':
        lst = chinese_food.copy()
    elif self == '西餐':
        lst = western_food.copy()
    elif self == '甜点':
        lst = dessert.copy()
    print('现在有如下选择：')
    for i in lst:
        print(i)
    c1 = input('这些东西够你选嘛？如果不够输入“不够”将开始添加你自己的内容，如果输入其他内容将开始选择午餐：')
    while c1 == '不够':
        userinput = input('请输入你需要添加的内容：')
        if userinput in lst:
            print('%s已经存在了，请换一个吧' % userinput)
        else:
            lst.append(userinput)
            if self == '中餐':
                chinese_food = lst.copy()
            elif self == '西餐':
                western_food = lst.copy()
            elif self == '甜点':
                dessert = lst.copy()
            for i in lst:
                print(i)
            c2 = input('已经添加了，还要继续添加吗？（是或否）')

            if c2 == '是':
                continue
            else:
                break

def SelectLunch(self):  #选择午餐函数
    Selectdishes(RandomChoice(self))  #调用选择菜品函数，并给选择菜品函数传送随机选择函数所返回的内容

def RandomChoice(self):  #随机选择函数  
    '''这是改蹦了的第一版选择器
    lst = self.copy()
    while lst:
        c3 = random.choice(lst)  #随机选择列表内的东西
        lst.remove(c3)  #删除已选择的内容，避免重复
        choice_a = input('我们吃%s可好？(好或不好)'% c3) #请用户判断所选内容是否符合要求
        if choice_a == '不好': #如果不符合客户要求
            if not lst:  #如果列表为空，则打印提示信息，并请用户选择是否继续运行
                reselect = input('已经没有了，要不要重新选一次呢？（输入“要”就重新选择）')  #输入是否继续运行
                if reselect == '要':  #如果要继续运行
                    lst = self.copy()  #则重新将列表复制给lst
                    RandomChoice(self)  #重新到while开始循环
                else:
                    print('好吧，那你自个想吃的吧')
                    exit()
            else:
                c4 = random.choice(lst)  #则重新选择随机内容，如果是午餐选择lunch里的内容，如果是选好餐别则选对应餐别的列表内容
                choice_a = input('%s不想吃的话，吃%s好不好呢？（好或不好）' % (c3,c4))  #输出上一个被客户否定的内容和重新选择的内容，再次询问是否合适。
                lst.remove(c4)  #删除已选择的内容，避免重复
                c3 = c4  #将新选择的内容复制给c3，在下次输出时会输出本次选择并被否定的内容。
        elif choice_a == '好': #如果符合要求则输出客户的要求。
            print('那我们就吃%s啦！'% c3)
            return c3'''
    lst = self.copy()
    randomchoice = random.choice(lst)
    lst.remove(randomchoice)
    choice_a = input('我们吃%s可好？(好或不好)'% randomchoice) #请用户判断所选内容是否符合要求
    while True:
        if choice_a == '好':  #如果用户选择好
            print('那我们就吃%s啦！\n'% randomchoice)
            return randomchoice
        else:  #如果用户选择不好
            if lst:  #如果列表不为空
                c4 = random.choice(lst)  #则重新选择随机内容，如果是午餐选择lunch里的内容，如果是选好餐别则选对应餐别的列表内容
                choice_a = input('%s不想吃的话，吃%s好不好呢？（好或不好）' % (randomchoice,c4))  #输出上一个被客户否定的内容和重新选择的内容，再次询问是否合适。
                lst.remove(c4)  #删除已选择的内容，避免重复
                randomchoice = c4  #将新选择的内容复制给c3，在下次输出时会输出本次选择并被否定的内容
            else:  #如果列表为空
                reselect = input('已经没有了，要不要重新选一次呢？（输入“要”就重新选择）')  #输入是否继续运行
                if reselect == '要':  #如果要继续运行
                    lst = self.copy()  #则重新将列表复制给lst
                    RandomChoice(self)  #重新到while开始循环
                else:
                    print('好吧，那你自个想吃的吧')
                    exit()

def Selectdishes(self):  #菜品选择函数
    if self == '中餐':  #判断午餐大类别
        RandomChoice(chinese_food)  #调用随机选择函数
    elif self == '西餐':
        RandomChoice(western_food)
    elif self == '甜点':
        RandomChoice(dessert)
        
def main():
    while True:
        choice = input('欢迎试用吃什么，你有以下几种选择:\n（拜托请按提示选择，第一次写程序，不按提示输入的话就会报错的）\n1、添加食品分类(还未开放)\n2、添加具体食物\n3、开始消灭选择困难症！(请输入1、2、3)')
        if choice == '1':
            PrintList(lunch)
        elif choice == '2':
            print(lunch)
            c5 = input('你想要添加的食物属于哪个分类？')
            PrintList(c5)
        elif choice == '3':
            SelectLunch(lunch)

main()