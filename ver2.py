"""
Author : Kunchala Anil
Date : Aug 24 2016
Gui application for Prepare2Pg 
"""

import sys
from PyQt4 import QtGui


class Example(QtGui.QWidget):
    
    def __init__(self):
        super(Example, self).__init__()
"""
optA,B,C,D is initialized as Self cause they needed to share information between Classes
"""
        self.optA = QtGui.QRadioButton("Option A")
        self.optB = QtGui.QRadioButton("Option B")
        self.optC = QtGui.QRadioButton("Option C")
        self.optD = QtGui.QRadioButton("Option D")
        self.initUI()
        
    def initUI(self):
        questionLabel = QtGui.QLabel('This is the First Question')
       
        submitBtn = QtGui.QPushButton("Submit")

        submitBtn.setCheckable(True)
        submitBtn.toggle()
        submitBtn.clicked.connect(self.submitFcn)

        grid = QtGui.QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(questionLabel, 1, 0)

        grid.addWidget(self.optA, 2, 0)
        grid.addWidget(self.optB, 3, 0)
        grid.addWidget(self.optC, 4, 0)
        grid.addWidget(self.optD, 5, 0)

        grid.addWidget(submitBtn,6,0)
   
        
        self.setLayout(grid) 
        
        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('Prepare2Pg')    
        self.show()

    def submitFcn(self):
        print "Submit Pressed"
        if self.optA.isChecked():
            print "Option A is Checked"
        elif self.optB.isChecked():
            print "Option B is Checked"
        elif self.optC.isChecked():
            print "Option C is  Checked"
        elif self.optD.isChecked():
            print "Option D is Checked"
        else:
            print "No Option is Selected"
            
            
        
        
def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
        main()
