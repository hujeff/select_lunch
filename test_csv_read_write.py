import pandas as pd

lunch = []

def OpenFile(self):
    print(type(self))
    with open(r'data\data.csv','r') as csvfile:
        linereader = csv.reader(csvfile)
        line =[row for row in linereader]
        #for line in linereader:
            #print(line)
        self = self.append(line)
    print(self)

OpenFile(lunch)