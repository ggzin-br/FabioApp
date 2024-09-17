# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_WidgetApp(object):
    def setupUi(self, WidgetApp):
        if not WidgetApp.objectName():
            WidgetApp.setObjectName(u"WidgetApp")
        WidgetApp.resize(800, 600)
        WidgetApp.setMaximumSize(QSize(1218, 969))
        WidgetApp.setCursor(QCursor(Qt.CursorShape.OpenHandCursor))
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.AppointmentNew))
        WidgetApp.setWindowIcon(icon)
        self.verticalLayout = QVBoxLayout(WidgetApp)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.input = QLineEdit(WidgetApp)
        self.input.setObjectName(u"input")
        self.input.setMaximumSize(QSize(16777215, 16777215))

        self.verticalLayout.addWidget(self.input)

        self.checkar = QPushButton(WidgetApp)
        self.checkar.setObjectName(u"checkar")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkar.sizePolicy().hasHeightForWidth())
        self.checkar.setSizePolicy(sizePolicy)
        self.checkar.setMaximumSize(QSize(16777215, 16777215))
        self.checkar.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.checkar.setCheckable(False)

        self.verticalLayout.addWidget(self.checkar)

        self.fabio = QLabel(WidgetApp)
        self.fabio.setObjectName(u"fabio")
        self.fabio.setMaximumSize(QSize(800, 510))
        self.fabio.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.fabio.setTextFormat(Qt.TextFormat.PlainText)
        self.fabio.setPixmap(QPixmap(u"fabiotuple.png"))
        self.fabio.setScaledContents(True)
        self.fabio.setWordWrap(False)

        self.verticalLayout.addWidget(self.fabio)


        self.retranslateUi(WidgetApp)

        QMetaObject.connectSlotsByName(WidgetApp)
    # setupUi

    def retranslateUi(self, WidgetApp):
        WidgetApp.setWindowTitle(QCoreApplication.translate("WidgetApp", u"WidgetApp", None))
        self.checkar.setText(QCoreApplication.translate("WidgetApp", u"Checkar", None))
        self.fabio.setText("")
    # retranslateUi

