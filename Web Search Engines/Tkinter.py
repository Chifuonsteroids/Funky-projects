from tkinter import * 
from goose3 import Goose

root =Tk()
root.configure(bg='light blue')

#Visualizing using tkinter
def info():
    article = Goose().extract(e1.get())
    title.set(article.title)
    meta.set(article.meta_description)
    string = article.cleaned_text[:150]
    art_dec.set(string.split('\n'))

#variable classes 
title = StringVar();
meta = StringVar();
art_dec = StringVar();

#Labels for each information  name using widget Label
Label(root, text="Website URL : ", bg="light grey").grid(row=0, sticky=W)
Label(root, text="Title : ", bg="light grey").grid(row=3, sticky=W)
Label(root,text="Meta information : ", bg="light grey").grid(row=4, sticky=W)
Label(root, text="Article Description : ", bg="light grey").grid(row=5, sticky=W)

#Lables for class variables name using widget entry
Label(root, text="", textvariable=title, bg="light grey").grid(row=3, column=1, sticky=W)
Label(root, text="", textvariable=meta, bg="light grey").grid(row=4, column=1, sticky=W)
Label(root, text="", textvariable=art_dec, bg="light grey").grid(row=5, column=1, sticky=W)

e1= Entry(root,width=100)
e1.grid(row=0, column=1)

#Buttons
b = Button(root, text="Show",command=info,bg = "blue")
b.grid(row=0, column=2, columnspan=2, rowspan=2, padx=5, pady=5,)

root.mainloop()