mp3NameChanger changes names of the music files to a standarized form of:

'Name of the Band - Title of a Song.mp3'     [or another type of music file like '.flac']

It:
- removes from the name: '_', track numbers, spaces and dots from the beginning
- changes letters of the words to start with a capital letters (except pronouns, prepositions etc.)
- takes the band's name from the mp3's properties and adds it to the file's name (if it is not in the name already)
- removes .jpg files (cover images) from the folder

You drag the folder with mp3 files on th .exe file and the program changes names in the folder.


Example:

'05.34 - die by_the BLADE.mp3' ---> 'Beast in Black - Die by the Blade.mp3'
['Beast in Black' taken from the properties]

'.victoria.mp3' ---> 'Krypteria - Victoria.mp3'
