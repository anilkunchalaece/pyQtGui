import sys
from PyQt4 import QtGui


class Example(QtGui.QWidget):
    
    def __init__(self):
        super(Example, self).__init__()
        
        self.initUI()
        
    def initUI(self):
        questionLabel = QtGui.QLabel('This is the First Question')
        optA = QtGui.QRadioButton("Option A")
        optB = QtGui.QRadioButton("Option B")
        optC = QtGui.QRadioButton("Option C")
        optD = QtGui.QRadioButton("Option D")
        submitBtn = QtGui.QPushButton("Submit")


        grid = QtGui.QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(questionLabel, 1, 0)

        grid.addWidget(optA, 2, 0)
        grid.addWidget(optB, 3, 0)
        grid.addWidget(optC, 4, 0)
        grid.addWidget(optD, 5, 0)

        grid.addWidget(submitBtn,6,0)


   
        
        self.setLayout(grid) 
        
        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('Prepare2Pg')    
        self.show()
        
def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
        main()
