# Minecraft Username Availability Checker
# https://github.com/jadc/mc-ign-availability
# by Jad Chehimi

import requests
import sys

# Prepare headers with unique user-agent
headers = {'User-Agent': 'availabilitychecker'}

# Decides file name to check for names in
if(len(sys.argv) > 1):
    targetfilename = sys.argv[1]
else:
    targetfilename = 'names.txt'

# Reads file from drag and drop or first argument, otherwise names.txt
try:
    targetfile = open(targetfilename, 'r')
except FileNotFoundError:
    print('Error. Names list (' + targetfilename + ') not found; either create it or use another file in the argument/drag and drop.')
    exit()

# For every mod id
for name in targetfile:
    # Remove whitespace
    name = name.strip()

    # Skip blank lines
    if not name:
        continue

    # API GET Request
    api = requests.get('https://api.mojang.com/users/profiles/minecraft/' + name, headers=headers)

    # Prepare output file
    availablesfilename = targetfilename + '-available.txt'
    f = open(availablesfilename, 'a')

    # Display available names
    if api.status_code != 200:
        print('\'' + name + '\' might be available! (status code ' + str(api.status_code) + ')')
        f.write('[' + str(api.status_code) + '] ' + name + '\n')

f.close()
print('Available names from \'' + targetfilename + '\' have been written to \'' + availablesfilename + '\'')
