from connect import connect

def menu():
    conn = connect()
    cur = conn.cursor()

    while True:
        print("\n1. Add/Update contact")
        print("2. Search")
        print("3. Show paginated")
        print("4. Delete")
        print("0. Exit")

        choice = input("Choose: ")

        if choice == "1":
            name = input("Name: ")
            phone = input("Phone: ")
            cur.execute("CALL upsert_contact(%s, %s)", (name, phone))
            conn.commit()

        elif choice == "2":
            pattern = input("Search: ")
            cur.execute("SELECT * FROM search_contacts(%s)", (pattern,))
            for row in cur.fetchall():
                print(row)

        elif choice == "3":
            limit = int(input("Limit: "))
            offset = int(input("Offset: "))
            cur.execute("SELECT * FROM get_contacts_paginated(%s, %s)", (limit, offset))
            for row in cur.fetchall():
                print(row)

        elif choice == "4":
            val = input("Enter name or phone: ")
            cur.execute("CALL delete_contact(%s)", (val,))
            conn.commit()

        elif choice == "0":
            break

    cur.close()
    conn.close()

menu()