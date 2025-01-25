import os
import shutil
import tkinter as tk
import ctypes as ct
import platform
from tkinter import filedialog
from tkinter import messagebox

class GUI:
    def __init__(self, root):

        self.root = root
        self.root.title("File Organisor")
        self.root.geometry("300x150")
        self.root.configure(bg="#222324")
        #Checks if on Windows system
        if platform.system() == "Windows":
            self.dark_title_bar(self.root)

        self.label = tk.Label(root, text="Select a directory to organize:", bg="#222324", fg="white")
        self.label.pack(pady=10)

        self.select_button = tk.Button(root, text="Select Directory", command=self.select_directory, bg="grey", fg="white")
        self.select_button.pack(pady=10)

        self.organize_button = tk.Button(root, text="Organize Files", command=self.organize_files, state=tk.DISABLED, bg="grey", fg="white")
        self.organize_button.pack(pady=10)

        self.directory = ""

    #Only works on Windows
    def dark_title_bar(self, window):
        window.update()
        set_window_attribute = ct.windll.dwmapi.DwmSetWindowAttribute
        get_parent = ct.windll.user32.GetParent
        hwnd = get_parent(window.winfo_id())
        value = 2
        value = ct.c_int(value)
        set_window_attribute(hwnd, 20, ct.byref(value),4)

    def select_directory(self):
        self.directory = filedialog.askdirectory()
        if self.directory:
            self.organize_button.config(state=tk.NORMAL)
            messagebox.showinfo("Selected Directory", f"Selected directory: {self.directory}")

    def organize_files(self):
        if self.directory:
            os.chdir(self.directory)
            fo = FileOrganisor()
            fo.OrganiseFiles(self.directory)
            messagebox.showinfo("Success", "Files organized successfully!")

class FileOrganisor:

    file_extensions = {
        '.txt': 'Text',
        '.doc': 'Document',
        '.docx': 'Document',
        '.pdf': 'Document',
        '.rtf': 'Document',
        '.odt': 'Document',
        '.jpg': 'Image',
        '.jpeg': 'Image',
        '.png': 'Image',
        '.gif': 'Image',
        '.bmp': 'Image',
        '.tiff': 'Image',
        '.mp3': 'Audio',
        '.wav': 'Audio',
        '.flac': 'Audio',
        '.aac': 'Audio',
        '.mp4': 'Video',
        '.avi': 'Video',
        '.mov': 'Video',
        '.wmv': 'Video',
        '.xlsx': 'Spreadsheet',
        '.xls': 'Spreadsheet',
        '.csv': 'Spreadsheet',
        '.pptx': 'Presentation',
        '.ppt': 'Presentation',
        '.zip': 'Archive',
        '.rar': 'Archive',
        '.7z': 'Archive',
        '.tar': 'Archive',
        '.exe': 'Executable',
        '.msi': 'Executable',
        '.py': 'Code',
        '.java': 'Code',
        '.html': 'Web',
        '.css': 'Web',
        '.js': 'Web'
    }

    def OrganiseFiles(self, directory):
        for extension, folder_name in self.file_extensions.items():
            files = [f for f in os.listdir() if f.lower().endswith(extension)]

            if files:
                folder_path = os.path.join(directory, folder_name)
                os.makedirs(folder_path, exist_ok=True)

                for file in files:
                    source_path = os.path.join(directory, file)
                    destination_path = os.path.join(folder_path, file)
                    shutil.move(source_path, destination_path)
                    print(f"Moved {file} to {folder_name} folder")

if __name__ == '__main__':
    root = tk.Tk()
    gui = GUI(root)
    root.mainloop()