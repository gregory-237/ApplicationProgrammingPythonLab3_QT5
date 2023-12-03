from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(997, 491)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: white;")
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1001, 101))
        self.frame.setStyleSheet("background-color: #a0a0a0;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(430, 20, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 110, 491, 251))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("lab3/figure.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(590, 110, 321, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("text-align: center;")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.input_line = QtWidgets.QLineEdit(self.centralwidget)
        self.input_line.setGeometry(QtCore.QRect(510, 190, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.input_line.setFont(font)
        self.input_line.setStyleSheet("border: 2px solid #666666;\n"
"border-radius: 100;\n"
"")
        self.input_line.setText("")
        self.input_line.setAlignment(QtCore.Qt.AlignCenter)
        self.input_line.setObjectName("input_line")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(700, 190, 93, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton{\n"
"border: 2px solid #666666;\n"
"border-radius: 100;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: #a0a0a0;\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.output_line = QtWidgets.QLineEdit(self.centralwidget)
        self.output_line.setGeometry(QtCore.QRect(812, 190, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.output_line.setFont(font)
        self.output_line.setStyleSheet("border: 2px solid #666666;\n"
"border-radius: 100;\n"
"")
        self.output_line.setText("")
        self.output_line.setAlignment(QtCore.Qt.AlignCenter)
        self.output_line.setObjectName("output_line")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(530, 160, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(844, 160, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.pushButtonPath = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonPath.setGeometry(QtCore.QRect(520, 260, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonPath.setFont(font)
        self.pushButtonPath.setStyleSheet("QPushButton{\n"
"border: 2px solid #666666;\n"
"border-radius: 100;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: #a0a0a0;\n"
"}")
        self.pushButtonPath.setObjectName("pushButtonPath")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(762, 261, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox.setFont(font)
        self.comboBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.comboBox.setAutoFillBackground(False)
        self.comboBox.setStyleSheet("QComboBox{\n"
"border: 2px solid #666666;\n"
"border-radius: 100;\n"
"}")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Курс Доллара"))
        self.label_3.setText(_translate("MainWindow", "Узнать курс за определенный день"))
        self.pushButton.setText(_translate("MainWindow", "ТЫК"))
        self.label_4.setText(_translate("MainWindow", "ДАТА"))
        self.label_5.setText(_translate("MainWindow", "ЗНАЧЕНИЕ"))
        self.pushButtonPath.setText(_translate("MainWindow", "Выберите папку"))
        self.comboBox.setItemText(0, _translate("MainWindow", "dataset"))
        self.comboBox.setItemText(1, _translate("MainWindow", "X и Y"))
        self.comboBox.setItemText(2, _translate("MainWindow", "разбивка по годам"))
        self.comboBox.setItemText(3, _translate("MainWindow", "разбивка по неделям"))