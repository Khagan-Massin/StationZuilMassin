from tkinter import *
#from PIL import ImageTk, Image
'''''''''
def onclick():
    base = int(entry.get())
    square = base ** 2
    outcome = f'square of: {base} = {square}'
    label['text'] = outcome

root = Tk()

label = Label(master=root, text="Hello World", height =2)
label.pack()

button = Button(master=root, text="Press", command=onclick)
button.pack(pady=10)

entry = Entry(master=root)
entry.pack(pady=10, padx=10)

root.mainloop()


img = Image.open(file='train.jpg')
bg = ImageTk.PhotoImage(img)
bg.pack()
label = Label(master = root, image=img)
label = Label(master = root,
              text = 'Hello World',
              background = 'red',
              foreground = 'white',
              font = ('Arial', 16, 'bold italic'),
              width = 15,
              height = 8)
'''''

root = Tk()