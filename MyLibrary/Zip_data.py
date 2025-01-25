import zipfile

# Path to the ZIP file
zip_path = "/Users/sanjaybiswas/Documents/Pycharm/Output_data/iris.csv.zip"

# Open and read a specific file inside the ZIP archive
with zipfile.ZipFile(zip_path, 'r') as zip_file:
    # List all files in the ZIP archive and filter out "__MACOSX/._" files
    list_of_files = [file for file in zip_file.namelist() if not file.startswith("__MACOSX/._")]
    print("List of files in the ZIP archive:")
    for file in list_of_files:
        print(f"- {file}")
    '''
    # Mention file name you want to read
    file_name = "iris.csv"
    if file_name in list_of_files:
        # Open the specified file
        with zip_file.open(file_name) as file:
            content = file.read().decode('utf-8')  # Decode to string if it's a text file
            print(f"\nContent of {file_name}:\n{content}")
    else:
        print(f"\n{file_name} not found in ZIP archive.")
    '''
    # Read the content of all files in the ZIP archive
    print("\nContent of all files in the ZIP archive:")
    for file_name in list_of_files:
        try:
            # Open and read the content of the file
            with zip_file.open(file_name) as file:
                content = file.read().decode('utf-8')  # Decode as a text file
                print(f"\nContent of {file_name}:\n{'-' * 40}\n{content}")
        except Exception as e:
            print(f"Error reading {file_name}: {e}")