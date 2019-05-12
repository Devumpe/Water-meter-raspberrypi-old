#-*- coding: utf-8 -*-
from google.cloud import storage
import pyrebase
import time
from tkinter import *
from PIL import ImageTk, Image
from subprocess import Popen
import os
import urllib2
#config database
config = {
    "apiKey": "AIzaSyB_jnpsPaxKs3xEhs-AbknZJXjcK-M4IeU",
    "authDomain": "water-meter-235712.firebaseapp.com",
    "databaseURL": "https://water-meter-235712.firebaseio.com",
    "projectId": "water-meter-235712",
    "storageBucket": "water-meter-235712.appspot.com",
    "messagingSenderId": "67042893322"   
}


# ไฟล์ที่จะอัพ
i=0;
text_file = open('/home/pi/water-meter/data.txt','r')
line = text_file.read().splitlines()    
textdate = line[i]
textrfid = line[i+1]
textimage = line[i+2]
text_file.close()

filename = textimage

#login
credential_path = "/home/pi/water-meter/water-meter-235712-firebase-adminsdk-ebgws-8362ef71ab.json"
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path
try:
# ที่อยู่ bucket
    urllib2.urlopen('oauth2.googleapis.com')

    client = storage.Client()
    bucket = client.get_bucket('water-meter-235712.appspot.com')

# อัพไฟล์ storage
    try:
        blob = bucket.blob('image/'+textimage)
        with open(filename, "rb") as fp:
            blob.upload_from_file(fp)
    
        firebase = pyrebase.initialize_app(config)

        db = firebase.database()
        timeStamp = time.strftime("%Y-%m-%d:%H-%M-%S")

        db.child("room").push({"image": {"rfid":textrfid,"url": blob.public_url,"date": textdate}})
        print(blob.public_url)

    
    except Exception as e:
        print("e")
        
except urllib2.URLError as err:
        print("dd")


def quit():
    global root
    root.destroy()

root = Tk()

canv = Canvas(root, width=1900, height=1000, bg='white')
canv.grid(row=2, column=3)
photo = Image.open("correct.jpg")

photo.resize((5, 20), Image.ANTIALIAS)
img = ImageTk.PhotoImage(photo)  # PIL solution
canv.create_image(130, 20, anchor=NW, image=img)

keyframe = Frame(canv, bg='#80c1ff', background="blue")
keyframe.place(relx=0.5, rely=0.6, relwidth=0.8, relheight=0.10, anchor='n')
label = Label(keyframe,text="keyroom:")

button = Button( root,text="Summit", font=40, command=quit)
button.place(relx=0.4, rely=0.70, relheight=0.1, relwidth=0.15)


root.mainloop()


