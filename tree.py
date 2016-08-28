#!/usr/bin/env python

from os.path import isfile, basename, getsize
from os import listdir, stat
from stat import *
import sys
import time

END = '\033[0m'
BLUE = '\033[94m'
GREEN = '\033[92m'
BOLD = '\033[1m'
FAIL = '\033[91m'

def get_tree(dir, tabs):
	output = ''
	for i in xrange(tabs):
		output += '|   '
	output += '|--> '
	if isfile(dir):
		info = stat(dir)
		return output + oct(info.st_mode)[-3:] + " " + BLUE + BOLD + basename(dir) + END + '\t|updated_at: ' + time.strftime('%Y-%m-%d %H:%M:%S' ,time.localtime(info.st_mtime)) + '\t|created_at: ' + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(info.st_ctime)) + '\t' + str(getsize(dir) >> 10) + 'KB\n'
	else:
		output += GREEN + BOLD + basename(dir) + END + END + '\n'
		for elem in listdir(dir):
			if elem[0] != '.' and elem != 'env' and elem != 'node_modules':
				output += get_tree(dir + '/' + elem, tabs + 1)
		return output

flag = len(sys.argv) > 2
try:
	dirname = sys.argv[1]
	print(get_tree(dirname, 0))
except:
	print(FAIL + 'could not read some files' + END)	
