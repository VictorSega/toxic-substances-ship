import Domain.Login as Login
import ChoiceScreen
from PyQt5 import uic, QtWidgets

app = QtWidgets.QApplication([])
form = uic.loadUi("PyQtScreens/interface.ui")
error_dialog = QtWidgets.QErrorMessage()

def ClearFields():
    form.lineUsur.setText("")
    form.lineSenha.setText("")

def LoginUser():
    inputedUser = form.lineUsur.text()
    inputedPassword = form.lineSenha.text()

    try:
        userLogged = Login.LoginUser(inputedUser, inputedPassword)
    except:
        ClearFields()
        error_dialog.showMessage('Tripulante não encontrado!')     

    if(not userLogged):        
        error_dialog.showMessage('Não foi possível autenticar, se afaste do navio!')
        raise Exception("Usuário ou senha incorretos!")
    
    ChoiceScreen.CallChoiceScreen()
    form.close()

form.ButtonLogin.clicked.connect(LoginUser)

form.show()
app.exec()
