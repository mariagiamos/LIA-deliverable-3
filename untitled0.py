print("deliverable 3")

import pandas as pd
data = pd.read_csv("Sleep_health_and_lifestyle_dataset.csv")

#2
#a)initial data inspection
#this step is to give a preview of our chosen dataset.
print(data.head())
#the head function gives a short preview of the dataset. it prints out the first 5 rows of the data set of all 13 columns.
print(data.info())
#the info function prints out the non null count(values that are not empty) in each column. From this short summary we see that Sleep disorders only have 155 values compared to all the  other columns who dont have missing values.
print(data.describe())
#the describe function summarizes the statistics of the dataset. It print out the count(values) for the columns, the mean of each column, the standard deviation, the minimum and max values in each column, and lastlt the 25% and 75% quartile range and the median.
print(data.shape)
#the shape attribute prints out the number of rows (374) and columns(13). 
print(data.columns)
#the column attribute prints out the list of all column titles in the dataset.
print(data.nunique())
#the nunique function prints out the unique numbers in each column.
print(data.value_counts())
#the value_count function prints out how many times each unique values appears in each column. 

#b)handle duplicate entries
print(data.duplicated())
print(data.drop_duplicates())
#As the duplicated() function is used, all our counts of the rows in the dataset are stated as false demonstrating that there are no duplicated rows.
#When the drop_duplicates() function is also used, the number of rows and columns stay the same as the original dataset.











