from Tkinter import *
from PIL import Image,ImageTk
from subprocess import Popen

root = Tk()
text = Text(root)
HEIGHT = 1000
WIDTH = 1900
canvas = Canvas(root,height=HEIGHT,width=WIDTH).pack()



def linkdatabase():
    import os
    Popen(["python3" , "upimage.py"])

    global root
    root.destroy()
    


labeltext = Label(canvas,text="Showdata", font='Helvetica 18 bold',background='DeepSkyblue2',foreground='white')
labeltext.place(relx=0.1, rely=0.05,relwidth=1, relheight=0.25,anchor='center')

i=0;
text_file = open('/home/pi/water-meter/data.txt','r')
line = text_file.read().splitlines()    
textdate = line[i]
textrfid = line[i+1]
textimage = line[i+2]
text_file.close()



frame = Frame(canvas,bg='#80c1ff')
frame.place(relx=0.5, rely=0.08, relwidth=0.5, relheight=0.5, anchor='n')
photo = Image.open(textimage)
#photo.resize((5, 20), Image.ANTIALIAS)
img = ImageTk.PhotoImage(photo)  # PIL solution
label = Label(frame,image=img)
label.pack()

dateframe = Frame(canvas, bg='#80c1ff', bd=5)
dateframe.place(relx=0.5, rely=0.7, relwidth=0.8, relheight=0.10, anchor='n')
timelabel = Label(dateframe,text="Date"+textdate)
timelabel.pack(side="bottom",fill="both",expand="yes")

keyframe = Frame(canvas, bg='#80c1ff', bd=5)
keyframe.place(relx=0.5, rely=0.6, relwidth=0.8, relheight=0.10, anchor='n')
uidlabel = Label(keyframe,text="Key Room"+textrfid)
uidlabel.pack(side="bottom",fill="both",expand="yes")



summitbtn = Button( root,text="Summit", font=40, command=linkdatabase)
summitbtn.place(relx=0.3, rely=0.83, relheight=0.13, relwidth=0.15)

root.mainloop()
