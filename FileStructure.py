import os

def get_file_structure(start_path: str, indent_level: int = 0) -> str:
    structure = ""
    indent = "    " * indent_level
    folder_name = os.path.basename(start_path)

    if indent_level == 0:
        structure += f"{folder_name}\n"

    try:
        entries = sorted(os.listdir(start_path))
    except PermissionError:
        return structure + f"{indent}- [Permission Denied]\n"

    for entry in entries:
        full_path = os.path.join(start_path, entry)
        if os.path.isdir(full_path):
            structure += f"{indent}- {entry}/\n"
            structure += get_file_structure(full_path, indent_level + 1)
        else:
            structure += f"{indent}- {entry}\n"

    return structure


def save_structure_to_file(start_path: str, output_file: str = "filepath.txt"):
    structure = get_file_structure(start_path)
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(structure)
    print(f"File structure saved to {output_file}")

# Either input a folder path beforehand or get prompted for one.
if __name__ == "__main__":
    path = r"" # Insert file path here

    if not path.strip():
        path = input("Please enter the directory path to scan: ").strip()

    if os.path.isdir(path):
        save_structure_to_file(path)
    else:
        print("Invalid directory path. Please check and try again.")
