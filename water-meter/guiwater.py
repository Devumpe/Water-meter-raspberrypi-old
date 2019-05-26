from Tkinter import *
from PIL import ImageTk, Image
root = Tk()

canv = Canvas(root, width=1900, height=1000, bg='white')
canv.grid(row=4, column=6)

labeltexttop = Label(root,text="Water Meter Camera", font='Helvetica 22 bold',background='DeepSkyblue2',foreground='white')
labeltexttop.place(relx=0.5, rely=0,relwidth=1, relheight=0.25,anchor='n')
photo = Image.open("correct.jpg")

photo.resize((5, 5), Image.ANTIALIAS)
img = ImageTk.PhotoImage(photo)  # PIL solution
background_label = Label(root, image=img)
background_label.place(relx=0.3, rely=0.25,anchor='n')

lower_frame = Frame(root, bg='#80c1ff', bd=10)
lower_frame.place(relx=0.8, rely=0.35, relwidth=0.3, relheight=0.15, anchor='n')

textlabel = Label(lower_frame,foreground='DeepSkyblue3',text='KeyRoom:19,23,06,45',font='Helvetica 16')
textlabel.pack(side="bottom",fill="both",expand="yes")
lower_frame2 = Frame(root, bg='#80c1ff', bd=10)
lower_frame2.place(relx=0.8, rely=0.55, relwidth=0.3, relheight=0.15, anchor='n')

textlabel = Label(lower_frame2,foreground='DeepSkyblue3',text='Date:12/05/2562,12:30',font='Helvetica 16')
textlabel.pack(side="bottom",fill="both",expand="yes")

button = Button(root,text="SUMMIT", font='Helvetica 22' , background='DeepSkyblue3',foreground='DeepSkyblue3')
button.place(relx=0.3, rely=0.83, relheight=0.15, relwidth=0.4)

mainloop()
