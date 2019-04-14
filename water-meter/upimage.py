from google.cloud import storage

# ไฟล์ที่จะอัพ
filename = "image/Dicut11.jpg"

# ที่อยู่ bucket
client = storage.Client()
bucket = client.get_bucket('water-meter-235712.appspot.com')

# อัพไฟล์
blob = bucket.blob('image/Dicut11.jpg')
with open(filename, "rb") as fp:
    blob.upload_from_file(fp)
print(blob.public_url)

