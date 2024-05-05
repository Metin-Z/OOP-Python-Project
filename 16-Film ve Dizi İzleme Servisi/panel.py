from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 500)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.labelUsername = QtWidgets.QLabel(self.centralwidget)
        self.labelUsername.setGeometry(QtCore.QRect(350, 20, 91, 21))
        self.labelUsername.setObjectName("labelUsername")
        self.labelUsername.setText("Kullanıcı Adı:")

        self.labelPassword = QtWidgets.QLabel(self.centralwidget)
        self.labelPassword.setGeometry(QtCore.QRect(350, 60, 91, 21))
        self.labelPassword.setObjectName("labelPassword")
        self.labelPassword.setText("Şifre:")

        self.lineUsername = QtWidgets.QLineEdit(self.centralwidget)
        self.lineUsername.setGeometry(QtCore.QRect(450, 20, 131, 21))
        self.lineUsername.setObjectName("lineUsername")

        self.linePassword = QtWidgets.QLineEdit(self.centralwidget)
        self.linePassword.setGeometry(QtCore.QRect(450, 60, 131, 21))
        self.linePassword.setObjectName("linePassword")
        self.linePassword.setEchoMode(QtWidgets.QLineEdit.Password)

        self.btnRegister = QtWidgets.QPushButton(self.centralwidget)
        self.btnRegister.setGeometry(QtCore.QRect(450, 100, 131, 31))
        self.btnRegister.setObjectName("btnRegister")
        self.btnRegister.setText("Kayıt Ol")

        self.labelContentList = QtWidgets.QLabel(self.centralwidget)
        self.labelContentList.setGeometry(QtCore.QRect(30, 20, 111, 21))
        self.labelContentList.setObjectName("labelContentList")
        self.labelContentList.setText("İçerik Listesi")

        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(30, 50, 311, 311))
        self.listWidget.setObjectName("listWidget")

        self.btnAddToList = QtWidgets.QPushButton(self.centralwidget)
        self.btnAddToList.setGeometry(QtCore.QRect(30, 370, 151, 31))
        self.btnAddToList.setObjectName("btnAddToList")
        self.btnAddToList.setText("Listeye Ekle")

        self.btnAddMovie = QtWidgets.QPushButton(self.centralwidget)
        self.btnAddMovie.setGeometry(QtCore.QRect(30, 410, 151, 31))
        self.btnAddMovie.setObjectName("btnAddMovie")
        self.btnAddMovie.setText("Film Ekle")

        self.btnWatch = QtWidgets.QPushButton(self.centralwidget)
        self.btnWatch.setGeometry(QtCore.QRect(190, 370, 151, 31))
        self.btnWatch.setObjectName("btnWatch")
        self.btnWatch.setText("İzle")

        self.btnWatchList = QtWidgets.QPushButton(self.centralwidget)
        self.btnWatchList.setGeometry(QtCore.QRect(190, 410, 151, 31))
        self.btnWatchList.setObjectName("btnWatchList")
        self.btnWatchList.setText("İzleme Geçmişi")

        self.btnToWatchList = QtWidgets.QPushButton(self.centralwidget)
        self.btnToWatchList.setGeometry(QtCore.QRect(350, 370, 151, 31))
        self.btnToWatchList.setObjectName("btnToWatchList")
        self.btnToWatchList.setText("İzlenecekler Listesi")

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Film ve Dizi İzleme Servisi"))
        self.labelUsername.setText(_translate("MainWindow", "Kullanıcı Adı:"))
        self.labelPassword.setText(_translate("MainWindow", "Şifre:"))
        self.labelContentList.setText(_translate("MainWindow", "İçerik Listesi"))
        self.btnAddToList.setText(_translate("MainWindow", "Listeye Ekle"))
        self.btnAddMovie.setText(_translate("MainWindow", "Film Ekle"))
        self.btnWatch.setText(_translate("MainWindow", "İzle"))
        self.btnWatchList.setText(_translate("MainWindow", "İzleme Geçmişi"))
        self.btnToWatchList.setText(_translate("MainWindow", "İzlenecekler Listesi"))
