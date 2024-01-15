import sys
from PyQt5.QtWidgets import QDesktopWidget, QApplication
app = QApplication(sys.argv)
q = QDesktopWidget().availableGeometry()
suma = 960+540
suma2=q.width()+q.height()
suma4=suma2/suma
suma3=None
if suma4 >= 2:
    suma3=suma4-1

elif suma4<=1.4:
    suma3=suma4-0.3

else:
    suma3=suma4-0.5

