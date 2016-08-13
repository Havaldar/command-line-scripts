#!/usr/bin/env python3

import sys
from os import listdir
from os.path import isfile, getsize, splitext

def get_all_files(dir, extentions):
	if isfile(dir):
		filename, extention = splitext(dir)
		try:
			extentions[extention] += getsize(dir)
		except KeyError:
			extentions[extention] = getsize(dir)
	else:
		for elem in listdir(dir):
			get_all_files(dir + '/' + elem, extentions)


def keywithmaxval(d):
	v = list(d.values())
	k = list(d.keys())
	return k[v.index(max(v))]

files  = []
total_sizes = {}
extentions = {'py': 'python', 'rb': 'ruby', 'java': 'java', 'c': 'c', 'o': 'binary', 's': 'assembly', 'html': 'html', 'css': 'css', 'js': 'javascript', 'txt': 'text', 'docx': 'word files', 'sh': 'shell', 'php': 'php', 'lua': 'lua', 'sca': 'sca'}
get_all_files(dirname, total_sizes)
most_used = keywithmaxvalue(total_sizes)
try:
	print('This file mostly contains: ' + extentions[most_used] + ' file types')
except KeyError:
	print('This file mostly contains: miscellaneous file types')

for elem in listdir(dirname):
	filename, extention = splitext(elem)
	if filename.lower() == 'readme':
		f = open(dirname + elem, 'r')
		print(f.read())
