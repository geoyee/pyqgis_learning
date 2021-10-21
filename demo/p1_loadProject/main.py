from qgis.core import QgsApplication
QgsApplication.setPrefixPath("D:/QGIS/apps/qgis-ltr", True)

from qgis.core import QgsProject


proj = QgsProject.instance()
print(proj.fileName())  # 空，没有文件
proj.read(r"demo\p1_loadProject\test.qgz")
print(proj.fileName())  # 文件路径