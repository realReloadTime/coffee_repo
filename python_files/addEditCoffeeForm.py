# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addEditCoffeeForm.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi2(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(429, 573)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(10, 440, 401, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.pushButton_delete = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_delete.setGeometry(QtCore.QRect(110, 500, 291, 41))
        self.pushButton_delete.setObjectName("pushButton_delete")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 0, 391, 381))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.spinBox_id = QtWidgets.QSpinBox(self.layoutWidget)
        self.spinBox_id.setMinimumSize(QtCore.QSize(270, 0))
        self.spinBox_id.setMaximum(999999999)
        self.spinBox_id.setObjectName("spinBox_id")
        self.horizontalLayout.addWidget(self.spinBox_id)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.lineEdit_name = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_name.setMaximumSize(QtCore.QSize(270, 20))
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.horizontalLayout_4.addWidget(self.lineEdit_name)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.comboBox_roast = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox_roast.setMinimumSize(QtCore.QSize(270, 20))
        self.comboBox_roast.setObjectName("comboBox_roast")
        self.horizontalLayout_2.addWidget(self.comboBox_roast)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.comboBox_type = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox_type.setMinimumSize(QtCore.QSize(270, 0))
        self.comboBox_type.setObjectName("comboBox_type")
        self.horizontalLayout_3.addWidget(self.comboBox_type)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)
        self.lineEdit_taste = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_taste.setMaximumSize(QtCore.QSize(270, 20))
        self.lineEdit_taste.setObjectName("lineEdit_taste")
        self.horizontalLayout_5.addWidget(self.lineEdit_taste)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_6.addWidget(self.label_6)
        self.lineEdit_cost = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_cost.setMaximumSize(QtCore.QSize(270, 16777215))
        self.lineEdit_cost.setObjectName("lineEdit_cost")
        self.horizontalLayout_6.addWidget(self.lineEdit_cost)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_7 = QtWidgets.QLabel(self.layoutWidget)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_7.addWidget(self.label_7)
        self.comboBox_volume = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox_volume.setMinimumSize(QtCore.QSize(270, 0))
        self.comboBox_volume.setObjectName("comboBox_volume")
        self.horizontalLayout_7.addWidget(self.comboBox_volume)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 460, 391, 41))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_8 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_8.addWidget(self.label_8)
        self.comboBox_item = QtWidgets.QComboBox(self.layoutWidget1)
        self.comboBox_item.setObjectName("comboBox_item")
        self.horizontalLayout_8.addWidget(self.comboBox_item)
        self.label_9 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_8.addWidget(self.label_9)
        self.lineEdit_value = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lineEdit_value.setObjectName("lineEdit_value")
        self.horizontalLayout_8.addWidget(self.lineEdit_value)
        self.pushButton_add = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_add.setGeometry(QtCore.QRect(110, 400, 291, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_add.sizePolicy().hasHeightForWidth())
        self.pushButton_add.setSizePolicy(sizePolicy)
        self.pushButton_add.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton_add.setObjectName("pushButton_add")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(10, 370, 391, 31))
        self.label_10.setWordWrap(True)
        self.label_10.setObjectName("label_10")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 429, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Изменить данные..."))
        self.pushButton_delete.setText(_translate("MainWindow", "Удалить"))
        self.label.setText(_translate("MainWindow", "ID(необязательно)"))
        self.label_4.setText(_translate("MainWindow", "Название"))
        self.label_2.setText(_translate("MainWindow", "Обжарка"))
        self.label_3.setText(_translate("MainWindow", "Тип"))
        self.label_5.setText(_translate("MainWindow", "Вкус"))
        self.label_6.setText(_translate("MainWindow", "Стоимость"))
        self.label_7.setText(_translate("MainWindow", "Объем"))
        self.label_8.setText(_translate("MainWindow", "Удалить запись, где:"))
        self.label_9.setText(_translate("MainWindow", "="))
        self.pushButton_add.setText(_translate("MainWindow", "Сохранить"))
        self.label_10.setText(_translate("MainWindow", "Установите существующее значение ID, чтобы изменить существующую запись"))