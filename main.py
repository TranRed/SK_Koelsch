from PyQt5 import QtCore, QtGui, QtWidgets
import view
import controller
import model

class MainWindow(QtWidgets.QMainWindow, view.Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

if __name__ == "__main__":
    import sys
    #create application object
    app = QtWidgets.QApplication(sys.argv)
    ui = MainWindow()
    controller.defaults(ui)
    ui.show()
    sys.exit(app.exec_())
