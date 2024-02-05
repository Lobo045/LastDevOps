import os

def create_client(client_name):
    client_file_path = f"clients/{client_name}.txt"
    with open(client_file_path, 'w') as client_file:
        # You can add more details or projects if needed
        client_file.write(f"Projects for {client_name}:\n")
    print(f"Client '{client_name}' created successfully!")

def add_project_to_client(client_name, project_name):
    client_file_path = f"clients/{client_name}.txt"
    with open(client_file_path, 'a') as client_file:
        client_file.write(f"- {project_name}\n")
    print(f"Project '{project_name}' added to client '{client_name}' successfully!")

def create_client_info(client_name, client_info):
    client_info_file_path = f"client_info/{client_name}_info.txt"
    with open(client_info_file_path, 'w') as info_file:
        info_file.write(client_info)
    print(f"Client information for '{client_name}' created successfully!")

def check_if_client_exists(client_name):
    client_file_path = f"clients/{client_name}.txt"
    return os.path.exists(client_file_path)

def list_clients():
    clients_folder = "clients"
    clients = [file.replace(".txt", "") for file in os.listdir(clients_folder) if file.endswith(".txt")]
    if not clients:
        print("No clients found.")
    else:
        print("List of clients:")
        for client in clients:
            print(f"- {client}")

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