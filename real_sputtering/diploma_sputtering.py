# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'diploma_sputtering.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1165, 706)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setStyleSheet("QWidget {\n"
"    background-color: rgb(200, 255, 255);\n"
"}\n"
"\n"
".QDial, .QPushButton {\n"
"    background-color: rgb(204, 204, 204);\n"
"}\n"
"\n"
".QLabel {\n"
"    background-color: rgb(226, 226, 226)\n"
"}\n"
"\n"
".QDoubleSpinBox, .QLineEdit {\n"
"    background-color: white\n"
"}")
        self.vacuum_chamber = QtWidgets.QLabel(Form)
        self.vacuum_chamber.setGeometry(QtCore.QRect(30, 20, 681, 181))
        self.vacuum_chamber.setStyleSheet("")
        self.vacuum_chamber.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.vacuum_chamber.setText("")
        self.vacuum_chamber.setObjectName("vacuum_chamber")
        self.tube_v1_chamber = QtWidgets.QLabel(Form)
        self.tube_v1_chamber.setGeometry(QtCore.QRect(50, 200, 71, 111))
        self.tube_v1_chamber.setText("")
        self.tube_v1_chamber.setObjectName("tube_v1_chamber")
        self.valve1 = QtWidgets.QPushButton(Form)
        self.valve1.setEnabled(False)
        self.valve1.setGeometry(QtCore.QRect(50, 310, 71, 81))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.valve1.setFont(font)
        self.valve1.setObjectName("valve1")
        self.tube_tm_v1 = QtWidgets.QLabel(Form)
        self.tube_tm_v1.setGeometry(QtCore.QRect(50, 390, 71, 111))
        self.tube_tm_v1.setText("")
        self.tube_tm_v1.setObjectName("tube_tm_v1")
        self.tm_pump = QtWidgets.QPushButton(Form)
        self.tm_pump.setEnabled(False)
        self.tm_pump.setGeometry(QtCore.QRect(10, 500, 151, 161))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.tm_pump.setFont(font)
        self.tm_pump.setObjectName("tm_pump")
        self.tube_v2_tm = QtWidgets.QLabel(Form)
        self.tube_v2_tm.setGeometry(QtCore.QRect(160, 540, 171, 81))
        self.tube_v2_tm.setText("")
        self.tube_v2_tm.setObjectName("tube_v2_tm")
        self.valve2 = QtWidgets.QPushButton(Form)
        self.valve2.setEnabled(False)
        self.valve2.setGeometry(QtCore.QRect(330, 540, 71, 81))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.valve2.setFont(font)
        self.valve2.setObjectName("valve2")
        self.tube_fl_v2 = QtWidgets.QLabel(Form)
        self.tube_fl_v2.setGeometry(QtCore.QRect(400, 540, 181, 81))
        self.tube_fl_v2.setText("")
        self.tube_fl_v2.setObjectName("tube_fl_v2")
        self.fl_pump = QtWidgets.QPushButton(Form)
        self.fl_pump.setEnabled(False)
        self.fl_pump.setGeometry(QtCore.QRect(580, 500, 151, 161))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.fl_pump.setFont(font)
        self.fl_pump.setObjectName("fl_pump")
        self.tube_fl_v3 = QtWidgets.QLabel(Form)
        self.tube_fl_v3.setGeometry(QtCore.QRect(620, 390, 71, 111))
        self.tube_fl_v3.setText("")
        self.tube_fl_v3.setObjectName("tube_fl_v3")
        self.valve3 = QtWidgets.QPushButton(Form)
        self.valve3.setEnabled(False)
        self.valve3.setGeometry(QtCore.QRect(620, 310, 71, 81))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.valve3.setFont(font)
        self.valve3.setObjectName("valve3")
        self.tube_v3_chamber = QtWidgets.QLabel(Form)
        self.tube_v3_chamber.setGeometry(QtCore.QRect(620, 200, 71, 111))
        self.tube_v3_chamber.setText("")
        self.tube_v3_chamber.setObjectName("tube_v3_chamber")
        self.Enable = QtWidgets.QPushButton(Form)
        self.Enable.setEnabled(False)
        self.Enable.setGeometry(QtCore.QRect(890, 0, 251, 81))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Enable.setFont(font)
        self.Enable.setObjectName("Enable")
        self.air_tube = QtWidgets.QLabel(Form)
        self.air_tube.setGeometry(QtCore.QRect(710, 20, 71, 21))
        self.air_tube.setText("")
        self.air_tube.setObjectName("air_tube")
        self.spinbox_l_fl = QtWidgets.QDoubleSpinBox(Form)
        self.spinbox_l_fl.setGeometry(QtCore.QRect(500, 440, 62, 22))
        self.spinbox_l_fl.setMinimum(0.01)
        self.spinbox_l_fl.setMaximum(30.0)
        self.spinbox_l_fl.setSingleStep(0.01)
        self.spinbox_l_fl.setProperty("value", 0.08)
        self.spinbox_l_fl.setObjectName("spinbox_l_fl")
        self.spinbox_d_fl = QtWidgets.QDoubleSpinBox(Form)
        self.spinbox_d_fl.setGeometry(QtCore.QRect(500, 470, 62, 22))
        self.spinbox_d_fl.setMinimum(0.01)
        self.spinbox_d_fl.setMaximum(10.0)
        self.spinbox_d_fl.setSingleStep(0.01)
        self.spinbox_d_fl.setProperty("value", 0.04)
        self.spinbox_d_fl.setObjectName("spinbox_d_fl")
        self.spinbox_l_tm = QtWidgets.QDoubleSpinBox(Form)
        self.spinbox_l_tm.setGeometry(QtCore.QRect(180, 440, 62, 22))
        self.spinbox_l_tm.setMinimum(0.01)
        self.spinbox_l_tm.setMaximum(30.0)
        self.spinbox_l_tm.setSingleStep(0.01)
        self.spinbox_l_tm.setProperty("value", 0.3)
        self.spinbox_l_tm.setObjectName("spinbox_l_tm")
        self.spinbox_d_tm = QtWidgets.QDoubleSpinBox(Form)
        self.spinbox_d_tm.setGeometry(QtCore.QRect(180, 470, 62, 22))
        self.spinbox_d_tm.setMinimum(0.01)
        self.spinbox_d_tm.setMaximum(10.0)
        self.spinbox_d_tm.setSingleStep(0.01)
        self.spinbox_d_tm.setProperty("value", 0.5)
        self.spinbox_d_tm.setObjectName("spinbox_d_tm")
        self.l_tm = QtWidgets.QLabel(Form)
        self.l_tm.setGeometry(QtCore.QRect(130, 440, 41, 16))
        self.l_tm.setAlignment(QtCore.Qt.AlignCenter)
        self.l_tm.setObjectName("l_tm")
        self.d_tm = QtWidgets.QLabel(Form)
        self.d_tm.setGeometry(QtCore.QRect(130, 470, 41, 16))
        self.d_tm.setAlignment(QtCore.Qt.AlignCenter)
        self.d_tm.setObjectName("d_tm")
        self.d_fl = QtWidgets.QLabel(Form)
        self.d_fl.setGeometry(QtCore.QRect(570, 470, 41, 16))
        self.d_fl.setAlignment(QtCore.Qt.AlignCenter)
        self.d_fl.setObjectName("d_fl")
        self.l_fl = QtWidgets.QLabel(Form)
        self.l_fl.setGeometry(QtCore.QRect(570, 440, 41, 16))
        self.l_fl.setAlignment(QtCore.Qt.AlignCenter)
        self.l_fl.setObjectName("l_fl")
        self.t1 = QtWidgets.QLabel(Form)
        self.t1.setGeometry(QtCore.QRect(890, 390, 41, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.t1.setFont(font)
        self.t1.setAlignment(QtCore.Qt.AlignCenter)
        self.t1.setObjectName("t1")
        self.t2 = QtWidgets.QLabel(Form)
        self.t2.setGeometry(QtCore.QRect(890, 440, 41, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.t2.setFont(font)
        self.t2.setAlignment(QtCore.Qt.AlignCenter)
        self.t2.setObjectName("t2")
        self.time_rewind = QtWidgets.QLabel(Form)
        self.time_rewind.setGeometry(QtCore.QRect(890, 540, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.time_rewind.setFont(font)
        self.time_rewind.setAlignment(QtCore.Qt.AlignCenter)
        self.time_rewind.setObjectName("time_rewind")
        self.p = QtWidgets.QLabel(Form)
        self.p.setGeometry(QtCore.QRect(890, 490, 41, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.p.setFont(font)
        self.p.setAlignment(QtCore.Qt.AlignCenter)
        self.p.setObjectName("p")
        self.timeSlider = QtWidgets.QSlider(Form)
        self.timeSlider.setGeometry(QtCore.QRect(890, 600, 241, 31))
        self.timeSlider.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.timeSlider.setMouseTracking(False)
        self.timeSlider.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.timeSlider.setMinimum(1)
        self.timeSlider.setMaximum(200)
        self.timeSlider.setSingleStep(1)
        self.timeSlider.setProperty("value", 100)
        self.timeSlider.setSliderPosition(100)
        self.timeSlider.setTracking(True)
        self.timeSlider.setOrientation(QtCore.Qt.Horizontal)
        self.timeSlider.setInvertedAppearance(False)
        self.timeSlider.setInvertedControls(False)
        self.timeSlider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.timeSlider.setTickInterval(50)
        self.timeSlider.setObjectName("timeSlider")
        self.readiness = QtWidgets.QLineEdit(Form)
        self.readiness.setGeometry(QtCore.QRect(170, 500, 21, 22))
        self.readiness.setStyleSheet("background-color: red;")
        self.readiness.setText("")
        self.readiness.setFrame(True)
        self.readiness.setObjectName("readiness")
        self.spinbox_Qin2 = QtWidgets.QDoubleSpinBox(Form)
        self.spinbox_Qin2.setGeometry(QtCore.QRect(180, 410, 81, 22))
        self.spinbox_Qin2.setDecimals(5)
        self.spinbox_Qin2.setMinimum(1e-05)
        self.spinbox_Qin2.setMaximum(10.0)
        self.spinbox_Qin2.setSingleStep(1e-05)
        self.spinbox_Qin2.setProperty("value", 1e-05)
        self.spinbox_Qin2.setObjectName("spinbox_Qin2")
        self.spinbox_Qin1 = QtWidgets.QDoubleSpinBox(Form)
        self.spinbox_Qin1.setGeometry(QtCore.QRect(491, 410, 71, 22))
        self.spinbox_Qin1.setDecimals(4)
        self.spinbox_Qin1.setMinimum(0.0001)
        self.spinbox_Qin1.setMaximum(2000.0)
        self.spinbox_Qin1.setSingleStep(0.0001)
        self.spinbox_Qin1.setProperty("value", 0.5)
        self.spinbox_Qin1.setObjectName("spinbox_Qin1")
        self.spinbox_V = QtWidgets.QDoubleSpinBox(Form)
        self.spinbox_V.setGeometry(QtCore.QRect(540, 210, 62, 22))
        self.spinbox_V.setMinimum(0.01)
        self.spinbox_V.setMaximum(100.0)
        self.spinbox_V.setSingleStep(0.01)
        self.spinbox_V.setProperty("value", 0.04)
        self.spinbox_V.setObjectName("spinbox_V")
        self.Q_tm = QtWidgets.QLabel(Form)
        self.Q_tm.setGeometry(QtCore.QRect(130, 410, 41, 16))
        self.Q_tm.setAlignment(QtCore.Qt.AlignCenter)
        self.Q_tm.setObjectName("Q_tm")
        self.Q_fl = QtWidgets.QLabel(Form)
        self.Q_fl.setGeometry(QtCore.QRect(570, 410, 41, 16))
        self.Q_fl.setAlignment(QtCore.Qt.AlignCenter)
        self.Q_fl.setObjectName("Q_fl")
        self.V_chamber = QtWidgets.QLabel(Form)
        self.V_chamber.setGeometry(QtCore.QRect(500, 210, 31, 21))
        self.V_chamber.setAlignment(QtCore.Qt.AlignCenter)
        self.V_chamber.setObjectName("V_chamber")
        self.spinbox_S1 = QtWidgets.QDoubleSpinBox(Form)
        self.spinbox_S1.setGeometry(QtCore.QRect(500, 380, 62, 22))
        self.spinbox_S1.setDecimals(4)
        self.spinbox_S1.setMinimum(0.0001)
        self.spinbox_S1.setMaximum(10.0)
        self.spinbox_S1.setSingleStep(0.0001)
        self.spinbox_S1.setProperty("value", 0.005)
        self.spinbox_S1.setObjectName("spinbox_S1")
        self.S_tm = QtWidgets.QLabel(Form)
        self.S_tm.setGeometry(QtCore.QRect(130, 380, 41, 16))
        self.S_tm.setAlignment(QtCore.Qt.AlignCenter)
        self.S_tm.setObjectName("S_tm")
        self.spinbox_S2 = QtWidgets.QDoubleSpinBox(Form)
        self.spinbox_S2.setGeometry(QtCore.QRect(180, 380, 61, 22))
        self.spinbox_S2.setDecimals(4)
        self.spinbox_S2.setMinimum(0.0001)
        self.spinbox_S2.setMaximum(10.0)
        self.spinbox_S2.setSingleStep(0.0001)
        self.spinbox_S2.setProperty("value", 0.09)
        self.spinbox_S2.setObjectName("spinbox_S2")
        self.S_fl = QtWidgets.QLabel(Form)
        self.S_fl.setGeometry(QtCore.QRect(570, 380, 41, 16))
        self.S_fl.setAlignment(QtCore.Qt.AlignCenter)
        self.S_fl.setObjectName("S_fl")
        self.x1 = QtWidgets.QLabel(Form)
        self.x1.setGeometry(QtCore.QRect(990, 640, 41, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.x1.setFont(font)
        self.x1.setAlignment(QtCore.Qt.AlignCenter)
        self.x1.setObjectName("x1")
        self.x100 = QtWidgets.QLabel(Form)
        self.x100.setGeometry(QtCore.QRect(880, 640, 41, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.x100.setFont(font)
        self.x100.setAlignment(QtCore.Qt.AlignCenter)
        self.x100.setObjectName("x100")
        self.x0_5 = QtWidgets.QLabel(Form)
        self.x0_5.setGeometry(QtCore.QRect(1100, 640, 41, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.x0_5.setFont(font)
        self.x0_5.setAlignment(QtCore.Qt.AlignCenter)
        self.x0_5.setObjectName("x0_5")
        self.overflow = QtWidgets.QPushButton(Form)
        self.overflow.setEnabled(False)
        self.overflow.setGeometry(QtCore.QRect(780, 10, 51, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.overflow.setFont(font)
        self.overflow.setObjectName("overflow")
        self.status = QtWidgets.QLabel(Form)
        self.status.setGeometry(QtCore.QRect(260, 210, 211, 111))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.status.setFont(font)
        self.status.setStyleSheet("background-color: white;")
        self.status.setFrameShape(QtWidgets.QFrame.Box)
        self.status.setTextFormat(QtCore.Qt.AutoText)
        self.status.setAlignment(QtCore.Qt.AlignCenter)
        self.status.setWordWrap(True)
        self.status.setObjectName("status")
        self.openChamber = QtWidgets.QPushButton(Form)
        self.openChamber.setGeometry(QtCore.QRect(890, 210, 191, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.openChamber.setFont(font)
        self.openChamber.setObjectName("openChamber")
        self.calculatingFilm = QtWidgets.QPushButton(Form)
        self.calculatingFilm.setEnabled(False)
        self.calculatingFilm.setGeometry(QtCore.QRect(890, 90, 191, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.calculatingFilm.setFont(font)
        self.calculatingFilm.setObjectName("calculatingFilm")
        self.gas_tube = QtWidgets.QLabel(Form)
        self.gas_tube.setGeometry(QtCore.QRect(710, 180, 71, 21))
        self.gas_tube.setText("")
        self.gas_tube.setObjectName("gas_tube")
        self.gas_flow = QtWidgets.QDial(Form)
        self.gas_flow.setEnabled(False)
        self.gas_flow.setGeometry(QtCore.QRect(780, 160, 50, 64))
        self.gas_flow.setMinimum(0)
        self.gas_flow.setMaximum(599)
        self.gas_flow.setObjectName("gas_flow")
        self.gas = QtWidgets.QLabel(Form)
        self.gas.setGeometry(QtCore.QRect(760, 130, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.gas.setFont(font)
        self.gas.setText("")
        self.gas.setAlignment(QtCore.Qt.AlignCenter)
        self.gas.setObjectName("gas")
        self.status_2 = QtWidgets.QLabel(Form)
        self.status_2.setGeometry(QtCore.QRect(890, 270, 191, 81))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.status_2.setFont(font)
        self.status_2.setStyleSheet("background-color: white;")
        self.status_2.setFrameShape(QtWidgets.QFrame.Box)
        self.status_2.setText("")
        self.status_2.setTextFormat(QtCore.Qt.AutoText)
        self.status_2.setAlignment(QtCore.Qt.AlignCenter)
        self.status_2.setWordWrap(True)
        self.status_2.setObjectName("status_2")
        self.water_button = QtWidgets.QPushButton(Form)
        self.water_button.setGeometry(QtCore.QRect(890, 150, 191, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.water_button.setFont(font)
        self.water_button.setStyleSheet("")
        self.water_button.setObjectName("water_button")
        self.pressure_value_2 = QtWidgets.QLabel(Form)
        self.pressure_value_2.setGeometry(QtCore.QRect(940, 490, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pressure_value_2.setFont(font)
        self.pressure_value_2.setStyleSheet("background-color: white;")
        self.pressure_value_2.setFrameShape(QtWidgets.QFrame.Box)
        self.pressure_value_2.setText("")
        self.pressure_value_2.setAlignment(QtCore.Qt.AlignCenter)
        self.pressure_value_2.setObjectName("pressure_value_2")
        self.time_label2_2 = QtWidgets.QLabel(Form)
        self.time_label2_2.setGeometry(QtCore.QRect(940, 440, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.time_label2_2.setFont(font)
        self.time_label2_2.setStyleSheet("background-color: white;")
        self.time_label2_2.setFrameShape(QtWidgets.QFrame.Box)
        self.time_label2_2.setText("")
        self.time_label2_2.setAlignment(QtCore.Qt.AlignCenter)
        self.time_label2_2.setObjectName("time_label2_2")
        self.time_label1_2 = QtWidgets.QLabel(Form)
        self.time_label1_2.setGeometry(QtCore.QRect(940, 390, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.time_label1_2.setFont(font)
        self.time_label1_2.setStyleSheet("background-color: white;")
        self.time_label1_2.setFrameShape(QtWidgets.QFrame.Box)
        self.time_label1_2.setText("")
        self.time_label1_2.setAlignment(QtCore.Qt.AlignCenter)
        self.time_label1_2.setObjectName("time_label1_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Vacuum system research"))
        self.valve1.setText(_translate("Form", "V1"))
        self.tm_pump.setText(_translate("Form", "TMP"))
        self.valve2.setText(_translate("Form", "V2"))
        self.fl_pump.setText(_translate("Form", "FLP"))
        self.valve3.setText(_translate("Form", "V3"))
        self.Enable.setText(_translate("Form", "Turn on power"))
        self.l_tm.setText(_translate("Form", "l"))
        self.d_tm.setText(_translate("Form", "d"))
        self.d_fl.setText(_translate("Form", "d"))
        self.l_fl.setText(_translate("Form", "l"))
        self.t1.setText(_translate("Form", "t1"))
        self.t2.setText(_translate("Form", "t2"))
        self.time_rewind.setText(_translate("Form", "time"))
        self.p.setText(_translate("Form", "p"))
        self.Q_tm.setText(_translate("Form", "Qin"))
        self.Q_fl.setText(_translate("Form", "Qin"))
        self.V_chamber.setText(_translate("Form", "V"))
        self.S_tm.setText(_translate("Form", "S"))
        self.S_fl.setText(_translate("Form", "S"))
        self.x1.setText(_translate("Form", "x1"))
        self.x100.setText(_translate("Form", "x100"))
        self.x0_5.setText(_translate("Form", "x0.5"))
        self.overflow.setText(_translate("Form", "Air"))
        self.status.setText(_translate("Form", "Power off"))
        self.openChamber.setText(_translate("Form", "Open chamber"))
        self.calculatingFilm.setText(_translate("Form", "Calculating film"))
        self.water_button.setText(_translate("Form", "Water"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
