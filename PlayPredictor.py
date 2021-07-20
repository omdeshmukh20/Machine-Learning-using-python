
#Discription:Play Predictor dataset
#Date: 20/07/21
#Author : Om Deshmukh

import pandas as pd 
import numpy as np 
from sklearn.neighbors import KNeighborsClassifier
from sklearn import preprocessing

def MarvellousPredictor(path):
	data=pd.read_csv(path)
	print("Dataset loaded successfully with the size",len(data))

	Fetures=["Wether","Temperature"]
	print("Fetures names are",Fetures)

	Wether=data.Wether
	Temperature=data.Temperature
	play=data.play

	lobj=preprocssing.LabelEncoder()

	WetherX=lobj.fit_transform(Wether)
	TemperatureX=lobj.fit_transform(Temperature)
	Label=lobj.fit_transfor(Play)

	print("Encoded Wether is")
	print(WetherX)

	print("Encode Temperature is")
	print(TemperatureX)

	Fetures=list(zip(WetherX,TemperatureX))

	obj=KNeighborsClassifier(n_neighbors=3)
	obj.fit(Fetures,Label)

	output=obj.predict([[0,2]])

	if output==1:
		print("You can play")
	else:
		print("U cannot play")
			

def main():
	print("____Marvellous Play Predict______")
	print("Enter the path of file which contains dataset")
	path=input()

	MarvellousPredictor(path)

if __name__ == '__main__':
	main()
