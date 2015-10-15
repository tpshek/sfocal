"""
06.02.2015 tps Fix bad UID values in SF Opera calendar file.
All the events have the same UID of "sfopera1".
How about incrememting them for each event instead?

Original file was encoded as ANSI/UTF-8 without BOM, which is
really an obsolete format & was causing problems.
Converted file to UTF-8 before running it through this script.
"""

import string
import codecs
import sys
import re

file_encoding = "utf-8"
calendar_file = "utf8.ics"
uid_string = "UID:sfopera"
regex_match_str = "^" + uid_string + "1"

# print(sys.getdefaultencoding()) 
# Make sure stdout knows about utf-8 
sys.stdout = codecs.getwriter(file_encoding)(sys.stdout.detach())


re_uid = re.compile(regex_match_str)
n = 1
fin = codecs.open(calendar_file, "r", file_encoding)
if fin:
  for line in fin:
    # If the current line contains an event ID that needs fixing,
    # replace the bad ID with a new unique ID.
    if re_uid.match(line):
      print(uid_string + str(n).zfill(3))
      n = n + 1 
    else:
      print(line.strip())
  fin.close()

##fin = open('icalendarevents.ashx', 'rU')
#fin = open('test.txt', 'r')
#if fin:
#  for line in fin:
#    if re_uid.match(line):
#      print("UID:sfopera" + str(n).zfill(3))
#      n = n + 1 
#    else:
#      print(line.strip())
#  fin.close()
#
