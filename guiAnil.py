# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'button.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1202, 906)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(50, 120, 841, 531))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.questionLabel = QtGui.QLabel(self.groupBox)
        self.questionLabel.setGeometry(QtCore.QRect(10, 40, 811, 91))
        self.questionLabel.setWordWrap(True)
        self.questionLabel.setObjectName(_fromUtf8("questionLabel"))
        self.groupBox_2 = QtGui.QGroupBox(self.groupBox)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 160, 781, 61))
        self.groupBox_2.setTitle(_fromUtf8(""))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.optA = QtGui.QRadioButton(self.groupBox_2)
        self.optA.setGeometry(QtCore.QRect(20, 20, 41, 17))
        self.optA.setObjectName(_fromUtf8("optA"))
        self.optALabel = QtGui.QLabel(self.groupBox_2)
        self.optALabel.setGeometry(QtCore.QRect(70, 20, 691, 21))
        self.optALabel.setObjectName(_fromUtf8("optALabel"))
        self.groupBox_3 = QtGui.QGroupBox(self.groupBox)
        self.groupBox_3.setGeometry(QtCore.QRect(20, 220, 781, 61))
        self.groupBox_3.setTitle(_fromUtf8(""))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.optB = QtGui.QRadioButton(self.groupBox_3)
        self.optB.setGeometry(QtCore.QRect(20, 20, 41, 17))
        self.optB.setObjectName(_fromUtf8("optB"))
        self.optBLabel = QtGui.QLabel(self.groupBox_3)
        self.optBLabel.setGeometry(QtCore.QRect(70, 20, 691, 21))
        self.optBLabel.setObjectName(_fromUtf8("optBLabel"))
        self.groupBox_4 = QtGui.QGroupBox(self.groupBox)
        self.groupBox_4.setGeometry(QtCore.QRect(20, 290, 781, 61))
        self.groupBox_4.setTitle(_fromUtf8(""))
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.optC = QtGui.QRadioButton(self.groupBox_4)
        self.optC.setGeometry(QtCore.QRect(20, 20, 41, 17))
        self.optC.setObjectName(_fromUtf8("optC"))
        self.optCLabel = QtGui.QLabel(self.groupBox_4)
        self.optCLabel.setGeometry(QtCore.QRect(70, 20, 691, 21))
        self.optCLabel.setObjectName(_fromUtf8("optCLabel"))
        self.groupBox_5 = QtGui.QGroupBox(self.groupBox)
        self.groupBox_5.setGeometry(QtCore.QRect(20, 360, 781, 61))
        self.groupBox_5.setTitle(_fromUtf8(""))
        self.groupBox_5.setObjectName(_fromUtf8("groupBox_5"))
        self.optD = QtGui.QRadioButton(self.groupBox_5)
        self.optD.setGeometry(QtCore.QRect(20, 20, 41, 17))
        self.optD.setObjectName(_fromUtf8("optD"))
        self.optDLabel = QtGui.QLabel(self.groupBox_5)
        self.optDLabel.setGeometry(QtCore.QRect(70, 20, 691, 21))
        self.optDLabel.setObjectName(_fromUtf8("optDLabel"))
        self.submitBtn = QtGui.QPushButton(self.groupBox)
        self.submitBtn.setGeometry(QtCore.QRect(220, 450, 141, 41))
        self.submitBtn.setObjectName(_fromUtf8("submitBtn"))
        self.submitBtn_2 = QtGui.QPushButton(self.groupBox)
        self.submitBtn_2.setGeometry(QtCore.QRect(620, 450, 141, 41))
        self.submitBtn_2.setObjectName(_fromUtf8("submitBtn_2"))
        self.groupBox.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1202, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Prepare2Pg", None))
        self.groupBox.setTitle(_translate("MainWindow", "Answer the Following Question", None))
        self.questionLabel.setText(_translate("MainWindow", "Question Goes Here -- Who is your best Ficrional Character ? ", None))
        self.optA.setText(_translate("MainWindow", "A.", None))
        self.optALabel.setText(_translate("MainWindow", "Superman", None))
        self.optB.setText(_translate("MainWindow", "B.", None))
        self.optBLabel.setText(_translate("MainWindow", "Batman", None))
        self.optC.setText(_translate("MainWindow", "C.", None))
        self.optCLabel.setText(_translate("MainWindow", "Iron Man", None))
        self.optD.setText(_translate("MainWindow", "D.", None))
        self.optDLabel.setText(_translate("MainWindow", "Captain America", None))
        self.submitBtn.setText(_translate("MainWindow", "Submit", None))
        self.submitBtn_2.setText(_translate("MainWindow", "Next", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

