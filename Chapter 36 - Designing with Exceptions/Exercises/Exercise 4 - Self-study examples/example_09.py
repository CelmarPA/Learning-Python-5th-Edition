# Email inbox scanning and maintenance utility

"""
Scan pop email box, fetching just headers, allowing
deletions without downloading the complete message
"""

import poplib, getpass

mailServer = 'your pop email server name here'                      # pop.server.net
mailUser = 'your pop email user name here'
mailPasswd = getpass.getpass('Password fro %s?' % mailServer)

print('Connecting...')

server = poplib.POP3_SSL(mailServer)
server.user(mailUser)
server.pass_(mailPasswd)

try:
    print(server.getwelcome())
    msgCount, mboxSize = server.stat()
    print('There are', msgCount,  'mail messages, size ', mboxSize)
    msgInfo = server.list()
    print(msgInfo)
    for i in range(msgCount):
        msgNum = i + 1
        msgSize = msgInfo[1][i].split()[1]
        resp, hdrLines, octets = server.top(msgNum, 0)              # Get hdrs only
        print('-' * 80)
        print('[%d: octets=%d, size=%s]' % (msgNum, octets, msgSize))

        for line in hdrLines: print(line)

        if input('Print?') in ['y', 'Y']:
            for line in server.retr(msgNum)[1]: print(line)                 # Get whole msg
        if input('Delete?' in ['y', 'Y']):
            print('Deleting...')
            server.dele(msgNum)                                             # Delete on srvr
        else:
            print('Skipping...')
finally:
    server.quit()                                                           # Make sure we unlock mbox

input('Bye.')                                                               # Keep windows up on Windows
