# Mushroom Classification Using Machine Learning


## Objective
The objective of this project is to build and evaluate machine learning models that can accurately classify mushrooms as **edible or poisonous** based on their physical characteristics. 


The dataset contains information about mushroom characteristics such as cap-diametercap-,shape,gill-attachment,gill-color,stem-height,stem-width,stem-color,	season,class.  

The data is first processed by removing missing values, and doing exploratory analysis.The data is then splited for train and test. Then it is scaled using standardscaler.

Several supervised learning models, including Logistic Regression, Decision Tree,K Nearest Neighbour and Random Forest, were implemented and evaluated. Logistic Regression was used as a baseline model, while Decision Tree and Random Forest were chosen for their ability to capture non-linear relationships and handle categorical data effectively.

Model performance was assessed using evaluation metrics such as accuracy,confusion matrix. Among the models tested, the Random Forest classifier achieved the best performance, delivering near-perfect classification accuracy and demonstrating strong robustness and generalization capability.

The results of this project highlight the effectiveness of ensemble learning methods in safety-critical classification tasks and demonstrate how machine learning can be successfully applied to real-world decision-making problems.
