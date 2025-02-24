# Fetch and open/play a file by FTP

import webbrowser, sys
from ftplib import FTP                          # Socket-based FTP tools
from getpass import getpass                     # Hidden password input

# if sys.version[0] == '2': input = raw_input # 2.X compatibility

nonPassive = False                              # Force active mode FTP for server?
fileName = input('File? ')                       # File to be downloaded
dirName = input('Dir? ') or '.'                  # File to be downloaded
siteName = input('Site? ')                       # FTP site to contact
user = input('User? ')                           # Use () for anonymous

if not user:
    userInfo = ()
else:
    from getpass import getpass                 # Hidden password input
    userInfo = (user, getpass('Pswd? tes'))

print('Connecting...')

connection = FTP(siteName)                      # Connect to FTP site
connection.login(*userInfo)                     # Default is anonymous login
connection.cwd(dirName)                         # Xfer 1k at a time to localfile

if nonPassive:                                  # Force active FTP if server requires
    connection.set_pasv(False)

print('Downloading...')

localFile = open(fileName, 'wb')                # Local file to store download

connection.retrbinary('RETR ' + fileName, localFile.write, 1024)
connection.quit()
localFile.close()

print('Playing...')
webbrowser.open(fileName)

# File? ProgramIndex
# Dir? pub/gnu
# Site? ftp.gnu.org
