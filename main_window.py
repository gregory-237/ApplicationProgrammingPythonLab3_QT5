import sys

from PyQt5.QtCore import Qt, QEvent
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import *


class Window(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.initUI()

    def initUI(self) -> None:
        self.center()
        self.setWindowTitle('Dollar rates')
        self.setWindowIcon(QIcon('img/web.png'))
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)
        self.show()

    def center(self) -> None:
        widget_rect = self.frameGeometry()
        pc_rect = QDesktopWidget().availableGeometry().center()
        widget_rect.moveCenter(pc_rect)
        self.move(widget_rect.center())

    def closeEvent(self, event) -> None:
        reply = QMessageBox.question(self, "Don't leave please(",
            "Are you sure to quit?", QMessageBox.Yes |
            QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())




