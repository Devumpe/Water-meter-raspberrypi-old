from google.cloud import storage
import pyrebase

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
filename = "image/Dicut11.jpg"

# ที่อยู่ bucket
client = storage.Client()
bucket = client.get_bucket('water-meter-235712.appspot.com')

# อัพไฟล์ storage
blob = bucket.blob('image/Dicut11.jpg')
with open(filename, "rb") as fp:
    blob.upload_from_file(fp)
print(blob.public_url)

#อัพไฟล์ database
firebase = pyrebase.initialize_app(config)

db = firebase.database()

db.child("room").push({"image": {"rfid":"12","url": blob.public_url,"date": "11/11"}})