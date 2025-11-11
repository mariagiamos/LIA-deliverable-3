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

#c)identify and manage missing values
print(data.isnull())
#there are only missing values in the Sleep Disorder column wherever true is stated.
print(data.fillna("None"))
#This fillna function in pandas was used to replace the missing values (NaN) in the dataset with a chose string "None". 
#c) We decided to fill categorial missing values with the string "None" since we are assuming that the individulas left it blank because they do not suffer from sleeping disorders. Many individuals dont suffer from sleep disorders as they can be healthy, in shape and have good lifestyle habits. 
#If we dropped rown we would loose a lot of valuable data which can affect the response of our 3 questions that need to be answered at the end of the deliverable. 
#Replacing it with none is a realistic and neutral option. 
      
#d)Correct data types and formats
#It is not necessary to corect data types and formats since they are already in the correct format. In each column, the type of data matches the columns format as they are either stated as intergers, floating numbers or Strings.
#this statement can be proven by the function info()
#Person ID, Age, Quality of Sleep,Physical Activity level, Stess level, Heart Rate and daily steps are all intergers
#Sleep Duration are floating numbers
#Occupation, Gender, BMI, Blood pressure and Sleep Disorders are all strings. 

#6.1 Visualizing statistical relationships
import seaborn as sns
sns.relplot(data, x="Sleep Duration", y="Stress Level", col="Gender", kind="scatter")
#2 scatter plots of Stress Level vs. Sleep Duration was generated between Male and Female showing increased stress levels result to low sleep duration.
sns.relplot(data, x="Quality of Sleep", y="Physical Activity Level", hue="Gender", size="Age", col="Sleep Disorder")
#2 scatter plots of Physical Activity Level vs. Quality of Sleep were generated between 2 sleep disorders: Sleep Apnea and Insomnia. Most people that get lower quality of sleep dont do much physical activity.
sns.relplot(data, x="Age", y="Physical Activity Level", kind="line")
#A line plot between Physical Activity Level and Age was generated showing how the values vary througout age.
sns.relplot(data, x="Sleep Duration", y="Quality of Sleep", kind="line", errorbar="sd")
#A line plot between Quality of Sleep vs.Sleep Duration was generated showing how increased sleep duartion results to increased quality of sleep with a standard deviation. 
sns.lmplot(data, x="Daily Steps", y="Heart Rate")
#A scatter plot with a linear regression line was generated between Stress levels vs. Daily Steps. 

















     

















