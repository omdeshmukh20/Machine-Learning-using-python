#Discription: Set recurssion limit
#Date: 23/07/21
#Author : Om Deshmukh

import sys

def main():
	print("Recurss=ion limt is:",sys.getrecursionlimit())

	sys.setrecursonlimit(1500)
	print("New recursion limit is:",sys.grtrecurionlimit())

if __name__ == '__main__':
		main()	
