import click
import getpass

@click.command()
def main():
    pass

@click.command()
def register():
    username = input("Enter username to register for OpenScan: ")
    password = input("Enter password to register for OpenScan: ")
## Store username and password securely

def login():
    username = input("Enter username to login: ")
    password = getpass.getpass("Enter password to login: ")
## Compare credentials with stored information
## Provide feedback to user

main.add_command(register)
main.add_command(login)

if __name__ == "__main__":
    main()