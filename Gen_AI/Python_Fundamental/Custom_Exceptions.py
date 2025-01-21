import subprocess

# Execute a terminal command fro clear screen
print(subprocess.run(["clear"], capture_output=True, text=True).stdout)

class FileNotFoundError(Exception):
    pass

class PermissionError(Exception):
    pass

def open_file(filename, mode):
    if filename != "data.txt":
        raise FileNotFoundError("The specified file does not exist.")
    if mode != "r":
        raise PermissionError("You do not have permission to write to this file.")
    print("File opened successfully.")


try:
    open_file("data.txt", "w")
except FileNotFoundError as e:
    print(f"File Error: {e}")
except PermissionError as e:
    print(f"Permission Error: {e}")

