# /home/helaman/Desktop/Void_IDE_testing/converter.py

import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
import threading
import os
import subprocess
import platform
import webbrowser

def run_async(func, *args):
    """Helper function to run heavy tasks in a background thread."""
    threading.Thread(target=func, args=args, daemon=True).start()

def convert_batch():
    source_folder = source_folder_entry.get()
    destination_folder = destination_folder_entry.get()
    
    if not os.path.exists(source_folder) or not os.path.exists(destination_folder):
        messagebox.showerror("Error", "Invalid source or destination folder.")
        return

    # Start the progress animation on the main thread
    progress_bar.start(10)
    convert_button.config(state='disabled')
    individual_button.config(state='disabled')

    def worker():
        for root_dir, dirs, files in os.walk(source_folder):
            for file in files:
                if file.lower().endswith(('.mp4', '.mov')):
                    input_path = os.path.join(root_dir, file)
                    base_name, ext = os.path.splitext(file)
                    output_path = os.path.join(destination_folder, f"{base_name}_fixed{ext}")
                    
                    subprocess.run(['ffmpeg', '-i', input_path, '-c:v', 'copy', '-c:a', 'pcm_s16le', '-y', output_path])
        
        # Safely reset the UI on the main thread when done
        root.after(0, finish_conversion, "Batch conversion completed.")

    run_async(worker)

def select_individual_files():
    if platform.system() == 'Linux':
        try:
            zenity_cmd = ['zenity', '--file-selection', '--multiple', '--file-filter=*.mp4 *.mov *.MP4 *.MOV']
            output = subprocess.run(zenity_cmd, capture_output=True, text=True).stdout.strip()
            files_selected = output.split('|') if output else []
        except subprocess.CalledProcessError:
            files_selected = []
    else:
        files_selected = filedialog.askopenfilenames(filetypes=[("Video Files", "*.mp4 *.mov *.MP4 *.MOV")])
        
    if files_selected and files_selected != ['']:
        destination_folder = destination_folder_entry.get()
        
        # Start progress animations
        progress_bar.start(10)
        convert_button.config(state='disabled')
        individual_button.config(state='disabled')

        def worker():
            for file in files_selected:
                input_path = os.path.abspath(file)
                output_folder = destination_folder if destination_folder else os.path.dirname(input_path)
                base_name, ext = os.path.splitext(os.path.basename(input_path))
                output_path = os.path.join(output_folder, f"{base_name}_fixed{ext}")
                
                subprocess.run(['ffmpeg', '-i', input_path, '-c:v', 'copy', '-c:a', 'pcm_s16le', '-y', output_path])
            
            root.after(0, finish_conversion, "Individual file conversion completed.")

        run_async(worker)

def finish_conversion(message):
    """Resets the UI elements safely on the main thread."""
    progress_bar.stop()
    convert_button.config(state='normal')
    individual_button.config(state='normal')
    messagebox.showinfo("Success", message)

def select_source_folder():
    if platform.system() == 'Linux':
        folder_selected = subprocess.run(['zenity', '--file-selection', '--directory'], capture_output=True, text=True).stdout.strip()
    else:
        folder_selected = filedialog.askdirectory()
    if folder_selected:
        source_folder_entry.delete(0, 'end')
        source_folder_entry.insert(0, folder_selected)

def select_destination_folder():
    if platform.system() == 'Linux':
        folder_selected = subprocess.run(['zenity', '--file-selection', '--directory'], capture_output=True, text=True).stdout.strip()
    else:
        folder_selected = filedialog.askdirectory()
    if folder_selected:
        destination_folder_entry.delete(0, 'end')
        destination_folder_entry.insert(0, folder_selected)

# --- UI Layout Setup ---
root = tk.Tk()
root.title('Batch Video Converter')

# Source layout
tk.Label(root, text='Source Folder:').grid(row=0, column=0, padx=10, pady=5)
source_folder_entry = tk.Entry(root, width=50)
source_folder_entry.grid(row=0, column=1, padx=10, pady=5)
tk.Button(root, text='Browse', command=select_source_folder).grid(row=0, column=2, padx=10, pady=5)

# Destination layout
tk.Label(root, text='Destination Folder:').grid(row=1, column=0, padx=10, pady=5)
destination_folder_entry = tk.Entry(root, width=50)
destination_folder_entry.grid(row=1, column=1, padx=10, pady=5)
tk.Button(root, text='Browse', command=select_destination_folder).grid(row=1, column=2, padx=10, pady=5)

# Interactive Buttons
convert_button = tk.Button(root, text='Convert Batch', command=convert_batch)
convert_button.grid(row=2, column=0, columnspan=3, pady=10)

individual_button = tk.Button(root, text='Select Individual Files', command=select_individual_files)
individual_button.grid(row=3, column=0, columnspan=3, pady=10)

# Progress Bar Widget (New!)
progress_bar = ttk.Progressbar(root, orient='horizontal', length=400, mode='indeterminate')
progress_bar.grid(row=4, column=0, columnspan=3, pady=15)


def open_github():
    webbrowser.open_new_tab("https://github.com/ClaudiusMinimus/video_audio_transcoder")

label = tk.Label(root, text='Visit GitHub Repository', cursor='hand2', fg='blue', underline=True)
label.grid(row=5, column=0, columnspan=3, pady=10, ipady=4)  # Adjusted padding to ensure the link appears underlined

label.bind('<Button-1>', lambda event: open_github())


root.mainloop()
