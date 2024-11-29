import sqlite3

conn = sqlite3.connect('library.db')
cursor = conn.cursor()


def print_menu():
    print("\nВыберите команду:")
    print("1. Вывести список книг")
    print("2. Вывести список читателей")
    print("3. Добавить книгу")
    print("4. Добавить читателя")
    print("5. Выдать книгу читателю")
    print("6. Принять книгу")
    print("7. Просмотреть, кто какую книгу взял и когда")
    print("8. Выход")


def list_books():
    cursor.execute("SELECT * FROM Books")
    books = cursor.fetchall()
    for book in books:
        print(book)


def list_readers():
    cursor.execute("SELECT * FROM Readers")
    readers = cursor.fetchall()
    for reader in readers:
        print(reader)


def add_book():
    id = int(input("Введите id книги: "))
    author = input("Введите автора книги: ")
    title = input("Введите название книги: ")
    publish_year = int(input("Введите год издания книги: "))
    cursor.execute("INSERT INTO Books (id, author, title, publish_year) VALUES (?, ?, ?, ?)", (id, author, title, publish_year))
    conn.commit()
    print("Книга успешно добавлена.")


def add_reader():
    id = int(input("Введите id читателя: "))
    name = input("Введите имя читателя: ")
    cursor.execute("INSERT INTO Readers (id, name) VALUES (?, ?)", (id, name))
    conn.commit()
    print("Читатель успешно добавлен.")


def lend_book():
    reader_id = int(input("Введите id читателя: "))
    book_id = int(input("Введите id книги: "))
    taking_date = input("Введите дату выдачи книги (YYYY-MM-DD): ")
    cursor.execute("INSERT INTO Records (reader_id, book_id, taking_date) VALUES (?, ?, ?)", (reader_id, book_id, taking_date))
    conn.commit()
    print("Книга успешно выдана.")


def return_book():
    reader_id = int(input("Введите id читателя: "))
    book_id = int(input("Введите id книги: "))
    returning_date = input("Введите дату возврата книги (YYYY-MM-DD): ")
    cursor.execute("UPDATE Records SET returning_date = ? WHERE reader_id = ? AND book_id = ? AND returning_date IS NULL", (returning_date, reader_id, book_id))
    conn.commit()
    print("Книга успешно возвращена.")


def view_book_records():
    cursor.execute('''
    SELECT Readers.name, Books.title, Records.taking_date, Records.returning_date
    FROM Records
    JOIN Readers ON Records.reader_id = Readers.id
    JOIN Books ON Records.book_id = Books.id
    ''')
    records = cursor.fetchall()
    for record in records:
        print(record)


def main():
    while True:
        print_menu()
        choice = input("Введите номер команды: ")

        if choice == '1':
            list_books()
        elif choice == '2':
            list_readers()
        elif choice == '3':
            add_book()
        elif choice == '4':
            add_reader()
        elif choice == '5':
            lend_book()
        elif choice == '6':
            return_book()
        elif choice == '7':
            view_book_records()
        elif choice == '8':
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

    conn.close()


if __name__ == "__main__":
    main()