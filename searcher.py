import os

def search_folder(directory, folder_name):
    for root, dirs, files in os.walk(directory):
        if folder_name in dirs:
            print(f"Folder found at: {os.path.join(root, folder_name)}")

# Replace the directory path and folder name with your desired values
search_folder("C:/Users/Username/Documents", "FolderName")
