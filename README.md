# Minecraft Username Availability Checker

This is a simple python script inspired by the methods described by Xinabox. His method of opening a bunch of tabs and seeing which api calls failed seemed very wrong to me, so here is a script that does it for you.

Since this script checks each name, it *may* take longer, but it shouldn't be too bad.

## Usage
1. Ensure you have Python 3 installed.
2. Download this repository. (use git clone or just the big green download button)
3. Write all the usernames you want to check into `names.txt`, separating each name with a new line.
4. Drag and drop `names.txt` onto the `availability.py` file.
5. A new file titled `names.txt-availability.txt` should appear.  
   In this file is every name that may be available as well as the status code the Mojang API returned in case you were debugging.
