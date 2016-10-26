# EvonyScoutingApp

This is a scouting app for Evony Age 2 based on pyEvony.

**scout.py**

It can be used to scout any city on any server. Although the stone price in that server needs to be below 1 for it to work. Usage:-

    python scout.py server mailguy declarewarcoord scoutcoord
    
here mailguy is name of a random guy who won't mind getting junk mail and declarewarcoord is co-ordinate of a random city who won't mind getting declares on.

Thanks to Tim for all the help with this one.

**scoutapp.py**

Its a graphical interface for scout.py. But it won't work unless the compiled version of scout.py is in the same folder as this one.

Both the compiled version of scout.py and scoutapp.py are in release folder. 

# Download the zip file in release folder,extract it and run scoutapp.exe to use it.

# CHANGELOG

-Added support for scouting multiple co-ordinates

-Added support for getting permanent url from evonyurl.com

-Added support for using Tim's scout viewer

**If anyone was using any of the previous versions, clean your temp folder. Its usually located in C:\Users\username\Appdata\Local\Temp**

**scout.exe was creating a temp folder named \_MEI... everytime it ran.**

**In the current version, this has been fixed.**
