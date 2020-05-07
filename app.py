import os
from glob import glob

#Get folders inside personal projects directory
folders = glob("/home/youruser/projects/*/")
for directory in folders:
    
    #Search inside each folder .db files
    files = [f for f in glob(directory + "**/*.db", recursive=True)]
    for f in files:
        #Zip each file founded 
        os.system('zip --encrypt backup.zip '+f)

#cp file to drive
os.system('cp backup.zip /run/user/9999/gvfs/google-drive:host=gmail.com,user=yourusername')