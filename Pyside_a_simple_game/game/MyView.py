# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'view.ui'
#
# Created: Wed Nov 09 18:13:47 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MyGame(object):
    def setupUi(self, MyGame):
        MyGame.setObjectName("MyGame")
        MyGame.resize(862, 321)
        self.gridLayoutWidget = QtGui.QWidget(MyGame)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 20, 141, 291))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.spiele = QtGui.QLabel(self.gridLayoutWidget)
        self.spiele.setText("")
        self.spiele.setObjectName("spiele")
        self.gridLayout.addWidget(self.spiele, 4, 1, 1, 1)
        self.label_5 = QtGui.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setItalic(True)
        font.setBold(True)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.gesamt = QtGui.QLabel(self.gridLayoutWidget)
        self.gesamt.setText("")
        self.gesamt.setObjectName("gesamt")
        self.gridLayout.addWidget(self.gesamt, 3, 1, 1, 1)
        self.label_4 = QtGui.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.falsch = QtGui.QLabel(self.gridLayoutWidget)
        self.falsch.setText("")
        self.falsch.setObjectName("falsch")
        self.gridLayout.addWidget(self.falsch, 2, 1, 1, 1)
        self.label_3 = QtGui.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.korrekt = QtGui.QLabel(self.gridLayoutWidget)
        self.korrekt.setText("")
        self.korrekt.setObjectName("korrekt")
        self.gridLayout.addWidget(self.korrekt, 1, 1, 1, 1)
        self.label = QtGui.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.offen = QtGui.QLabel(self.gridLayoutWidget)
        self.offen.setText("")
        self.offen.setObjectName("offen")
        self.gridLayout.addWidget(self.offen, 0, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_6 = QtGui.QLabel(MyGame)
        self.label_6.setGeometry(QtCore.QRect(190, 10, 651, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.horizontalLayoutWidget = QtGui.QWidget(MyGame)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(190, 250, 656, 61))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_neu = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_neu.setObjectName("pushButton_neu")
        self.horizontalLayout_2.addWidget(self.pushButton_neu)
        self.pushButton_ende = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_ende.setObjectName("pushButton_ende")
        self.horizontalLayout_2.addWidget(self.pushButton_ende)
        self.gridLayoutWidget_3 = QtGui.QWidget(MyGame)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(190, 60, 656, 189))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout_4 = QtGui.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.pushButton_13 = QtGui.QPushButton(self.gridLayoutWidget_3)
        self.pushButton_13.setObjectName("pushButton_13")
        self.gridLayout_4.addWidget(self.pushButton_13, 4, 3, 1, 1)
        self.pushButton_3 = QtGui.QPushButton(self.gridLayoutWidget_3)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout_4.addWidget(self.pushButton_3, 2, 3, 1, 1)
        self.pushButton_10 = QtGui.QPushButton(self.gridLayoutWidget_3)
        self.pushButton_10.setObjectName("pushButton_10")
        self.gridLayout_4.addWidget(self.pushButton_10, 3, 5, 1, 1)
        self.pushButton_7 = QtGui.QPushButton(self.gridLayoutWidget_3)
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout_4.addWidget(self.pushButton_7, 3, 2, 1, 1)
        self.pushButton_4 = QtGui.QPushButton(self.gridLayoutWidget_3)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout_4.addWidget(self.pushButton_4, 2, 4, 1, 1)
        self.pushButton_11 = QtGui.QPushButton(self.gridLayoutWidget_3)
        self.pushButton_11.setObjectName("pushButton_11")
        self.gridLayout_4.addWidget(self.pushButton_11, 4, 1, 1, 1)
        self.pushButton_14 = QtGui.QPushButton(self.gridLayoutWidget_3)
        self.pushButton_14.setObjectName("pushButton_14")
        self.gridLayout_4.addWidget(self.pushButton_14, 4, 4, 1, 1)
        self.pushButton_5 = QtGui.QPushButton(self.gridLayoutWidget_3)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout_4.addWidget(self.pushButton_5, 2, 5, 1, 1)
        self.pushButton_8 = QtGui.QPushButton(self.gridLayoutWidget_3)
        self.pushButton_8.setObjectName("pushButton_8")
        self.gridLayout_4.addWidget(self.pushButton_8, 3, 3, 1, 1)
        self.pushButton_12 = QtGui.QPushButton(self.gridLayoutWidget_3)
        self.pushButton_12.setObjectName("pushButton_12")
        self.gridLayout_4.addWidget(self.pushButton_12, 4, 2, 1, 1)
        self.pushButton_15 = QtGui.QPushButton(self.gridLayoutWidget_3)
        self.pushButton_15.setObjectName("pushButton_15")
        self.gridLayout_4.addWidget(self.pushButton_15, 4, 5, 1, 1)
        self.pushButton_9 = QtGui.QPushButton(self.gridLayoutWidget_3)
        self.pushButton_9.setObjectName("pushButton_9")
        self.gridLayout_4.addWidget(self.pushButton_9, 3, 4, 1, 1)
        self.pushButton = QtGui.QPushButton(self.gridLayoutWidget_3)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_4.addWidget(self.pushButton, 2, 1, 1, 1)
        self.pushButton_6 = QtGui.QPushButton(self.gridLayoutWidget_3)
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout_4.addWidget(self.pushButton_6, 3, 1, 1, 1)
        self.pushButton_2 = QtGui.QPushButton(self.gridLayoutWidget_3)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_4.addWidget(self.pushButton_2, 2, 2, 1, 1)

        self.retranslateUi(MyGame)
        QtCore.QObject.connect(self.pushButton_ende, QtCore.SIGNAL("clicked()"), MyGame.close)
        QtCore.QMetaObject.connectSlotsByName(MyGame)

    def retranslateUi(self, MyGame):
        MyGame.setWindowTitle(QtGui.QApplication.translate("MyGame", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("MyGame", "Spiele", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MyGame", "gesamt:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MyGame", "falsch:", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MyGame", "korrekt:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MyGame", "offen:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("MyGame", "Drücken Sie die Buttons in aufsteigender Richtung!", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_neu.setText(QtGui.QApplication.translate("MyGame", "Neu", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_ende.setText(QtGui.QApplication.translate("MyGame", "Ende", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_13.setText(QtGui.QApplication.translate("MyGame", "PushButton", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_3.setText(QtGui.QApplication.translate("MyGame", "PushButton", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_10.setText(QtGui.QApplication.translate("MyGame", "PushButton", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_7.setText(QtGui.QApplication.translate("MyGame", "PushButton", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_4.setText(QtGui.QApplication.translate("MyGame", "PushButton", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_11.setText(QtGui.QApplication.translate("MyGame", "PushButton", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_14.setText(QtGui.QApplication.translate("MyGame", "PushButton", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_5.setText(QtGui.QApplication.translate("MyGame", "PushButton", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_8.setText(QtGui.QApplication.translate("MyGame", "PushButton", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_12.setText(QtGui.QApplication.translate("MyGame", "PushButton", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_15.setText(QtGui.QApplication.translate("MyGame", "PushButton", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_9.setText(QtGui.QApplication.translate("MyGame", "PushButton", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("MyGame", "PushButton", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_6.setText(QtGui.QApplication.translate("MyGame", "PushButton", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QtGui.QApplication.translate("MyGame", "PushButton", None, QtGui.QApplication.UnicodeUTF8))
