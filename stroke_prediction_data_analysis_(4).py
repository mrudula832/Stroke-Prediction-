# -*- coding: utf-8 -*-
"""stroke-prediction-data-analysis (4).ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1gYj9GVBG6S8u1LPv-DjBl0v3nbqu-5qZ
"""

# Commented out IPython magic to ensure Python compatibility.
import pandas as pd
import numpy as np
# %matplotlib inline
import seaborn as sns
!pip install missingno
import missingno as mn

"""# ****File Introduction****"""

df =  pd.read_csv('/content/healthcare-dataset-stroke-data.csv')

df

df['stroke'].value_counts()

# lets check all stats
df.describe()

"""We can see that there are missing values and errors in the data which we have to first recitfy and further confirm as we can see above that the count of bmi does not match the  count of the remaining attributes"""

# lets check for null values
df.isnull().sum()

"""# No lets fill in the missing values"""

# we need to first examine connections of missing values
mn.matrix(df)

mn.heatmap(df)

mn.dendrogram(df)

# so we can fill bmi's missing values with smoking_status vlues as we can see the connection from the dendrogram
df[df['bmi'].isnull()]['smoking_status'].value_counts()

from matplotlib import pyplot as plt
plt.hist(df['bmi'])

# Since the data Above it too diversified its not safe to fill using just one cateogry with the remaining missing values
# instead we shall use interpolation to fetch the nearest form of data to fill the missing values
df['bmi'] = df['bmi'].interpolate(method ='linear', limit_direction='forward')

# lets check if that worked
df.isnull().sum()

"""Thus we have no filled all missing values and now we conduct exploratory data analysis

# Exploratory Data Analysis
"""

# lets check all correlations here
df.corr()

# lets groupby bmi
# to get more insights on interelated health variables together through visualization
health_status = df.groupby(by = 'bmi')

# LETS NOW CHECK ITS RELATIONS WITH other variables
health_status.plot.bar();

measure = df[['avg_glucose_level','stroke']].head(20)

measure.sort_values(by='avg_glucose_level')

# lets check the relationship throughout all given datapoints in both attributes
df.plot.scatter('avg_glucose_level','stroke')

"""As our data is not accruate about measurements of stroke rates, thus the max insights we can derive here is that patients with higher glucose levels have a higher chance of strock, which is agreed upon by medicinal principles and can be checked here
https://www.google.com/search?q=high+glucose+level+risks&oq=high+glucose+level+ri&aqs=chrome.0.0j69i57j0i22i30j0i390l2.7168j0j7&sourceid=chrome&ie=UTF-8

# lets now make a prediction using linear regression in uspervised machine learning algorithms
"""

df

# lets drop unnessecary categorical columns
df.drop(['gender'], axis=1, inplace=True)

df.drop(['smoking_status'], axis=1, inplace=True)

df.drop(['ever_married'], axis=1, inplace=True)

df.drop(['work_type'], axis=1, inplace=True)

df.drop(['Residence_type'], axis=1, inplace=True)

"""Lets se x and y variables to make predictions for strock"""

x = df.drop(['stroke'], axis=1)

y = df['stroke']

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split as ttl

# lets split the training and testing data

tx, tex, ty, tey = ttl(x, y, test_size=0.3, random_state=0)

Model_str = LinearRegression()

# now lets fit the training data
Model_str = Model_str.fit(tx,ty)

Model_str.intercept_

Model_str.coef_

# Now to predict with the test data
Model_str.predict(tex)

prediction = Model_str.predict(tex)

"""# Our Prediction has been made and shows some level of accuracy based on the data we fed it, its not accurate because we havent taken into place Patient with already present health conditions based on their blood test analysis

# Thus we should now Validate our datas accuracy and check where our errors have been made.
"""

from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error

r2_score(prediction, tey)

mean_absolute_error(prediction, tey)

mean_squared_error(prediction, tey)

"""# SO based on these results it is undoubtly correct that our models predictions are highly inaccurate as stated for the reason above because the accuracy of the data fed into it is not enough to amalgamate a prediction for strock without knowing the remaining blood history of the patient.
# However our model serves as good based model and benchmark on how to predict a strock using the right data for any future model
"""