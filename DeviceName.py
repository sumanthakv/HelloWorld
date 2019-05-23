import sys
import subprocess
import time
import datetime
from auto_instr import *
from PyQt5 import QtCore, QtGui, uic, QtWidgets
qtCreatorFile = "DeviceName.ui" # Enter file here.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.run.clicked.connect(self.prog)
        self.refresh.clicked.connect(self.cleared)
        self.clearData.clicked.connect(self.clearAll)
    def dev_no(self):
        dev = str(self.DName.text())
        return dev
    def complete(self):
        com="completed"
        self.textBrowser.setText(com)
    def running(self):
        # com="    "
        self.textBrowser.clear()
    def cleared(self):
        MyApp.running(self)
    def clearAll(self):
        self.data_storing.clear()
    def prog(self):
        self.starttime.setText(str(datetime.datetime.now().time()))
        dev_no_input = MyApp.dev_no(self)
        # dev_no_input ='ss1'

        # curr_cmpl = (.02)
        # addr= gpib.addr(0,5)
        # volt_input=[2.7,3.3,5.5]
        # datalog.filename = 'text1'
        # datalog.header('Device', 'CC1_p1_2 voltage', 'current(mA)')
        # ke2400.on(addr)
        # ke2400.off(addr)
        # ke2400.forVmeasI(addr,3.3, curr_cmpl)
        # device=dev_no_input
        # device=device.upper()
        # for v in volt_input:
        #     read_current=ke2400.forVmeasI(addr, v, curr_cmpl)
        #     read_current=1000*read_current
        #     data = [str(device), v, float(read_current)]
        #     time.sleep(2)
        #     self.data_storing.append(str(device) + "\t" + str(v) + "\t" + str(read_current))
        #     # self.data_storing.setPlainText(str(device) + "\t" + str(v) + "\t" + str(read_current))
        #     print(data)
        #     datalog.data(data)
        # ke2400.off(addr)
        self.data_storing.append(str(dev_no_input))
        for scriptInstance in [1]:
            sys.stdout = open('resuslt%s.txt' % scriptInstance, 'a')
            sys.stdout.write(dev_no_input)
            subprocess.check_call(['python', 'Z:/py_lib/pythonfiles/device_load.py'], stdout=sys.stdout,stderr=subprocess.STDOUT)
            # sys.stdout.close()
        MyApp.complete(self)
        print("completed")
        self.Endtime.setText(str(datetime.datetime.now().time()))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    # dev_no_input =window.prog().dev_no_input
    sys.exit(app.exec_())

# app = QtWidgets.QApplication(sys.argv)
# window = MyApp()
# dev_no_input =window.prog().dev_no_input
# window.show()
# sys.exit(app.exec_())