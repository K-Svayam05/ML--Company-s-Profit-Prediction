from IPython.display import display
import numpy as np 
import matplotlib.pyplot as plt 
from sklearn.compose import ColumnTransformer
import pandas as pd 
import seaborn as sns

companies=pd.read_csv('1000_Companies.csv')
X=companies.iloc[:, :-1].values
Y=companies.iloc[:, 4].values
# display(companies.head())

# # Select only numeric columns for correlation analysis
# numeric_columns = companies.select_dtypes(include=[np.number])
# correlation_matrix = numeric_columns.corr()
# sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=.5)
# plt.show()

# Encoding Categorical Data
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder=LabelEncoder()