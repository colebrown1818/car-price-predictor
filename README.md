# Car Price Predictor

## Introduction
Using API for gathering data from a web search, cleaning the data, creating a model, and using a GUI to take in variables and predict a car price based on final model. Using just Toyota Tacomas to build the data set and predict.

## Dataset
The dataset used was pulled from a website search of car listings and then converted to a pandas dataframe. A copy of the data used was saved to a .csv file in the directory.

## Process

The car price predictor model jupyter file is the file to build and save the model.

The car price predictor python file is the GUI that uses the saved model to take inputs for a car and display a predicted price.

The cars_data.csv is the data used for building the model which was gathered from a car listing website.

xgboost_tuned pickle is the model file used in the car price predictor GUI.

## Results
The statistic metrics for the model build are in the jupyter file and I used a xgboost tuned model. The GUI is running and able to be used to input tacoma information and get back a predicted car price.

