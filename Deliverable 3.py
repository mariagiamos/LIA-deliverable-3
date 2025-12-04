print("deliverable 3")

import pandas as pd
data = pd.read_csv("Sleep_health_and_lifestyle_dataset.csv")
import seaborn as sns
#2. Preliminary steps-----------------------------------

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

#3. Univariate Non-Graphical EDA
#In this step, we analyze each variable separately to better understand the distribution of values.
#We will split our dataset into numerical variables and categorical variables because they are summarized differently.

#First, we remove the Person ID column. This column is just an identifier and does not represent any real measurement or category.
#Keeping it would distort our results and is unnecessary for analysis.
data = data.drop(columns=["Person ID"])

#seperate numerical and categorical variables
num = data.select_dtypes(include="number") #only keeps numerical clumns
cat = data.select_dtypes(exclude="number") #only keeps non-numerical columns

#a) Numerical Values
print("Numerical Values")
for column in num.columns:
    print("Variable:", column)
    print("Mean:", num[column].mean()) #average value
    print("Median:", num[column].median()) #midle value
    print("Mode:", num[column].mode()[0]) #most frequent values, and mode (0) so that it takes the first mode
    print("Standard Deviation:", num[column].std())
    print("Variance:", num[column].var()) #square of the std
    print("Quartiles (Q1, Q2, Q3):")
    print(num[column].quantile([0.25, 0.50, 0.75]))
    
#b) Categorical Variables
print("Categorical Variables")
for col in cat.columns:
    print("Variable:", col)
    print(cat[col].value_counts()) #frequency counts of each category
    print(cat[col].value_counts(normalize=True)) #proportions instead of counts
    print("Mode:", cat[col].mode()[0]) #most common category
    print("Unique:", cat[col].nunique()) #how many different categories


#4. Univariate graphical EDA-------------------------------------------------------
variables= ['Age', 'Sleep Duration', 'Quality of Sleep', 'Physical Activity Level', 'Stress Level', 'Heart Rate', 'Daily Steps' ]  #numerical variables 


#a) Custom and appropriate number of bins
for var in variables:   #create a simple for loop to generate plots for 7 variables mentionned above
    sns.displot(data, x=var,bins=10)
    

#b) Conditioning on other variables
for var in variables:
    sns.displot(data,x=var, bins=10, hue='Gender', element= 'step') #added 'step' to make the genders easier to distinguish

    
#c) Stacked histogram
for var in variables:
    sns.displot(data,x=var, bins=10, hue='Occupation', multiple= 'stack')

#d) Dodge bars
for var in variables:
    sns.displot(data,x=var, bins=10, hue='BMI Category', multiple='dodge')

#e) Normalized histogram statistics
for var in variables:
    sns.displot(data, x=var, bins=10, stat='density', common_norm=False)

#f) Kernel density estimation (choosing the smoothing bandwidth)
for var in variables:
    sns.displot(data, x=var, kind='kde', bw_adjust= .25 ) 

#g) Empirical cumulative distributions
for var in variables:
    sns.displot(data, x=var, kind='ecdf')



#Questions to answer for five of the numerical variables

#4.1 What is the distribution of the variable? (is the data normally distributed, skewed, bimodal, etc?)
#Age: It is multimodal due to its several dips in between the bins and irregular, but perhaps slightly skewed towards older ages. 
#Sleep Duration: It is multimodal because poeple cluster around different sleep duration habits ( 6 ,7,8 hours usually are more commmun) which produces multiple bumps and dimps instead of a smooth curve. 
#Daily Steps: It is also multimodal with no clear skewness.
#Heart Rate: It looks somewhat normaly distributed in the beguining between 65 and 75 bpm, but it is longer on the right side making it none symetrical and right-skewed towards the 75 to 85 bpm.
#Stress Levels: Because there are several bars at specific numbers (integers) thus has discrite levels of stress, making it neither normally distributed, not skewed or bimodial. But, we can see that the lowest level is 6 and highest is 8.

#4.2 Are there any outliers? (are there extreme values that fall outside the typical range?)
#Age: None
#Sleep Duration: None
#Daily Steps: None 
#Heart Rate: I wasn't so sure about this one , so i plotted a box plot (below) and it clearly shows quite a few outliners extending from 77 to higher than 80 bpm. Also I might add that this is the heart rate at rest I suppose which would make sense for a resting heart rate higher than 80 to be taken as an outliner because it is not healty and often is linked to overweight and diseases. 
sns.boxplot(y=data['Heart Rate'])
#Stress Levels: None
   
#4.3 What is the spread and central tendency? (where is the median? How spread out is the data?)
#Age: Central Tendency around 45 years and is spread out between 25 and 60 years and is very unevenly spread out mosly in the earlier ages.
#Sleep Duration: Central Tendency around 7 hours and the data is spread out unevenly with a few drastic drops in between data.
#Daily Steps: Central Tendency around 7000 steps and the data is spread out unevenly.
#Heart Rate: Central Tendency is a little over 70 bpm and the data spreads out into lower count towards the right end .
#Stress Levels: Central Tendency is 5 and isn't very spread out. 
    
#4.4 Is the data symmetric or skewed? (is the data skewed left or right?)
#Age: It is not really symmetric or skewed ( a little right-skewed but it can be neglected)
#Sleep Duration: Not symmetric at all or skewed. 
#Daily Steps: Not symmetric, with no clear skewness. 
#Heart Rate: May seem symetric at first, but not at the end where it is clearly right-skewed.
#Stress Levels: The histogram that is the least symetric and not skewed. 
    
