#Discription: Predicted result and Result got
#Date: 18/07/21
#Author : Om Deshmukh

from sklearn.datasets import load_iris
import numpy as np
from sklearn import tree

def main():
	datasets=load_iris()

	print("Features of dataset")
	print(datasets.feature_names)

	print("Target_names of dataset")
	print(datasets.target_names)

	print("Iris data set is:")

	index=[1,51,101]
	test_target=datasets.target[index]
	test_feature=datasets.data[index]

	train_target=np.delete(datasets.target,index)	
	train_feature=np.delete(datasets.data,index,axis=0)

	obj=tree.DecisionTreeClassifier()
	obj.fit(train_feature,train_target)

	result=obj.predict(test_feature)

	print("Result prediction by ML",result)

	print("Result expected",test_target)


if __name__ == '__main__':
	main()
