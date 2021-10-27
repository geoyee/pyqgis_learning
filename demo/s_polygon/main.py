## console
from qgis.core import *
from demo.view import showgeoms


# 边界
l1 = QgsLineString([
    QgsPoint(0, 0),
    QgsPoint(1, 0),
    QgsPoint(1, 1),
    QgsPOINT(0, 1)
])
showgeoms([l1], "l1")

# 面
p2 = QgsPolygon()
p2.setExteriorRing(QgsLineString(l1))
showgeoms([p2], "p2")

# 挖洞
p3 = QgsPolygon(p2)
inring = QgsLineString(
    [0.4, 0.6, 0.6, 0.4], 
    [0.7, 0.7, 0.2, 0.2]
)
p3.addInteriorRing(inring)
showgeoms([p3], "p3")