#4.5 How frequent are certain ranges of values? (which value ranges are most common?)
#Age: Around 45 years
#Sleep Duration: Between 6.5 hours , 7.25-7.5 hours and around 8 hours which is the highest. 
#Daily Steps: 8000 steps
#Heart Rate: Between 67 and 70 bpm.
#Stress Levels: 3 and 8 ( slighty higger) which shows how stress is lived in both extremes; not at all and a lot, with little in the middle around 6. 

#5 Multivariate non-graphical EDA
#a) Relationship between Gender and Sleep Disorder in proportions
print("Crosstab between Gender and Sleep Disorder")
#This table shows how many individuals of each gender have or do not have sleep disorders.
tab1 = pd.crosstab(data["Gender"], data["Sleep Disorder"], normalize='index')
print(tab1)

#b) Rekationship between BMI and sleep disorder
print ("Crosstab between BMI and Sleep Disorder")
#this tabke shows how many individuals of each gender have or do not have sleep disorders
tab2=pd.crosstab(data["BMI Category"], data["Sleep Disorder"], normalize='index')
print(tab2)

#c) Relationship between Occupation and Sleep Disorder
print("Crosstab between Occupation and Sleep Disorder")
#this one shows which occupatopms have higher proportions of sleep disorders
tab3 = pd.crosstab(data["Occupation"], data["Sleep Disorder"], normalize='index') #its index to give a proportion
print(tab3)

#d)Relationship between Quality of Sleep and Stress Level
print("Crosstab between Quality of Sleep and Stress Level")
#this table shows how stress levels vary across different sleep quality categories
tab4 = pd.crosstab(data["Quality of Sleep"], data["Stress Level"], normalize='index')
print(tab4)

#e)Three-way table: Gender + Occupation vs Sleep Disorder
print("Three-way Crosstab - Gender and Occupation vs Sleep Disorder")
#this table shows the proportions of sleep disorders within each (Gender, Occupation) combination
tab5 = pd.crosstab([data["Gender"], data["Occupation"]], data["Sleep Disorder"], normalize='index')
print(tab5)

#6. Multivariate graphical EDA-----------------------------------------------------------
#6.1 Visualizing statistical relationships
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

#6.2.Visualizing categorical data 
# --- Fix Blood Pressure Ordering for ALL Graphs ---

# Extract systolic value for proper numeric sorting
data["BP_Systolic"] = data["Blood Pressure"].apply(lambda x: int(x.split("/")[0]))

# Sort LOW → HIGH correctly
data = data.sort_values(by="BP_Systolic", ascending=False)

#Categorical data: Gender, Occupation, BMI Category, Blood Pressure and Sleep Disorder
#a)categorical scatter plot with jitter enabled
sns.catplot(data, x='Sleep Disorder', y='Blood Pressure', kind='strip', jitter=True)
#Jitter is enabled so the points spread out and overlapping values are easier to see.

#b)categorical scatter plot with jitter disabled (explain your choice of variable for this one)
sns.catplot(data, x='Gender', y='Blood Pressure', kind='strip', jitter=False)
#Jitter is off because Gender only has two categories, so points stay aligned and easier to compare.

#c)“beeswarm” plot representing 3 variables
sns.catplot(data, x='Sleep Disorder', y='Blood Pressure', hue='Gender', kind='swarm')
#A beeswarm (swarm) plot showing Blood Pressure distributions across sleep disorder types by Gender.

#d)box plot representing 3 variables
sns.catplot(data, x='Sleep Disorder', y='Blood Pressure', hue='Gender', kind='box')
#Box plot showing the distribution of Blood Pressure for each sleep disorder category split by Gender.

#e)box plot showing the shape of the distribution (boxenplot)
sns.catplot(data, x='BMI Category', y='Blood Pressure', kind='boxen')
#Boxen plot showing how Blood Pressure distribution shape changes across BMI categories.


#f)split violin plot representing 3 variables with bandwidth adjusted
sns.catplot(data, x='BMI Category', y='Sleep Duration', hue='Gender', kind='violin', split=True, bw_adjust=0.7)
#Split violin comparing Male and Female Sleep Duration for each BMI Category with adjusted bandwidth.

#g)violin plot with scatter points inside the violin shapes
sns.catplot(data, x='Sleep Disorder', y='Blood Pressure', hue='Gender', kind='violin', inner='point')
#Violin plot showing the distribution of Blood Pressure with summary points inside each violin.

#h) 1 bar plot representing 3 variables showing 97% confidence intervals
sns.catplot(data, x='BMI Category' , y='Blood Pressure' , hue='Gender', kind='bar', errorbar=('pi', 97))

#i) 1 point plot representing 3 variables showing 90% confidence intervals and lines in dashed style
sns.catplot(data, x='Sleep Disorder' , y='Blood Pressure' , hue='Gender', kind='point', errorbar=('pi', 90), linestyles=['-','--'])

#j) 1 bar plot showing the number of observations in each category
sns.catplot(data, x= 'Sleep Disorder', hue='Gender', kind='count') #Counts the number of each sleep disorder; Insomnia and Sleep Apnea and made it more visible to see the difference in males and females. Males have

#6.3. Visualizing bivariate distributions
#a) 1 “heatmap” plot representing 2 variables with color intensity bar and adjusted bin width.
sns.displot(data, x='Age', y='Sleep Duration', binwidth=(1,3), cbar=True)

#b) 1 distribution plot with 2 variables making use of bivariate density contours with amount of curves and its lowest level adjusted (use a kernel density estimation displot()).
sns.displot(data, x='Age', y='Sleep Duration', kind='kde')

#c) 1 “heatmap” plot representing 3 variables, again of kind kde.
sns.displot(data, x='Age', y='Quality of Sleep', hue='Occupation', kind='kde')














     

















