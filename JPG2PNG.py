import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image
import os

root= tk.Tk()

canvas1 = tk.Canvas(root, width = 300, height = 250, bg = 'lightsteelblue2', relief = 'raised')
canvas1.pack()

label1 = tk.Label(root, text='File Conversion Tool', bg = 'lightsteelblue2')
label1.config(font=('helvetica', 20))
canvas1.create_window(150, 60, window=label1)

def convertToPNG():

  imglist = []
  ipath = ''

  import_file_path = filedialog.askdirectory()

  for root, dirs, files in os.walk(import_file_path):
    for filename in files:
      if '.jpg' in filename:
        imglist.append(filename)
      
  ipath = import_file_path
  
  print(os.path.normpath(os.path.join(ipath,'PNGfiles')))

  try:
    os.mkdir(os.path.normpath(os.path.join(ipath,'PNGfiles')))
  except:
    pass
  
  for i in imglist:

    im1 = Image.open(os.path.normpath(os.path.join(ipath,i)))
    #export_file_path = filedialog.asksaveasfilename(defaultextension='.png')

    im1.save(os.path.normpath(os.path.join(ipath,'PNGfiles',i[:-4]+'.png')))
    print(os.path.normpath(os.path.join(ipath,'PNGfiles',i[:-4]+'.png')))

saveAsButton_PNG = tk.Button(text='Convert JPG to PNG', command=convertToPNG, bg='royalblue', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 180, window=saveAsButton_PNG)

root.mainloop()
