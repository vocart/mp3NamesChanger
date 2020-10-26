import os
import re
import fnmatch
import sys
import mutagen

# enables to drop folder on app
droppedFile = sys.argv[0]

path = sys.argv[1]

# list of files in the folder:
playlist = list(os.listdir(path))

for oldFilename in playlist:

    # removing .jpg files (album covers)
    jpg = '*.Jpg'
    if fnmatch.fnmatch(oldFilename, jpg):
        os.remove('{}/{}'.format(path, oldFilename))
        playlist = list(os.listdir(path))

    else:
        pass

# changing the structure of titles to suit the pattern:
# 'Artist Name - Title of the File.mp3'
for oldFilename in playlist:

    newFilename = oldFilename.title().replace('_', ' ')

    # removing first characters if they are not letters
    for let in newFilename:
        if let.isalpha():
            break
        else:
            newFilename = newFilename[1:]
    
    # the formula checks if the file has an artist in file's properties and adds it
    # to the name
    mf = mutagen.File('{}/{}'.format(path, oldFilename))

    for key in ("albumartist", "artist", "TPE1", "TPE2", "aART", "\xa9ART"):
        try:
            value = mf.get(key, None)
            
        except ValueError:
            value = None

        if value is not None:
            bandName = value[-1]
            print(bandName)
            newFilename2 = bandName + ' - ' + newFilename
            # checks if the filename has the band name already
            comparison = re.search(bandName.upper(), newFilename.upper())
            if not comparison:
                newFilename2 = bandName + ' - ' + newFilename
            else:
                newFilename2 = newFilename 
            break
        else:
            newFilename2 = newFilename

    # changing first letters of words that we want to start with a small letter
    newFilename2 = newFilename2.replace('.Mp3', '.mp3').replace(' The ', ' the ')\
        .replace(' Of ', ' of ').replace(' A ', ' a ').replace(' To ', ' to ').replace(' And ', ' and ')\
        .replace(' At ', ' at ').replace(' In ', ' in ').replace(' On ', ' on ').replace('\'S', '\'s')\
        .replace(' Into ', ' into ').replace(' As ', ' as ').replace(' By ', ' by ')\
        .replace(' With ', ' with ').replace(' Up ', ' up ').replace('\'Ll', '\'ll').replace(' For ', ' for ')
     
    # changing the file's name for the new one
    os.rename('{}/{}'.format(path, oldFilename), '{}/{}'.format(path, newFilename2))  
