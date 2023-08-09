# Author 24bkdoor
# Giving back to the community
# Foldersize24
# Automation made easy

import tkinter as tk
from tkinter import scrolledtext
import subprocess
from tkinter.scrolledtext import ScrolledText


def list_folders():
    result = subprocess.run(["ls", "-lt", "--time=creation"], capture_output=True, text=True)
    output = result.stdout

    scrolled_text.delete(1.0, tk.END)  # Clear the existing content
    scrolled_text.insert(tk.END, output)


# Create the main window
window = tk.Tk()
window.title('[[**]]~ Foldersize24 GUI ~[[**]]')

# Create a button to trigger the listing
list_button = tk.Button(window, text="~[[**]] List Folders ~[[**]]", command=list_folders)
list_button.pack()

# Create a scrolled text widget to display the output
scrolled_text: ScrolledText = scrolledtext.ScrolledText(window, wrap=tk.WORD)
scrolled_text.pack()

# Run the GUI main loop
window.mainloop()
