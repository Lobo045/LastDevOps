import os

# Example of usage
if __name__ == "__main__":
    while True:
        print("\n1. Create a client")
        print("2. Add project to a client")
        print("3. Add client information")
        print("4. Check if a client exists")
        print("5. List all clients")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            client_name = input("Enter client name: ")
            create_client(client_name)
        elif choice == "2":
            client_name = input("Enter client name: ")
            project_name = input("Enter project name: ")
            add_project_to_client(client_name, project_name)
        elif choice == "3":
            client_name = input("Enter client name: ")
            client_info = input("Enter client information: ")
            create_client_info(client_name, client_info)
        elif choice == "4":
            client_name = input("Enter client name: ")
            if check_if_client_exists(client_name):
                print(f"Client '{client_name}' exists.")
            else:
                print(f"Client '{client_name}' does not exist.")
        elif choice == "5":
            list_clients()
        elif choice == "6":
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")