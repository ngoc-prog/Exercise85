from PyQt6.QtWidgets import QApplication, QMainWindow

from chapter4_oop.exercise85.ui.LoginMainWindowExt import LoginMainWindowExt

app=QApplication([])
mainwindow=QMainWindow()
myui=LoginMainWindowExt()
myui.setupUi(mainwindow)
myui.showWindow()
app.exec()