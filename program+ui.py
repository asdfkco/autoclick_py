import sys
import keyboard
import pyautogui
from PyQt5.QtWidgets import *
from PyQt5 import uic
import tkinter.messagebox as msgbox
from PyQt5 import QtCore, QtGui, QtWidgets


pyautogui.FAILSAFE = False

global diection
global speeds
global clicks_
global count



class Ui_MainWindow(object):
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(462, 433)
        MainWindow.setMinimumSize(QtCore.QSize(462, 433))
        MainWindow.setMaximumSize(QtCore.QSize(462, 433))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.run = QtWidgets.QPushButton(self.centralwidget)
        self.run.setGeometry(QtCore.QRect(20, 310, 421, 71))
        self.run.setObjectName("run")
        self.click = QtWidgets.QLineEdit(self.centralwidget)
        self.click.setGeometry(QtCore.QRect(20, 240, 241, 51))
        self.click.setObjectName("click")
        self.speed = QtWidgets.QLineEdit(self.centralwidget)
        self.speed.setGeometry(QtCore.QRect(20, 140, 241, 51))
        self.speed.setObjectName("speed")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 100, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 200, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 20, 411, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.left = QtWidgets.QCheckBox(self.centralwidget) 
        self.left.setEnabled(True)
        self.left.setGeometry(QtCore.QRect(290, 110, 96, 19))
        self.left.setTabletTracking(False)
        self.left.setChecked(True)
        self.left.setObjectName("left")
        self.buttonGroup = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.left)
        self.right = QtWidgets.QCheckBox(self.centralwidget)
        self.right.setGeometry(QtCore.QRect(290, 130, 96, 19))
        self.right.setObjectName("right")
        self.buttonGroup.addButton(self.right)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(280, 80, 111, 81))
        self.groupBox.setObjectName("groupBox")
        self.click_button = QtWidgets.QPushButton(self.centralwidget)
        self.click_button.setGeometry(QtCore.QRect(280, 240, 161, 51))
        self.click_button.setObjectName("click_button")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(280, 160, 181, 71))
        self.label_4.setObjectName("label_4")
        self.groupBox.raise_()
        self.run.raise_()
        self.click.raise_()
        self.speed.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.left.raise_()
        self.right.raise_()
        self.click_button.raise_()
        self.label_4.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 462, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        
        

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.click_button.clicked.connect(self.button_click)
        self.run.clicked.connect(self.sp_cl_value)
        self.run.clicked.connect(self.click_checked)    
        self.run.clicked.connect(self.button_run)   

    def click_checked(self):
        if self.left.isChecked():
            self.diection = "left"
        elif self.right.isChecked():
            self.diection = "right"

    def button_click(self):
        while(True):
            if(keyboard.is_pressed('f3')):
                self.mouse_positon = pyautogui.position()
                break 
        
    def error_message(self, title, message):
        msgbox.showerror(title, message)

    def sp_cl_value(self):
        self.speeds = self.speed.text()
        self.clicks_ = self.click.text()        
        
    
    
    def button_run(self):
        try:
            count = 0
            if(self.clicks_=="" and self.speeds==""):
                    while(keyboard.is_pressed('f4')==False):
                        pyautogui.moveTo(self.mouse_positon)
                        pyautogui.click(button=self.diection)
                        
            elif(self.speeds==""):
                while(keyboard.is_pressed('f4')==False and not(count == int(self.clicks_))):
                    pyautogui.moveTo(self.mouse_positon)
                    pyautogui.click(button=self.diection)
                    count += 1
                    
            elif(self.clicks_==""):
                while(keyboard.is_pressed('f4')==False):
                    pyautogui.moveTo(self.mouse_positon)
                    pyautogui.click(interval=int(self.speeds),button=self.diection)
            else:
                while(keyboard.is_pressed('f4')==False and not(count == int(self.clicks_))):
                    pyautogui.moveTo(self.mouse_positon)
                    pyautogui.click(interval=int(self.speeds),button=self.diection)
                    count += 1
                
        except ValueError:
            self.error_message('Value Error','Please enter only integers')
            pass
        except AttributeError:
            self.error_message('Attribute Error','please mouse location specify')
            pass
        except OverflowError:
            self.error_message('Overflow Error','Please set it from 2,147,483,647~0')
            
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.run.setText(_translate("MainWindow", "run"))
        self.label.setText(_translate("MainWindow", "speed(second)"))
        self.label_2.setText(_translate("MainWindow", "click(tims)"))
        self.label_3.setText(_translate("MainWindow", "If textbox is clean value is default\n"
"shut down key f4"))
        self.left.setText(_translate("MainWindow", "left"))
        self.right.setText(_translate("MainWindow", "right"))
        self.groupBox.setTitle(_translate("MainWindow", "click direction"))
        self.click_button.setText(_translate("MainWindow", "click location"))
        self.label_4.setText(_translate("MainWindow", "press button and\n"
"you press f3\n"
"you mouse location\n"
"saved"))
            


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())