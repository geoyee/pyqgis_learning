import numpy as np


# TODO: 效率低
def raster2ndarray(lyr):
    '''
        input: lyr(QgsMapLayerType.QgsRasterLayer)
        output: _(ndarray)
    '''
    provider= lyr.dataProvider()
    # 多少个波段
    blocks = []
    for c in range(lyr.bandCount()):
        blocks.append(provider.block((c + 1), lyr.extent(), lyr.width(), lyr.height()))
    values=[]
    for i in range(lyr.width()):
        tmps = []
        for j in range(lyr.height()):
            tmps.append([blocks[k].value(i, j) for k in range(lyr.bandCount())])
        values.append(tmps)
    return np.array(values)


def convert_coord(point, tform):
    olp = np.ones((1, 3))
    olp[0, :2] = point
    nwp = np.dot(tform, olp.T)
    return nwp.T[0, :2]