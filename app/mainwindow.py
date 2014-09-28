# -*- coding: utf-8 -*-

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from shapely.wkt import loads
import re

class Form(QWidget):
	def __init__(self, parent=None):
		super(Form, self).__init__(parent)

		self.startButton = QPushButton("&Start")
		self.nextButton = QPushButton("&Next")
		self.scene = QGraphicsScene()
		self.view = QGraphicsView()
		self.view.setScene(self.scene)
		self.view.setMinimumSize(400, 400)    

		sidePanel = QWidget()
		sideLayout = QVBoxLayout()
		sideLayout.addWidget(self.startButton)
		sideLayout.addWidget(self.nextButton)
		sidePanel.setLayout(sideLayout)

		mainLayout = QHBoxLayout()
		mainLayout.addWidget(sidePanel, 0, Qt.AlignTop)
		mainLayout.addWidget(self.view)
		self.setLayout(mainLayout)    
    
		self.startButton.clicked.connect(self.initSimulation)
		self.startButton.clicked.connect(self.doStep)
	
		self.setWindowTitle("Robot localization demo")

	def initSimulation(self):

		pattern = 'POLYGON.?\(\([0-9,\. \-]+\)\)'

		with open('test_map.csv') as f:
			content = f.readlines()
			for line in content:
				m = re.search(pattern, line)
				if m:
					poly = loads(m.group(0))
					#print(poly.exterior.coords)
					qpoly = QPolygonF()
					for x, y in poly.exterior.coords:						
						qpoly.append(QPointF(x,y))
					self.scene.addPolygon(qpoly, QPen(), QBrush(QColor(179,112,123)))
			self.view.fitInView(self.scene.sceneRect())

	def doStep(self):
		pass