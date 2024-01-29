# Import the 'os' module to handle file operations
import os

# Function to create a new note
def create_note():
    # Prompt the user to enter the note's title and content
    note_title = input("Enter note title: ")

    # Initialize an empty list to store the lines of content
    note_content = []

    print("Enter note content (type 'done' on a new line when finished):")

    # Continue reading lines of content until the user enters 'done'
    while True:
        line = input()
        if line == 'done':
            break
        note_content.append(line)

    # Define the filename for the note, using the 'notes' directory
    note_filename = f"notes/{note_title}.txt"

    # Open the note file in write mode and write the content to it
    with open(note_filename, "w") as note_file:
        for line in note_content:
            note_file.write(line + '\n')

    print(f"Note '{note_title}' created successfully!")

# Function to view existing notes
def view_notes():
    # Specify the directory where notes are stored
    notes_directory = "notes/"
    
    # Check if the 'notes' directory is empty
    if not os.listdir(notes_directory):
        print("No notes found.")
        return

    # Display a list of available notes by listing files in the directory
    print("Available notes:")
    for filename in os.listdir(notes_directory):
        # Remove the '.txt' extension from filenames and print
        print(filename[:-4])

# Function to delete a note
def delete_note():
    # Prompt the user to enter the title of the note they want to delete
    note_title = input("Enter the title of the note you want to delete: ")
    
    # Define the filename for the note to be deleted
    note_filename = f"notes/{note_title}.txt"
    
    # Check if the note file exists
    if os.path.exists(note_filename):
        # If it exists, remove the note file
        os.remove(note_filename)
        # Notify the user that the note has been deleted successfully
        print(f"Note '{note_title}' deleted successfully!")
    else:
        # If the note file does not exist, inform the user
        print(f"Note '{note_title}' not found.")

# Entry point of the program
if __name__ == "__main__":
    # Display a menu for the Note-taking App
    print("Note-taking App")
    print("Options:")
    print("1. Create a new note")
    print("2. View existing notes")
    print("3. Delete a note")
    
    # Prompt the user to enter their choice
    choice = input("Enter your choice: ")

    # Based on the user's choice, call the corresponding function
    if choice == "1":
        create_note()
    elif choice == "2":
        view_notes()
    elif choice == "3":
        delete_note()
    else:
        # Handle an invalid choice by displaying a message
        print("Invalid choice.")
