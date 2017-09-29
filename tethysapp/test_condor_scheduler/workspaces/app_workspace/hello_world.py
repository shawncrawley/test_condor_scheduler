#!/usr/bin/env python
import time

print "Hello World!"
time.sleep(5)
print "And Nathan!"
time.sleep(5)

with open('output.py', 'w+') as f:
    f.write('#!/usr/bin/env python')
    f.write('print "Hello Shawn!\n"')
