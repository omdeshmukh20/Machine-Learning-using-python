#Discription: Studing head brain datasett
#Date: 21/07/21
#Author : Om Deshmukh

import pandas as pd 
import numpy as pd

def MeanData(arr):
	size=len(arr)
	sum=0

	for i in range(size):
		sum


def HeadBrain(Name):
	dataset=pd.read_csv(Name)
	print("Size of our dataset is",dataset.shape)

	X=datset["Head Size(cm^3"].values
	Y=dataset["Brain Weight(grams"].values

	print("Length of X",len(X))
	print("Length of Y",len(y))


def main():
	print("Enter file name of dataset")
	name=input()

	HeadBrain(name)

if __name__ == '__main__':
		main()	
