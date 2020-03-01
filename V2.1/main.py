import select_lunch
import random

def select_food():
    lst = select_lunch.selectlunch()  #从函数中获得的是一个元祖
    lst = [x.strip() for x in lst]
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
                choice_a = input('不想吃的话，吃%s好不好呢？（好或不好）' %c4)  #输出上一个被客户否定的内容和重新选择的内容，再次询问是否合适。
                lst.remove(c4)  #删除已选择的内容，避免重复
                randomchoice = c4  #将新选择的内容复制给c3，在下次输出时会输出本次选择并被否定的内容
            else:  #如果列表为空
                reselect = input('已经没有了，要不要重新选一次呢？（输入“要”就重新选择）')  #输入是否继续运行
                if reselect == '要':  #如果要继续运行
                    lst = select_lunch.selectlunch()   #则重新将列表复制给lst
                    randomchoice(lst)  #重新到while开始循环
                else:
                    print('好吧，那你自个想吃的吧')
                    exit()

select_food()