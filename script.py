import tkinter as tk
from tkinter import ttk
import shutil
import os

def copy_files():
    source_folder = source_folder_entry.get()
    destination_folder = destination_folder_entry.get()
    filenames = filenames_entry.get().split(",")  # Split filenames by comma

    copied_files = []
    not_found_files = []

    # Create Assets and Exports folders in the destination folder
    assets_folder = os.path.join(destination_folder, "assets")
    exports_folder = os.path.join(destination_folder, "exports")
    clips_folder = os.path.join(destination_folder, "clips")
    projectFiles_folder = os.path.join(destination_folder, "Project Files")
    os.makedirs(assets_folder, exist_ok=True)
    os.makedirs(exports_folder, exist_ok=True)
    os.makedirs(clips_folder, exist_ok=True)
    os.makedirs(projectFiles_folder, exist_ok=True)
    for filename in filenames:
        source_path = os.path.join(source_folder, filename.strip())  # Remove leading/trailing spaces
        destination_path = os.path.join(destination_folder, filename.strip())  # Remove leading/trailing spaces

        if os.path.exists(destination_path):
            print("Multiple files already in directory")
        else:
            try:
                shutil.copy(source_path, destination_path)
                copied_files.append(filename)
            except FileNotFoundError:
                not_found_files.append(filename)
            except Exception as e:
                result_text.insert(tk.END, f"Error copying {filename}: {e}\n")

    # Clear the filenames & destination text box after successful copy
    filenames_entry.delete(0, tk.END)
    destination_folder_entry.delete(0, tk.END)

    # Display the copied and not found files separately
    result_text.insert(tk.END, "Copied Files:\n")
    for filename in copied_files:
        result_text.insert(tk.END, f"Copied: {filename}\n")

    result_text.insert(tk.END, "\nFiles Not Found:\n")
    for filename in not_found_files:
        result_text.insert(tk.END, f"File not found: {filename}\n")

# Create the main window
window = tk.Tk()
window.title("File Copy Tool")

# Create and place GUI components
source_folder_label = ttk.Label(window, text="Source Folder:")
source_folder_label.pack(pady=5)

source_folder_entry = ttk.Entry(window, width=40)
source_folder_entry.pack()

destination_folder_label = ttk.Label(window, text="Destination Folder:")
destination_folder_label.pack(pady=5)

destination_folder_entry = ttk.Entry(window, width=40)
destination_folder_entry.pack()

filenames_label = ttk.Label(window, text="List of Filenames (comma-separated):")
filenames_label.pack(pady=5)

filenames_entry = ttk.Entry(window, width=40)
filenames_entry.pack()

copy_button = ttk.Button(window, text="Copy Files", command=copy_files)
copy_button.pack(pady=10)

result_text = tk.Text(window, height=10, width=60)
result_text.pack()

# Start the GUI event loop
window.mainloop()
