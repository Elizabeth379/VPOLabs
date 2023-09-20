import glob
import os


def search_files_with_extension(extension):
    current_dir = "C:/projects/vpo/l1t5"
    search_pattern = os.path.join(current_dir, f"**/*.{extension}")
    return glob.glob(search_pattern, recursive=True)

def searching_time():
    file_extension = "py"
    files = search_files_with_extension(file_extension)

    if not files:
        print(f"Files with extension .{file_extension} not found.")
    else:
        print("List of found files:\n")
        for f in files:
            print(f)

if __name__ == "__main__":
    searching_time()