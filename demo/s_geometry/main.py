from qgis import *
import numpy as np
from demo.view import showgeoms


xs = np.random.random(100) * 100
ys = np.random.random(100) * 100
pts = QgsLineString(xs, ys)
mp = QgsMultiPoint()
_ = [mp.addGeometry(pt) for pt in pts]
gmp = QgsGeometry(mp)
showgeoms([mp], "gmp")
# 外接矩形
bbx = gmp.boundingBox()
print(bbx)
gbbx = QgsGeometry.fromRect(bbx)
print(gbbx)
showgeoms([gbbx], "gbbx")
# 中心点
cd = gmp.centroid()
showgeoms([cd], "centroid")
# 计算缓冲区
bpg = gbbx.buffer(10, 10)
showgeoms([bpg], "bpg")
showgeoms(bpg.get().exteriorRing(), "bpg_p")