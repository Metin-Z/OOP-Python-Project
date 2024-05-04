from PyQt5 import QtCore, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("font: 8pt 'MS Shell Dlg 2';")
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Kitap bilgilerini ve kontrollerini oluşturun.
        self.labelBookTitle = QtWidgets.QLabel(self.centralwidget)
        self.labelBookTitle.setGeometry(QtCore.QRect(30, 20, 100, 20))
        self.labelBookTitle.setText("Kitap Adı:")
        
        self.lineBookTitle = QtWidgets.QLineEdit(self.centralwidget)
        self.lineBookTitle.setGeometry(QtCore.QRect(140, 20, 150, 20))
        
        self.labelBookAuthor = QtWidgets.QLabel(self.centralwidget)
        self.labelBookAuthor.setGeometry(QtCore.QRect(30, 50, 100, 20))
        self.labelBookAuthor.setText("Yazar:")
        
        self.lineBookAuthor = QtWidgets.QLineEdit(self.centralwidget)
        self.lineBookAuthor.setGeometry(QtCore.QRect(140, 50, 150, 20))
        
        self.labelBookPublisher = QtWidgets.QLabel(self.centralwidget)
        self.labelBookPublisher.setGeometry(QtCore.QRect(30, 80, 100, 20))
        self.labelBookPublisher.setText("Yayınevi:")
        
        self.lineBookPublisher = QtWidgets.QLineEdit(self.centralwidget)
        self.lineBookPublisher.setGeometry(QtCore.QRect(140, 80, 150, 20))
        
        self.labelBookContent = QtWidgets.QLabel(self.centralwidget)
        self.labelBookContent.setGeometry(QtCore.QRect(30, 110, 100, 20))
        self.labelBookContent.setText("Kitap İçeriği:")
        
        self.lineBookContent = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.lineBookContent.setGeometry(QtCore.QRect(140, 110, 150, 60))
        
        self.btnKitapEkle = QtWidgets.QPushButton(self.centralwidget)
        self.btnKitapEkle.setGeometry(QtCore.QRect(140, 180, 150, 30))
        self.btnKitapEkle.setText("Kitap Ekle")
        
        # Kitap tablosunu oluşturun.
        self.tblBooks = QtWidgets.QTableWidget(self.centralwidget)
        self.tblBooks.setGeometry(QtCore.QRect(320, 20, 450, 300))
        self.tblBooks.setColumnCount(3)
        self.tblBooks.setHorizontalHeaderLabels(["Kitap Adı", "Yazar", "Yayınevi"])
        self.tblBooks.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        
        # Kitap silme düğmesini oluşturun.
        self.btnKitapSil = QtWidgets.QPushButton(self.centralwidget)
        self.btnKitapSil.setGeometry(QtCore.QRect(320, 340, 150, 30))
        self.btnKitapSil.setText("Kitap Sil")
        
        # Kullanıcı giriş bölümünü oluşturun.
        self.labelUsername = QtWidgets.QLabel(self.centralwidget)
        self.labelUsername.setGeometry(QtCore.QRect(30, 220, 100, 20))
        self.labelUsername.setText("Kullanıcı Adı:")
        
        self.lineUsername = QtWidgets.QLineEdit(self.centralwidget)
        self.lineUsername.setGeometry(QtCore.QRect(140, 220, 150, 20))
        
        self.labelPassword = QtWidgets.QLabel(self.centralwidget)
        self.labelPassword.setGeometry(QtCore.QRect(30, 250, 100, 20))
        self.labelPassword.setText("Şifre:")
        
        self.linePassword = QtWidgets.QLineEdit(self.centralwidget)
        self.linePassword.setGeometry(QtCore.QRect(140, 250, 150, 20))
        self.linePassword.setEchoMode(QtWidgets.QLineEdit.Password)
        
        self.labelSetPassword = QtWidgets.QLabel(self.centralwidget)
        self.labelSetPassword.setGeometry(QtCore.QRect(30, 280, 100, 20))
        self.labelSetPassword.setText("Şifre Belirle:")
        
        self.lineSetPassword = QtWidgets.QLineEdit(self.centralwidget)
        self.lineSetPassword.setGeometry(QtCore.QRect(140, 280, 150, 20))
        self.lineSetPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        
        self.btnGiris = QtWidgets.QPushButton(self.centralwidget)
        self.btnGiris.setGeometry(QtCore.QRect(140, 310, 150, 30))
        self.btnGiris.setText("Giriş")
        
        # Kullanıcı yorum ekleme düğmesini oluşturun.
        self.btnYorumEkle = QtWidgets.QPushButton(self.centralwidget)
        self.btnYorumEkle.setGeometry(QtCore.QRect(320, 380, 150, 30))
        self.btnYorumEkle.setText("Yorum Ekle")
        
        # Okuma listesi düğmelerini oluşturun.
        self.btnOkumaListesi = QtWidgets.QPushButton(self.centralwidget)
        self.btnOkumaListesi.setGeometry(QtCore.QRect(320, 420, 150, 30))
        self.btnOkumaListesi.setText("Okuma Listesi")
        
        self.btnOkumaListesineEkle = QtWidgets.QPushButton(self.centralwidget)
        self.btnOkumaListesineEkle.setGeometry(QtCore.QRect(320, 460, 150, 30))
        self.btnOkumaListesineEkle.setText("Listeye Ekle")
        
        self.btnOkumaListesindenCikar = QtWidgets.QPushButton(self.centralwidget)
        self.btnOkumaListesindenCikar.setGeometry(QtCore.QRect(320, 500, 150, 30))
        self.btnOkumaListesindenCikar.setText("Listeden Çıkar")
        
        MainWindow.setCentralWidget(self.centralwidget)
        
        # Menüyü oluşturun.
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Kitap Paylaşım Platformu"))
        self.menu.setTitle(_translate("MainWindow", "Menu"))
