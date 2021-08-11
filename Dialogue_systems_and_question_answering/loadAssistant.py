import json,re
import main.myailml as alimls

import main.loadData as datas

Trams,Forcasts,Restans =  datas.readData()

def showData():
    for i in Forcasts:
        print(i.data)



def showForcaset(date):
    for i in Forcasts:
        if i.data == date:
            print(i.forecast)

def showCategory():
    setList = set()
    for i in Restans:
        setList.add(i.categoryName)
    for item in setList:
        print(item)

def HandlerForcast(str):
    # showData()
    # date = input("please choose date(Entre all):")
    showForcaset(str)

def chooseForcast(category):
    for i in Restans:
        if i.categoryName == category:
            print(f"name is {i.shopName} and avgPrice is {i.avgPrice}")

def HandlerRestaurant(str):
    # print("**************show category***************")
    # showCategory()
    # category = input("please choose category(Entre all ):")
    chooseForcast(str)

def showSite():
    setList = set()
    for tram in Trams:
        for stop in tram.stopLine:
            setList.add(str(stop))
    for i in setList:
        print(i)
def chooseTram(site):
    for tram in Trams:
        for i in tram.stopLine:
            if str(i) == site:
                print(tram.tramName)

def HandlerTram(str):
    # showSite()
    # site = input("Please choose where you want to go:")
    chooseTram(str)





def Handler(str):
    ty,keyword = parse(str)
    if ty != None and keyword != None:
        if ty == '1':
            HandlerForcast(keyword)
        if ty == '2':
            HandlerRestaurant(keyword)
        if ty == '3':
            HandlerTram(keyword)
        elif ty ==None:
            alimls.tellAlice(str)
    pass


def generateOneRules():
    rules = {
             "1":['I want to know the weather on (.*)','Please tell me the weather on (.*)',"Tell me the weather on (.*)"],
             "2":['Please tell me some (.*) stores','(.*) has recommended it',"Recommend some (.*) restaurants"],
             "3": ['Tell me the subway station next to (.*)', 'What are the subways to (.*)'],
             }
    return rules
def parse(str):
    res = None
    type = None
    rule = generateOneRules()
    for i_type, items in rule.items():
        for pattern in items:
            match = re.search(pattern, str)
            if match is not None:
                item = match.group(1)
                res = item
                type = i_type
    return type,res
def vaildStr(str):
    if str == None:
        print("please begin entre!!")
        return False
    return True
def generationMenu(digit,name):
    formAtmenu = f"Entre {digit} for find {name}"
    return formAtmenu
def printTips():
    index = 1
    for i in ['forcast', 'restaurant', 'tram']:
        print(generationMenu(index, i))
        index += 1

def helloAssistant():
    print("**************************************************************")
    print("*************begin****************************************")
    print("Hello I am aliml:")
    # printTips()


    while True:
        str = input("> Entre: ")
        if vaildStr(str):
            Handler(str)

# if __name__ == '__main__':
#     helloAssistant()