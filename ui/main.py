import tkinter as tk

from PIL import Image, ImageTk
from machinelearning import logic

def change_pic():
    handler = entry.get()
    result = logic.calculate_person_type(handler)
    value = "{0} is a {1} person".format(handler, result)
    if result == 'cat':
        vlabel.configure(image=root.photo)
        text.configure(text=value)
    elif result == 'dog':
        vlabel.configure(image=root.photo1)
        text.configure(text=value)
    elif result == 'dogcat':
        vlabel.configure(image=root.photo2)
        value = "{} loves dogs and cats equally".format(handler)
        text.configure(text=value)
    else:
        vlabel.configure(image=root.photo4)
        text.configure(text="{} was not found.".format(handler))



root = tk.Tk()


photo_status = 'Results'

root.minsize(1000,600)
root.title("CatDogPerson")

photo = '../images/cat_mk3.png'
photo1 = "../images/dog.png"
photo2 = "../images/cat_and_dog.png"
photo3 = "../images/loading.png"
photo4 = "../images/error.png"

# I should make all these repeating patterns into a function and just call it with different arguments
# but I'm too lazy atm
# FIXME:// Make this look nicer

image = Image.open(photo)
image = image.resize((300, 250), Image.ANTIALIAS)

root.photo = ImageTk.PhotoImage(image)

image = Image.open(photo1)
image = image.resize((300, 250), Image.ANTIALIAS)

root.photo1 = ImageTk.PhotoImage(image)

image = Image.open(photo2)
image = image.resize((300, 250), Image.ANTIALIAS)

root.photo2 = ImageTk.PhotoImage(image)

image = Image.open(photo3)
image = image.resize((300, 250), Image.ANTIALIAS)

root.photo3 = ImageTk.PhotoImage(image)

image = Image.open(photo4)
image = image.resize((300, 250), Image.ANTIALIAS)

root.photo4 = ImageTk.PhotoImage(image)

vlabel=tk.Label(root,image=root.photo)
vlabel.pack()

b2=tk.Button(root,text="Check",command=change_pic)
b2.pack()

entry = tk.Entry(root)

entry.pack()

text = tk.Label(root, text=photo_status)
text.pack()

root.mainloop()
