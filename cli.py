import click
import getpass
import psycopg2

def connect_to_database():
    conn = psycopg2.connect(
        host="",
        port=26257,
        database="defaultdb",
        user="OpenScan",
        password="eax8Hk7VQkmtOA3R7yo2mQ"
    )
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
    cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
    conn.commit()
    cursor.close()
    conn.close()

@click.command()
def login():
    username = input("Enter username to login: ")
    password = getpass.getpass("Enter password to login: ")
    conn = connect_to_database()
    cursor = conn.cursor()
    cursor.execute("SELECT username, password FROM users WHERE username = %s AND password = %s", (username, password))
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
