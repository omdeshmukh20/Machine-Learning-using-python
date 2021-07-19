#Discription: Load dataset through pandas.
#Date: 19/07/21
#Author : Om Deshmukh

import pandas as pd

def main():
	data=pd.read_csv("iris.csv")
	print(len(data))
	print(data.head())
if __name__ == '__main__':
 	main() 
