## console
from qgis.core import (
    QgsPoint, QgsFeature, QgsVectorLayer, QgsProject)
import random


NUMS = 100
feats = []
for i in range(NUMS):
    # 随机创建坐标
    x = random.random() * 360 - 180
    y = random.random() * 180 - 90
    pt = QgsPoint(x, y)  # 创建点
    feat = QgsFeature()
    feat.setGeometry(pt)
    feats.append(feat)
# 创建图层
p_layer = QgsVectorLayer("point", "random_point", "memory")
pr = p_layer.dataProvider()
is_ok, fts = pr.addFeatures(feats)  # 添加图层
p_layer.updateExtents()  # 更新事件
QgsProject.instance().addMapLayer(p_layer)  # 图层添加到项目
iface.zoomFull()