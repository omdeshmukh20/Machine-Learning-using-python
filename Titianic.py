#Discription: Titanic Dataset using maximum libriaries.
#Date: 24/07/21
#Author : Om Deshmukh

# Imports
import numpy as np
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure,show
from seaborn import countplot
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix

# ML Operation
def TitanicLogistic():

    print("Logistic Regression with Titanic Dataset")
    
    # STEP 1 - Load Data
    titanic_Data = pd.read_csv("MarvellousTitanicDataset.csv")

    # Data Analysis
    print("First 5 record of Dataset \n")
    print(titanic_Data.head())
    
    print("Total number of records are : ",len(titanic_Data))
    print("Dataset information: \n ",titanic_Data.info())

    # STEP 2 - Analise the Data
    #FIG 1
    print("Visulisation of survived and non survived passangers:")
    figure()

    countplot(data=titanic_Data,x="Survived").set_title("Survived vs Non Survived")
    show()

    #FIG2
    print("Visulisation according to Sex")
    figure()

    countplot(data=titanic_Data,x="Survived",hue="Sex").set_title("Visulisation according to Sex")
    show()

    #FIG3
    print("Visulisation according to PassangerClass")
    figure()

    countplot(data=titanic_Data,x="Survived",hue="Pclass").set_title("Visulisation according to Pclass")
    show()


    print("Survived vs Nonsurvided based on Age")
    figure()

    titanic_Data["Age"].plot.hist().set_title("Survived vs Nonsurvided based on Age")
    show()

    #STEP 3 - Data cleaning
    titanic_Data.drop("zero",axis=1,inplace=True)
    print("data after column removale")
    titanic_Data.head()

    Sex=pd.get_dummies(titanic_Data["Sex"])
    print(Sex.head())
    Sex=pd.get_dummies(titanic_Data["Sex"],drop_first=True)
    print("sex column after updation")
    print(Sex)

    Pclass=pd.get_dummies(titanic_Data["Pclass"])
    print(Pclass.head())
  

    #concat sex and pclass field in our datset
    titanic_Data=pd.concat([titanic_Data,Sex,Pclass],axis=1)
    print("Data after concatination")
    print(titanic_Data.head())


    # Removing unnecessary fields 
    titanic_Data.drop(["Sex","sibsp","Parch","Embarked"],axis=1,inplace=True)
    print(titanic_Data.head())

    # Divide the dataset into X and Y
    x=titanic_Data.drop("Survived",axis=1)
    y=titanic_Data["Survived"]

    # Split the data for training anf testing purpose
    xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=0.5)

     # Get the model object
    obj = LogisticRegression(max_iter=1000)


	#STEP 4 - Train the dataset
    obj.fit(xtrain,ytrain)

    #STEP 5- Testing
    output=obj.predict(xtest)

    # Get the Accuracy of model
    print("\nAccuracy of given dataset is : ")
    print(accuracy_score(ytest, output))


    print("confusion_matrix is")
    print(confusion_matrix(ytest,output))

# Entry Point
def main():

    TitanicLogistic()
    
  
# Starter
if(__name__ == "__main__"):
    main()
