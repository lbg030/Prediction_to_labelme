# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'segmentation.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QGroupBox, QHBoxLayout, QHeaderView,
    QLabel, QMainWindow, QMenu, QMenuBar,
    QSizePolicy, QStatusBar, QTextBrowser, QToolButton,
    QTreeView, QVBoxLayout, QWidget)

class Ui_SemiLabeling(object):
    def setupUi(self, SemiLabeling):
        if not SemiLabeling.objectName():
            SemiLabeling.setObjectName(u"SemiLabeling")
        SemiLabeling.resize(1512, 900)
        SemiLabeling.setMinimumSize(QSize(1200, 900))
        SemiLabeling.setStyleSheet(u"")
        self.actionShow_Image_Counts = QAction(SemiLabeling)
        self.actionShow_Image_Counts.setObjectName(u"actionShow_Image_Counts")
        self.actionShow_Image = QAction(SemiLabeling)
        self.actionShow_Image.setObjectName(u"actionShow_Image")
        self.actionSave_Indexed_Mask = QAction(SemiLabeling)
        self.actionSave_Indexed_Mask.setObjectName(u"actionSave_Indexed_Mask")
        self.actionSave_Indexed_Mask.setCheckable(True)
        self.actionSave_Indexed_Mask.setChecked(True)
        self.centralwidget = QWidget(SemiLabeling)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(-1, -1, 0, -1)
        self.groupBox_7 = QGroupBox(self.centralwidget)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.groupBox_7.setStyleSheet(u"")
        self.toolButton_7 = QToolButton(self.groupBox_7)
        self.toolButton_7.setObjectName(u"toolButton_7")
        self.toolButton_7.setGeometry(QRect(10, 30, 70, 55))

        self.verticalLayout_4.addWidget(self.groupBox_7)

        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setStyleSheet(u"")
        self.toolButton_5 = QToolButton(self.groupBox)
        self.toolButton_5.setObjectName(u"toolButton_5")
        self.toolButton_5.setGeometry(QRect(10, 30, 70, 55))

        self.verticalLayout_4.addWidget(self.groupBox)

        self.verticalLayout_4.setStretch(0, 1)
        self.verticalLayout_4.setStretch(1, 8)

        self.horizontalLayout.addLayout(self.verticalLayout_4)

        self.image_label = QLabel(self.centralwidget)
        self.image_label.setObjectName(u"image_label")
        self.image_label.setStyleSheet(u"")

        self.horizontalLayout.addWidget(self.image_label)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.groupBox_5 = QGroupBox(self.centralwidget)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setStyleSheet(u"")
        self.verticalLayout_6 = QVBoxLayout(self.groupBox_5)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.treeView = QTreeView(self.groupBox_5)
        self.treeView.setObjectName(u"treeView")

        self.verticalLayout_6.addWidget(self.treeView)

        self.textBrowser = QTextBrowser(self.groupBox_5)
        self.textBrowser.setObjectName(u"textBrowser")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textBrowser.sizePolicy().hasHeightForWidth())
        self.textBrowser.setSizePolicy(sizePolicy)
        self.textBrowser.setMinimumSize(QSize(100, 30))

        self.verticalLayout_6.addWidget(self.textBrowser)

        self.verticalLayout_6.setStretch(0, 9)
        self.verticalLayout_6.setStretch(1, 1)

        self.verticalLayout_5.addWidget(self.groupBox_5)

        self.verticalLayout_5.setStretch(0, 4)

        self.horizontalLayout.addLayout(self.verticalLayout_5)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 8)
        self.horizontalLayout.setStretch(2, 4)
        SemiLabeling.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(SemiLabeling)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1512, 37))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        SemiLabeling.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(SemiLabeling)
        self.statusbar.setObjectName(u"statusbar")
        SemiLabeling.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menuFile.addAction(self.actionShow_Image)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSave_Indexed_Mask)

        self.retranslateUi(SemiLabeling)

        QMetaObject.connectSlotsByName(SemiLabeling)
    # setupUi

    def retranslateUi(self, SemiLabeling):
        SemiLabeling.setWindowTitle(QCoreApplication.translate("SemiLabeling", u"SemiLabeling", None))
        self.actionShow_Image_Counts.setText(QCoreApplication.translate("SemiLabeling", u"Show Image Counts", None))
        self.actionShow_Image.setText(QCoreApplication.translate("SemiLabeling", u"Show Image", None))
        self.actionSave_Indexed_Mask.setText(QCoreApplication.translate("SemiLabeling", u"Save Indexed Mask", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("SemiLabeling", u"Files", None))
        self.toolButton_7.setText(QCoreApplication.translate("SemiLabeling", u"Open\n"
"Directory", None))
        self.groupBox.setTitle(QCoreApplication.translate("SemiLabeling", u"Prediction", None))
        self.toolButton_5.setText(QCoreApplication.translate("SemiLabeling", u"prediction", None))
        self.image_label.setText("")
        self.groupBox_5.setTitle(QCoreApplication.translate("SemiLabeling", u"Image Tree", None))
        self.textBrowser.setHtml(QCoreApplication.translate("SemiLabeling", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'.AppleSystemUIFont'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Total Images : </p></body></html>", None))
        self.menuFile.setTitle(QCoreApplication.translate("SemiLabeling", u"File", None))
    # retranslateUi

