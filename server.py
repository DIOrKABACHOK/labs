import socket
import threading
import os


def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_char = chr((ord(char.lower()) - ord('a') + shift) % 26 + ord('a'))
            if char.isupper():
                shift_char = shift_char.upper()
            result += shift_char
        else:
            result += char
    return result


def pair_cipher(text, key):
    result = ""
    for char in text:
        if char.isalpha():
            index = key.index(char.lower())
            result += chr(index + ord('a'))
        else:
            result += char
    return result


def generate_inverse_key(key):
    inverse_key = [''] * 26
    for i, char in enumerate(key):
        inverse_key[ord(char) - ord('a')] = chr(i + ord('a'))
    return ''.join(inverse_key)


def vigenere_cipher(text, key, decrypt=False):
    result = ""
    key_len = len(key)
    for i, char in enumerate(text):
        if char.isalpha():
            shift = ord(key[i % key_len].lower()) - ord('a')
            if decrypt:
                shift = -shift
            shift_char = chr((ord(char.lower()) - ord('a') + shift) % 26 + ord('a'))
            if char.isupper():
                shift_char = shift_char.upper()
            result += shift_char
        else:
            result += char
    return result


def handle_client(client_socket):
    while True:
        data = client_socket.recv(1024).decode()
        if not data:
            break

        if data.startswith("ENCRYPT"):
            parts = data.split()
            method = parts[1]
            key = parts[2] if len(parts) > 2 else None
            filename = parts[3] if len(parts) > 3 else parts[2]

            with open(filename, 'r') as file:
                content = file.read()
            client_socket.send(f"Original: {content}".encode())
            client_socket.recv(1024)

            if method == "CAESAR":
                shift = int(key) if key else 3
                encrypted_content = caesar_cipher(content, shift)
                encrypted_filename = os.path.splitext(filename)[0] + ".enc"
            elif method == "PAIR":
                key = key if key else "bcdefghijklmnopqrstuvwxyza"
                encrypted_content = pair_cipher(content, key)
                encrypted_filename = os.path.splitext(filename)[0] + ".pair.enc"
            elif method == "VIGENERE":
                key = key if key else "deus"
                encrypted_content = vigenere_cipher(content, key)
                encrypted_filename = os.path.splitext(filename)[0] + ".vigenere.enc"

            with open(encrypted_filename, 'w') as file:
                file.write(encrypted_content)
            client_socket.send(f"Encrypted: {encrypted_content}".encode())

        elif data.startswith("DECRYPT"):
            parts = data.split()
            method = parts[1]
            key = parts[2] if len(parts) > 2 else None
            filename = parts[3] if len(parts) > 3 else parts[2]

            with open(filename, 'r') as file:
                content = file.read()
            client_socket.send(f"Encrypted: {content}".encode())
            client_socket.recv(1024)

            if method == "CAESAR":
                shift = int(key) if key else 3
                decrypted_content = caesar_cipher(content, -shift)
                decrypted_filename = os.path.splitext(filename)[0] + ".denc"
            elif method == "PAIR":
                key = key if key else "bcdefghijklmnopqrstuvwxyza"
                inverse_key = generate_inverse_key(key)
                decrypted_content = pair_cipher(content, inverse_key)
                decrypted_filename = os.path.splitext(filename)[0] + ".pair.denc"
            elif method == "VIGENERE":
                key = key if key else "deus"
                decrypted_content = vigenere_cipher(content, key, decrypt=True)
                decrypted_filename = os.path.splitext(filename)[0] + ".vigenere.denc"

            with open(decrypted_filename, 'w') as file:
                file.write(decrypted_content)
            client_socket.send(f"Decrypted: {decrypted_content}".encode())

    client_socket.close()


def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('127.0.0.1', 12345))
    server.listen(5)
    print("Сервер запущен и ожидает подключений...")

    while True:
        client_socket, addr = server.accept()
        print(f"Подключение от {addr}")
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()


if __name__ == "__main__":
    start_server()