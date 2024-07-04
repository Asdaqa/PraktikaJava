import sys
import sqlite3

from PySide6.QtWidgets import QApplication, QMainWindow, QDialog, QMessageBox

from login_window import Ui_LoginWindow
from registration_window import Ui_registration_window
from settings_window import Ui_Dialog

import connection

# class EquipmentTracker(QMainWindow):
#     def __init__(self):
#         super(EquipmentTracker, self).__init__()
#         self.ui = Ui_MainWindow()
#         self.ui.setupUi(self)

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = EquipmentTracker()
#     window.show()


app = QApplication(sys.argv)

login_window = QDialog()
ui_login = Ui_LoginWindow()
ui_login.setupUi(login_window)
login_window.show()

settings_window = QDialog()
ui_settings = Ui_Dialog()
ui_settings.setupUi(settings_window)

db_connection = sqlite3.connect("users.db")
cursor = db_connection.cursor()

# Функция для кнопки, которая перебрасывает на окно регистрации
def openRegistrationWindow():
    global RegistrationWindow
    RegistrationWindow = QDialog()
    ui = Ui_registration_window()
    ui.setupUi(RegistrationWindow)
    login_window.close()
    RegistrationWindow.show()

    def register_user():
        login = ui.EnterRegistrationLogin.text()
        password = ui.EnterRegistrationPassword.text()

        if not login or not password:
            
            return

        try:
            # Вставляем данные в базу данных
            cursor.execute(
                "INSERT INTO users (login, password) VALUES (?, ?)", (login, password)
            )
            db_connection.commit()

            ui.EnterRegistrationLogin.clear()
            ui.EnterRegistrationPassword.clear()
            db_connection.close()
        except sqlite3.IntegrityError:
            pass
            
        RegistrationWindow.close()
        login_window.show()

    ui.ButtonRegistration.clicked.connect(register_user)


def loginsUser():
    login = ui_login.EnterLogin.text()
    password = ui_login.EnterPassword.text()
    login_window.close()
    settings_window.show()

    if not login or not password:
        return
    
    try:
        # Проверяем, существует ли пользователь в базе данных
        cursor.execute("SELECT  FROM users WHERE login = ? AND password = ?", (login, password))
        user = cursor.fetchone()


        login_window.close()
        settings_window.show()

    except Exception as e:
            print("Ошибка", f"Ошибка: {e}")
            pass


def clearSearch():
    ui_settings.lineEquipment.clear()
    ui_settings.lineStatus.clear()
    ui_settings.lineCustomers.clear()
    ui_settings.lineResponsible.clear()

# Открытие окна регистрации
ui_login.ButtonCome.clicked.connect(loginsUser)
ui_login.ButtonRegister.clicked.connect(openRegistrationWindow)
ui_settings.pushButton_2.clicked.connect(clearSearch)


sys.exit(app.exec())