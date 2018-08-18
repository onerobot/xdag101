#!/usr/bin/python
# -*- coding: UTF-8 -*- 

import sys

inFileName = sys.argv[1]
outFileName = inFileName + "_res.log"

fin = open(inFileName, "r")
fout = open(outFileName, "w")
state = 0
rowdata = {}
datalist = []
for line in fin:
	if state == 0:
		pos = line.find("<tr>")
		if pos != -1:
			rowdata.clear()
			state = 1
	elif state == 1:
		pos = line.find("<th>")
		if pos != -1:
			pos2 = line.find("</th>")
			if pos2 != -1:
				rowdata['n'] = line[pos+4:pos2]
				state = 2
	elif state == 2:
		pos = line.find('_blank">')
		if pos != -1:
			pos2 = line.find("</a>")
			if pos2 != -1:
				rowdata['address'] = line[pos+8:pos2]
		pos3 = line.find('href="')
		if pos3 != -1:
			pos4 = line.find('" target')
			if pos4 != -1:
				rowdata['url'] = line[pos3+6:pos4]
				state = 3
	elif state == 3:
		pos = line.find("<th>")
		if pos != -1:
			pos2 = line.find("</th>")
			if pos2 != -1:
				rowdata['balance'] = line[pos+4:pos2]
				retline = '| ' + rowdata['n'] + ' | [' +  rowdata['address'] + '](' + rowdata['url'] + ') | ' + rowdata['balance'] + ' |  |\n'
				print retline
				fout.write(retline)
				datalist.append(rowdata)
				state = 0
fin.close()
fout.close()


#<tr>
#<th>4</th>
#<th><a href="https://explorer.xdag.io/block/U54RHG+snKt+rzpWVv/iN3ZOaXx3MZCJ" target="_blank">U54RHG+snKt+rzpWVv/iN3ZOaXx3MZCJ</a></th>
#<th>10052743.033111125</th>
#<th>0505-0722</th>
#</tr>
