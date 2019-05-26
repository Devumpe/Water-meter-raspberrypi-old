from Tkinter import *
from PIL import ImageTk, Image
root = Tk()

canv = Canvas(root, width=1900, height=1000, bg='white')
canv.grid(row=4, column=6)

labeltexttop = Label(root,text="Water Meter Camera", font='Helvetica 35 bold',background='DeepSkyblue2',foreground='white')
labeltexttop.place(relx=0.5, rely=0,relwidth=1, relheight=0.25,anchor='n')
photo = Image.open("correct.jpg")

photo.resize((5, 5), Image.ANTIALIAS)
img = ImageTk.PhotoImage(photo)  # PIL solution
background_label = Label(root, image=img)
background_label.place(relx=0.5, rely=0.25,relwidth=0.5, relheight=0.5,anchor='n')


textlabel = Label(root,foreground='DeepSkyblue3',text='Upload Done!',font='Helvetica 22 bold')
textlabel.place(relx=0.5, rely=0.75,anchor='n')


button = Button(root,text="NEXT", font='Helvetica 30' , background='DeepSkyblue3',foreground='DeepSkyblue3')
button.place(relx=0.3, rely=0.83, relheight=0.15, relwidth=0.4)

mainloop()
