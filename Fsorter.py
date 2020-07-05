#import nedeed librarys
import os, glob
import shutil

#going to create file folders

#going to check folders

#checking that pictures folder  exists
if os.path.isdir("pictures") == True:
    #pictures folder exists
    print("pictures folder exists , going to check videos folder")
else:
    #pictures folder doest exists going to create it
    
    os.mkdir("pictures")
    print("pictures folder created :) , going to check videos folder")

#end of checking pictures folder

#chacking that videos folder exists
if(os.path.isdir("videos") == True):
    #video folder exists
    print("video folder exists , going to check music folders")
else:
    #video folder doesnt exists going to create it
    os.mkdir("videos")
    print("videos folder created going to check music folders :)")
#end of checking video folders

#checking that music folder exists 
if(os.path.isdir("exe") == True):
    #musics folder exists
    print("musics folder exists going to check (exe) folders")
else:
    #music folder doesnt exists going to create it
    os.mkdir("exe")
    print("exe folder created :)")

#checking that documents folders exists
if(os.path.isdir("documents") == True):
    #documents folder exists
    print("documents folder exists :)")
else:
    #documents folder exists
    os.mkdir("documents")
    print("documents folder created")
#end of checking documents folder

#end of checking folder

while 1:
      #start of moving pictures files
    os.chdir(".")
    for file in glob.glob("*.jpg"):
        shutil.move(file , "pictures")

    os.chdir(".")
    for file in glob.glob("*.png"):
        shutil.move(file , "pictures")

    os.chdir(".")
    for file in glob.glob("*.jpeg"):
        shutil.move(file , "pictures")

    #end of moving pictures file

    #start of moving video files
    os.chdir(".")
    for file in glob.glob("*.mp4"):
        shutil.move(file , "videos")

    os.chdir(".")
    for file in glob.glob("*.avi"):
        shutil.move(file , "videos")


    os.chdir(".")
    for file in glob.glob("*.mov"):
        shutil.move(file , "videos")

    os.chdir(".")
    for file in glob.glob("*.wmv"):
        shutil.move(file , "videos")

    os.chdir(".")
    for file in glob.glob("*.wmv"):
        shutil.move(file , "videos")

    os.chdir(".")
    for file in glob.glob("*.flv"):
        shutil.move(file , "videos")

    #end of moving video files

    #start of moving audio files
    os.chdir(".")
    for file in glob.glob("*.mp3"):
        shutil.move(file , "musics")

    os.chdir(".")
    for file in glob.glob("*.wav"):
        shutil.move(file , "musics")

    os.chdir(".")
    for file in glob.glob("*.wav"):
        shutil.move(file , "musics")

    #end of moving audio files

    #start of moving apps
    os.chdir(".")
    for file in glob.glob("*.exe"):
        if file !="Fsorter by Mazdak.exe":
            shutil.move(file , "exe")

    os.chdir(".")
    for file in glob.glob("*.lnk"):
        shutil.move(file , "exe")


    #end of moving apps

    #start of moving documents

    os.chdir(".")
    for file in glob.glob("*.txt"):
        shutil.move(file , "documents")

    os.chdir(".")
    for file in glob.glob("*.pptx"):
        shutil.move(file , "documents")

    os.chdir(".")
    for file in glob.glob("*.docx"):
        shutil.move(file , "documents")

#end of moving documents