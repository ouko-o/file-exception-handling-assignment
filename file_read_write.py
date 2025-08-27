# file_read_write.py

def modify_content(content):
    """Modify file content by converting to uppercase."""
    return content.upper()

def main():
    input_file = "input.txt"
    output_file = "output.txt"

    try:
        with open(input_file, "r") as file:
            content = file.read()

        modified_content = modify_content(content)

        with open(output_file, "w") as file:
            file.write(modified_content)

        print(f"Modified content written to {output_file}")

    except FileNotFoundError:
        print(f"Error: {input_file} not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
