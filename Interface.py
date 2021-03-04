import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QPushButton)
from PyQt5.QtCore import pyqtSlot, QRect, QCoreApplication

class Window():
	def __init__(self, width=500, height=500, x_offset=500, y_offset=200):
		self.app = QApplication(sys.argv)
		self.w = QWidget()
		self.w.setWindowTitle('Интерфейс')
		self.w.resize(width, height)
		self.w.move(x_offset, y_offset)

	def print_window(self):
		self.w.show()
		sys.exit(self.app.exec_())

a = Window(800, 600)
a.print_window()