import pandas as pd
dataset = pd.read_csv( 'salarydata.csv' )
X = dataset[ 'YearsExperience' ].values.reshape(30,1)
Y = dataset[ 'Salary' ]

from sklearn.linear_model import LinearRegression

model = LinearRegression()

model.fit(X,Y)

import joblib
joblib.dump( model, 'salary.pk1' )
