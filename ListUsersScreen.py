import Domain.User as User
import re
from PyQt5 import uic, QtWidgets

app = QtWidgets.QApplication([])
form = uic.loadUi("PyQtScreens/interTela_tripulante.ui")
error_dialog = QtWidgets.QErrorMessage()

class InitializeUserScreen:
    def __init__(self):
        
        self.ListUsers()

    def ListUsers(self):
        form.listWidget.addItems(User.GetUsers())
    
    def ClearListWidget(self):
        form.listWidget.clear()

initializeUserScreen = InitializeUserScreen()

def RestartListWidget():
    initializeUserScreen.ClearListWidget()
    initializeUserScreen.ListUsers()

def ClearFields():
    form.lineText_tripulante.setText("")
    form.lineText_senha.setText("")

def GetUserId():
    user = form.listWidget.currentItem()
    if not user:
        error_dialog.showMessage('Selecione um tripulante!')
        raise Exception("Nenhum tripulante selecionado")
    userId = re.sub(r"[\D]", "", user.text())
    return userId

def InsertUser():
    username = form.lineText_tripulante.text()
    password = form.lineText_senha.text()
    if not username:
        error_dialog.showMessage('Insira um valor no campo de nome do novo tripulante!')
    elif not password:
        error_dialog.showMessage('Insira um valor no campo de senha do novo tripulante!')
    else:
        ClearFields()
        User.InsertUser(username, password)        
        RestartListWidget()

def UpdateUser():
    username = form.lineText_tripulante.text()    
    userId = GetUserId()
    if not username:
        error_dialog.showMessage('Insira um valor no campo de texto para atualizar o nome do tripulante!')
    else:
        ClearFields()
        User.UpdateUser(username, userId)        
        RestartListWidget()

def DeleteUser():
    userId = GetUserId()
    ClearFields()
    User.DeleteUser(userId)
    RestartListWidget()

def CallListUsersScreen():
    form.show()
    app.exec()
    
form.ButtonInserir.clicked.connect(InsertUser)
form.ButtonDelet.clicked.connect(DeleteUser)
form.ButtonUp.clicked.connect(UpdateUser)