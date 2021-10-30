## console
from qgis import *
import numpy as np


r1 = QgsGeometry.fromRect(
    QgsRectangle(QgsPointXY(0.0, 0.0), QgsPointXY(10.0, 10.0)))
r2 = QgsGeometry.fromRect(
    QgsRectangle(QgsPointXY(5.0, 5.0), QgsPointXY(15.0, 15.0)))
showgeoms([r1], "r1")
showgeoms([r2], "r2")
# 交集
p1 = r1.intersection(r2)
showgeoms([p1], "p1")
# 并集
p2 = r1.combine(r2)
showgeoms([p2], "p2")
# 差集
p3 = r1.difference(r2)  # r1-r2
showgeoms([p3], "p3")
p4 = r2.difference(r1)  # r2-r1
showgeoms([p4], "p4")