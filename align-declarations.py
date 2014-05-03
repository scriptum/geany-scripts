#!/usr/bin/env python
#-*- coding:utf-8 -*-

import sys, fileinput, re

lines = []
maxlen = 0

exp = re.compile("(^\s*)((?:static |const )*\w+)\s*(.*)$")

for line in fileinput.input():
	m = re.search(exp, line)
	other = m.group(3)
	word = m.group(2)
	curlen = len(word) + len(other) - len(other.lstrip("*"))
	if curlen > maxlen:
		maxlen = curlen
	lines.append([m.group(1), m.group(2), m.group(3)])

maxlen += 1

for line in lines:
	print ("%s%-"+str(maxlen - len(line[2]) + len(line[2].lstrip("*")))+"s%s") % (line[0], line[1], line[2])
