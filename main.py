import sys
import getpass
import paramiko
from colorama import init, Fore, Style

# Color initialization
init(autoreset=True)
orange = Fore.LIGHTMAGENTA_EX
yellow = Fore.LIGHTYELLOW_EX
white = Fore.WHITE

servers = ["server1", "server2", "serverames or IP addresses
usernames = ["admin", "root", "testsired usernames
passwords = ["password123", "123456", "letmeinords

def print_menu():
    print(orange + "=== SSH Login Test ===")
    print(yellow + "1. Run SSH login test")
    print("0. Exit")
    print("======================")

def run_ssh_login_test():
    print("\nRunning SSH login test...\n")

    for server in servers:
        for username in usernames:
            for password in passwords:
                ssh = paramiko.SSHClient()
                ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                try:
                    ssh.connect(server, username=username, password=password)
                    print(orange + f"Successful login with username: {username}, password: {password} on server: {server}")
                    # Execute further actions or tests here
                except paramiko.AuthenticationException:
                    print(f"Login failed with username: {username}, password: {password} on server: {server}")
                finally:
                    ssh.close()
    
    print("\nSSH login test complete.")

def execute_script():
    print("Executing the script...")
    # Add your script execution commands here

    print("Script execution complete.")

while True:
    print_menu()
    choice = input(white + "Enter your choice (" + yellow + "0" + white + " to exit, " + yellow + "1" + white + " to execute): ")

    if choice == "1":
        run_ssh_login_test()
    elif choice == "0":
        print("\n" + orange + "Thanks for using SSH Login Test!")
        sys.exit()
    else:
        print(white + "Invalid option. Please try again.")

    print()