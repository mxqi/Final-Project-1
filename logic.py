from PyQt6.QtWidgets import *
from gui import *


class Logic(QMainWindow, Ui_Project1):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButtonExit.hide()
        self.pushButtonVote.clicked.connect(lambda: self.vote())
        self.pushButtonExit.clicked.connect(lambda: self.exit())

    def vote(self):
        jane = 0
        john = 0
        total = 0
        userID = self.inputID.text().strip()
        if not (self.radioButtonJane.isChecked() or self.radioButtonJohn.isChecked()):
            self.labelStatus.setText('Please select an option')
            return

        with open('ids.txt', 'r+') as file:
            lines = file.readlines()
            ids = [line.split()[0] for line in lines]
            votes = [line.split()[1] for line in lines]
            if userID in ids:
                self.labelStatus.setText('ID already voted')
                return
            if not userID or len(userID) < 5:
                self.labelStatus.setText('Invalid ID')
                return

            self.labelStatus.setText('Voted successfully')
            ids.append(userID)
            file.seek(0)
            for line in lines:
                file.write(line)
            if self.radioButtonJane.isChecked():
                file.write(f'{userID} Jane\n')
            else:
                file.write(f'{userID} John\n')

            for x in votes:
                if x == 'Jane':
                    jane += 1
                elif x == 'John':
                    john += 1
                total += 1

        self.labelJaneResults.setText(str(jane))
        self.labelJohnResults.setText(str(john))
        self.labelTotalResults.setText(str(total))


        self.pushButtonVote.hide()
        self.pushButtonExit.show()
        self.inputID.clear()
        self.radioButtonJane.setChecked(False)
        self.radioButtonJohn.setChecked(False)

    def exit(self):
        self.close()
