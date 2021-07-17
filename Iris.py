#Discription: Load iris dataset
#Date: 17/07/21
#Author : Om Deshmukh.
from sklearn.datasets import load_iris

def main():
	datasets=load_iris()

	print("Features of dataset")
	print(datasets.feature_names)

	print("Target_names of dataset")
	print(datasets.target_names)


if __name__ == '__main__':
	main()
