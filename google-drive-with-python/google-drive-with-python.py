"""
Created on Sun Apr  7 15:05:26 2019
@author: June
"""

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gauth = GoogleAuth()
gauth.LocalWebserverAuth() # client_secrets.json need to be in the same directory as the script
drive = GoogleDrive(gauth)

# View all folders and file in your Google Drive
fileList = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()
for file in fileList:
  print('Title: %s, ID: %s' % (file['title'], file['id']))
  # Get the folder ID that you want
  if(file['title'] == "To Share"):
      fileID = file['id']


# Initialize GoogleDriveFile instance with file id.
file1 = drive.CreateFile({"mimeType": "text/csv", "parents": [{"kind": "drive#fileLink", "id": fileID}]})
file1.SetContentFile("small_file.csv")
file1.Upload() # Upload the file.
print('Created file %s with mimeType %s' % (file1['title'], file1['mimeType']))


"""
file_list = drive.ListFile({'q': "'<folder ID>' in parents and trashed=false"}).GetList()
"""
fileList = drive.ListFile({'q': "'2mavWSQhVfr7GnX2JHa45Qd43bTaYCHXE' in parents and trashed=false"}).GetList()
for file in fileList:
  print('Title: %s, ID: %s' % (file['title'], file['id']))
   # Get the folder ID that you want
  if(file['title'] == "picture"):
      fileID = file['id']


# Initialize GoogleDriveFile instance with file id.
file2 = drive.CreateFile({'id': fileID})
file2.Trash()  # Move file to trash.
file2.UnTrash()  # Move file out of trash.
file2.Delete()  # Permanently delete the file.
