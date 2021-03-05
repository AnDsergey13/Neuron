# http://www.pyqtgraph.org/

"""
pip install PyOpenGL PyOpenGL_accelerate
pip install PyQt5
"""

"""
Примеры
pyqtgraph.examples.run()
"""

import sys
# from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QPushButton)
from PyQt5.QtWidgets import QApplication
# from PyQt5.QtCore import pyqtSlot, QRect, QCoreApplication
from pyqtgraph.Qt import QtCore, QtGui

import pyqtgraph as pg
import pyqtgraph.opengl as gl

import numpy as np

class Window():
	def __init__(self, width=500, height=500, x_offset=500, y_offset=200):
		self.app = QApplication(sys.argv)
		#self.app = pg.QtGui.QApplication.exec_()
		# pg.mkQApp()
		self.w = gl.GLViewWidget()
		self.w.setWindowTitle('Интерфейс')
		self.w.resize(width, height)
		self.w.move(x_offset, y_offset)

	def set_color_grid(self, R=255, G=255, B=255, A=100):
		self.color = (R, G, B, A)

	def set_coord(self):
		self.axis = gl.GLAxisItem(size = QtGui.QVector3D(50,50,50))
		self.w.addItem(self.axis)

	def create_grid(self):
		self.xgrid = gl.GLGridItem(size = QtGui.QVector3D(50,50,1), color=self.color)
		self.ygrid = gl.GLGridItem(size = QtGui.QVector3D(50,50,1), color=self.color)
		self.zgrid = gl.GLGridItem(size = QtGui.QVector3D(50,50,1), color=self.color)

		self.w.addItem(self.xgrid)
		self.w.addItem(self.ygrid)
		self.w.addItem(self.zgrid)

		self.xgrid.rotate(90, 0, 1, 0)
		self.ygrid.rotate(90, 1, 0, 0)

		self.xgrid.scale(1, 1, 1)
		self.ygrid.scale(1, 1, 1)
		self.zgrid.scale(1, 1, 1)

	def create_line(self, points):
		self.line = gl.GLLinePlotItem(pos=points, color=(255,0,0,255), width=1, antialias="lines",mode="line_strip")
		self.w.addItem(self.line)

	def update():
		self.w.show()

	def print_window(self):
		self.w.show()
		#sys.exit(self.app.exec_())

a = Window(1000, 800, 0, 0)
# a.set_color_grid(255, 255, 255, 10)
# a.create_grid()
a.set_coord()
a.create_line(np.array([[10,10,10],[10,10,29],[29,10,29],[29,10,10],[10,29,10],[10,29,29],[29,29,29],[29,29,10]]))
a.print_window()