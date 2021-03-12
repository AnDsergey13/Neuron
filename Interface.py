# http://www.pyqtgraph.org/

"""
pip install PyOpenGL PyOpenGL_accelerate
pip install PyQt5
"""

"""
Примеры
pyqtgraph.examples.run()
raspberri https://github.com/pyqtgraph/pyqtgraph/issues/1260
"""
# import Neuron_controller as nc

import sys
# from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QPushButton)
from PyQt5.QtWidgets import QApplication
from pyqtgraph.Qt import QtCore, QtGui

import pyqtgraph as pg
import pyqtgraph.opengl as gl

import numpy as np

class Window():
	def __init__(self, width=500, height=500, x_offset=500, y_offset=200):
		self.app = QApplication(sys.argv)
		self.w = gl.GLViewWidget()
		self.w.setWindowTitle('Интерфейс')
		self.w.resize(width, height)
		self.w.move(x_offset, y_offset)

		self.list_obj_points = []

	def set_color_grid(self, R=255, G=255, B=255, A=100):
		self.color = (R, G, B, A)

	def set_coord(self):
		axis = gl.GLAxisItem(size = QtGui.QVector3D(50,50,50))
		self.w.addItem(axis)

	def create_grid(self):
		self.xgrid = gl.GLGridItem(size = QtGui.QVector3D(50,50,1), color=self.color)
		self.ygrid = gl.GLGridItem(size = QtGui.QVector3D(50,50,1), color=self.color)
		self.zgrid = gl.GLGridItem(size = QtGui.QVector3D(50,50,1), color=self.color)

		self.w.addItem(self.xgrid)
		self.w.addItem(self.ygrid)
		self.w.addItem(self.zgrid)

		self.xgrid.rotate(90, 1, 0, 0)
		self.ygrid.rotate(90, 1, 0, 0)

		self.xgrid.scale(1, 1, 1)
		self.ygrid.scale(1, 1, 1)
		self.zgrid.scale(1, 1, 1)

	def create_line(self, points):
		line = gl.GLLinePlotItem(pos=points, color=(255,0,0,255), width=1, antialias="lines",mode="line_strip")
		self.w.addItem(line)

	def gen_line_for_cube(self, points):
		""" Создание массива точек для отрисовки границ куба в пространстве с помощью линии"""
		def gen_index():
			""" Возвращает при вызове следующие индексы для массива 0, 1, 1, 2, 2, 3, 3, 0"""
			l = [i for i in range(4)]

			# Разворачиваем список для удобного взятия отрицательного индекса
			for i in reversed(range(len(l))):
				yield l[-i-1]
				yield l[-i]

		def replace(xyz, up_y_cube):
			""" Преобразует координаты точки нижней плоскости, в координаты точки верхней плоскости, путём замены в координатах у(игрика)"""
			xyz = np.delete(xyz, 1)
			xyz = np.insert(xyz, 1, up_y_cube)
			return xyz

		up_y_cube = points[4][1]
		new_arr = np.array(())
		get_index = gen_index()

		# Создаём точки прохода линии для нижней плоскости и для примыкающих веритикальных рёбер
		for i in range(4):
			new_arr = np.concatenate([new_arr, points[next(get_index)]])
			index = next(get_index)
			new_arr = np.concatenate([new_arr, points[index]])
			new_arr = np.concatenate([new_arr, replace(points[index], up_y_cube)])
		# В связи с тем что массив имеет вид [x0, y0, z0, x1, y1, z1, x2, y2 ,z2, ...]
		# Преобразуем его в нормальный вид [[x0, y0, z0], [x1, y1, z1], [x2, y2 ,z2], ...]
		new_arr = np.reshape(new_arr, (int(len(new_arr)/3), 3))
		# Добавляем точки верхней плоскости
		new_arr = np.concatenate([new_arr, points[5:]])
		# Добавляем последнюю точку, которая закрывает последнее ребро
		new_arr = np.append(new_arr, [points[4]], axis = 0)
		return new_arr

	def create_point(self, xyz, size=3):
		point = gl.GLScatterPlotItem(pos=xyz, size=size, color=(0,255,0,255))
		self.list_obj_points.append(point)
		self.w.addItem(point)

	def draw_neurons(self, obj_neuron_controller=None, time=50):
		self.time_update = time
		self.nc = obj_neuron_controller

		self.t = QtCore.QTimer()
		self.t.timeout.connect(self.update)
		self.t.start(self.time_update)

	def update(self):
		print(self.list_obj_points)
		for pos_, i in enumerate(self.list_obj_points):
			new_xyz = np.array(self.nc.get_list_xyz()[pos_])
			print(len(self.list_obj_points), new_xyz)
			self.list_obj_points[pos_].setData(pos=new_xyz)

	def print_window(self):
		self.w.show()
		sys.exit(self.app.exec_())


