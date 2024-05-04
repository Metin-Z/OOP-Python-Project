from PyQt5 import QtCore, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Proje Tablosu
        self.tblProjects = QtWidgets.QTableWidget(self.centralwidget)
        self.tblProjects.setGeometry(QtCore.QRect(10, 10, 400, 200))
        self.tblProjects.setRowCount(0)
        self.tblProjects.setColumnCount(3)
        self.tblProjects.setHorizontalHeaderLabels(["Proje Adı", "Başlangıç Tarihi", "Bitiş Tarihi"])
        self.tblProjects.setObjectName("tblProjects")

        # Görev Tablosu
        self.tblTasks = QtWidgets.QTableWidget(self.centralwidget)
        self.tblTasks.setGeometry(QtCore.QRect(10, 250, 400, 200))
        self.tblTasks.setRowCount(0)
        self.tblTasks.setColumnCount(3)
        self.tblTasks.setHorizontalHeaderLabels(["Görev Adı", "Çalışan", "İlerleme"])
        self.tblTasks.setObjectName("tblTasks")

        # Proje Ekleme Alanı
        self.labelProjectName = QtWidgets.QLabel(self.centralwidget)
        self.labelProjectName.setGeometry(QtCore.QRect(450, 20, 80, 20))
        self.labelProjectName.setObjectName("labelProjectName")
        self.labelProjectName.setText("Proje Adı:")
        
        self.lineProjectName = QtWidgets.QLineEdit(self.centralwidget)
        self.lineProjectName.setGeometry(QtCore.QRect(540, 20, 200, 20))
        self.lineProjectName.setObjectName("lineProjectName")

        self.labelStartDate = QtWidgets.QLabel(self.centralwidget)
        self.labelStartDate.setGeometry(QtCore.QRect(450, 50, 80, 20))
        self.labelStartDate.setObjectName("labelStartDate")
        self.labelStartDate.setText("Başlangıç Tarihi:")
        
        self.lineStartDate = QtWidgets.QLineEdit(self.centralwidget)
        self.lineStartDate.setGeometry(QtCore.QRect(540, 50, 200, 20))
        self.lineStartDate.setObjectName("lineStartDate")

        self.labelEndDate = QtWidgets.QLabel(self.centralwidget)
        self.labelEndDate.setGeometry(QtCore.QRect(450, 80, 80, 20))
        self.labelEndDate.setObjectName("labelEndDate")
        self.labelEndDate.setText("Bitiş Tarihi:")
        
        self.lineEndDate = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEndDate.setGeometry(QtCore.QRect(540, 80, 200, 20))
        self.lineEndDate.setObjectName("lineEndDate")

        # Proje Ekle Butonu
        self.btnAddProject = QtWidgets.QPushButton(self.centralwidget)
        self.btnAddProject.setGeometry(QtCore.QRect(450, 120, 100, 30))
        self.btnAddProject.setText("Proje Ekle")
        self.btnAddProject.setObjectName("btnAddProject")

        # Görev Ekleme Alanı
        self.labelTaskName = QtWidgets.QLabel(self.centralwidget)
        self.labelTaskName.setGeometry(QtCore.QRect(450, 250, 80, 20))
        self.labelTaskName.setObjectName("labelTaskName")
        self.labelTaskName.setText("Görev Adı:")
        
        self.lineTaskName = QtWidgets.QLineEdit(self.centralwidget)
        self.lineTaskName.setGeometry(QtCore.QRect(540, 250, 200, 20))
        self.lineTaskName.setObjectName("lineTaskName")

        self.labelEmployee = QtWidgets.QLabel(self.centralwidget)
        self.labelEmployee.setGeometry(QtCore.QRect(450, 280, 80, 20))
        self.labelEmployee.setObjectName("labelEmployee")
        self.labelEmployee.setText("Çalışan:")
        
        self.lineEmployee = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEmployee.setGeometry(QtCore.QRect(540, 280, 200, 20))
        self.lineEmployee.setObjectName("lineEmployee")

        self.labelProgress = QtWidgets.QLabel(self.centralwidget)
        self.labelProgress.setGeometry(QtCore.QRect(450, 310, 80, 20))
        self.labelProgress.setObjectName("labelProgress")
        self.labelProgress.setText("İlerleme:")
        
        self.lineProgress = QtWidgets.QLineEdit(self.centralwidget)
        self.lineProgress.setGeometry(QtCore.QRect(540, 310, 200, 20))
        self.lineProgress.setObjectName("lineProgress")

        # Görev Ekle Butonu
        self.btnAddTask = QtWidgets.QPushButton(self.centralwidget)
        self.btnAddTask.setGeometry(QtCore.QRect(450, 350, 100, 30))
        self.btnAddTask.setText("Görev Ekle")
        self.btnAddTask.setObjectName("btnAddTask")

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = MainWindow.statusBar()
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "İş Takip ve Yönetim Sistemi"))

