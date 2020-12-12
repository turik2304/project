from PySide import QtGui, QtCore
from diploma import Ui_Form
from numpy import exp
import sys
import vacuum_system
import time
import calculating_pressure
import core

fl_but = "off"
v1_but = "off"
v2_but = "off"
v3_but = "off"
tm_but = "off"


class MainWindow(QtGui.QMainWindow, Ui_Form):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.P = [100000]
        self.time = 0
        self.time02 = 0
        self.time_interval = 100
        self.p0 = 100000
        self.p02 = 133
        self.p_cur = self.p0

        self.setupUi(self)
        self.time_label1.setText(str(0))
        self.time_label2.setText(str(0))
        self.pressure_value.setText(str(self.p0))
        self.show()
        # instantiation the vacuum system
        self.vac_system = vacuum_system.VacuumSystem(self.p0)

    def Enable_fl_pump(self):
        global fl_but
        if fl_but == "off":
            fl_but = "on"
            self.Timer_on()
        else:
            fl_but = "off"
            self.Timer_on()

    def Enable_tm_pump(self):
        global tm_but
        if tm_but == "off":
            tm_but = "on"
            self.Timer_on()
        else:
            tm_but = "off"
            self.Timer_on()

    def Enable_valve_1(self):
        global v1_but
        if v1_but == "off":
            v1_but = "on"
            self.Timer_on()
        else:
            v1_but = "off"
            self.Timer_on()

    def Enable_valve_2(self):
        global v2_but
        if v2_but == "off":
            v2_but = "on"
            self.Timer_on()
        else:
            v2_but = "off"
            self.Timer_on()

    def Enable_valve_3(self):
        global v3_but
        if v3_but == "off":
            v3_but = "on"
            self.Timer_on()
        else:
            v3_but = "off"
            self.Timer_on()

    def Timer_on(self):
        self.TimerUp = QtCore.QTimer()  # do not move to __init__
        if fl_but == "on" and v3_but == "on":
            self.TimerUp.start()
            self.TimerUp.setInterval(self.time_interval)
            self.TimerUp.timeout.connect(self.updateTime)

        elif fl_but == "on" and tm_but == "on" and v2_but == "on" and v1_but == "on" and v3_but == "off":
            self.TimerUp.start()
            self.TimerUp.setInterval(self.time_interval)
            self.TimerUp.timeout.connect(self.updateTime2)

        elif fl_but == "on" and v3_but == "off" and v2_but == "off":
            self.TimerUp.stop()
            self.p02 = self.p_cur

        else:
            self.TimerUp.stop()

    def updateTime(self):
        self.time += 1
        self.p_cur = self.vac_system.pump.start_pump(self.time, self.p0)
        self.P.append(self.p_cur)
        print self.P
        self.pressure_value.setText(str(round(self.p_cur, 2)))
        self.time_label1.setText(str(self.time))

    def updateTime2(self):
        self.time02 += 1
        self.p_cur = self.vac_system.pump2.start_pump(self.time02, self.p02)
        self.P.append(self.p_cur)
        print self.P
        self.pressure_value.setText(str(round(self.p_cur, 5)))
        self.time_label2.setText(str(self.time02))




if __name__ == "__main__":
    # create app
    app = QtGui.QApplication(sys.argv)

    # create form and init UI
    ui = MainWindow()

    # logic

    #ui.Enable.clicked.connect()
    ui.fl_pump.clicked.connect(ui.Enable_fl_pump)
    ui.valve3.clicked.connect(ui.Enable_valve_3)
    ui.valve2.clicked.connect(ui.Enable_valve_2)
    ui.valve1.clicked.connect(ui.Enable_valve_1)
    ui.tm_pump.clicked.connect(ui.Enable_tm_pump)

    # run app
    sys.exit(app.exec_())