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

        
        # plot sides
        ax.add_collection3d(Poly3DCollection(verts,
         facecolors=materialData['farbe'], linewidths=1, edgecolors='black', alpha=.25))

        ax.set_xlabel('b')
        ax.set_xbound(0,upper)
        ax.set_ylabel('c')
        ax.set_ybound(0,upper)
        ax.set_zlabel('a')
        ax.set_zbound(0,upper)
        plt.ioff()

