from PyQt5 import QtCore, QtGui, QtWidgets
import view
import controller
import model


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = view.Ui_MainWindow()
    ui.setupUi(MainWindow)
    controller.defaults(ui)
    MainWindow.show()
    sys.exit(app.exec_())
