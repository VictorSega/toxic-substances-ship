import ListUsersScreen
import ListToxicSubstancesScreen
from PyQt5 import uic, QtWidgets

app = QtWidgets.QApplication([])
form = uic.loadUi("PyQtScreens/interTela_escolha.ui")

def CallListUserScreen():
    ListUsersScreen.CallListUsersScreen()
    form.close()

def CallListToxicSubstance():
    ListToxicSubstancesScreen.CallListToxicSubstancesScreen()
    form.close()

def CallChoiceScreen():
    form.show()
    app.exec()

form.pushButton.clicked.connect(CallListUserScreen)
form.pushButton_2.clicked.connect(CallListToxicSubstance)