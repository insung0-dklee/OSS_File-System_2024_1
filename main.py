import os

def getParentDir(path):
    return os.path.dirname(path)

import os

def getParentDir(path):
    return os.path.dirname(path)

import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

def resize_image(image, size):
    return image.resize(size, Image.ANTIALIAS)

def open_and_resize():
    file_path = filedialog.askopenfilename()
    if file_path:
        image = Image.open(file_path)
        if size_var.get() == 'Large':
            resized_image = resize_image(image, (256, 256))
        elif size_var.get() == 'Medium':
            resized_image = resize_image(image, (128, 128))
        else:  # Small
            resized_image = resize_image(image, (64, 64))
        
        img = ImageTk.PhotoImage(resized_image)
        image_label.configure(image=img)
        image_label.image = img

app = tk.Tk()
app.title('File Icon Resizer')

size_var = tk.StringVar(value='Medium')

tk.Radiobutton(app, text='Large', variable=size_var, value='Large').pack()
tk.Radiobutton(app, text='Medium', variable=size_var, value='Medium').pack()
tk.Radiobutton(app, text='Small', variable=size_var, value='Small').pack()

open_button = tk.Button(app, text='Open Image', command=open_and_resize)
open_button.pack()

image_label = tk.Label(app)
image_label.pack()

app.mainloop()
