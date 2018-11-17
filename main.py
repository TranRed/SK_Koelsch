from PyQt5 import QtCore, QtGui, QtWidgets
import view

def set_sizes(a,b,c):
    ui.lineEdit_semifinishedSideA.setText(a)
    ui.lineEdit_semifinishedSideB.setText(b)
    ui.lineEdit_semifinishedSideC.setText(c)

def calc_semifinished():
    if (
        (not ui.lineEdit_bodySideA.text().isdigit()) or
        (not ui.lineEdit_bodySideB.text().isdigit()) or
        (not ui.lineEdit_bodySideC.text().isdigit()) or
        (not ui.lineEdit_allowanceSideA.text().isdigit()) or
        (not ui.lineEdit_allowanceSideB.text().isdigit()) or
        (not ui.lineEdit_allowanceSideC.text().isdigit())):
        set_sizes("0","0","0")
    else:

        a = int(ui.lineEdit_bodySideA.text()) + int(ui.lineEdit_allowanceSideA.text())
        b = int(ui.lineEdit_bodySideB.text()) + int(ui.lineEdit_allowanceSideB.text())
        c = int(ui.lineEdit_bodySideC.text()) + int(ui.lineEdit_allowanceSideC.text())

        if a <= 10:
            if b <= 10:
                if c <= 10:
                    set_sizes("10","10","10")
                elif c <= 20:
                    set_sizes("10","10","20")
                elif c <= 30:
                    set_sizes("10","10","30")
                else:
                    #size not available
                    set_sizes("0","0","0")
            elif b <= 20:
                if c <= 20:
                    set_sizes("10","20","20")
                elif c <= 30:
                    set_sizes("10","20","30")
                else:
                    #size not available
                    set_sizes("0","0","0")
            elif b <= 30:
                if c <= 20:
                    set_sizes("10","30","20")
                elif c <= 30:
                    set_sizes("10","30","30")
                else:
                    #size not available
                    set_sizes("0","0","0")
            else:
                #size not available
                set_sizes("0","0","0")
        elif a <= 20:
            if b <= 20:
                if c <= 20:
                    set_sizes("20","20","20")
                elif c <= 30:
                    set_sizes("20","20","30")
                else:
                    #size not available
                    set_sizes("0","0","0")
            elif b <= 30:
                if c <= 20:
                    set_sizes("20","30","20")
                elif c <= 30:
                    set_sizes("20","30","30")
                else:
                    #size not available
                    set_sizes("0","0","0")
        else:
            #size not available
            set_sizes("0","0","0")


def connect_size_fields():
    ui.lineEdit_bodySideA.textChanged.connect(lambda: calc_semifinished())
    ui.lineEdit_bodySideB.textChanged.connect(lambda: calc_semifinished())
    ui.lineEdit_bodySideC.textChanged.connect(lambda: calc_semifinished())
    ui.lineEdit_allowanceSideA.textChanged.connect(lambda: calc_semifinished())
    ui.lineEdit_allowanceSideB.textChanged.connect(lambda: calc_semifinished())
    ui.lineEdit_allowanceSideC.textChanged.connect(lambda: calc_semifinished())


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = view.Ui_MainWindow()
    ui.setupUi(MainWindow)
    connect_size_fields()
    MainWindow.show()
    sys.exit(app.exec_())
