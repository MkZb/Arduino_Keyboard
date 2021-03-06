from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QAction, qApp, QMenu, QSystemTrayIcon


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(801, 317)
        MainWindow.setMinimumSize(QtCore.QSize(801, 317))
        MainWindow.setMaximumSize(QtCore.QSize(801, 317))
        MainWindow.setMouseTracking(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.profileButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.profileButton_1.setGeometry(QtCore.QRect(70, 50, 211, 91))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.profileButton_1.setFont(font)
        self.profileButton_1.setObjectName("profileButton_1")
        self.profileButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.profileButton_2.setGeometry(QtCore.QRect(290, 50, 211, 91))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.profileButton_2.setFont(font)
        self.profileButton_2.setObjectName("profileButton_2")
        self.profileButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.profileButton_3.setGeometry(QtCore.QRect(510, 50, 211, 91))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.profileButton_3.setFont(font)
        self.profileButton_3.setObjectName("profileButton_3")
        self.profileButton_custom = QtWidgets.QPushButton(self.centralwidget)
        self.profileButton_custom.setGeometry(QtCore.QRect(230, 160, 331, 101))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.profileButton_custom.setFont(font)
        self.profileButton_custom.setAutoDefault(False)
        self.profileButton_custom.setObjectName("profileButton_custom")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(280, 0, 221, 41))
        self.label.setScaledContents(False)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 801, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.tray_icon = QSystemTrayIcon(self)
        self.tray_icon.activated.connect(self.showFromTray)
        show_action = QAction("Show", self)
        quit_action = QAction("Exit", self)
        hide_action = QAction("Hide", self)
        show_action.triggered.connect(self.show)
        hide_action.triggered.connect(self.hide)
        quit_action.triggered.connect(qApp.quit)
        tray_menu = QMenu()
        tray_menu.addAction(show_action)
        tray_menu.addAction(quit_action)
        self.tray_icon.setContextMenu(tray_menu)
        self.tray_icon.show()

    def closeEvent(self, event):
        event.ignore()
        self.hide()

    def showFromTray(self, reason):
        if reason == 3:
            self.show()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.profileButton_1.setText(_translate("MainWindow", "1"))
        self.profileButton_2.setText(_translate("MainWindow", "2"))
        self.profileButton_3.setText(_translate("MainWindow", "3"))
        self.profileButton_custom.setText(_translate("MainWindow", "Custom"))
        self.label.setText(_translate("MainWindow",
                                      "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600; color:#00007f;\">Choose profile</span></p></body></html>"))
