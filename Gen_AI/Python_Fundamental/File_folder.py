import os  # Import the os module
import shutil  # Import the shutil module for moving files

# Check if a folder exists and create it if it doesn't
def create_folder(destination_folder):
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)  # Create the folder if it doesn't exist
        print(f"Folder created: {destination_folder}")
    else:
        print(f"Folder already exists: {destination_folder}")

# Search for files based on file name substring or file extension
def search_files(folder_path, search_param):
    """
    Dynamically search for files by file name or file extension.

    Parameters:
        folder_path (str): The path to the folder to search in.
        search_param (str): The search parameter, either a file name substring or a file extension.

    Returns:
        list: A list of matching file paths.
    """
    # Ensure the folder exists
    if not os.path.exists(folder_path):
        print(f"Folder '{folder_path}' does not exist.")
        return []

    # Identify the type of search based on the parameter value
    if search_param.startswith("."):
        search_type = "extension"
        matching_files = [file for file in os.listdir(folder_path) if file.endswith(search_param)]
    else:
        search_type = "name"
        matching_files = [file for file in os.listdir(folder_path) if search_param.lower() in file.lower()]

    # Print results and return the matching file paths
    if matching_files:
        print(f"Files matching by {search_type} '{search_param}' in '{folder_path}':")
        for file in matching_files:
            print(f"--- {file}")
        return [os.path.join(folder_path, file) for file in matching_files]
    else:
        print(f"No files matching by {search_type} '{search_param}' found in '{folder_path}'.")
        return []

# Move files to a destination folder
def move_files(file_paths, destination_folder):
    """
    Move the list of files to the destination folder.

    Parameters:
        file_paths (list): List of file paths to move.
        destination_folder (str): Path to the destination folder.

    Returns:
        None
    """
    create_folder(destination_folder)  # Ensure the destination folder exists

    for file_path in file_paths:
        if os.path.exists(file_path):
            shutil.move(file_path, destination_folder)  # Move the file
            print(f"Moved: {file_path} -> {destination_folder}")
        else:
            print(f"File not found: {file_path}")

# Delete files from a folder
def delete_files(file_paths):
    """
    Delete the list of files.

    Parameters:
        file_paths (list): List of file paths to delete.

    Returns:
        None
    """
    for file_path in file_paths:
        if os.path.exists(file_path):
            os.remove(file_path)  # Delete the file
            print(f"Deleted: {file_path}")
        else:
            print(f"File not found: {file_path}")

# Example Usage
folder_path = '/Users/sanjaybiswas/Downloads'  # Replace with your folder path
search_param = '.docx'  # Example: '.csv' for extension, 'report' for name
destination_folder = '/Users/sanjaybiswas/Documents/Doc_files'  # Replace with your destination folder path

# Search for matching files
matching_files = search_files(folder_path, search_param)

# Move matching files to the destination folder
'''if matching_files:
    move_files(matching_files, destination_folder)'''


