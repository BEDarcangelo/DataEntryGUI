import pymysql
from appJar import gui

def pressSJCX(button):
    if button == "Cancel":
        app.stop()
    else:
        table = app.getRadioButton("table")
        date = app.getEntry("Date")
        sjcx_in = float(app.getEntry("SJCX In"))
        sjcx_out = float(app.getEntry("SJCX Out"))
        balance = float(app.getEntry("Balance"))
        cash_value = float(app.getEntry("Cash Value"))
        trans_type = app.getEntry("Type")
        trans_who = app.getEntry("Who")
        reason = app.getEntry("Reason")
        trans_category = app.getEntry("Category")

        sql = "INSERT INTO %s (date, sjcx_in, sjcx_out, balance, cash_value, trans_type, trans_who, reason, trans_category) VALUES ('%s', '%f', '%f', '%f', '%f', '%s', '%s', '%s', '%s');" %(table, date, sjcx_in, sjcx_out, balance, dollar_value, trans_type, trans_who, reason, trans_category)
        SJCXcursor.execute(sql)
        SJCXdb.commit()

        print(sql)
        
def pressBTC(button):
    if button == "Cancel":
        app.stop()
        
    else:
        table = app.getRadioButton("table")
        date = app.getEntry("Date")
        btc_in = float(app.getEntry("BTC In"))
        btc_out = float(app.getEntry("BTC Out"))
        balance = float(app.getEntry("Balance"))
        fees_paid = float(app.getEntry("Fees Paid"))
        cash_value = float(app.getEntry("Cash Value"))
        trans_type = app.getEntry("Type")
        reason = app.getEntry("Reason")

        sql = "INSERT INTO %s (date, btc_in, btc_out, balance, fees_paid, cash_value, trans_type, reason) VALUES ('%s', '%f', '%f', '%f', '%f', '%f', '%s', '%s');" %(table, date, btc_in, btc_out, balance, fees_paid, cash_value, trans_type, reason)
        BTCcursor.exectue(sql)
        BTCdb.commit()
        
        print(sql)

def BTC_Input(cursor, db):

    global BTCdb
    global BTCcursor
    global app
    BTCdb = db
    BTCcursor = cursor
    app = gui("Input Window", "400x500")
    
    app.addLabel("tableSelect", "Which table would you like to modify?")
    app.addRadioButton("table", "Electrum1_of_3")
    app.addRadioButton("table", "Electrum2_of_3")
    app.addRadioButton("table", "Coinbase")

    app.startLabelFrame("Please Enter Your Data Below")
    
    app.addLabelEntry("Date")
    app.addLabelEntry("BTC In")
    app.addLabelEntry("BTC Out")
    app.addLabelEntry("Balance")
    app.addLabelEntry("Fees Paid")
    app.addLabelEntry("Cash Value")
    app.addLabelEntry("Type")
    app.addLabelEntry("Reason")

    #Label Frame Styling
    app.setBg("#107EC9")
    app.setLabelFrameFg("Please Enter Your Data Below", "#ffffff")
    app.setLabelFg("Date", "#062E49")
    app.setEntryDefault("Date", "YYYYMMDD")
    app.setLabelFg("BTC In", "#062E49")
    app.setLabelFg("BTC Out", "#062E49")
    app.setLabelFg("Balance", "#062E49")
    app.setLabelFg("Fees Paid", "#062E49")
    app.setLabelFg("Cash Value", "#062E49")
    app.setLabelFg("Type", "#062E49")
    app.setLabelFg("Reason", "#062E49")

    app.stopLabelFrame()

    #Main Styling
    app.setBg("#107EC9")
    app.setFont(14, font="Times")
    app.getLabelWidget("tableSelect").config(font="Times 16")
    app.setLabelBg("tableSelect", "#ffffff")
    app.setLabelFg("tableSelect", "#107EC9")

    #Radio Button Styling
    app.setRadioButtonBg("table", "#107EC9")
    app.setRadioButtonFg("table", "#062E49")
    app.setRadioButtonAlign("table", "center")

    app.addButtons(["Confirm", "Cancel"], pressBTC)

    app.go()

def SJCX_Input(cursor, db):
    global SJCXdb    
    global SJCXcursor
    global app
    
    SJCXdb = db
    SJCXcursor = cursor
    app = gui("Input Window", "400x500")

    app.addLabel("tableSelect", "Which table would you like to access?")
    app.addRadioButton("table", "Main_Wallet")
    app.addRadioButton("table", "SJCX1_of_3")
    app.addRadioButton("table", "Shawns_Hot_Wallet")
    app.addRadioButton("table", "James_Hot_Wallet")
    
    app.startLabelFrame("Please Enter Your Data Below")
    
    app.addLabelEntry("Date")
    app.addLabelEntry("SJCX In")
    app.addLabelEntry("SJCX Out")
    app.addLabelEntry("Balance")
    app.addLabelEntry("Cash Value")
    app.addLabelEntry("Type")
    app.addLabelEntry("Who")
    app.addLabelEntry("Reason")
    app.addLabelEntry("Category")

    #Label Frame Styling
    app.setBg("#107EC9")
    app.setLabelFrameFg("Please Enter Your Data Below", "#ffffff")
    app.setLabelFg("Date", "#062E49")
    app.setEntryDefault("Date", "YYYYMMDD")
    app.setLabelFg("SJCX In", "#062E49")
    app.setLabelFg("SJCX Out", "#062E49")
    app.setLabelFg("Balance", "#062E49")
    app.setLabelFg("Cash Value", "#062E49")
    app.setLabelFg("Type", "#062E49")
    app.setLabelFg("Who", "#062E49")
    app.setLabelFg("Reason", "#062E49")
    app.setLabelFg("Category", "#062E49")

    app.stopLabelFrame()

    #Main Styling
    app.setBg("#107EC9")
    app.setFont(14, font="Times")
    app.getLabelWidget("tableSelect").config(font="Times 16")
    app.setLabelBg("tableSelect", "#ffffff")
    app.setLabelFg("tableSelect", "#107EC9")

    #Radio Button Styling
    app.setRadioButtonBg("table", "#107EC9")
    app.setRadioButtonFg("table", "#062E49")
    app.setRadioButtonAlign("table", "center")

    app.addButtons(["Confirm", "Cancel"], pressSJCX)

    app.go()
    
