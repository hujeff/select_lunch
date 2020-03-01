import writefiles
import random
a = writefiles.writefiles()  #从函数中获得的是一个元祖
b = list(a)  #将元祖转换为列表
lunch = b[:1][0]  #将列表切片，从列表中取出各个元素生成新的列表，下同。
chinese_food = b[1:2][0]
western_food = b[2:3][0]
dessert = b[3:][0]

#print(type(b))  #检查b是否为列表
#print(lunch,'\n',chinese_food,'\n',western_food,'\n',dessert) #检查各个变量中列表的内容

def selectlunch():
    global lunch,chinese_food,western_food,dessert,foodlist  #声明全局变量，只能在函数内声明。
    print(lunch)
    choicea = input('请输入您想选择的内容（1、中餐  2、西餐  3、甜点）：')  #让用户输入选择具体想吃的类别
    if choicea == '中餐':  #开始判断用户选择，并将用户选择的列表复制给foodlist，供后面使用。
        foodlist = chinese_food.copy()
    elif choicea == '西餐':
        foodlist = western_food.copy()
    elif choicea == '甜点':
        foodlist = dessert.copy()
    else:
        choicea = random.choice(lunch)  #随机从lunch中选择一个，并在下面重新匹配。（后期看看有没有啥子优化一下。）
        print('不知道你想吃啥，给你随便选了一个')
        if choicea == '中餐':  #再次判断用户选择，并将用户选择的列表复制给foodlist，供后面使用。
            foodlist = chinese_food.copy()
        elif choicea == '西餐':
            foodlist = western_food.copy()
        elif choicea == '甜点':
            foodlist = dessert.copy()
    print('您选择了%s，其中包含了:'%choicea)  #列出用户选择类别的内容。
    for i in foodlist:
        print(i)
    c1 = input('这些东西够你选嘛？如果不够输入“不够”将开始添加你自己的内容，如果输入其他内容将开始选择午餐：')
    while True:
        if c1 == '不够':
            userinput = input('请输入你需要添加的内容：')
            print(userinput)
            c = [x.strip() for x in foodlist]  #去掉所有\n的转义符，生成新的列表，给下面判断用户输入时用。
            if userinput in c:  #如果用户输入的内容已经存在于列表，就要求重新输入。
                print('%s已经存在了，请换一个吧' % userinput)
            else:  #否则将用户输入的内容加上换行符以后添加到列表末尾，并写入文件中保存。
                foodlist.append(userinput + '\n')
                if choicea == '中餐':
                    with open (r'chinese_food.txt','a+',encoding='utf-8') as filewrite:
                        filewrite.writelines(userinput + '\n')
                elif choicea == '西餐':
                    with open (r'western_food.txt','a+',encoding='utf-8') as filewrite:
                        filewrite.writelines(userinput + '\n')
                elif choicea == '甜点':
                    with open (r'dessert.txt','a+',encoding='utf-8') as filewrite:
                        filewrite.writelines(userinput + '\n')
                for i in foodlist:
                    print(i)
                c2 = input('已经添加了，还要继续添加吗？（是或否）')
                if c2 == '是':
                    continue
                else:
                    break
        else:
            break
    return foodlist
selectlunch()