import csv
import psycopg2
from config import load_config
def create_table():
    conn=psycopg2.connect(host="localhost", database="suppliers", user="postgres", password="ersultan7")
    cur=conn.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS phonebook (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100),
        contact VARCHAR(20)
        );
        """)
    conn.commit()
    cur.close()
    print("Database has been created or already exists")

def add_contacts(name,contact):
    config=load_config()
    conn=psycopg2.connect(**config)
    cur=conn.cursor()
    cur.execute("INSERT INTO phonebook (name,contact) VALUES (%s, %s)", (name,contact))
    conn.commit()
    print("the contact has been added")
    cur.close()
    conn.close()

def view_contacts():
    config=load_config()
    conn=psycopg2.connect(**config)
    cur=conn.cursor()
    cur.execute("SELECT * FROM phonebook")
    rows=cur.fetchall()
    if rows:
        print("contacts:")
        for row in rows:
            print(f"{row[0]}. {row[1]}-{row[2]}")
    else:
        print("the phonebook is empty")
    cur.close()
    conn.close()

def update_contacts(contact_id, new_name, new_contact):
    config=load_config()
    conn=psycopg2.connect(**config)
    cur=conn.cursor()
    contact_id = int(contact_id)
    cur.execute("UPDATE phonebook SET name=%s, contact=%s WHERE id=%s", (new_name, new_contact, contact_id))
    conn.commit()
    print("the contact has been updated")
    cur.close()
    conn.close()

def delete_contacts(contact_id):
    config=load_config()
    conn=psycopg2.connect(**config)
    cur=conn.cursor()
    cur.execute("DELETE from phonebook WHERE id=%s", (contact_id,))
    conn.commit()
    print("the contact has been deleted")
    cur.close()
    conn.close()

def search_contacts(keyword):
    config=load_config()
    conn=psycopg2.connect(**config)
    cur=conn.cursor()
    cur.execute("SELECT * FROM phonebook WHERE name ILIKE %s OR contact ILIKE %s", (f"%{keyword}%", f"%{keyword}%"))
    rows=cur.fetchall()
    if rows:
        for row in rows:
            print("the result of the searching:")
            print(f"{row[0]}. {row[1]} - {row[2]}")
    else:
        print("no match found")
    cur.close()
    conn.close()

def csv_import(filename):
    config=load_config()
    conn=psycopg2.connect(**config)
    cur=conn.cursor()
    with open(filename, newline='') as csvfile:
        reader=csv.DictReader(csvfile)
        for row in reader:
            name=row['name']
            contact=row['contact']
            cur.execute("INSERT INTO phonebook (name, contact) VALUES (%s,%s)", (name,contact))
    conn.commit()
    print("data from csv-file has beeen added")
    cur.close()
    conn.close()
def main():
    create_table()
    while True:
        print("Interface:")
        print("1 - view contacts")
        print("2 - add contacts")
        print("3 - update contacts")
        print("4 - search contacts")
        print("5 - delete contacts")
        print("6 - import from csv-file")
        print("0 - exit")
        choice=int(input())
        
        if choice==1:
            view_contacts()
        
        elif choice==2:
            name=input("name:")
            contact=input("contact:")
            add_contacts(name,contact)

        elif choice==3:
            contact_id=input("contact id:")
            name=input("new name:")
            contact=input("new contact:")
            update_contacts(contact_id,name,contact)
        
        elif choice==4:
            keyword=input("search for:")
            search_contacts(keyword)
        
        elif choice==5:
            contact_id=input("contact id:")
            delete_contacts(contact_id)
        
        elif choice==6:
            filename=input("name of csv-file:")
            csv_import(filename)
        
        elif choice==0:
            print("exiting...")
            break

        else:
            print("no such command")

if __name__ == '__main__':
    main()