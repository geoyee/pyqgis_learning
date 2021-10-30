from qgis.core import *


def getgtypes():
    return 'point', 'linestring', 'polygon', \
           'multipoint','multilinestring','multipolygon'


def showgeoms(geoms, name="tmp", gtype=None):
    if gtype is None:
        gtype = geoms[0].constGet().geometryType() \
                if isinstance(geoms[0], QgsGeometry) else geoms[0].geometryType()
        gtype = gtype.lower()
    if gtype not in getgtypes():
        raise Exception("gtype should be one of :{" + ','.join(getgtypes()) + "}")
    vl = QgsVectorLayer(gtype, name, "memory")
    pr = vl.dataProvider()
    feats = []
    for geom in geoms:
        feat = QgsFeature()
        feat.setGeometry(geom)
        feats.append(feat)
    pr.addFeatures(feats)
    QgsProject.instance().addMapLayer(vl)
    iface.zoomFull()