from PySide6.QtWidgets import QApplication, QMainWindow, QDialog, QMessageBox
import sqlite3
from registration_window import Ui_registration_window



ui = Ui_registration_window()

def create_table():
    """Создает таблицу пользователей в базе данных"""
    db_connection = sqlite3.connect("users.db")
    cursor = db_connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            login TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    """)
    db_connection.commit()
    db_connection.close()

def register_user():
    """Обработчик нажатия кнопки "Зарегистрироваться" """
    login = ui.EnterRegistrationLogin.text()
    password = ui.EnterRegistrationPassword.text()

    if not login or not password:
        
        return

    try:
        # Вставляем данные в базу данных
        db_connection = sqlite3.connect("users.db")
        cursor = db_connection.cursor()
        cursor.execute(
            "INSERT INTO users (login, password) VALUES (?, ?)", (login, password)
        )
        db_connection.commit()

        ui.EnterRegistrationLogin.clear()
        ui.EnterRegistrationPassword.clear()
        db_connection.close()
    except sqlite3.IntegrityError:
        pass
