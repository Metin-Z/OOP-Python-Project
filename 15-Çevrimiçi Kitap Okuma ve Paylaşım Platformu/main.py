from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QMessageBox, QInputDialog
from PyQt5.QtCore import Qt
from panel import Ui_MainWindow
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Kitap ekleme ve silme işlemleri için sinyalleri bağlayın.
        self.ui.btnKitapEkle.clicked.connect(self.add_book)
        self.ui.btnKitapSil.clicked.connect(self.delete_book)

        # Kitap tablosuna çift tıklama olayı ekleyin.
        self.ui.tblBooks.cellDoubleClicked.connect(self.show_book_content)

        # Kullanıcı girişi işlemi için sinyali bağlayın.
        self.ui.btnGiris.clicked.connect(self.login)

        # Kullanıcı yorumlarını eklemek için sinyali bağlayın.
        self.ui.btnYorumEkle.clicked.connect(self.add_comment)

        # Okuma listesi düğmelerini bağlayın.
        self.ui.btnOkumaListesi.clicked.connect(self.show_reading_list)
        self.ui.btnOkumaListesineEkle.clicked.connect(self.add_to_reading_list)
        self.ui.btnOkumaListesindenCikar.clicked.connect(self.remove_from_reading_list)

        # Veri yapısı olarak kitap ve içeriklerini depolamak için sözlükler kullanın.
        self.books = {}  # Kitap bilgilerini saklamak için bir sözlük
        self.book_contents = {}  # Kitap içeriklerini saklamak için bir sözlük
        self.book_comments = {}  # Kitap yorumlarını saklamak için bir sözlük

        self.users = {
            "admin": {"password": "admin123", "reading_list": []},
            "user1": {"password": "password1", "reading_list": []},
            "user2": {"password": "password2", "reading_list": []}
        }
        
        self.current_user = None  

        self.update_book_table()

    def add_book(self):
        book_title = self.ui.lineBookTitle.text()
        book_author = self.ui.lineBookAuthor.text()
        book_publisher = self.ui.lineBookPublisher.text()
        book_content = self.ui.lineBookContent.toPlainText()

        if book_title and book_author and book_publisher:
            self.books[book_title] = {
                'author': book_author,
                'publisher': book_publisher,
                'content': book_content
            }
            self.book_contents[book_title] = book_content
            self.book_comments[book_title] = []

            self.update_book_table()

            self.ui.lineBookTitle.clear()
            self.ui.lineBookAuthor.clear()
            self.ui.lineBookPublisher.clear()
            self.ui.lineBookContent.clear()

    def update_book_table(self):
        self.ui.tblBooks.setRowCount(len(self.books))
        for row, (book_title, book_info) in enumerate(self.books.items()):
            self.ui.tblBooks.setItem(row, 0, QTableWidgetItem(book_title))
            self.ui.tblBooks.setItem(row, 1, QTableWidgetItem(book_info['author']))
            self.ui.tblBooks.setItem(row, 2, QTableWidgetItem(book_info['publisher']))
        
        self.ui.tblBooks.resizeColumnsToContents()

    def delete_book(self):
        selected_row = self.ui.tblBooks.currentRow()
        if selected_row != -1:
            book_title = self.ui.tblBooks.item(selected_row, 0).text()
            
            del self.books[book_title]
            del self.book_contents[book_title]
            del self.book_comments[book_title]
            
            self.update_book_table()

    def show_book_content(self, row, column):
        book_title = self.ui.tblBooks.item(row, 0).text()
        
        book_content = self.book_contents.get(book_title)
        
        book_comments = self.book_comments.get(book_title, [])

        if book_content:
            content_message = f"Kitap Adı: {book_title}\n\n{book_content}\n\n"
            
            if book_comments:
                comment_message = "Yorumlar:\n"
                for user, comment in book_comments:
                    comment_message += f"{user}: {comment}\n"
                content_message += comment_message
            else:
                content_message += "Henüz yorum yapılmamış."
            
            QMessageBox.information(self, "Kitap İçeriği ve Yorumlar", content_message)
        else:
            QMessageBox.warning(self, "Uyarı", f"{book_title} kitabının içeriği bulunamadı.")

    def login(self):
        username = self.ui.lineUsername.text()
        password = self.ui.linePassword.text()
        set_password = self.ui.lineSetPassword.text()

        if username not in self.users and set_password:
            self.users[username] = {"password": set_password, "reading_list": []}
            self.current_user = username
            QMessageBox.information(self, "Kullanıcı Oluşturuldu", "Yeni kullanıcı oluşturuldu ve giriş yapıldı!")
        elif username in self.users and self.users[username]["password"] == password:
            self.current_user = username
            QMessageBox.information(self, "Giriş Başarılı", f"Hoş geldiniz, {username}!")
        else:
            QMessageBox.warning(self, "Hatalı Giriş", "Geçersiz kullanıcı adı veya şifre.")

    def add_comment(self):
        selected_row = self.ui.tblBooks.currentRow()
        if selected_row != -1:
            book_title = self.ui.tblBooks.item(selected_row, 0).text()

            comment, ok = QInputDialog.getText(self, "Yorum Ekle", "Yorumunuzu girin:")
            if ok and comment:
                self.book_comments[book_title].append((self.current_user, comment))
                
                QMessageBox.information(self, "Yorum Eklendi", f"Yorumunuz başarıyla eklendi.")
        else:
            QMessageBox.warning(self, "Uyarı", "Lütfen bir kitap seçin.")

    def show_reading_list(self):
        reading_list = self.users[self.current_user]["reading_list"]

        if reading_list:
            QMessageBox.information(self, f"{self.current_user} Okuma Listesi", "\n".join(reading_list))
        else:
            QMessageBox.warning(self, "Okuma Listesi", "Okuma listesi boş.")

    def add_to_reading_list(self):
        selected_row = self.ui.tblBooks.currentRow()
        if selected_row != -1:
            book_title = self.ui.tblBooks.item(selected_row, 0).text()

            self.users[self.current_user]["reading_list"].append(book_title)
            QMessageBox.information(self, "Okuma Listesine Eklendi", f"{book_title} okuma listesine eklendi.")
        else:
            QMessageBox.warning(self, "Uyarı", "Lütfen bir kitap seçin.")

    def remove_from_reading_list(self):
        selected_row = self.ui.tblBooks.currentRow()
        if selected_row != -1:
            book_title = self.ui.tblBooks.item(selected_row, 0).text()

            if book_title in self.users[self.current_user]["reading_list"]:
                self.users[self.current_user]["reading_list"].remove(book_title)
                QMessageBox.information(self, "Okuma Listesinden Kaldırıldı", f"{book_title} okuma listesinden kaldırıldı.")
            else:
                QMessageBox.warning(self, "Uyarı", f"{book_title} zaten okuma listesinde değil.")
        else:
            QMessageBox.warning(self, "Uyarı", "Lütfen bir kitap seçin.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
