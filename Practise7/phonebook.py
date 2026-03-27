import csv
from connect import connect

def create_table():
    conn = connect()
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS phonebook (
            id SERIAL PRIMARY KEY,
            first_name VARCHAR(100) NOT NULL,
            phone VARCHAR(20) NOT NULL UNIQUE
        );
    """)

    conn.commit()
    cur.close()
    conn.close()

def insert_from_console():
    conn = connect()
    cur = conn.cursor()

    name = input("Enter name: ")
    phone = input("Enter phone: ")

    cur.execute(
        "INSERT INTO phonebook (first_name, phone) VALUES (%s, %s)",
        (name, phone)
    )

    conn.commit()
    cur.close()
    conn.close()

    print("Contact added successfully!")

def insert_from_csv(filename):
    conn = connect()
    cur = conn.cursor()

    with open(filename, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            name, phone = row
            cur.execute(
                "INSERT INTO phonebook (first_name, phone) VALUES (%s, %s) ON CONFLICT (phone) DO NOTHING",
                (name, phone)
            )

    conn.commit()
    cur.close()
    conn.close()

    print("Contacts imported from CSV!")

def show_all_contacts():
    conn = connect()
    cur = conn.cursor()

    cur.execute("SELECT * FROM phonebook ORDER BY id")
    rows = cur.fetchall()

    print("\n--- PhoneBook ---")
    for row in rows:
        print(row)

    cur.close()
    conn.close()

def search_by_name():
    conn = connect()
    cur = conn.cursor()

    name = input("Enter name to search: ")

    cur.execute(
        "SELECT * FROM phonebook WHERE first_name ILIKE %s",
        ('%' + name + '%',)
    )

    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    conn.close()

def search_by_phone_prefix():
    conn = connect()
    cur = conn.cursor()

    prefix = input("Enter phone prefix: ")

    cur.execute(
        "SELECT * FROM phonebook WHERE phone LIKE %s",
        (prefix + '%',)
    )

    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    conn.close()

def update_contact():
    conn = connect()
    cur = conn.cursor()

    old_name = input("Enter current name of contact to update: ")
    print("1. Update name")
    print("2. Update phone")
    choice = input("Choose option: ")

    if choice == "1":
        new_name = input("Enter new name: ")
        cur.execute(
            "UPDATE phonebook SET first_name = %s WHERE first_name = %s",
            (new_name, old_name)
        )
    elif choice == "2":
        new_phone = input("Enter new phone: ")
        cur.execute(
            "UPDATE phonebook SET phone = %s WHERE first_name = %s",
            (new_phone, old_name)
        )

    conn.commit()
    cur.close()
    conn.close()

    print("Contact updated successfully!")

def delete_contact():
    conn = connect()
    cur = conn.cursor()

    print("1. Delete by name")
    print("2. Delete by phone")
    choice = input("Choose option: ")

    if choice == "1":
        name = input("Enter name to delete: ")
        cur.execute("DELETE FROM phonebook WHERE first_name = %s", (name,))
    elif choice == "2":
        phone = input("Enter phone to delete: ")
        cur.execute("DELETE FROM phonebook WHERE phone = %s", (phone,))

    conn.commit()
    cur.close()
    conn.close()

    print("Contact deleted successfully!")

def menu():
    create_table()

    while True:
        print("\n===== PHONEBOOK MENU =====")
        print("1. Add contact from console")
        print("2. Import contacts from CSV")
        print("3. Show all contacts")
        print("4. Search by name")
        print("5. Search by phone prefix")
        print("6. Update contact")
        print("7. Delete contact")
        print("0. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            insert_from_console()
        elif choice == "2":
            insert_from_csv("contacts.csv")
        elif choice == "3":
            show_all_contacts()
        elif choice == "4":
            search_by_name()
        elif choice == "5":
            search_by_phone_prefix()
        elif choice == "6":
            update_contact()
        elif choice == "7":
            delete_contact()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid option!")

menu()