# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Form_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(680, 453)
        font = QtGui.QFont()
        font.setPointSize(12)
        Form.setFont(font)
        self.twStaffs = QtWidgets.QTableWidget(Form)
        self.twStaffs.setGeometry(QtCore.QRect(10, 231, 661, 211))
        self.twStaffs.setObjectName("twStaffs")
        self.twStaffs.setColumnCount(0)
        self.twStaffs.setRowCount(0)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(21, 11, 257, 211))
        self.widget.setObjectName("widget")
        self.formLayout = QtWidgets.QFormLayout(self.widget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.leFio = QtWidgets.QLineEdit(self.widget)
        self.leFio.setObjectName("leFio")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.leFio)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.splitter = QtWidgets.QSplitter(self.widget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.rbMale = QtWidgets.QRadioButton(self.splitter)
        self.rbMale.setObjectName("rbMale")
        self.rbFamale = QtWidgets.QRadioButton(self.splitter)
        self.rbFamale.setObjectName("rbFamale")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.splitter)
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.spAge = QtWidgets.QSpinBox(self.widget)
        self.spAge.setObjectName("spAge")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.spAge)
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.lePhone = QtWidgets.QLineEdit(self.widget)
        self.lePhone.setObjectName("lePhone")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lePhone)
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.leEmail = QtWidgets.QLineEdit(self.widget)
        self.leEmail.setObjectName("leEmail")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.leEmail)
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.cbPost = QtWidgets.QComboBox(self.widget)
        self.cbPost.setObjectName("cbPost")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.cbPost)
        self.label_7 = QtWidgets.QLabel(self.widget)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.spAge_2 = QtWidgets.QSpinBox(self.widget)
        self.spAge_2.setObjectName("spAge_2")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.spAge_2)
        self.widget1 = QtWidgets.QWidget(Form)
        self.widget1.setGeometry(QtCore.QRect(320, 10, 80, 95))
        self.widget1.setObjectName("widget1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pbOpen = QtWidgets.QPushButton(self.widget1)
        self.pbOpen.setObjectName("pbOpen")
        self.verticalLayout.addWidget(self.pbOpen)
        self.pbInsert = QtWidgets.QPushButton(self.widget1)
        self.pbInsert.setObjectName("pbInsert")
        self.verticalLayout.addWidget(self.pbInsert)
        self.pbDelete = QtWidgets.QPushButton(self.widget1)
        self.pbDelete.setObjectName("pbDelete")
        self.verticalLayout.addWidget(self.pbDelete)
        self.rbFamale.raise_()
        self.rbMale.raise_()
        self.twStaffs.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.leFio.raise_()
        self.lePhone.raise_()
        self.leEmail.raise_()
        self.spAge.raise_()
        self.cbPost.raise_()
        self.spAge_2.raise_()
        self.pbOpen.raise_()
        self.pbInsert.raise_()
        self.pbDelete.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "????????????????????"))
        self.label.setText(_translate("Form", "??????"))
        self.label_2.setText(_translate("Form", "??????"))
        self.rbMale.setText(_translate("Form", "??????"))
        self.rbFamale.setText(_translate("Form", "??????"))
        self.label_3.setText(_translate("Form", "??????????????"))
        self.label_4.setText(_translate("Form", "??????????????"))
        self.label_5.setText(_translate("Form", "??????????"))
        self.label_6.setText(_translate("Form", "??????????????????"))
        self.label_7.setText(_translate("Form", "????????"))
        self.pbOpen.setText(_translate("Form", "??????????????"))
        self.pbInsert.setText(_translate("Form", "????????????????"))
        self.pbDelete.setText(_translate("Form", "??????????????"))
