# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt6 UI code generator 6.7.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Project1(object):
    def setupUi(self, Project1):
        Project1.setObjectName("Project1")
        Project1.setEnabled(True)
        Project1.resize(400, 500)
        Project1.setMinimumSize(QtCore.QSize(400, 500))
        Project1.setMaximumSize(QtCore.QSize(400, 500))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Text, brush)
        Project1.setPalette(palette)
        self.centralwidget = QtWidgets.QWidget(parent=Project1)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButtonVote = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonVote.setGeometry(QtCore.QRect(160, 220, 81, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButtonVote.setFont(font)
        self.pushButtonVote.setObjectName("pushButtonVote")
        self.labelVote = QtWidgets.QLabel(parent=self.centralwidget)
        self.labelVote.setGeometry(QtCore.QRect(120, 10, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(33)
        self.labelVote.setFont(font)
        self.labelVote.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.labelVote.setObjectName("labelVote")
        self.radioButtonJohn = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.radioButtonJohn.setGeometry(QtCore.QRect(90, 120, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(21)
        self.radioButtonJohn.setFont(font)
        self.radioButtonJohn.setObjectName("radioButtonJohn")
        self.radioButtonJane = QtWidgets.QRadioButton(parent=self.centralwidget)
        self.radioButtonJane.setGeometry(QtCore.QRect(220, 120, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(21)
        self.radioButtonJane.setFont(font)
        self.radioButtonJane.setObjectName("radioButtonJane")
        self.labelJohn = QtWidgets.QLabel(parent=self.centralwidget)
        self.labelJohn.setGeometry(QtCore.QRect(130, 290, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.labelJohn.setFont(font)
        self.labelJohn.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.labelJohn.setObjectName("labelJohn")
        self.labelJane = QtWidgets.QLabel(parent=self.centralwidget)
        self.labelJane.setGeometry(QtCore.QRect(130, 330, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.labelJane.setFont(font)
        self.labelJane.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.labelJane.setObjectName("labelJane")
        self.labelTotal = QtWidgets.QLabel(parent=self.centralwidget)
        self.labelTotal.setGeometry(QtCore.QRect(130, 370, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.labelTotal.setFont(font)
        self.labelTotal.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.labelTotal.setObjectName("labelTotal")
        self.labelJohnResults = QtWidgets.QLabel(parent=self.centralwidget)
        self.labelJohnResults.setGeometry(QtCore.QRect(240, 290, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.labelJohnResults.setFont(font)
        self.labelJohnResults.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.labelJohnResults.setObjectName("labelJohnResults")
        self.labelTotalResults = QtWidgets.QLabel(parent=self.centralwidget)
        self.labelTotalResults.setGeometry(QtCore.QRect(240, 370, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.labelTotalResults.setFont(font)
        self.labelTotalResults.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.labelTotalResults.setObjectName("labelTotalResults")
        self.labelJaneResults = QtWidgets.QLabel(parent=self.centralwidget)
        self.labelJaneResults.setGeometry(QtCore.QRect(240, 330, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.labelJaneResults.setFont(font)
        self.labelJaneResults.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.labelJaneResults.setObjectName("labelJaneResults")
        self.inputID = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.inputID.setGeometry(QtCore.QRect(190, 70, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.inputID.setFont(font)
        self.inputID.setText("")
        self.inputID.setMaxLength(5)
        self.inputID.setObjectName("inputID")
        self.labelID = QtWidgets.QLabel(parent=self.centralwidget)
        self.labelID.setGeometry(QtCore.QRect(20, 70, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.labelID.setFont(font)
        self.labelID.setObjectName("labelID")
        self.labelStatus = QtWidgets.QLabel(parent=self.centralwidget)
        self.labelStatus.setGeometry(QtCore.QRect(40, 160, 321, 41))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Text, brush)
        self.labelStatus.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.labelStatus.setFont(font)
        self.labelStatus.setText("")
        self.labelStatus.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.labelStatus.setObjectName("labelStatus")
        self.pushButtonExit = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonExit.setEnabled(True)
        self.pushButtonExit.setGeometry(QtCore.QRect(160, 220, 81, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButtonExit.setFont(font)
        self.pushButtonExit.setObjectName("pushButtonExit")
        Project1.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=Project1)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 37))
        self.menubar.setObjectName("menubar")
        Project1.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=Project1)
        self.statusbar.setObjectName("statusbar")
        Project1.setStatusBar(self.statusbar)

        self.retranslateUi(Project1)
        QtCore.QMetaObject.connectSlotsByName(Project1)

    def retranslateUi(self, Project1):
        _translate = QtCore.QCoreApplication.translate
        Project1.setWindowTitle(_translate("Project1", "Project 1"))
        self.pushButtonVote.setText(_translate("Project1", "Vote"))
        self.labelVote.setText(_translate("Project1", "Voting"))
        self.radioButtonJohn.setText(_translate("Project1", "John"))
        self.radioButtonJane.setText(_translate("Project1", "Jane"))
        self.labelJohn.setText(_translate("Project1", "John"))
        self.labelJane.setText(_translate("Project1", "Jane"))
        self.labelTotal.setText(_translate("Project1", "Total"))
        self.labelJohnResults.setText(_translate("Project1", "0"))
        self.labelTotalResults.setText(_translate("Project1", "0"))
        self.labelJaneResults.setText(_translate("Project1", "0"))
        self.inputID.setPlaceholderText(_translate("Project1", "5 digits"))
        self.labelID.setText(_translate("Project1", "Enter ID Number"))
        self.pushButtonExit.setText(_translate("Project1", "Exit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Project1 = QtWidgets.QMainWindow()
    ui = Ui_Project1()
    ui.setupUi(Project1)
    Project1.show()
    sys.exit(app.exec())
