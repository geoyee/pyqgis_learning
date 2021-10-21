# 需要设置vscode的解释器为python-qgis-ltr.bat
from qgis.core import QgsApplication
QgsApplication.setPrefixPath("D:/QGIS/apps/qgis-ltr", True)


qgs = QgsApplication([], False)
qgs.initQgis()
pass
qgs.exitQgis()