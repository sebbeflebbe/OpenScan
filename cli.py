import click
import getpass
import sqlite3

def connect_to_database():
    conn = sqlite3.connect('database.db')
    return conn

@click.group()
def main():
    pass

@click.command()
def register():
    username = input("Enter username to register for OpenScan: ")
    password = input("Enter password to register for OpenScan: ")
    conn = connect_to_database()
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT)")
    cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
    conn.commit()
    cursor.close()
    conn.close()

@click.command()
def login():
    username = input("Enter username to login to OpenScan: ")
    password = getpass.getpass("Enter password to login to OpenScan: ")
    conn = connect_to_database()
    cursor = conn.cursor()
    cursor.execute("SELECT username, password FROM users WHERE username = ? AND password = ?", (username, password))
    result = cursor.fetchone()
    if result:
        print("Login successful!")
    else:
        print("Invalid credentials!")
    cursor.close()
    conn.close()

main.add_command(register)
main.add_command(login)

if __name__ == "__main__":
    main()
