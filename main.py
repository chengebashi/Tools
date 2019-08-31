import sys
from PyQt5 import  QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from windows import Ui_MainWindow
import swap
import re, threading

class MyMainWindow(QMainWindow, Ui_MainWindow):
    info1 = ''
    def __init__(self):
        super(MyMainWindow, self).__init__()
        self.setupUi(self)


    def start_swap(self):
        # a = self.lineEdit.text()
        # b = re.match('^\d+$', a)
        # if b:
        num = self.lineEdit.text()
        b = re.match('^\d+$', num)
        if self.info1 == '':
            box = QtWidgets.QMessageBox()
            box.warning(self, "提示", "你还没选转换成什么呢？")
        if self.info1 == 28:
            if b:
                now = swap.second8(num)
                self.textBrowser.append(str(now))
            else:
                box = QtWidgets.QMessageBox()
                box.warning(self, "提示", "输入有误，请重新输入!")
        elif self.info1 == 210:
            if b:
                now = swap.second10(num)
                self.textBrowser.append(str(now))
            else:
                box = QtWidgets.QMessageBox()
                box.warning(self, "提示", "输入有误，请重新输入!")
        elif self.info1 == 216:
            if b:
                now = swap.second16(num)
                self.textBrowser.append(str(now))
            else:
                box = QtWidgets.QMessageBox()
                box.warning(self, "提示", "输入有误，请重新输入!")

        elif self.info1 == 82:
            if b:
                now = swap.eighth2(num)
                self.textBrowser.append(str(now))
            else:
                box = QtWidgets.QMessageBox()
                box.warning(self, "提示", "输入有误，请重新输入!")

        elif self.info1 == 810:
            if b:
                now = swap.eighth10(num)
                self.textBrowser.append(str(now))
            else:
                box = QtWidgets.QMessageBox()
                box.warning(self, "提示", "输入有误，请重新输入!")

        elif self.info1 == 816:
            if b:
                now = swap.eighth16(num)
                self.textBrowser.append(str(now))
            else:
                box = QtWidgets.QMessageBox()
                box.warning(self, "提示", "输入有误，请重新输入!")
        elif self.info1 == 102:
            if b:
                now = swap.tenth2(num)
                self.textBrowser.append(str(now))
            else:
                box = QtWidgets.QMessageBox()
                box.warning(self, "提示", "输入有误，请重新输入!")

        elif self.info1 == 108:
            if b:
                now = swap.tenth8(num)
                self.textBrowser.append(str(now))
            else:
                box = QtWidgets.QMessageBox()
                box.warning(self, "提示", "输入有误，请重新输入!")

        elif self.info1 == 1016:
            if b:
                now = swap.tenth16(num)
                self.textBrowser.append(str(now))
            else:
                box = QtWidgets.QMessageBox()
                box.warning(self, "提示", "输入有误，请重新输入!")

        elif self.info1 == 162:
            if b:
                now = swap.sixth2(num)
                self.textBrowser.append(str(now))
            else:
                box = QtWidgets.QMessageBox()
                box.warning(self, "提示", "输入有误，请重新输入!")

        elif self.info1 == 168:
            if b:
                now = swap.sixth8(num)
                self.textBrowser.append(str(now))
            else:
                box = QtWidgets.QMessageBox()
                box.warning(self, "提示", "输入有误，请重新输入!")

        elif self.info1 == 1610:
            if b:
                now = swap.sixth10(num)
                self.textBrowser.append(str(now))
            else:
                box = QtWidgets.QMessageBox()
                box.warning(self, "提示", "输入有误，请重新输入!")

    def second_eight(self):
        # if self.radioButton.text() == '二进制转八进制':
            # if self.radioButton.isChecked()==True:
            # num = self.lineEdit.text()
            # self.info1 = swap.second8(num)
        self.info1 = 28

    def second_ten(self):
        self.info1 = 210

    def second_sixteen(self):
        self.info1 = 216

    def eight_two(self):
        self.info1 = 82

    def eight_ten(self):
        self.info1 = 810

    def eigh_sixteen(self):
        self.info1 = 816

    def ten_two(self):
        self.info1 = 102

    def ten_eight(self):
        self.info1 = 108

    def ten_sixteen(self):
        self.info1 = 1016

    def sixteen_two(self):
        self.info1 = 162

    def sixteen_eight(self):
        self.info1 = 168

    def sixteen_ten(self):
        self.info1 = 1610


if __name__ == '__main__':
    app = QApplication(sys.argv)
    wi = MyMainWindow()
    wi.show()
    sys.exit(app.exec_())
