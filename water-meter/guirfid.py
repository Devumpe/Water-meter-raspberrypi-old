import time
from threading import Thread
from tkinter import *
import io
import sys
from subprocess import Popen
from datetime import *


RQS_0=0
RQS_QUIT=1
RQS_CAPTURE=2
rqs=RQS_0

root = Tk()

HEIGHT = 1000
WIDTH = 1900
canvas = Canvas(root,height=HEIGHT,width=WIDTH).pack()

labeltexttop = Label(canvas,text="Water Meter Camera", font='Helvetica 22 bold',background='DeepSkyblue2',foreground='white')
labeltexttop.place(relx=0.5, rely=0,relwidth=1, relheight=0.25,anchor='n')



lower_frame = Frame(root, bg='#80c1ff', bd=10)
lower_frame.place(relx=0.5, rely=0.35, relwidth=0.8, relheight=0.15, anchor='n')

textlabel = Label(lower_frame,foreground='gray69',text='KeyRoom:19,02,45,43',font='Helvetica 16')
textlabel.pack(side="bottom",fill="both",expand="yes")


button = Button(root,text="NEXT", font='Helvetica 30 ' ,foreground='gray69')
button.place(relx=0.3, rely=0.6, relheight=0.3, relwidth=0.4)

root.mainloop()


  










  





