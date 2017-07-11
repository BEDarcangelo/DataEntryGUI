import pymysql
from appJar import gui
import GUI_Input
import GUI_Query
export DISPLAY=0.0

def hideAll():
    app.hideLabel("title")
    app.hideEntry("Username")
    app.hideEntry("Password")
    app.hideButton("Submit")
    app.hideButton("Cancel")

def functionButtons():
    app.addLabel("functionSelect", "Select a function")    
    app.addRadioButton("function", "Input")
    app.addRadioButton("function", "Query")
    app.addRadioButton("function", "Update")
    app.addRadioButton("function", "Delete")

    #Function Selection Styling
    app.setLabelBg("functionSelect", "#ffffff")
    app.setLabelFg("functionSelect", "#107EC9")
    app.setRadioButtonAlign("function", "center")
    app.setRadioButtonFg("function", "#062E49")

def pressBTC(button):
    if button == "Exit":
        app.stop()

    else:
        function = app.getRadioButton("function")
        database = app.getRadioButton("database")

        db = pymysql.connect('localhost', user, pswd, database)
        cursor = db.cursor()

        if function == "Input":
            if database == "BTC_Accounting":
                GUI_Input.BTC_Input(cursor, db)
            else:
                GUI_Input.SJCX_Input(cursor, db)
            
        elif function == "Query":
            if database == "BTC_Accounting":
                GUI_Query.BTC_Query(cursor, db)
            else:
                GUI_Query.SJCX_Query(cursor, db)
            
        elif function == "Update":
            print (function)
            
        else:
            print (function)

def press(button):
    if button == "Cancel":
        app.stop()

    else:
        
        hideAll()
        app.addLabel("dbSelect", "What database would you like to access?")
        app.addRadioButton("database", "BTC_Accounting")
        app.addRadioButton("database", "SJCX_Accounting")
        functionButtons()

        #Setting Global Variables
        user = app.getEntry("Username")
        pswd = app.getEntry("Password")
        
        app.addButtons(["Enter", "Exit"], pressBTC)

        #Database Selection Styling
        app.setLabelBg("dbSelect", "#ffffff")
        app.setLabelFg("dbSelect", "#107EC9")
        app.setRadioButtonAlign("database", "center")
        app.setRadioButtonFg("database", "#062E49")

       
app = gui("Login Window", "400x500")
app.addImage("logo", "storj.jpg")
app.addLabel("title", "Welcome to the Storj SQL Database")
app.addLabelEntry("Username")
app.addSecretLabelEntry("Password")
app.addButtons(["Submit", "Cancel"], press)

#Login Window Styling
app.setBg("#107EC9")
app.setFont(14, font="Times")
app.getLabelWidget("title").config(font="Times 18")
app.setLabelBg("title", "white")
app.setLabelFg("title", "#107EC9")
app.setLabelFg("Username", "#ffffff")
app.setLabelFg("Password", "#ffffff")
app.setFocus("Username")

#Initialize Global Variables
global user
global pswd
global database

app.go()
