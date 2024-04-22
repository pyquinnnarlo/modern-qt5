from PyQt5.QtWidgets import QCommandLinkButton
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class ClickableCardPrimaryButton(QCommandLinkButton):
    def __init__(self, header, text, width=400, height=75, parent=None):
        super().__init__(header, text, parent, width=400, height=75)
        self.setFixedSize(width, height)
        self.setCursor(Qt.CursorShape.PointingHandCursor)
        
        self.setStyleSheet("""
            QCommandLinkButton {
                background-color: #0070F0;  /* Set your desired background color */
                color: #ffffff;  /* Set your desired text color */
                border-radius: 10%;  /* Make it round */
                font-family: "Arial";
                font-size: 18px;
         
            }
            QCommandLinkButton:hover {
                background-color: #2980b9;  /* Hover color */
            }
        """)
        
        
class ClickableCardGrayButton(QCommandLinkButton):
    def __init__(self, header, text, width=400, height=75, parent=None):
        super().__init__(header, text, parent, width=400, height=75)
        self.setFixedSize(width, height)  # Set your desired size for the button
        self.setCursor(Qt.CursorShape.PointingHandCursor)

        self.setStyleSheet("""
            QCommandLinkButton {
                background-color: #3F3F46;  /* Set your desired background color */
                color: #ffffff;  /* Set your desired text color */
                border-radius: 10%;  /* Make it round */
                font-family: "Arial";
                font-size: 18px;
            }
            QCommandLinkButton:hover {
                background-color: #323238;  /* Hover color */
            }
        """)    
        
        
class ClickableCardSecondaryButton(QCommandLinkButton):
    def __init__(self, header, text, width=400, height=75, parent=None):
        super().__init__(header, text, parent, width=400, height=75)
        self.setFixedSize(width, height)  # Set your desired size for the button
        self.setCursor(Qt.CursorShape.PointingHandCursor)

        self.setStyleSheet("""
            QCommandLinkButton {
                background-color: #9455D3;  /* Set your desired background color */
                color: #ffffff;  /* Set your desired text color */
                border-radius: 10%;  /* Make it round */
                font-family: "Arial";
                font-size: 18px;
            }
            QCommandLinkButton:hover {
                background-color: #a25ee7;  /* Hover color */
            }
        """)   
        

class ClickableCardSuccessButton(QCommandLinkButton):
    def __init__(self, header, text, width=400, height=75, parent=None):
        super().__init__(header, text, parent, width=400, height=75)
        self.setFixedSize(width, height)  # Set your desired size for the button
        self.setCursor(Qt.CursorShape.PointingHandCursor)

        self.setStyleSheet("""
            QCommandLinkButton {
                background-color: #18C964;  /* Set your desired background color */
                color: #ffffff;  /* Set your desired text color */
                border-radius: 10%;  /* Make it round */
                font-family: "Arial";
                font-size: 18px;
            }
            QCommandLinkButton:hover {
                background-color: #18C964;  /* Hover color */
            }
        """)  
        
        
class ClickableCardWarningButton(QCommandLinkButton):
    def __init__(self, header, text, width=400, height=75, parent=None):
        super().__init__(header, text, parent, width=400, height=75)
        self.setFixedSize(width, height)  # Set your desired size for the button
        self.setCursor(Qt.CursorShape.PointingHandCursor)

        self.setStyleSheet("""
            QCommandLinkButton {
                background-color: #F5A524;  /* Set your desired background color */
                color: #ffffff;  /* Set your desired text color */
                border-radius: 10%;  /* Make it round */
                font-family: "Arial";
                font-size: 18px;
            }
            QCommandLinkButton:hover {
                background-color: #ff9f05;  /* Hover color */
            }
        """) 
        
        
class ClickableCardDangerButton(QCommandLinkButton):
    def __init__(self, header, text, width=400, height=75, parent=None):
        super().__init__(header, text, parent, width=400, height=75)
        self.setFixedSize(width, height)  # Set your desired size for the button
        self.setCursor(Qt.CursorShape.PointingHandCursor)

        self.setStyleSheet("""
            QCommandLinkButton {
                background-color: #F31260;  /* Set your desired background color */
                color: #ffffff;  /* Set your desired text color */
                border-radius: 10%;  /* Make it round */
                font-family: "Arial";
                font-size: 18px;
            }
            QCommandLinkButton:hover {
                background-color: #ff357b;  /* Hover color */
            }
        """) 
        
        
class ClickableCardFadedButton(QCommandLinkButton):
    def __init__(self, header, text, width=400, height=75, parent=None):
        super().__init__(header, text, parent, width=400, height=75)
        self.setFixedSize(width, height)  # Set your desired size for the button
        self.setCursor(Qt.CursorShape.PointingHandCursor)

        self.setStyleSheet("""
            QCommandLinkButton {
                background-color: #27272A;  /* Set your desired background color */
                color: #ffffff;  /* Set your desired text color */
                border-radius: 10%;  /* Make it round */
                font-family: "Arial";
                font-size: 18px;
            }
            QCommandLinkButton:hover {
                background-color: #2f2f30;  /* Hover color */
            }
        """) 
        
        
class ClickableCardBorderedButton(QCommandLinkButton):
    def __init__(self, header, text, width=400, height=75, parent=None):
        super().__init__(header, text, parent, width=400, height=75)
        self.setFixedSize(width, height)  # Set your desired size for the button
        self.setCursor(Qt.CursorShape.PointingHandCursor)

        self.setStyleSheet("""
            QCommandLinkButton {
                background-color: none;  /* Set your desired background color */
                color: #0070F0;  /* Set your desired text color */
                border-radius: 10%;  /* Make it round */
                font-family: "Arial";
                border: 1px solid #0070F0;
                font-size: 18px;
            }
          
        """) 
        
        
class ClickableCardLightButton(QCommandLinkButton):
    def __init__(self, header, text, width=400, height=75, parent=None):
        super().__init__(header, text, parent, width=400, height=75)
        self.setFixedSize(width, height)  # Set your desired size for the button
        self.setCursor(Qt.CursorShape.PointingHandCursor)

        self.setStyleSheet("""
            QCommandLinkButton {
                background-color: none;  /* Set your desired background color */
                color: #0070F0;  /* Set your desired text color */
                border-radius: 10%;  /* Make it round */
                font-family: "Arial";
                border: none;
                font-size: 18px;
            }
        
            QCommandLinkButton:pressed {
                color: white;
                background-color: #bbdbff;
                
            }
          
        """) 
        
        



