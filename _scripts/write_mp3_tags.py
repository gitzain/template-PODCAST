# -*- coding: utf-8 -*-
import os
import sys
import eyed3

TEXT_ENCODING = 'utf8'

# get workdir from first arg or use current dir 
if (len(sys.argv) > 1):
    fpath = sys.argv[1]
else:
    fpath = os.path.abspath(os.path.dirname(sys.argv[0]))

for fn in os.listdir(fpath):

    fname = os.path.join(fpath, fn)
    if fname.lower().endswith('.mp3'):
        print(fn),
        episode = eyed3.load(fname)

        # Do stuff here
        print(episode.tag.album)

print('Done')