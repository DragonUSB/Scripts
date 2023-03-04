import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget

btn = QPushButton('Este es un Button', w)
btn.setToolTip('This is a <b>QPushButton</b> widget')
btn.move(50, 50)
	
if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = QWidget()
    w.setWindowTitle('Ventana PyQT-5')
    w.setWindowIcon(QIcon('icon.ico'))
    w.resize(1280, 720)
    w.show()
	
    sys.exit(app.exec_())	