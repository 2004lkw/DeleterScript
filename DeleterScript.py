'''
Delete_Dir_By_Number 
This python script is created to delete all files in a given directory execpt the most recent ## of files.
This was originally created to remove multiples of back up files that reside in a directory.
In the class ScriptSettings below, you should change the KeepValue to the number of files you would like to save (default 3)
and change the DirPath to the path you want the script to look in.
Be sure that you have the correct permissions to perform the delete operation.
'''
import os
import sys
import time
import stat
import platform

# The path of the directory you want to search for the files.

class ScriptSettings:
    # Amount of most-recent files you want to keep.
    KeepValue = 3
    # Drive and directory you want to search
    DirPath = "Drive:\\Path\\Here\\"

# object that will hold the files and time stamps

class filesObject:
    fileName = ""
    fileTime = 0

    def __init__(self, nameIn, TimeIn):
        self.fileName = nameIn
        self.fileTime = TimeIn

# create the file object with the info we need.
FileObj = ScriptSettings()
if FileObj.KeepValue < 1:
    sys.exit(0)  # Because you need to keep at least 1!
if FileObj.DirPath.endswith("\\") == False and platform.system() == "Windows":
    # we're on windows
    # add a \ to the end of the path ..  intended for windows users.
    FileObj.DirPath = FileObj.DirPath+"\\"

# Begin here by getting the files in the path in a list.
files = os.listdir(FileObj.DirPath)
filesList = []  # file list to keep unsorted
filesListFinal = []  # file list to keep sorted

# now get the file names and associate them with their time
#   in to an object that can hold them.
for fileNow in files:
    # if this is a file and not a directory...
    if os.path.isfile(FileObj.DirPath+fileNow):
        # get the time for this file.
        timeout1 = os.path.getmtime(FileObj.DirPath+fileNow)
        # get this created with the INIT (With path!)
        tmpFile = filesObject(FileObj.DirPath+fileNow, timeout1)
        # appending this object into a list
        filesList.append(tmpFile)

terminateLoop = 0
sortedThisLoop = 0
tmpfile = filesObject(filesList[0].fileName, filesList[0].fileTime)
filesListFinal.append(tmpfile)  # our starter obj.
xCount = 1
while xCount < FileObj.KeepValue:
    tmpfile = filesObject(filesList[0].fileName, filesList[0].fileTime)
    filesListFinal.append(tmpfile)  # our starter obj (again).
    xCount += 1

# keep NumOfFilesToKeep
while terminateLoop == 0:
    # reset the control var
    sortedThisLoop = 0
    for thisFile in filesList:
        if thisFile.fileTime > filesListFinal[0].fileTime:
            filesListFinal[0].fileTime = thisFile.fileTime
            filesListFinal[0].fileName = thisFile.fileName
            # Set the control var.  If this isn't set, then
            #   we're out of sorts.
            sortedThisLoop = 1
        xCount = 1
        while xCount < FileObj.KeepValue and sortedThisLoop == 0:
            # if this isn't a sorted variable and we have more than 1 entry to sort...
            if thisFile.fileTime > filesListFinal[xCount].fileTime and thisFile.fileTime < filesListFinal[xCount - 1].fileTime:
                # Greater than current time but less than previous index's time
                filesListFinal[xCount].fileTime = thisFile.fileTime
                filesListFinal[xCount].fileName = thisFile.fileName
                sortedThisLoop = 1
                break
            xCount += 1
    if sortedThisLoop == 0:
        terminateLoop = 1

deleteThis = True
xCount = 0
keepCount = 0
for curFile in filesList:
    deleteThis = True
    while xCount < FileObj.KeepValue:
        if curFile.fileName == filesListFinal[xCount].fileName:
            deleteThis = False
            break
        xCount += 1
    if deleteThis == True:
        print("Deleting "+curFile.fileName)
        keepCount += 1
        os.remove(curFile.fileName)
    xCount = 0
print("Deleted "+str(keepCount)+" files.")

xCount = 0
print("Saved the files : ")
while xCount < FileObj.KeepValue:
    print(filesListFinal[xCount].fileName+" -> " +
          str(filesListFinal[xCount].fileTime))
    xCount += 1
