#Discription: print ID, Feature, Lable of iris datasaet
#Date: 17/07/21
#Author : Om Deshmukh

from sklearn.datasets import load_iris

def main():
	datasets=load_iris()

	print("Features of dataset")
	print(datasets.feature_names)

	print("Target_names of dataset")
	print(datasets.target_names)

	print("Iris data set is:")

	for icnt in range(len(datasets.target)):
		print("ID: %d Feature:%s Label: %s" %(icnt,datasets.data[icnt], datasets.target[icnt]))

if __name__ == '__main__':
	main()
