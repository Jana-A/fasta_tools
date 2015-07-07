#!/usr/bin/env python3
#------------------------------
# Description: Input a file containing fasta sequences.
#   The output is a generator object of the sequences in there original order.
#-----------------------------
import re

class fasta_seq_file:
	def __init__(self, file_name):
		self.header_order = []
		self.dict_container = {}
		with open(file_name, 'r') as file_handle:
			current_seq_header = ''
			for line in file_handle:
				if re.search('^>', line):
					current_seq_header = line
					self.dict_container[line] = ''
					self.header_order.append(line)
				else:
					self.dict_container[current_seq_header] += re.sub('\n', '', line)
	def fasta_generator(self):
		for header in self.header_order:
			yield header + self.dict_container[header]

if __name__ == '__main__':
	import argparse
	parser = argparse.ArgumentParser()
	parser.add_argument('-f', '--seq_file', help='The path to file containing fasta sequences.')
	args = parser.parse_args()
	input_file = args.seq_file
	my_obj = fasta_seq_file(input_file)
	seq_gener = my_obj.fasta_generator()
	condition = True
	while (condition):
		value = next(seq_gener, False)
		if (value):
			print (value)
		else:
			condition = value
