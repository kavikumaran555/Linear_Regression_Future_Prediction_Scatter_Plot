# Linear_Regression_Future_Prediction_Scatter_Plot
# Python Linear Regression Prediction

This project demonstrates how to use **Multiple Linear Regression** in Python to predict sales amount based on three input variables:
- Experience (in years)
- Calls Made
- Meetings Conducted

The dataset contains 50 records representing sales team performance data.

## What this project does
- Trains a Linear Regression model using scikit-learn
- Predicts sales amount for new unseen data
- Displays actual and predicted sales values on a scatter plot

## Libraries used
- pandas
- numpy
- matplotlib
- scikit-learn

## Code explanation
1. The dataset is read using pandas.
2. A Linear Regression model is trained using:
   - `Experience_Years`
   - `Calls_Made`
   - `Meetings_Conducted`
3. The model predicts new sales amounts for unseen data.
4. A scatter plot shows the difference between **actual (blue)** and **predicted (red)** sales points.

## File included
- `python_linear_regression_prediction_python_data.csv` – Dataset used for training and prediction
- `Python Linear Regression Prediction.ipynb` – Jupyter Notebook with code

## Output
A scatter plot comparing actual vs predicted sales data.
The red points represent predicted sales for new input values.

