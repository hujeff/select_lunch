def writefiles():

    try:
        with open (r'lunch.txt','r',encoding='utf-8') as lunchr:
            lunch = lunchr.readlines()  #如果文件存在就读，每行为一个元素，存放到lunch里。
    except IOError:
        lunch = ['中餐','西餐','甜点']
        for i in lunch:
            with open (r'lunch.txt','a+',encoding='utf-8') as lunchw:
                lunchw.writelines(i+'\n')  #如果文件不存在就写

    try:
        with open (r'chinese_food.txt','r',encoding='utf-8') as chinese_foodr:
            chinese_food = chinese_foodr.readlines()
    except IOError:
        chinese_food = ['鱼香肉丝','青椒肉丝','鱼香茄子','红烧鱼块','香干回锅肉','粉蒸肉','干锅花菜','玉米排骨','小白菜','小炒黄牛肉']
        for i in chinese_food:
            with open (r'chinese_food.txt','a+',encoding='utf-8') as chinese_foodw:
                chinese_foodw.writelines(i+'\n')

    try:
        with open (r'western_food.txt','r',encoding='utf-8') as western_foodr:
            western_food = western_foodr.readlines()
    except IOError:
        western_food = ['巨无霸汉堡','墨西哥鸡肉卷','薯条','嫩牛五方','板烧鸡腿堡','黑椒牛排','通心粉','双层皇堡']
        for i in western_food:
            with open (r'western_food.txt','a+',encoding='utf-8') as western_foodw:
                western_foodw.writelines(i+'\n')

    try:
        with open (r'dessert.txt','r',encoding='utf-8') as dessertr:
            dessert = dessertr.readlines()
    except IOError:
        dessert = ['三明治','蛋糕','龟苓膏','奶茶','冰淇淋','麦片']
        for i in dessert:
            with open (r'dessert.txt','a+',encoding='utf-8') as dessertw:
                dessertw.writelines(i+'\n')

    return(lunch,chinese_food,western_food,dessert)