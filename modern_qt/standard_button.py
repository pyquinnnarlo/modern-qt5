# pyqt5_round_button/roundbutton.py

from PyQt5.QtWidgets import QPushButton
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class RoundButtonPrimary(QPushButton):
    def __init__(self, text, parent=None):
        super().__init__(text, parent)
        self.setFixedSize(100, 45)  # Set your desired size for the button
        self.setCursor(Qt.CursorShape.PointingHandCursor)

        self.setStyleSheet("""
            QPushButton {
                background-color: #0070F0;  /* Set your desired background color */
                color: #ffffff;  /* Set your desired text color */
                border-radius: 10%;  /* Make it round */
                font-family: "Arial";
                font-size: 15px;
            }
            QPushButton:hover {
                background-color: #2980b9;  /* Hover color */
            }
        """)


class RoundButtonGray(QPushButton):
    def __init__(self, text, parent=None):
        super().__init__(text, parent)
        self.setFixedSize(100, 45)  # Set your desired size for the button
        self.setCursor(Qt.CursorShape.PointingHandCursor)

        self.setStyleSheet("""
            QPushButton {
                background-color: #3F3F46;  /* Set your desired background color */
                color: #ffffff;  /* Set your desired text color */
                border-radius: 10%;  /* Make it round */
                font-family: "Arial";
                font-size: 15px;
            }
            QPushButton:hover {
                background-color: #575749;  /* Hover color */
            }
        """)



class RoundButtonSecondary(QPushButton):
    def __init__(self, text, parent=None):
        super().__init__(text, parent)
        self.setFixedSize(100, 45)  # Set your desired size for the button
        self.setCursor(Qt.CursorShape.PointingHandCursor)

        self.setStyleSheet("""
            QPushButton {
                background-color: #9455D3;  /* Set your desired background color */
                color: #ffffff;  /* Set your desired text color */
                border-radius: 10%;  /* Make it round */
                font-family: "Arial";
                font-size: 15px;
            }
            QPushButton:hover {
                background-color: #a45fea;  /* Hover color */
            }
        """)
        
class RoundedButtonSuccess(QPushButton):
    def __init__(self, text, parent=None):
        super().__init__(text, parent) 
        self.setFixedSize(100, 45)
        self.setCursor(Qt.CursorShape.PointingHandCursor)
        
        self.setStyleSheet("""
            QPushButton {
                background-color: #18C964;  /* Set your desired background color */
                color: #ffffff;  /* Set your desired text color */
                border-radius: 10%;  /* Make it round */
                font-family: "Arial";
                font-size: 15px;
            }
            QPushButton:hover {
                background-color: #1ce372;  /* Hover color */
            }
                           
        """)
        
        
        
class RoundedButtonWarning(QPushButton):
    def __init__(self, text, parent=None):
        super().__init__(text, parent) 
        self.setFixedSize(100, 45)
        self.setCursor(Qt.CursorShape.PointingHandCursor)
        
        self.setStyleSheet("""
            QPushButton {
                background-color: #F5A524;  /* Set your desired background color */
                color: #ffffff;  /* Set your desired text color */
                border-radius: 10%;  /* Make it round */
                font-family: "Arial";
                font-size: 15px;
            }
            QPushButton:hover {
                background-color: #ff9f05;  /* Hover color */
                
            }
                           
        """)


from PyQt5.QtWidgets import *

class RoundedButtonDanger(QPushButton):
    def __init__(self, text, parent=None):
        super().__init__(text, parent) 
        self.setFixedSize(100, 45)
        self.setCursor(Qt.CursorShape.PointingHandCursor)
        
        
        self.setStyleSheet("""
            QPushButton {
                background-color: #F31260;  /* Set your desired background color */
                color: #ffffff;  /* Set your desired text color */
                border-radius: 10%;  /* Make it round */
                font-family: "Arial";
                font-size: 15px;
            }
            QPushButton:hover {
                background-color: #ff357b;  /* Hover color */
                
            }
                           
        """)
        
        
class RoundedButtonFaded(QPushButton):
    def __init__(self, text, parent=None):
        super().__init__(text, parent) 
        self.setFixedSize(100, 45)
        self.setCursor(Qt.CursorShape.PointingHandCursor)
        
        
        self.setStyleSheet("""
            QPushButton {
                background-color: #27272A;  /* Set your desired background color */
                color: #0070F0;  /* Set your desired text color */
                border-radius: 10%;  /* Make it round */
                font-family: "Arial";
                border: 1px solid #1c1c1c;
                font-size: 15px;
            }
            QPushButton:hover {
                background-color: #2f2f30;  /* Hover color */
                
            }
                           
        """)
        
        
class RoundedButtonBordered(QPushButton):
    def __init__(self, text, parent=None):
        super().__init__(text, parent) 
        self.setFixedSize(100, 45)
        self.setCursor(Qt.CursorShape.PointingHandCursor)
        
        
        self.setStyleSheet("""
            QPushButton {
                background-color: none;  /* Set your desired background color */
                color: #0070F0;  /* Set your desired text color */
                border-radius: 10%;  /* Make it round */
                font-family: "Arial";
                border: 1px solid #0070F0;
                font-size: 15px;
            }
            QPushButton:pressed {
                color: white;
                background-color: #0070F0;
                
            }             
        """)
        
        
class RoundedButtonLight(QPushButton):
    def __init__(self, text, parent=None):
        super().__init__(text, parent) 
        self.setFixedSize(100, 45)
        self.setCursor(Qt.CursorShape.PointingHandCursor)
        
        
        self.setStyleSheet("""
            QPushButton {
                background-color: none;  /* Set your desired background color */
                color: #0070F0;  /* Set your desired text color */
                border-radius: 10%;  /* Make it round */
                font-family: "Arial";
                border: none;
                font-size: 15px;
            }
            QPushButton:hover {
                background-color: #4d9efa;
                color: white;
            }
            QPushButton:pressed {
                color: white;
                background-color: #0070F0;
                
            }             
        """)
        
        

        

        
        
# class RoundedButtonShadow(QPushButton):
#     def __init__(self, text, parent=None):
#         super().__init__(text, parent) 
#         self.setFixedSize(100, 45)
#         self.setCursor(Qt.CursorShape.PointingHandCursor)
        
        
#         self.setStyleSheet("""
#             QPushButton {
#                 background-color: none;  /* Set your desired background color */
#                 color: #0070F0;  /* Set your desired text color */
#                 border-radius: 10%;  /* Make it round */
#                 font-family: "Arial";
#                 border: none;
#                 font-size: 15px;
#                 box-shadow: 2px 2px 2px #4d9efa;
#             }
#             QPushButton:hover {
#                 background-color: #4d9efa;
#                 color: white;
#             }
#             QPushButton:pressed {
#                 color: white;
#                 background-color: #0070F0;
                
#             }             
#         """)