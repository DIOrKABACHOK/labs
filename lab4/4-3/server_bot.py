import socket
import easygui as eg


def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12345))
    server_socket.listen(1)
    eg.msgbox("Сервер запущен и ожидает подключения...", title="Сервер")

    client_socket, addr = server_socket.accept()
    eg.msgbox(f"Подключен клиент: {addr}", title="Сервер")

    bot_responses = {
        "привет": "Привет! Как дела?",
        "как дела": "У меня все хорошо, спасибо!",
        "что делаешь": "Общаюсь с тобой!",
        "пока": "До встречи!",
        "exit": "Сервер завершает работу."
    }

    while True:
        message = client_socket.recv(1024).decode('utf-8')
        if message.lower() == 'exit':
            eg.msgbox("Клиент отключился.", title="Сервер")
            break
        eg.msgbox(f"Клиент: {message}", title="Сервер")

        response = bot_responses.get(message.lower(), "Я не понимаю, что ты имеешь в виду.")
        client_socket.send(response.encode('utf-8'))
        if response.lower() == 'exit':
            eg.msgbox("Сервер завершает работу.", title="Сервер")
            break

    client_socket.close()
    server_socket.close()


if __name__ == "__main__":
    start_server()