import sys
from PyQt5 import QtWidgets, QtCore

help(QtWidgets)
app = QtWidgets.QApplication(sys.argv)

widget = QtWidgets.QWidget()
widget.resize(360,360)
widget.setWindowTitle('hello pyqt')
widget.show()
sys.exit(app.exec_())