import sys
import keyboard
import pyautogui
from PyQt5.QtWidgets import *
from PyQt5 import uic
import tkinter.messagebox as msgbox

form_class = uic.loadUiType("uiui.ui")[0]

pyautogui.FAILSAFE = False

global diection
global speeds
global clicks_
global count
global mouse_positon



class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.click_button.clicked.connect(self.button_click)
        self.run.clicked.connect(self.speed_text)
        self.run.clicked.connect(self.clicks_text)
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

    def speed_text(self):
        self.speeds = self.speed.text()
        
    def clicks_text(self):
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
            

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()