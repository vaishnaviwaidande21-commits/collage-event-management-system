import sys
import os

# Add project path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from admin.admin_menu import admin_menu


def main():

    print("\n======================================")
    print(" College Event Management System ")
    print("======================================")

    admin_menu()


if __name__ == "__main__":
    main()