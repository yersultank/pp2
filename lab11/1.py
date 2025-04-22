import csv
import os
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

contact_list=[["Yera", 88287387],["Oleg", 41273789],["Bolat", 58827913]]
    
# add_contact="""CREATE OR REPLACE PROCEDURE add_contact(name VARCHAR(20), contact VARCHAR(20))
#         LANGUAGE plpgsql
#         AS $$
#         BEGIN
#                 INSERT INTO phonebook(name,contact) VALUES (name,contact);
#         END;
#         $$;"""

# search_contacts="""
# CREATE OR REPLACE FUNCTION search_contacts(keyword TEXT)
# RETURNS TABLE (id INTEGER, name TEXT, contact TEXT)
# LANGUAGE plpgsql
# AS $$
# BEGIN
# 	RETURN QUERY
# 	SELECT * FROM phonebook WHERE name ILIKE '%' || keyword || '%'
# 	OR contact ILIKE '%' || keyword || '%';
# END;
# $$;
#         """


def add_contacts(name,contact):
    config=load_config()
    conn=psycopg2.connect(**config)
    cur=conn.cursor()
    cur.execute("CALL add_contact(%s, %s)", (name,contact))
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
    cur.execute("CALL delete_contact(%s)", (contact_id,))
    conn.commit()
    print("the contact has been deleted")
    cur.close()
    conn.close()

def add_many_contacts(contact_list):
    config = load_config()
    conn = psycopg2.connect(**config)
    cur = conn.cursor()
    cur.execute("""CALL add_many_contacts(ARRAY[
                ROW('Yera', 88287387),
                ROW('Oleg', 41273789),
                ROW('Bolat', 58827913)
                ]::contact_input[])""")
    conn.commit()
    print("the contacts were added")
    cur.close()
    conn.close()
def search_contacts(keyword):
    config=load_config()
    conn=psycopg2.connect(**config)
    cur=conn.cursor()
    cur.execute("SELECT * FROM search_contacts(%s)", (keyword, ))
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
        print("7 - add multiple contacts")
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
        
        elif choice==7:
            add_many_contacts(contact_list)
        
        elif choice==0:
            print("exiting...")
            break

        else:
            print("no such command")

if __name__ == '__main__':
    main()