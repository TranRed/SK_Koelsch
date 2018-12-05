from PyQt5 import QtCore, QtGui, QtWidgets
import view
import controller
import model

from popups import material

class MainWindow(QtWidgets.QMainWindow, view.Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

class MaterialDialog(QtWidgets.QDialog, material.Ui_Material):
    def __init__(self, mode, parent=None):
        self.mode = mode
        super(MaterialDialog, self).__init__(parent)
        self.setupUi(self)
        if self.mode == 'N':
            self.pushButton_sfg.setHidden(True)
            self.pushButton_delete.setHidden(True)

if __name__ == "__main__":
    import sys
    #create application object
    app = QtWidgets.QApplication(sys.argv)
    ui = MainWindow()
    controller.defaults(ui)
    ui.show()
    sys.exit(app.exec_())
