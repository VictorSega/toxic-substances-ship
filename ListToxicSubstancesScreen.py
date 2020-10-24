import Domain.ToxicSubstance as ToxicSubstance
import re
from PyQt5 import uic, QtWidgets

app = QtWidgets.QApplication([])
form = uic.loadUi("PyQtScreens/interTela_subs_toxica.ui")
error_dialog = QtWidgets.QErrorMessage()

class InitializeToxicSubstanceScreen:
    def __init__(self):
        
        self.ListToxicSubstances()

    def ListToxicSubstances(self):
        form.listWidget.addItems(ToxicSubstance.GetToxicSubstances())
    
    def ClearListWidget(self):
        form.listWidget.clear()

initializeToxicSubstanceScreen = InitializeToxicSubstanceScreen()

def RestartListWidget():
    initializeToxicSubstanceScreen.ClearListWidget()
    initializeToxicSubstanceScreen.ListToxicSubstances()

def ClearFields():
    form.lineText_subsToxica.setText("")
    form.lineText_quantidade.setText("")

def VerifyIfIsInteger(value):
    try:
        int(value)
    except:
        error_dialog.showMessage('A quantidade deve ser um número inteiro')
        raise Exception("Quantidade inválida")

def GetToxicSubstanceId():
    toxicSubstance = form.listWidget.currentItem()
    if not toxicSubstance:
        error_dialog.showMessage('Selecione uma substância tóxica!')
        raise Exception("Nenhuma substância tóxica selecionado")
    toxicSubstanceId = re.search(r'\d+', toxicSubstance.text()).group()
    return toxicSubstanceId

def InsertToxicSubstance():
    name = form.lineText_subsToxica.text()
    quantity = form.lineText_quantidade.text()
    if not name:
        error_dialog.showMessage('Insira um valor no campo de nome da substância tóxica!')
    elif not quantity:
        error_dialog.showMessage('Insira um valor no campo de quantidade da substância tóxica!')
    else:
        VerifyIfIsInteger(quantity)
        ClearFields()
        ToxicSubstance.InsertToxicSubstance(name, quantity)        
        RestartListWidget()

def UpdateToxicSubstanceQuantity(toxicSubstanceId, quantity):
    VerifyIfIsInteger(quantity)
    ClearFields()
    ToxicSubstance.UpdateToxicSubstanceQuantity(toxicSubstanceId, quantity)
    RestartListWidget()

def UpdateToxicSubstanceName(toxicSubstanceId, name):
    ClearFields()
    ToxicSubstance.UpdateToxicSubstanceName(toxicSubstanceId, name)
    RestartListWidget()

def UpdateToxicSubstanceQuantityAndName(toxicSubstanceId, name, quantity):
    VerifyIfIsInteger(quantity)
    ClearFields()
    ToxicSubstance.UpdateToxicSubstanceQuantityAndName(toxicSubstanceId, name, quantity)  
    RestartListWidget()

def UpdateToxicSubstance():
    name = form.lineText_subsToxica.text()
    quantity = form.lineText_quantidade.text()       
    toxicSubstanceId = GetToxicSubstanceId()
    if quantity and not name:        
        UpdateToxicSubstanceQuantity(toxicSubstanceId, quantity)
    elif name and not quantity:
        UpdateToxicSubstanceName(toxicSubstanceId, name)
    elif name and quantity:
        UpdateToxicSubstanceQuantityAndName(toxicSubstanceId, name, quantity)
    else:
        error_dialog.showMessage('Insira um nome e/ou um valor para a substância tóxica!')    

def DeleteToxicSubstance():
    toxicSubstanceId = GetToxicSubstanceId()
    ClearFields()
    ToxicSubstance.DeleteToxicSubstance(toxicSubstanceId)
    RestartListWidget()

def CallListToxicSubstancesScreen():
    form.show()
    app.exec()
    
form.ButtonInserir.clicked.connect(InsertToxicSubstance)
form.ButtonDelet.clicked.connect(DeleteToxicSubstance)
form.ButtonUp.clicked.connect(UpdateToxicSubstance)