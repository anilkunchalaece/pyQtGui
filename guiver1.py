#Author : Kunchala Anil
#Date : Aug 23 2016
"""
Iam using python 2.7 with pyQt4
Download the pyQt4 from https://www.riverbankcomputing.com/software/pyqt/download
Note : Download the Binary package
s
"""

import sys
from PyQt4 import QtGui

def main():
	app=QtGui.QApplication(sys.argv)
	
	w=QtGui.QWidget()
	w.resize(250,250)
	w.move(200,200)
	w.setWindowTitle('Prepare 2 PG')
	w.show()
	
	sys.exit(app.exec_())
	
if __name__ == '__main__':
	main()