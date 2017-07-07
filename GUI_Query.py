import pymysql
from appJar import gui

def selectString(selectedOptions):
    x = 0
    selectedColumns = ""

    while x < len(selectedOptions):

        if len(selectedOptions) == 1:
            if selectedOptions[x] == "All":
                selectedColumns += "*"
            else:
                selectedColumns += selectedOptions[x]
                
        elif x == len(selectedOptions)-1:
            selectedColumns += selectedOptions[x]

        else:
            selectedColumns += selectedOptions[x] + ","
            
        x += 1
        
    return selectedColumns

def selectOptions(optionList):
    x = 0
    selectedOptions = []

    while x < len(optionList):
        if app.getCheckBox(optionList[x]) == True:
            selectedOptions.append(optionList[x])
        x+=1
    return selectString(selectedOptions)

def press(button):
    if button == "Cancel":
        app.stop()
        
    else:
        if db == "BTC_Accounting":
            optionList = ["All", "id", "date", "btc_in", "btc_out", "balance", "fees_paid", "cash_value", "trans_type", "reason"]
        else:
            optionList = ["All", "id", "date", "sjcx_in", "sjcx_out", "balance", "cash_value", "trans_type", "trans_who", "reason", "trans_category"]

        columns = selectOptions(optionList)
        table = app.getRadioButton("table")
        condition = app.getEntry("Condition")

        if condition == "":

            sql = "SELECT %s FROM %s;" %(columns, table)
            DBcursor.execute(sql)
            result = DBcursor.fetchall()
            print(result)
            
        else:
            sql = "SELECT %s FROM %s WHERE %s;" %(columns, table, condition)
            DBcursor.execute(sql)
            result = DBcursor.fetchall()
            print(result)


def BTC_Query(database, cursor):
    
    global app
    global db
    global DBcursor
    app = gui("Query Window", "400x500")
    db = database
    DBcursor = cursor

    app.startLabelFrame("What columns would you like to select?")
    
    app.addCheckBox("All", 2,1)
    app.addCheckBox("id", 2, 2)
    app.addCheckBox("date", 3, 1)
    app.addCheckBox("btc_in", 3, 2)
    app.addCheckBox("btc_out", 4, 1,)
    app.addCheckBox("balance", 4, 2)
    app.addCheckBox("fees_paid", 5, 1)
    app.addCheckBox("cash_value", 5, 2)
    app.addCheckBox("trans_type", 6, 1)
    app.addCheckBox("reason", 6, 2)
    #Label Frame 1 Styling
    app.setBg("#107EC9")
    app.setLabelFrameFg("What columns would you like to select?", "#ffffff")
    app.setCheckBoxBg("All", "#107EC9")
    app.setCheckBoxBg("id", "#107EC9")
    app.setCheckBoxBg("date", "#107EC9")
    app.setCheckBoxBg("btc_in", "#107EC9")
    app.setCheckBoxBg("btc_out", "#107EC9")
    app.setCheckBoxBg("balance", "#107EC9")
    app.setCheckBoxBg("fees_paid", "#107EC9")
    app.setCheckBoxBg("cash_value", "#107EC9")
    app.setCheckBoxBg("trans_type", "#107EC9")
    app.setCheckBoxBg("reason", "#107EC9")
    app.setCheckBoxFg("All", "#062E49")
    app.setCheckBoxFg("id", "#062E49")
    app.setCheckBoxFg("date", "#062E49")
    app.setCheckBoxFg("btc_in", "#062E49")
    app.setCheckBoxFg("btc_out", "#062E49")
    app.setCheckBoxFg("balance", "#062E49")
    app.setCheckBoxFg("fees_paid", "#062E49")
    app.setCheckBoxFg("cash_value", "#062E49")
    app.setCheckBoxFg("trans_type", "#062E49")
    app.setCheckBoxFg("reason", "#062E49")

    app.stopLabelFrame()

    app.addLabel("tableSelect", "Which table would you like to use?")
    app.addRadioButton("table", "Electrum1_of_3")
    app.addRadioButton("table", "Electrum2_of_3")
    app.addRadioButton("table", "Coinbase")

    app.addLabel("conditionEntry", "What condition(s) would you like?")
    app.addEntry("Condition")
    app.addButtons(["Submit", "Cancel"], press)

    #Main Styling
    app.setBg("#107EC9")
    app.setFont(14, font="Times")

    #Radio Button Styling
    app.setLabelBg("tableSelect", "#ffffff")
    app.setLabelFg("tableSelect", "#107EC9")
    app.setRadioButtonBg("table", "#107EC9")
    app.setRadioButtonFg("table", "#062E49")
    app.setRadioButtonAlign("table", "center")

    #Condition Styling
    app.setLabelBg("conditionEntry", "#ffffff")
    app.setLabelFg("conditionEntry", "#107EC9")
    app.setEntryDefault("Condition", "i.e. id = 1...")
    

    app.go()

