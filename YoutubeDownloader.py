# Initialize libraries
import os
from pytube import YouTube, exceptions
from time import time
from tkinter import *
from customtkinter import *

# Initialize appearance and folder
set_appearance_mode("Dark") # System/Light/Dark
set_default_color_theme("blue")
for i in os.listdir(os.getcwd()):
    if i == "youtube_downloads": # Avoids creating multiple folders
        break
else:
    os.mkdir("youtube_downloads")

# Function to download video
def download_video(entryfield):
    try:
        download_location = "youtube_downloads/"
        YouTube(entryfield).streams.first().download(download_location)


        # "Download successful" pop-up
        popup = CTk()
        popup.title("Download Status")
        popup.geometry("200x100")
        popup.grid_columnconfigure(0, weight=1)
        popup.grid_rowconfigure((0,1), weight=1)

        msg = StringVar()
        msg.set(f"Downloaded")

        label = CTkLabel(popup, text=msg.get())
        label.grid(row=0, column=0)

        button = CTkButton(popup, text="OK", command=popup.destroy)
        button.grid(row=1, column=0)

        popup.mainloop()
    except exceptions.RegexMatchError: # Error message in case of invalid link
        error = CTk()
        error.title("Error")
        error.resizable(False, False)
        error.geometry("300x200")

        error.grid_rowconfigure((0,1), weight=1)
        error.grid_columnconfigure(0, weight=1)

        error_label = CTkLabel(error, text="Invalid YouTube link  :( ")
        error_label.grid(row=0, column=0)

        button = CTkButton(error, text="OK", command=error.destroy)
        button.grid(row=1, column=0)
        error.mainloop()

# Main pop-up settings
master = CTk()
master.title("YouTube Downloader")
master.grid_rowconfigure((0,1), weight=1)
master.grid_columnconfigure((0,1), weight=1)
master.geometry("300x100")

CTkLabel(master, text="Enter YouTube video URL:").grid(row=0, column=0)

entry = CTkEntry(master)
entry.grid(row=0, column=1)

CTkButton(master, text='Download', command=lambda *args: download_video(entry.get())).grid(row=1, column=0, columnspan=2)
master.mainloop()
