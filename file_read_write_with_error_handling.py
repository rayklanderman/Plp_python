# Title: File Read & Write with Error Handling

def modify_file_content(content):
    """
    Modifies the content of the file by converting it to uppercase.
    :param content: Original content from the file
    :return: Modified content
    """
    return content.upper()

def read_and_write_files():
    """
    Reads a file and writes a modified version of its content to a new file.
    Handles errors gracefully if the file doesn't exist or can't be read.
    """
    try:
        # Ask the user for the input filename
        input_file = input("Enter the name of the file to read: ").strip()
        
        # Attempt to open and read the file
        with open(input_file, "r") as file:
            content = file.read()
        
        # Modify the content
        modified_content = modify_file_content(content)
        
        # Write the modified content to a new file
        output_file = "modified_" + input_file
        with open(output_file, "w") as file:
            file.write(modified_content)
        
        print(f"Content modified and written to {output_file}")
    
    except FileNotFoundError:
        print(f"Error: The file '{input_file}' does not exist. Please check the filename and try again.")
    except IOError:
        print(f"Error: Unable to read or write to the file. Please check the file permissions.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the program
if __name__ == "__main__":
    read_and_write_files()
