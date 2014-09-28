#!/usr/local/bin/python
# -*- coding: utf-8 -*-
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import mainwindow

if __name__ == '__main__':
	import sys

	app = QApplication(sys.argv)

	screen = mainwindow.Form()
	screen.show()

	sys.exit(app.exec_())