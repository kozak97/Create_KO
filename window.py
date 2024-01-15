import sys
from PyQt5.QtWidgets import QDesktopWidget, QApplication
app = QApplication(sys.argv)
q = QDesktopWidget().availableGeometry()
suma = 960+540
suma2=q.width()+q.height()
suma3=suma2/suma-0.2
if suma3 >= 1.3:
    p1 = 30
    p2 = 14
    p3 = 10

else:
    p1 = 15
    p2 = 14
    p3 = 10
