import sys
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QLabel
from PyQt5.QtWidgets import QFileDialog, QDialog, QSpinBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize, Qt
from faker import file_faker
import random


class UI(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(500, 400)
        self.setWindowIcon(QIcon('src/icon.png'))
        self.setWindowTitle('ByeDeadline')
        self.doc_button = QPushButton()
        self.doc_button.setIcon(QIcon('src/doc.png'))
        self.doc_button.setIconSize(QSize(200, 200))
        self.doc_button.clicked.connect(lambda: self.pushButton('docx'))
        self.ppt_button = QPushButton()
        self.ppt_button.setIcon(QIcon('src/ppt.png'))
        self.ppt_button.setIconSize(QSize(200, 200))
        self.ppt_button.clicked.connect(lambda: self.pushButton('pptx'))
        self.xls_button = QPushButton()
        self.xls_button.setIcon(QIcon('src/xls.png'))
        self.xls_button.setIconSize(QSize(200, 200))
        self.xls_button.clicked.connect(lambda: self.pushButton('xlsx'))
        self.pdf_button = QPushButton()
        self.pdf_button.setIcon(QIcon('src/pdf.png'))
        self.pdf_button.setIconSize(QSize(200, 200))
        self.pdf_button.clicked.connect(lambda: self.pushButton('pdf'))
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

    def pushButton(self, fType):
        fName = QFileDialog.getSaveFileName(self, 'save', './', f'*.{fType}')
        if fName[0] == '':
            return
        strings = fName[0].split('.')
        fName = '_'.join(strings[:-1])
        dialog = QDialog(self)
        dialog.setFixedSize(160, 80)
        dialog.setWindowTitle('size')
        dialog.setWindowModality(Qt.ApplicationModal)
        spinBox = QSpinBox(dialog)
        spinBox.setRange(1, 2 ** 15)
        spinBox.setValue(1024)
        label1 = QLabel('Size: ', dialog)
        label2 = QLabel('KB', dialog)
        okButton = QPushButton('ok', dialog)

        def clickOK():
            size = spinBox.value() + random.randint(-99, 99)
            size = max(1, size)
            file_faker(size, fName, fType)

        okButton.clicked.connect(clickOK)
        layer1 = QHBoxLayout()
        layer1.addWidget(label1)
        layer1.addWidget(spinBox)
        layer1.addWidget(label2)
        layer2 = QHBoxLayout()
        layer2.addWidget(okButton)
        layer3 = QVBoxLayout()
        layer3.addLayout(layer1)
        layer3.addLayout(layer2)
        dialog.setLayout(layer3)
        dialog.exec()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    windows = UI()
    windows.show()
    sys.exit(app.exec())
