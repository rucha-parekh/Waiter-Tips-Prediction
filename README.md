# Waiter-Tips-Prediction

**Project Overview**
This is a Machine Learning project that leverages the Support Vector Regressor (SVR) model to predict the tip a waiter might receive. The prediction is based on various influential factors such as the day of the week, time of the day, the gender of the customer, the total bill amount, the number of people in the group, and whether the customers are smokers or not. By analyzing these parameters, the model aims to provide accurate insights into tipping patterns, helping to understand the relationship between customer behavior and tipping tendencies.

**Dataset Description**
The dataset 'tips.csv' includes 12 kb of data and has 7 columns which can be used to train the model:
1. total_bill
2. tip
3. sex
4. smoker
5. day
6. time
7. size

**Dataset Preprocessing and EDA**
The following EDA steps are taken:
1. Description of data
2. Checking for null values
3. Graphs to compare correlation of data

 The following preprocessing steps are taken:
 1. Label Encoding
 2. Removing null values
 3. Detecting and removing outliers
 4. Removing leading and trailing spaces

**Model Selection**
The data is split into training data and testing data. Different models are compared according to their men sqaured error and the SVR model is found to have the least MSE.

**Deployment**
The m!odel is deployed using flask

![Screenshot 2024-11-19 162312](https://github.com/user-attachments/assets/c037e90c-9df6-4152-986b-b3efc885e02d)


