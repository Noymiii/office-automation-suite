import os
import shutil

def organize_directory(target_folder):
    """
    Scans the target folder and moves files into subfolders based on extension.
    """
    # 1. Define file type mappings
    extensions = {
        'Documents': ['.pdf', '.docx', '.txt', '.xlsx', '.pptx'],
        'Images': ['.jpg', '.jpeg', '.png', '.gif', '.svg'],
        'Videos': ['.mp4', '.mov', '.avi'],
        'Archives': ['.zip', '.rar', '.tar']
    }

    # Verify path exists
    if not os.path.exists(target_folder):
        print(f"❌ Error: The folder '{target_folder}' does not exist.")
        return

    print(f"📂 Scanning: {target_folder}...")

    # 2. Iterate through files
    for filename in os.listdir(target_folder):
        file_path = os.path.join(target_folder, filename)

        # Skip directories and hidden files
        if os.path.isdir(file_path) or filename.startswith('.'):
            continue

        # 3. Check extension and move
        moved = False
        _, ext = os.path.splitext(filename)
        
        for folder_name, ext_list in extensions.items():
            if ext.lower() in ext_list:
                # Create destination folder if it doesn't exist
                dest_folder = os.path.join(target_folder, folder_name)
                os.makedirs(dest_folder, exist_ok=True)
                
                # Move the file
                try:
                    shutil.move(file_path, os.path.join(dest_folder, filename))
                    print(f"✅ Moved: {filename} -> {folder_name}/")
                    moved = True
                    break
                except Exception as e:
                    print(f"⚠️ Could not move {filename}: {e}")

        if not moved:
            print(f"ℹ️ Skipped: {filename} (Unknown extension)")

if __name__ == "__main__":
    # Change this path to test! Use raw string (r"path") for Windows paths.
    target_dir = input("Enter full path to folder to clean: ").strip()
    organize_directory(target_dir)