def SJCX_Query(database, cursor):
    
    global app
    global db
    global DBcursor
    app = gui("Query Window", "400x500")
    db = database
    DBcursor = cursor

    app.startLabelFrame("What columns would you like to select?")
    
    app.addCheckBox("All", 2,1)
    app.addCheckBox("id", 2, 2)
    app.addCheckBox("date", 3, 1)
    app.addCheckBox("sjcx_in", 3, 2)
    app.addCheckBox("sjcx_out", 4, 1,)
    app.addCheckBox("balance", 4, 2)
    app.addCheckBox("cash_value", 5, 1)
    app.addCheckBox("trans_type", 5, 2)
    app.addCheckBox("trans_who", 6, 1)
    app.addCheckBox("reason", 6, 2)
    app.addCheckBox("trans_category", 7, 1)
    #Label Frame 1 Styling
    app.setBg("#107EC9")
    app.setLabelFrameFg("What columns would you like to select?", "#ffffff")
    app.setCheckBoxBg("All", "#107EC9")
    app.setCheckBoxBg("id", "#107EC9")
    app.setCheckBoxBg("date", "#107EC9")
    app.setCheckBoxBg("sjcx_in", "#107EC9")
    app.setCheckBoxBg("sjcx_out", "#107EC9")
    app.setCheckBoxBg("balance", "#107EC9")
    app.setCheckBoxBg("cash_value", "#107EC9")
    app.setCheckBoxBg("trans_type", "#107EC9")
    app.setCheckBoxBg("trans_who", "#107EC9")
    app.setCheckBoxBg("reason", "#107EC9")
    app.setCheckBoxBg("trans_category", "#107EC9")
    app.setCheckBoxFg("All", "#062E49")
    app.setCheckBoxFg("id", "#062E49")
    app.setCheckBoxFg("date", "#062E49")
    app.setCheckBoxFg("sjcx_in", "#062E49")
    app.setCheckBoxFg("sjcx_out", "#062E49")
    app.setCheckBoxFg("balance", "#062E49")
    app.setCheckBoxFg("cash_value", "#062E49")
    app.setCheckBoxFg("trans_type", "#062E49")
    app.setCheckBoxFg("trans_who", "#062E49")
    app.setCheckBoxFg("reason", "#062E49")
    app.setCheckBoxFg("trans_category", "#062E49")

    app.stopLabelFrame()

    app.addLabel("tableSelect", "Which table would you like to use?")
    app.addRadioButton("table", "Main_Wallet")
    app.addRadioButton("table", "SJCX1_of_3")
    app.addRadioButton("table", "Shawns_Hot_Wallet")
    app.addRadioButton("table", "James_Hot_Wallet")

    app.addLabel("conditionEntry", "What condition(s) would you like?")
    app.addEntry("Condition")
    app.addButtons(["Submit", "Cancel"], press)

    #Main Styling
    app.setBg("#107EC9")
    app.setFont(14, font="Times")

    #Radio Button Styling
    app.setLabelBg("tableSelect", "#ffffff")
    app.setLabelFg("tableSelect", "#107EC9")
    app.setRadioButtonBg("table", "#107EC9")
    app.setRadioButtonFg("table", "#062E49")
    app.setRadioButtonAlign("table", "center")

    #Condition Styling
    app.setLabelBg("conditionEntry", "#ffffff")
    app.setLabelFg("conditionEntry", "#107EC9")
    app.setEntryDefault("Condition", "i.e. id = 1...")
    

    app.go()

