import pandas as pandas
import numpy as numpy
import matplotlib.pyplot as pyplot
from sklearn.linear_model import LinearRegression

data = pandas.read_csv('python_linear_regression_prediction_python_data.csv')
print(data)

x = data[['Experience_Years','Calls_Made','Meetings_Conducted']]
y = data['Sales_Amount']

model = LinearRegression()
model.fit(x,y)

print("Coefficient:",model.coef_)
print("Intercept",model.intercept_)

new_data = pandas.DataFrame({
    'Experience_Years': [8, 12, 15],
    'Calls_Made': [105, 150, 180],
    'Meetings_Conducted': [10, 14, 18]})

Predicted_y = model.predict(new_data)
print(Predicted_y)

pyplot.figure(figsize=(15,8))
pyplot.scatter(data['Experience_Years'],data['Sales_Amount'], color='blue', label='Actual Sales')
pyplot.scatter(new_data['Experience_Years'],Predicted_y,color='red',label='Predicted Sales')
pyplot.legend()
pyplot.xlabel('Experience Years')
pyplot.ylabel('Sales Amount')
pyplot.show()
