#!/usr/bin/env python
#-*- coding:utf-8 -*-

import sys, fileinput, re

lines = []
maxlen = 0

exp = re.compile("(^\s*)((?:static |const )*\w+)\s*(.*)$")

for line in fileinput.input():
	m = re.search(exp, line)
	if m:
		other = m.group(3)
		word = m.group(2)
		curlen = len(word) + len(other) - len(other.lstrip("*("))
		if curlen > maxlen:
			maxlen = curlen
		lines.append([m.group(1), m.group(2), m.group(3)])
	else:
		lines.append(line)

maxlen += 1

for line in lines:
	if type(line) != "str" and len(line) == 3:
		print ("%s%-"+str(maxlen - len(line[2]) + len(line[2].lstrip("*(")))+"s%s") % (line[0], line[1], line[2])
	else:
		print line.rstrip("\n\r")
