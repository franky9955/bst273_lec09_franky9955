#!/usr/bin/env python

import argparse

parser = argparse.ArgumentParser( description="" )

parser.add_argument(
	"data_file",
	help="path to the file we want to read",
)

#-------------------------------------------------------------------------------
# Are there other arguments we need?
#-------------------------------------------------------------------------------

args = parser.parse_args( )

#print(args)
#print(args.data_file)

fh = open(args.data_file)   #this is how we hold on to file
print("the file handle is" + str(fh))

lines = 0
words = 0
chars = 0

#read file line by line
for line in fh:
	lines += 1

	print(lines)	





#-------------------------------------------------------------------------------
# our code for analyzing the data
#-------------------------------------------------------------------------------
