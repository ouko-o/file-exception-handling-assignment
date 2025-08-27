# error_handling_lab.py

def read_file():
    filename = input("Enter filename to read: ")

    try:
        with open(filename, "r") as file:
            print("\nFile Content:\n")
            print(file.read())

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except PermissionError:
        print(f"Error: No permission to read '{filename}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    read_file()
