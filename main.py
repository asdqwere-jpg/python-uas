def getTodayDate():
    from datetime import date
    return date.today().strftime("%d/%m/%Y")

def showMenu():
    print('Please Choose An Option :')
    print('1. Insert New Order')  
    print('2. Data Report')
    print('0. Exit')

def showReportMenu():
    print('Please Choose An Option :')
    print('1. By Today')
    print('2. By Week')
#     print('2. Show All Data')
    print('0. Exit')
    
def showMenuOrder():
    import ast
    paging = 0
    menuDatabase = open('menu.json', 'r')
    menuData = ast.literal_eval(menuDatabase.read())
    menuDatabase.close()
    for menu in menuData:
        print(paging + ' ' + menu)
        paging += 1