from PySide2 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog,QComboBox,QMessageBox,QAction
import sys,os
import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
from ui import Ui_MainWindow

# Create Application
app = QtWidgets.QApplication(sys.argv)

# init
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()

# Logic
filesCount=0
images = []
prices= [] # The price of order app takes frpm Photo name

imageFolder = ""
driver = webdriver.Chrome()
driver.get("https://tap.az/elanlar/new")


#Contacts
def infodialog():
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Information)
    msg.setText("Creator: Ilkin Aslanli\n+(994)51-622-23-23")
    msg.setWindowTitle("Info")
    msg.setStandardButtons(QMessageBox.Ok)
    retval = msg.exec_()



# Message Box for showing errors
def showdialog(msge):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Information)
    msg.setText(msge)
    msg.setWindowTitle("Info")
    msg.setStandardButtons(QMessageBox.Ok)
    retval = msg.exec_()

# Function for working with folder
def selImgFolder():
    try:
        global images
        global imageFolder
        global filesCount
        global prices

        imageFolder = QFileDialog.getExistingDirectory() # Open the folder
        ui.label_10.setText(imageFolder) # Path
        files = os.listdir(imageFolder) # Adding all files which are in the folder

        for file in files:
            if (file.endswith('.jpg') or file.endswith('.jpeg') or file.endswith('.png')): # check if it's an image
                filter = file.split('.')[0] # select first part of photo name (Ex.: index.jpg, result:index)
                if('(' in filter): # In you program there may be many photos with the same name (price), like  ( 200.jpg, 200(2).jpg)
                    prices.append(filter.split('(')[0])
                else:
                    prices.append(file.split('.')[0])
                filesCount+=1 
                images.append(file)
        
    except Exception as e:
        showdialog(str(e))


# Getting categories
def categories():
    try:
        category = driver.find_element_by_name("lot[category_path]")

        category = str(category.text).split('\n')
        for item in category: # Adding all types to comboBoX
            ui.comboBox_2.addItem(item)
    except Exception as e:
        showdialog(str(e))

# Select the type of category
def pod_category_select():
    
    category_index = ui.comboBox_2.currentIndex()
    category = Select(driver.find_element_by_name("lot[category_path]"))
    category.select_by_index(category_index)
    driver.implicitly_wait(10)
    
    if(ui.comboBox_2.currentIndex()!=0): # If the current index of combox box is not 0 ( Program works with only 4 types of order ) 

        if (ui.comboBox_2.currentIndex() == 20):#20 is the current id of selected item
            ui.comboBox.clear()
            pod_category = driver.find_element_by_name("lot[property_set][754]")
           
        if (ui.comboBox_2.currentIndex() ==21):
            ui.comboBox.clear()
            pod_category = driver.find_element_by_name("lot[property_set][755]")
           
        if (ui.comboBox_2.currentIndex() == 22):
            ui.comboBox.clear()
            pod_category = driver.find_element_by_name("lot[property_set][756]")
           
        if (ui.comboBox_2.currentIndex() == 23):
            ui.comboBox.clear()
            pod_category = driver.find_element_by_name("lot[property_set][757]")
           
        if (ui.comboBox_2.currentIndex() == 24):
            ui.comboBox.clear()
            pod_category = driver.find_element_by_name("lot[property_set][758]")
            
        pod_category = str(pod_category.text).split('\n')
        for item in pod_category:
            ui.comboBox.addItem(item)

#Program has to click on 2 checkboxex
def checkBoxSolve():
    try:
        while (True):
            try:
               
                driver.find_element_by_name("lot[service]").click()
                driver.find_element_by_id("lot_contact_attributes_update_user").click()

                break
            except:
                continue
    except Exception as e:
        showdialog(str(e))

# Handling Errors
def errorCheck():
    
    try:
        errors=""
        if not ui.lineEdit.text() or not ui.lineEdit_2.text() or not ui.lineEdit_4.text() or not ui.textEdit.toPlainText() or not ui.lineEdit_5.text() or not ui.label_10.text() or ui.comboBox.currentIndex()==0:
            errors+="Elan tam doldurulmayib"

        return  errors
    except Exception as e:
        showdialog(str(e))

# Adding Information on WebSite
def addingInfo():
    ui.label_11.setText("0" + "/" + str(filesCount))
    ui.pushButton.setEnabled(False)
    errors = errorCheck()
    if not errors:

        for i in range(0, filesCount):

            try:
               
                checkBoxSolve()
                driver.implicitly_wait(10) 
                category_index = ui.comboBox_2.currentIndex()
                category = Select(driver.find_element_by_name("lot[category_path]"))
                category.select_by_index(category_index)
                driver.implicitly_wait(10)
                if (ui.comboBox_2.currentIndex() == 20):
                    category = Select(driver.find_element_by_name("lot[property_set][754]"))
                    category.select_by_index(ui.comboBox.currentIndex())

                if (ui.comboBox_2.currentIndex() == 21):
                    category = Select(driver.find_element_by_name("lot[property_set][755]"))
                    category.select_by_index(ui.comboBox.currentIndex())

                if (ui.comboBox_2.currentIndex() == 22):
                    category = Select(driver.find_element_by_name("lot[property_set][756]"))
                    category.select_by_index(ui.comboBox.currentIndex())

                if (ui.comboBox_2.currentIndex() == 23):
                    category = Select(driver.find_element_by_name("lot[property_set][757]"))
                    category.select_by_index(ui.comboBox.currentIndex()) 
                    
                if (ui.comboBox_2.currentIndex() == 24):
                    category = Select(driver.find_element_by_name("lot[property_set][758]"))
                    category.select_by_index(ui.comboBox.currentIndex())
              
               
                driver.find_element_by_id('lot_price').clear()
                driver.find_element_by_id('lot_price').send_keys(prices[i])

                driver.find_element_by_id('lot_body').clear()
                driver.find_element_by_id('lot_body').send_keys(ui.textEdit.toPlainText())

                driver.find_element_by_name('lot[title]').clear()
                driver.find_element_by_name('lot[title]').send_keys(ui.lineEdit.text())

                driver.find_element_by_name('lot[contact_attributes][name]').clear()
                driver.find_element_by_name('lot[contact_attributes][name]').send_keys(ui.lineEdit_2.text())

                driver.find_element_by_name('lot[contact_attributes][phones_separated]').clear()
                driver.find_element_by_name('lot[contact_attributes][phones_separated]').send_keys(ui.lineEdit_3.text())

                driver.find_element_by_name('lot[contact_attributes][email]').clear()
                driver.find_element_by_name('lot[contact_attributes][email]').send_keys(ui.lineEdit_4.text())

                driver.find_element_by_class_name('pond-new-img-field').send_keys(imageFolder+'/'+images[i])
                time.sleep(int(ui.lineEdit_5.text()))
                driver.find_element_by_name('button').click()
                ui.label_11.setText(str(i+1) + "/" + str(filesCount))

                driver.get("https://tap.az/elanlar/new")
            except Exception as e:
                showdialog(str(images[0])+" Elave olunmadi:"+str(e))
        ui.pushButton.setEnabled(True)
        driver.get("https://tap.az/elanlar/new")
    else:
        showdialog(errors)
        ui.pushButton.setEnabled(True)


categories()
pod_category_select()
ui.toolButton.clicked.connect(selImgFolder)
ui.pushButton.clicked.connect(addingInfo)
ui.pushButton_2.clicked.connect(infodialog)
ui.comboBox_2.currentIndexChanged.connect(pod_category_select)


#Run
sys.exit(app.exec_())

