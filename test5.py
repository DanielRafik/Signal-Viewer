# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test5.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1094, 546)
        font = QtGui.QFont()
        font.setFamily("Myanmar Text")
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(30, 40, 181, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.ProcessControl_GroupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.ProcessControl_GroupBox.setGeometry(QtCore.QRect(880, 350, 191, 131))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.ProcessControl_GroupBox.setFont(font)
        self.ProcessControl_GroupBox.setFlat(False)
        self.ProcessControl_GroupBox.setCheckable(False)
        self.ProcessControl_GroupBox.setObjectName("ProcessControl_GroupBox")
        self.Play_PushButton = QtWidgets.QPushButton(self.ProcessControl_GroupBox)
        self.Play_PushButton.setGeometry(QtCore.QRect(20, 30, 71, 28))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Play_PushButton.setFont(font)
        self.Play_PushButton.setObjectName("Play_PushButton")
        self.Pause_PushButton = QtWidgets.QPushButton(self.ProcessControl_GroupBox)
        self.Pause_PushButton.setGeometry(QtCore.QRect(100, 30, 71, 28))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Pause_PushButton.setFont(font)
        self.Pause_PushButton.setObjectName("Pause_PushButton")
        self.Report_PushButton = QtWidgets.QPushButton(self.ProcessControl_GroupBox)
        self.Report_PushButton.setGeometry(QtCore.QRect(20, 80, 151, 28))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Report_PushButton.setFont(font)
        self.Report_PushButton.setObjectName("Report_PushButton")
        self.Hide_GroupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.Hide_GroupBox.setGeometry(QtCore.QRect(260, 390, 191, 91))
        self.Hide_GroupBox.setObjectName("Hide_GroupBox")
        self.Channel1_CheckBox = QtWidgets.QCheckBox(self.Hide_GroupBox)
        self.Channel1_CheckBox.setGeometry(QtCore.QRect(10, 20, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.Channel1_CheckBox.setFont(font)
        self.Channel1_CheckBox.setObjectName("Channel1_CheckBox")
        self.Channel2_CheckBox = QtWidgets.QCheckBox(self.Hide_GroupBox)
        self.Channel2_CheckBox.setGeometry(QtCore.QRect(10, 40, 81, 20))
        self.Channel2_CheckBox.setObjectName("Channel2_CheckBox")
        self.Channel3_CheckBox = QtWidgets.QCheckBox(self.Hide_GroupBox)
        self.Channel3_CheckBox.setGeometry(QtCore.QRect(10, 60, 81, 20))
        self.Channel3_CheckBox.setObjectName("Channel3_CheckBox")
        self.Figure_Slider = QtWidgets.QSlider(self.centralwidget)
        self.Figure_Slider.setGeometry(QtCore.QRect(20, 340, 651, 22))
        self.Figure_Slider.setOrientation(QtCore.Qt.Horizontal)
        self.Figure_Slider.setObjectName("Figure_Slider")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(542, 400, 131, 22))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(542, 430, 131, 22))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(542, 460, 131, 22))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.Channel1_Label = QtWidgets.QLabel(self.centralwidget)
        self.Channel1_Label.setGeometry(QtCore.QRect(474, 400, 61, 21))
        self.Channel1_Label.setObjectName("Channel1_Label")
        self.Channnel_Label = QtWidgets.QLabel(self.centralwidget)
        self.Channnel_Label.setGeometry(QtCore.QRect(474, 430, 61, 21))
        self.Channnel_Label.setObjectName("Channnel_Label")
        self.Channel3_Label = QtWidgets.QLabel(self.centralwidget)
        self.Channel3_Label.setGeometry(QtCore.QRect(474, 460, 61, 21))
        self.Channel3_Label.setObjectName("Channel3_Label")
        self.BrowseFiles_PushButton = QtWidgets.QPushButton(self.centralwidget)
        self.BrowseFiles_PushButton.setGeometry(QtCore.QRect(30, 450, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Myanmar Text")
        font.setBold(True)
        font.setWeight(75)
        self.BrowseFiles_PushButton.setFont(font)
        self.BrowseFiles_PushButton.setObjectName("BrowseFiles_PushButton")
        self.CineSpeed_Slider = QtWidgets.QSlider(self.centralwidget)
        self.CineSpeed_Slider.setGeometry(QtCore.QRect(140, 380, 91, 22))
        self.CineSpeed_Slider.setOrientation(QtCore.Qt.Horizontal)
        self.CineSpeed_Slider.setObjectName("CineSpeed_Slider")
        self.CineSpeed_Label = QtWidgets.QLabel(self.centralwidget)
        self.CineSpeed_Label.setGeometry(QtCore.QRect(30, 380, 81, 21))
        self.CineSpeed_Label.setObjectName("CineSpeed_Label")
        self.Spectrogram_GroupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.Spectrogram_GroupBox_2.setGeometry(QtCore.QRect(690, 350, 181, 131))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Spectrogram_GroupBox_2.setFont(font)
        self.Spectrogram_GroupBox_2.setObjectName("Spectrogram_GroupBox_2")
        self.Range_ComboBox = QtWidgets.QComboBox(self.Spectrogram_GroupBox_2)
        self.Range_ComboBox.setGeometry(QtCore.QRect(20, 50, 61, 61))
        self.Range_ComboBox.setObjectName("Range_ComboBox")
        self.Range_ComboBox.addItem("")
        self.Range_ComboBox.addItem("")
        self.Range_ComboBox.addItem("")
        self.Range_ComboBox.addItem("")
        self.Max_Label = QtWidgets.QLabel(self.Spectrogram_GroupBox_2)
        self.Max_Label.setGeometry(QtCore.QRect(100, 20, 31, 16))
        self.Max_Label.setObjectName("Max_Label")
        self.Min_Label = QtWidgets.QLabel(self.Spectrogram_GroupBox_2)
        self.Min_Label.setGeometry(QtCore.QRect(150, 20, 55, 16))
        self.Min_Label.setObjectName("Min_Label")
        self.Min_Slider = QtWidgets.QSlider(self.Spectrogram_GroupBox_2)
        self.Min_Slider.setGeometry(QtCore.QRect(150, 40, 22, 71))
        self.Min_Slider.setOrientation(QtCore.Qt.Vertical)
        self.Min_Slider.setObjectName("Min_Slider")
        self.Range_Label = QtWidgets.QLabel(self.Spectrogram_GroupBox_2)
        self.Range_Label.setGeometry(QtCore.QRect(30, 20, 41, 31))
        self.Range_Label.setObjectName("Range_Label")
        self.Max_Slider = QtWidgets.QSlider(self.Spectrogram_GroupBox_2)
        self.Max_Slider.setGeometry(QtCore.QRect(110, 40, 22, 71))
        self.Max_Slider.setOrientation(QtCore.Qt.Vertical)
        self.Max_Slider.setObjectName("Max_Slider")
        self.SelectChannel_ComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.SelectChannel_ComboBox.setGeometry(QtCore.QRect(30, 410, 101, 31))
        self.SelectChannel_ComboBox.setEditable(False)
        self.SelectChannel_ComboBox.setObjectName("SelectChannel_ComboBox")
        self.SelectChannel_ComboBox.addItem("")
        self.SelectChannel_ComboBox.addItem("")
        self.SelectChannel_ComboBox.addItem("")
        self.splitter_2 = QtWidgets.QSplitter(self.centralwidget)
        self.splitter_2.setGeometry(QtCore.QRect(20, 60, 1041, 271))
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.Figure_groupBox = QtWidgets.QGroupBox(self.splitter_2)
        self.Figure_groupBox.setObjectName("Figure_groupBox")
        self.Figure_Widget = PlotWidget(self.Figure_groupBox)
        self.Figure_Widget.setGeometry(QtCore.QRect(0, 20, 661, 251))
        self.Figure_Widget.setObjectName("Figure_Widget")
        self.Spectrogram_GroupBox = QtWidgets.QGroupBox(self.splitter_2)
        self.Spectrogram_GroupBox.setObjectName("Spectrogram_GroupBox")
        self.SpectrogramSelectChannel_Label = QtWidgets.QLabel(self.Spectrogram_GroupBox)
        self.SpectrogramSelectChannel_Label.setGeometry(QtCore.QRect(80, 230, 91, 41))
        self.SpectrogramSelectChannel_Label.setObjectName("SpectrogramSelectChannel_Label")
        self.comboBox_3 = QtWidgets.QComboBox(self.Spectrogram_GroupBox)
        self.comboBox_3.setGeometry(QtCore.QRect(170, 240, 151, 21))
        self.comboBox_3.setEditable(False)
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.Spectrogram_Widget = PlotWidget(self.Spectrogram_GroupBox)
        self.Spectrogram_Widget.setGeometry(QtCore.QRect(0, 20, 381, 211))
        self.Spectrogram_Widget.setObjectName("Spectrogram_Widget")
        self.ZoomOut_PushButton = QtWidgets.QPushButton(self.centralwidget)
        self.ZoomOut_PushButton.setGeometry(QtCore.QRect(117, 10, 91, 28))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.ZoomOut_PushButton.setFont(font)
        self.ZoomOut_PushButton.setObjectName("ZoomOut_PushButton")
        self.SignalColor_ComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.SignalColor_ComboBox.setGeometry(QtCore.QRect(140, 410, 91, 31))
        self.SignalColor_ComboBox.setObjectName("SignalColor_ComboBox")
        self.SignalColor_ComboBox.addItem("")
        self.SignalColor_ComboBox.addItem("")
        self.SignalColor_ComboBox.addItem("")
        self.ZoomIn_PushButton = QtWidgets.QPushButton(self.centralwidget)
        self.ZoomIn_PushButton.setGeometry(QtCore.QRect(20, 10, 91, 28))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.ZoomIn_PushButton.setFont(font)
        self.ZoomIn_PushButton.setObjectName("ZoomIn_PushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1094, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.ProcessControl_GroupBox.setTitle(_translate("MainWindow", "Process Control"))
        self.Play_PushButton.setText(_translate("MainWindow", "Play"))
        self.Pause_PushButton.setText(_translate("MainWindow", "Pause"))
        self.Report_PushButton.setText(_translate("MainWindow", "Report"))
        self.Hide_GroupBox.setTitle(_translate("MainWindow", "Hide"))
        self.Channel1_CheckBox.setText(_translate("MainWindow", "Channel 1"))
        self.Channel2_CheckBox.setText(_translate("MainWindow", "Channel 2"))
        self.Channel3_CheckBox.setText(_translate("MainWindow", "Channel 3"))
        self.Channel1_Label.setText(_translate("MainWindow", "Channel 1"))
        self.Channnel_Label.setText(_translate("MainWindow", "Channel 2"))
        self.Channel3_Label.setText(_translate("MainWindow", "Channel 3"))
        self.BrowseFiles_PushButton.setText(_translate("MainWindow", " Browse Files"))
        self.CineSpeed_Label.setText(_translate("MainWindow", "Cine Speed"))
        self.Spectrogram_GroupBox_2.setTitle(_translate("MainWindow", "Spectrogram "))
        self.Range_ComboBox.setItemText(0, _translate("MainWindow", "Red"))
        self.Range_ComboBox.setItemText(1, _translate("MainWindow", "Yellow"))
        self.Range_ComboBox.setItemText(2, _translate("MainWindow", "Green"))
        self.Range_ComboBox.setItemText(3, _translate("MainWindow", "Blue"))
        self.Max_Label.setText(_translate("MainWindow", "Max"))
        self.Min_Label.setText(_translate("MainWindow", "Min"))
        self.Range_Label.setText(_translate("MainWindow", "Range"))
        self.SelectChannel_ComboBox.setItemText(0, _translate("MainWindow", "Channel 1"))
        self.SelectChannel_ComboBox.setItemText(1, _translate("MainWindow", "Channel 2"))
        self.SelectChannel_ComboBox.setItemText(2, _translate("MainWindow", "Channel 3"))
        self.Figure_groupBox.setTitle(_translate("MainWindow", "Figure"))
        self.Spectrogram_GroupBox.setTitle(_translate("MainWindow", "Spectrogram"))
        self.SpectrogramSelectChannel_Label.setText(_translate("MainWindow", "Select channel"))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "Channel 1"))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "Channel 2"))
        self.comboBox_3.setItemText(2, _translate("MainWindow", "Channel 3"))
        self.ZoomOut_PushButton.setText(_translate("MainWindow", "Zoom out"))
        self.SignalColor_ComboBox.setItemText(0, _translate("MainWindow", "Red"))
        self.SignalColor_ComboBox.setItemText(1, _translate("MainWindow", "Green"))
        self.SignalColor_ComboBox.setItemText(2, _translate("MainWindow", "Blue"))
        self.ZoomIn_PushButton.setText(_translate("MainWindow", "Zoom in"))

from pyqtgraph import PlotWidget

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

