import socket
import easygui


def send_file_to_server(filename, method, key=None):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('127.0.0.1', 12345))
    if key:
        client.send(f"ENCRYPT {method} {key} {filename}".encode())
    else:
        client.send(f"ENCRYPT {method} {filename}".encode())

    response = client.recv(4096).decode()
    original_text = response.split(": ")[1]
    easygui.msgbox(original_text, title="Оригинальный текст")

    client.send("ACK".encode())
    response = client.recv(4096).decode()
    encrypted_text = response.split(": ")[1]
    easygui.msgbox(encrypted_text, title="Зашифрованный текст")

    client.close()


def get_file_from_server(filename, method, key=None):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('127.0.0.1', 12345))
    if key:
        client.send(f"DECRYPT {method} {key} {filename}".encode())
    else:
        client.send(f"DECRYPT {method} {filename}".encode())

    response = client.recv(4096).decode()
    encrypted_text = response.split(": ")[1]
    easygui.msgbox(encrypted_text, title="Зашифрованный текст")

    client.send("ACK".encode())
    response = client.recv(4096).decode()
    decrypted_text = response.split(": ")[1]
    easygui.msgbox(decrypted_text, title="Расшифрованный текст")

    client.close()


def main():
    while True:
        choice = easygui.buttonbox("Выберите действие:",
                                   choices=["Отправить файл на сервер", "Получить файл с сервера", "Выйти"])

        if choice == "Отправить файл на сервер":
            filename = easygui.fileopenbox(title="Выберите файл для отправки")
            if filename:
                method = easygui.buttonbox("Выберите метод шифрования:", choices=["CAESAR", "PAIR", "VIGENERE"])
                if method:
                    if method == "CAESAR":
                        key = easygui.enterbox("Введите шаг сдвига для шифра Цезаря (целое число):", default="3")
                    elif method == "PAIR":
                        key = easygui.enterbox("Введите ключ для шифра пар (строка из 26 уникальных букв):",
                                               default="bcdefghijklmnopqrstuvwxyza")
                    elif method == "VIGENERE":
                        key = easygui.enterbox("Введите ключ для шифра Виженера (строка):", default="deus")
                    if key:
                        send_file_to_server(filename, method, key)

        elif choice == "Получить файл с сервера":
            filename = easygui.fileopenbox(title="Выберите файл для получения")
            if filename:
                method = easygui.buttonbox("Выберите метод расшифрования:", choices=["CAESAR", "PAIR", "VIGENERE"])
                if method:
                    if method == "CAESAR":
                        key = easygui.enterbox("Введите шаг сдвига для шифра Цезаря (целое число):", default="3")
                    elif method == "PAIR":
                        key = easygui.enterbox("Введите ключ для шифра пар (строка из 26 уникальных букв):",
                                               default="bcdefghijklmnopqrstuvwxyza")
                    elif method == "VIGENERE":
                        key = easygui.enterbox("Введите ключ для шифра Виженера (строка):", default="deus")
                    if key:
                        get_file_from_server(filename, method, key)

        elif choice == "Выйти":
            break


if __name__ == "__main__":
    main()