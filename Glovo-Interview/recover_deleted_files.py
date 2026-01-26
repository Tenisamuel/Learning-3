import os
import platform

def get_trash_location():
    system = platform.system()

    if system == "Windows":
        return "C:\\$Recycle.Bin"
    elif system == "Linux":
        return os.path.expanduser("~/.local/share/Trash/files")
    elif system == "Darwin":  # macOS
        return os.path.expanduser("~/.Trash")
    else:
        return None

def list_deleted_files():
    trash_path = get_trash_location()

    if not trash_path or not os.path.exists(trash_path):
        print("Trash location not found for this system.")
        return

    print(f"\nDeleted files found in: {trash_path}\n")

    for item in os.listdir(trash_path):
        item_path = os.path.join(trash_path, item)
        print(item_path)

if __name__ == "__main__":
    list_deleted_files()