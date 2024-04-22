from PyQt5.QtWidgets import QPushButton
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class RoundedButtonYellowSolid(QPushButton):
    def __init__(self, text, parent=None):
        super().__init__(text, parent) 
        self.setFixedSize(100, 40)
        self.setCursor(Qt.CursorShape.PointingHandCursor)
        
        
        self.setStyleSheet("""
            QPushButton {
                background-color: #F5A524;  /* Set your desired background color */
                color: black;  /* Set your desired text color */
                border-radius: 20%;  /* Make it round */
                font-family: "Arial";
                border: none;
                font-size: 16px;
            }
            QPushButton:hover {
                background-color: #F5A524;
                color: white;
            }
            QPushButton:pressed {
                color: white;
                background-color: #F5A524;
                
            }             
        """)
        
        
class RoundedButtonYellowBordered(QPushButton):
    def __init__(self, text, parent=None):
        super().__init__(text, parent) 
        self.setFixedSize(100, 40)
        self.setCursor(Qt.CursorShape.PointingHandCursor)
        
        
        self.setStyleSheet("""
            QPushButton {
                background-color: none;  /* Set your desired background color */
                color: #F5A524;  /* Set your desired text color */
                border-radius: 20%;  /* Make it round */
                font-family: "Arial";
                border: 2px solid #F5A524;
                font-size: 16px;
            }
           
            QPushButton:pressed {
                color: white;
                background-color: #F5A524;
                
            }             
        """)
        
        
class RoundedButtonYellowLight(QPushButton):
    def __init__(self, text, parent=None):
        super().__init__(text, parent) 
        self.setFixedSize(100, 40)
        self.setCursor(Qt.CursorShape.PointingHandCursor)
        
        
        self.setStyleSheet("""
            QPushButton {
                background-color: none;  /* Set your desired background color */
                color: #F5A524;  /* Set your desired text color */
                border-radius: 20%;  /* Make it round */
                font-family: "Arial";
                border: none;
                font-size: 16px;
            }
           
            QPushButton:pressed {
                color: white;
                background-color: #F5A524;
                
            }             
        """)
        