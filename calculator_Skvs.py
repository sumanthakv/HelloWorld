import sys
from time import sleep
from PyQt5 import QtCore, QtGui, uic, QtWidgets
qtCreatorFile = "calci.ui" # Enter file here.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        # self.close.clicked.connect(self.closee)
        self.one.clicked.connect(self.lcd1)
        self.two.clicked.connect(self.lcd2)
        self.three.clicked.connect(self.lcd3)
        # self.four.clicked.connect(self.lcd4)
        # self.five.clicked.connect(self.lcd5)
        # self.six.clicked.connect(self.lcd6)
        # self.seven.clicked.connect(self.lcd7)
        # self.eight.clicked.connect(self.lcd8)
        # self.nine.clicked.connect(self.lcd9)
        # self.zero.clicked.connect(self.lcd0)
        self.add.clicked.connect(self.lcd_plus)
        # self.enter.clicked.connect(self.display_results)

        # self.two.clicked.connect(self.lcd2)

    def lcd1(self):
        self.lcdNumber.display(1)
        a=1
        print(a)
        return a

    def lcd2(self):
        self.lcdNumber.display(2)
        b=2
        print(b)
        return b

    def lcd3(self):
        self.lcdNumber.display(3)
        c = 3
        print(c)
        return c

    def lcd_plus(self):

        a=MyApp.lcd1(self)
        b=MyApp.lcd2(self)
        c=MyApp.lcd3(self)
        add=a+b+c
        self.enter.clicked.connect(self.display_results)

        # plus="+"
        # print(plus)
        self.lcdNumber.display("plus")
        a,b,c = 0,0,0
        print("++++++++++++++++++++++++++++")
        print(a)
        print(b)
        return add

    def display_results(self):
        sum=MyApp.lcd_plus(self)
        self.lcdNumber.display(sum)
        # sum=0
        return sum
    def prog(self):
       print( MyApp.num_1(self))
       MyApp.lcd()
       MyApp.close.clicked.close()
    def closee(self):
        self.enter.close()
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())