import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QLabel, QLineEdit, QPushButton, QListWidgetItem
from panel import Ui_MainWindow

class AddMovieDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Film Ekle")
        self.resize(300, 100)

        self.label = QLabel("Film Adı:", self)
        self.label.setGeometry(20, 20, 60, 20)

        self.lineMovieName = QLineEdit(self)
        self.lineMovieName.setGeometry(90, 20, 150, 20)

        self.btnConfirm = QPushButton("Onayla", self)
        self.btnConfirm.setGeometry(100, 50, 100, 30)
        self.btnConfirm.clicked.connect(self.accept)

    def get_movie_name(self):
        return self.lineMovieName.text()

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.btnRegister.clicked.connect(self.register_user)
        self.btnAddToList.clicked.connect(self.add_to_list)
        self.btnAddMovie.clicked.connect(self.add_movie)
        self.btnWatch.clicked.connect(self.watch_content)
        self.btnWatchList.clicked.connect(self.show_watch_history)
        self.btnToWatchList.clicked.connect(self.show_to_watch_list)

        self.users = {}  # Kullanıcıları saklamak için sözlük
        self.contents = ["Film 1", "Film 2", "Film 3"]  # İçerik listesi
        self.watch_history = {}  # İzleme geçmişi
        self.to_watch_list = {}  # İzlenecekler listesi
        self.current_user = ""  # Son giriş yapan kullanıcı

    def register_user(self):
        username = self.lineUsername.text()
        password = self.linePassword.text()
        if username and password:
            self.users[username] = password
            self.watch_history[username] = []
            self.to_watch_list[username] = []
            self.current_user = username  # Yeni kullanıcıyı oturum açan kullanıcı olarak ayarla
            self.lineUsername.clear()
            self.linePassword.clear()
            print("Kullanıcı başarıyla kaydedildi:", username)
        else:
            print("Kullanıcı adı ve şifre boş olamaz.")

    def add_to_list(self):
        selected_content = self.listWidget.currentItem()
        if selected_content:
            if self.current_user in self.users:
                # Kullanıcının izleme listesine içeriği ekleyin
                self.to_watch_list[self.current_user].append(selected_content.text())
                print(f"{self.current_user} kullanıcısının izlenecekler listesine {selected_content.text()} eklendi.")
            else:
                print("Kullanıcı bulunamadı.")
        else:
            print("Lütfen bir içerik seçin.")

    def add_movie(self):
        dialog = AddMovieDialog()
        if dialog.exec_():
            movie_name = dialog.get_movie_name()
            if movie_name:
                self.listWidget.addItem(movie_name)
                print(f"{movie_name} listeye eklendi.")

    def watch_content(self):
        selected_content = self.listWidget.currentItem()
        if selected_content:
            if self.current_user in self.users:
                # Kullanıcının izleme geçmişine içeriği ekleyin
                self.watch_history[self.current_user].append(selected_content.text())
                print(f"{self.current_user} kullanıcısı {selected_content.text()} içeriğini izledi.")
                
                if selected_content.text() in self.to_watch_list[self.current_user]:
                    self.to_watch_list[self.current_user].remove(selected_content.text())
                    print(f"{selected_content.text()} izlenecekler listesinden kaldırıldı.")
            else:
                print("Kullanıcı bulunamadı.")
        else:
            print("Lütfen bir içerik seçin.")

    def show_watch_history(self):
        if self.current_user in self.users:
            watch_history_text = f"{self.current_user} için İzleme Geçmişi Listesi:\n" + '\n'.join(self.watch_history[self.current_user])
            self.show_dialog("İzleme Geçmişi", watch_history_text)
        else:
            print("Kullanıcı bulunamadı.")

    def show_to_watch_list(self):
        if self.current_user in self.users:
            to_watch_list_text = f"{self.current_user} için İzlenecekler Listesi:\n" + '\n'.join(self.to_watch_list[self.current_user])
            self.show_dialog("İzlenecekler Listesi", to_watch_list_text)
        else:
            print("Kullanıcı bulunamadı.")

    def show_dialog(self, title, message):
        dialog = QDialog(self)
        dialog.setWindowTitle(title)
        dialog.setGeometry(100, 100, 400, 300)

        label = QLabel(message, dialog)
        label.move(20, 20)

        dialog.exec_()

    def set_current_user(self, username):
        self.current_user = username

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
