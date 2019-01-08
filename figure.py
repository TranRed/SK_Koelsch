from PyQt5 import QtCore, QtGui, QtWidgets
import numpy as np
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection, Line3DCollection
from itertools import product, combinations
import re
from decimal import *
import model


def set_sides(inA, inB, inC):
    global a
    a = inA
    global b
    b = inB
    global c
    c = inC

class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super(Window, self).__init__(parent)

        global a
        global b
        global c

        # a figure instance to plot on
        self.figure = plt.figure()

        # this is the Canvas Widget that displays the `figure`
        # it takes the `figure` instance as a parameter to __init__
        self.canvas = FigureCanvas(self.figure)

        # set the layout
        layout = QtWidgets.QVBoxLayout()

        #layout.addWidget(self.toolbar)
        layout.addWidget(self.canvas)
        self.setLayout(layout)





    def change_plot(self,a,b,c, materialData):
        self.figure.clear(True)
        ax = self.figure.add_subplot(111, projection='3d')

        plt.ion()
        list = [a, b, c]

        upper = max(list)

        points = np.array([[0, 0, 0],
                          [0, 0, a],
                          [0, c, a],
                          [0, c, 0],
                          [b, 0, 0],
                          [b, 0, a],
                          [b, c, a],
                          [b, c, 0]])

        P = [[1 , 0 ,  0],
         [0 , 1 , 0],
         [0 , 0 ,  1]]

        Z = np.zeros((8,3))
        for i in range(8): Z[i,:] = np.dot(points[i,:],P)

        r = [-1,1]

        X, Y = np.meshgrid(r, r)
        # plot vertices
        ax.scatter3D(Z[:, 0], Z[:, 1], Z[:, 2])

        # list of sides' polygons of figure
        verts = [[Z[0],Z[1],Z[2],Z[3]],
         [Z[4],Z[5],Z[6],Z[7]],
         [Z[0],Z[1],Z[5],Z[4]],
         [Z[2],Z[3],Z[7],Z[6]],
         [Z[1],Z[2],Z[6],Z[5]],
         [Z[4],Z[7],Z[3],Z[0]],
         [Z[2],Z[3],Z[7],Z[6]]]

        color = self.calculateColor(materialData)
        # plot sides
        ax.add_collection3d(Poly3DCollection(verts,
         facecolors=color, linewidths=1, edgecolors='black', alpha=.25))

        ax.set_xlabel('b')
        ax.set_xbound(0,upper)
        ax.set_ylabel('c')
        ax.set_ybound(0,upper)
        ax.set_zlabel('a')
        ax.set_zbound(0,upper)
        plt.ioff()

    def calculateColor(self, materialData):
        mat_split = re.findall('[A-Z][^A-Z]*', materialData['chembez'])
        split = []
        sum_nums = 0
        red = 0
        green = 0
        blue = 0

        for element in mat_split:
            part = []
            ele_pure = re.sub(r'[,0-9]+', '', element)
            part.append(ele_pure)
            ele_num = re.sub(r'[a-zA-Z]+', '', element)
            ele_num = re.sub(r'[,]+', '.', ele_num)
            if ele_num != '':
                part.append(Decimal(ele_num))
                sum_nums += Decimal(ele_num)
            else:
                part.append(Decimal("1.0"))
                sum_nums += Decimal("1.0")
            split.append(part)

        for entry in split:
            factor = entry[1] / sum_nums
            entryColor = model.read_color(entry[0])
            red += entryColor['r'] * factor
            green += entryColor['g'] * factor
            blue += entryColor['b'] * factor

        color = '#%02x%02x%02x' % (int(red),int(green),int(blue))
        return color
