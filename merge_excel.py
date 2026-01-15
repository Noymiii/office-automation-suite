import os
import pandas as pd
from datetime import datetime

def merge_excel_files(source_folder, output_filename="master_report.xlsx"):
    """
    Reads all Excel files in a folder and combines them into one master file.
    """
    all_data = []
    files_found = 0

    print(f"🔍 Looking for Excel files in: {source_folder}")

    if not os.path.exists(source_folder):
        print("❌ Error: Source folder not found.")
        return

    # 1. Loop through files
    for file in os.listdir(source_folder):
        if file.endswith(('.xlsx', '.xls')) and not file.startswith('~$'):
            print(f"📖 Reading: {file}...")
            file_path = os.path.join(source_folder, file)
            
            try:
                # Read data
                df = pd.read_excel(file_path)
                # Optional: Add a column to track source file
                df['Source_File'] = file
                all_data.append(df)
                files_found += 1
            except Exception as e:
                print(f"⚠️ Error reading {file}: {e}")

    # 2. Combine and Save
    if all_data:
        try:
            master_df = pd.concat(all_data, ignore_index=True)
            output_path = os.path.join(source_folder, output_filename)
            master_df.to_excel(output_path, index=False)
            print(f"\n🎉 Success! Merged {files_found} files.")
            print(f"💾 Saved as: {output_path}")
        except Exception as e:
            print(f"❌ Error saving master file: {e}")
    else:
        print("⚠️ No valid Excel files found to merge.")

if __name__ == "__main__":
    folder_path = input("Enter folder path containing Excel files: ").strip()
    merge_excel_files(folder_path)