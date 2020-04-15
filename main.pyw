import sys
import sqlite3
from PyQt5.QtGui     import *
from PyQt5.QtCore    import *
from PyQt5.QtWidgets import *

conn = sqlite3.connect("database.db")
c = conn.cursor()

class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'PyQt5'
        self.left = 20
        self.top = 50
        self.width = 300
        self.height = 150
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        button_signin = QPushButton('Sign In', self)
        button_signin.move(100,30)
        button_signin.clicked.connect(self.signin)      

        button_signup = QPushButton('Sign Up', self)
        button_signup.move(100,80)
        button_signup.clicked.connect(self.signup)
        self.show()

    def signin(self):
        self.w = MainWindowsignin()
        self.w.show()
        self.hide()
    def signup(self):
        self.w = MainWindowsignup()
        self.w.show()
        self.hide()

class MainWindowsignin(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.setMinimumSize(QSize(330, 250))    
        self.setWindowTitle("Sign In") 

        self.emailLabel = QLabel(self)
        self.emailLabel.setText('<font size="4"> Email Id </font>')
        self.emailLabel.move(20, 20)
        
        self.line_email = QLineEdit(self)
        self.line_email.move(100, 20)
        self.line_email.resize(200, 32)

        self.passwordLabel = QLabel(self)
        self.passwordLabel.setText('<font size="4"> Password </font>')
        self.passwordLabel.move(20, 60)
        
        self.line_password = QLineEdit(self)
        self.line_password.move(100, 60)
        self.line_password.resize(200, 32)
        

        py1button = QPushButton('Sign In', self)
        py1button.clicked.connect(self.signin)
        py1button.resize(100,32)
        py1button.move(120, 110)

        self.Label = QLabel(self)
        self.Label.setText('Dont have an account?')
        self.Label.resize(300, 50)
        self.Label.move(110, 140)
        
        py2button = QPushButton('Sign Up', self)
        py2button.clicked.connect(self.signup)
        py2button.resize(100,32)
        py2button.move(120, 190)

        self.show()


    def signin(self):
        emailid = self.line_email.text()
        password = self.line_password.text()
        result = c.execute("SELECT * from users WHERE emailid= ? AND password= ?", (emailid, password))
        if(len(result.fetchall())>0):
            QMessageBox.information(QMessageBox(),'Successful','Login Successful.')
            self.w = MainWindow()
            self.w.show()
            self.hide()
                            
        else:
            QMessageBox.information(QMessageBox(),'Error','Login UnSuccessful.')

    def signup(self):
        self.w = MainWindowsignup()
        self.w.show()
        self.hide()
                                                                                              
class MainWindowsignup(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.setMinimumSize(QSize(330, 290))    
        self.setWindowTitle("Sign Up") 

        self.nameLabel = QLabel(self)
        self.nameLabel.setText('<font size="4"> Name </font>')
        self.nameLabel.move(20, 20)
        
        self.line_name = QLineEdit(self)
        self.line_name.move(100, 20)
        self.line_name.resize(200, 32)
        
        self.emailLabel = QLabel(self)
        self.emailLabel.setText('<font size="4"> Email Id </font>')
        self.emailLabel.move(20, 60)
        
        self.line_email = QLineEdit(self)
        self.line_email.move(100, 60)
        self.line_email.resize(200, 32)

        self.passwordLabel = QLabel(self)
        self.passwordLabel.setText('<font size="4"> Password </font>')
        self.passwordLabel.move(20, 100)
        
        self.line_password = QLineEdit(self)
        self.line_password.move(100, 100)
        self.line_password.resize(200, 32)
        

        pybutton = QPushButton('Sign Up', self)
        pybutton.clicked.connect(self.signup)
        pybutton.resize(100,32)
        pybutton.move(120, 150)

        self.Label = QLabel(self)
        self.Label.setText('Already have an account?')
        self.Label.resize(300, 50)
        self.Label.move(110, 180)
        
        py2button = QPushButton('Sign In', self)
        py2button.clicked.connect(self.signin)
        py2button.resize(100,32)
        py2button.move(120, 230)
    
        self.show()


    def signup(self):
        name = self.line_name.text()
        emailid = self.line_email.text()
        password = self.line_password.text()
        try:
            c.execute("INSERT INTO users (name,emailid,password) VALUES (?,?,?)",(name,emailid,password))
            conn.commit()
            QMessageBox.information(QMessageBox(),'Successful','Successfully Registered.')
            self.w = MainWindowsignin()
            self.w.show()
            self.hide()
        except Exception:
            QMessageBox.warning(QMessageBox(), 'Error', 'Registration Unsuccessful.')
            
    def signin(self):
            self.w = MainWindowsignin()
            self.w.show()
            self.hide()


class MainWindow(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.title = 'PyQt5'
        self.left = 20
        self.top = 50
        self.width = 640
        self.height = 400
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('File')
        editMenu = mainMenu.addMenu('Edit')
        viewMenu = mainMenu.addMenu('View')
        searchMenu = mainMenu.addMenu('Search')
        toolsMenu = mainMenu.addMenu('Tools')
        helpMenu = mainMenu.addMenu('Help')
        
        exitButton = QAction(QIcon('exit24.png'), 'Exit', self)
        exitButton.setShortcut('Ctrl+Q')
        exitButton.setStatusTip('Exit application')
        exitButton.triggered.connect(self.close)
        fileMenu.addAction(exitButton)
    
        self.show()
            
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())














		    
