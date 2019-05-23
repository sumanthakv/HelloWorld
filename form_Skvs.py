import sys
import csv
import sys,os
os.chdir("Z:\py_lib")

from PyQt5 import QtCore, QtGui, uic, QtWidgets
qtCreatorFile = "form_Skvs.ui" # Enter file here.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class datalog(object):

    def __init__(self,filename):
        self.filename = filename

    def data(var1):
        with open(datalog.filename + '.csv', 'a', newline='') as csvfile:
            mywriter1 = csv.writer(csvfile, delimiter=',', dialect='excel')
            mywriter1.writerow(var1)

    def header(var1, *var):
        with open(datalog.filename+ '.csv', 'a', newline='') as csvfile:
            mywriter2 = csv.DictWriter(csvfile, dialect='excel', fieldnames=[var1, *var])
            mywriter2.writeheader()

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.submit.clicked.connect(self.prog)
        self.age.setMaximum(50)
        self.age.setMinimum(15)
        self.dob.displayFormat()

    
    def Name(self):
        cname=str(self.name1.text())
        return cname
    def faname(self):
       fname=str(self.fname.text())
       return fname
    def Age(self):
        cage=str(self.age.value())
        return cage
    def prog(self):
        Cname=MyApp.Name(self)
        Fname=MyApp.faname(self)
        print(Cname)
        print(Fname)
        A=MyApp.Age(self)
        print(A)
        P=MyApp.phone(self)
        print(P)
        D=MyApp.dateOfBir(self)
        print(D)
        PL=MyApp.pla(self)
        print(PL)
        TL = MyApp.taluk(self)
        print(TL)
        DS=MyApp.Dist(self)
        print(DS)
        pincode=MyApp.PIN(self)
        print(pincode)
        os.chdir("Z:\py_lib")
        datalog.filename="form_dta"
        # datalog.header('CandidateName', 'Father name', 'Age', "DOB", "phonenumber", "place",'taluk','dist','pioncode')
        x = [Cname,Fname,A,D,P,PL,TL,DS,pincode]
        datalog.data(x)
    def phone(self):
        num=str(self.phno.text())
        return num
    def dateOfBir(self):
        DOB=(self.dob.date())
        d=[]
        temp=(DOB.toPyDate())
        d.append(temp)
        print(type(temp))
        return temp
    def pla(self):
        P=str(self.place.text())
        return P
    def taluk(self):
        T=str(self.Taluk.text())
        return T
    def Dist(self):
        D=str(self.distict.text())
        return D
    def PIN(self):
        Pi=str(self.pin.text())
        return Pi

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
