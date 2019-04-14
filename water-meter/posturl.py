import firebase_admin
from firebase_admin import credentials
from firebase_admin import storage

bucket = storage.bucket()
blob = bucket.blob(BLOB_PATH)
blob.upload_from_filename('water-meter-235712.appspot.com')
print(blob.public_url)