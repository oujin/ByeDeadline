import sys
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout
from PyQt5.QtGui import QIcon
# from PyQt5 import QtCore
from PyQt5.QtCore import QSize


class UI(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(500, 400)
        self.setWindowIcon(QIcon('src/icon.png'))
        self.setWindowTitle('ByeDDL')
        self.doc_button = QPushButton()
        self.doc_button.setIcon(QIcon('src/doc.png'))
        self.doc_button.setIconSize(QSize(200, 200))
        self.ppt_button = QPushButton()
        self.ppt_button.setIcon(QIcon('src/ppt.png'))
        self.ppt_button.setIconSize(QSize(200, 200))
        self.xls_button = QPushButton()
        self.xls_button.setIcon(QIcon('src/xls.png'))
        self.xls_button.setIconSize(QSize(200, 200))
        self.pdf_button = QPushButton()
        self.pdf_button.setIcon(QIcon('src/pdf.png'))
        self.pdf_button.setIconSize(QSize(200, 200))
        self.layer1 = QVBoxLayout()
        self.layer2 = QVBoxLayout()
        self.layer1.addWidget(self.pdf_button)
        self.layer1.addWidget(self.doc_button)
        self.layer2.addWidget(self.ppt_button)
        self.layer2.addWidget(self.xls_button)
        self.layer3 = QHBoxLayout()
        self.layer3.addLayout(self.layer1)
        self.layer3.addLayout(self.layer2)
        self.setLayout(self.layer3)
    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    windows = UI()
    windows.show()
    sys.exit(app.exec())
