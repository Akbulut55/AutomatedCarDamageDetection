import os


def rename_files_in_folder(folder_path):
    # Get a list of all files in the folder
    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

    # Sort files to ensure consistent numbering
    files.sort()

    # Rename files to sequential numbers
    for i, file_name in enumerate(files, start=1):
        # Extract file extension
        file_extension = os.path.splitext(file_name)[1]

        # Construct new file name
        new_name = f"{i}{file_extension}"

        # Get full paths
        old_path = os.path.join(folder_path, file_name)
        new_path = os.path.join(folder_path, new_name)

        # Rename file
        os.rename(old_path, new_path)


# Example usage
# Replace "path_to_folder" with the path to your folder
rename_files_in_folder("testimages")