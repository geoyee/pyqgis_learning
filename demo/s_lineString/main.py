## console
import math
import random
from qgis.core import *
from demo.view import showgeoms


lines = []
pts = [QgsPoint(x, math.cos(x) + (x % 3 - 1) * random.random() * 5) \
       for x in range(100)]
L1 = QgsLineString()
L1.setPoints(pts)
showgeoms([L1], "L1")
L1.addVertex(QgsPoint(100, 9))