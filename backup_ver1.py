#!/usr/bin/python
# Filename: backup_ver1.py

import os
import time

# 1. The files and directories to be backed up are specified in a list.
source = ['/Users/maoshuhao/Desktop/function1.py', '/Users/maoshuhao/Desktop/search.js']
# If you are using Windows, use source = [r'C:\Documents', r'D:\Work'] or something like that

# 2. The backup must be stored in a main backup directory
target_dir = '/Users/maoshuhao/Desktop/' # Remember to change this to what you will be using

today = target_dir + time.strftime('%Y%m%d')

now = time.strftime('%H%M%S')

comment = raw_input('Enter a comment --> ')

if len(comment)==0:
	target = today + os.sep + now + '.zip'
else:
	target = today + os.sep + now + '_' + comment.replace(' ','_') + '.zip'
if not os.path.exists(today):
	os.mkdir(today)
	print 'Successfully created directory', today

# target = today + os.sep + now + '.zip'

print os.sep
print target
# 3. The files are backed up into a zip file.
# 4. The name of the zip archive is the current date and time
# target = target_dir + time.strftime('%Y%m%d%H%M%S') + '.zip'

# 5. We use the zip command (in Unix/Linux) to put the files in a zip archive
# zip_command = "zip -qr '%s' %s" % (target, ' '.join(source))

tar = 'tar -cvzf %s %s' % (target, ' '.join(source))

# Run the backup
if os.system(tar) == 0:
    print 'Successful backup to', target
else:
    print 'Backup FAILED'