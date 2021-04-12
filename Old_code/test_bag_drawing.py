import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui
import pyqtgraph.opengl as gl
import numpy as np
import sys
import time

class test_class():
	def __init__(self):
		self.app = pg.mkQApp("GLScatterPlotItem Example")
		self.w = gl.GLViewWidget()
		self.w.setWindowTitle('Интерфейс')
		self.w.resize(300, 300)
		self.w.move(400, 200)

		self.w.show()

	def create_grid(self):
		self.xgrid = gl.GLGridItem(size = QtGui.QVector3D(50,50,1), color=(50, 50,50, 150))
		self.ygrid = gl.GLGridItem(size = QtGui.QVector3D(50,50,1), color=(50, 50,50, 150))
		self.zgrid = gl.GLGridItem(size = QtGui.QVector3D(50,50,1), color=(50, 50,50, 150))

		self.w.addItem(self.xgrid)
		self.w.addItem(self.ygrid)
		self.w.addItem(self.zgrid)

		self.xgrid.rotate(90, 1, 0, 0)
		self.ygrid.rotate(90, 0, 1, 0)

		self.xgrid.scale(1, 1, 1)
		self.ygrid.scale(1, 1, 1)
		self.zgrid.scale(1, 1, 1)

	def create_neuron(self, xyz_neuron, size_point=8, color_point=(0, 255, 0, 255)):
		self.xyz_neuron = xyz_neuron
		self.point = gl.GLScatterPlotItem(pos=xyz_neuron, size=size_point, color=color_point)
		# self.list_obj_points.append(point)
		self.w.addItem(self.point)


		self.t = QtCore.QTimer()
		self.t.timeout.connect(self.update)
		self.t.start(100)

	def update(self):
		x, y, z = self.xyz_neuron

		self.xyz_neuron = np.array([x + 0, y + 1, z + 0])
		self.point.setData(pos=self.xyz_neuron)



	def start(self):
		if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
			print("Запуск")
			QtGui.QApplication.instance().exec_()
			print("Конец")

a = test_class()
a.create_grid()
a.create_neuron(np.array([0, 0, 0]))

a.start()