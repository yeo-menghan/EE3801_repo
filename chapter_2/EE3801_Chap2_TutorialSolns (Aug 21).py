import pandas as pd


# PP: 2.1a - forming a data frame and printing 
'''

mydict = {"1_Country": ["Brazil", "Russia", "India", "China", "SouthAfr"],
       "2_Capital": ["Brasilia", "Moscow", "New Dehli", "Beijing", "Pretoria"],
       "3_Currency": ["Brazilian real", "Russian Ruble", "Indian Rupee", "Chinese Yuan", "South African Rand "],
       "4_Currency_Sym": ["R", "₽", "₹", "¥", "R"] }

country_info = pd.DataFrame(mydict)
print('The type is: ', type(country_info))  # what do you observe?
print()
print(country_info)  # what do you observe?
print()
print('country_info[1:] will print:\n ',country_info[1:])  # see what this prints
print()
print('==============')

# changing the default row indices to meaningful entries
country_info.index = ["BR", "RU", "IN", "CH", "SA"] 
print()
# Print out with new index values
print('country_info with new indices: \n', country_info)
print()
#
# Series

country_info.loc['BR']  # this should extract all cols in row 'BR' - Check.

BRser = country_info.loc['BR'] # loc() method 
print('BRser type is: \n',type(BRser))
print('BRser is:\n',BRser) # Chk what it prints  
print()
print('BRser[2] is:\n',BRser[2])  #see what it is printing 
print('==============')

# Extract currency col

Curr = country_info["3_Currency"]
print('Curr is: \n', Curr)
print()
# Chk what these print 
print('Curr[1] is: ',Curr[1])
print('Curr[RU] is: ', Curr['RU'])  
#===============================
print()

# PP 2.1b - extract and concatenate

# Making a copy  of Country feature column 

new = country_info["1_Country"].copy() # extract the column
print('new is of type: ', type(new))
# Concatenating Country column with Currency column by
# overwriting the current Currency column:

country_info["4_Currency_Sym"] = country_info["4_Currency_Sym"].str.cat(new, sep =", ") 

print(country_info)

#
'''
#============ ========= ========= ========= 

# PP:2.2   Reading a csv file and related commands

'''
#
BFA = pd.read_csv('bodyfat_Example 2.2.csv')

# Prints out the entire bodyfat data - entire file - clumsy! 

#print(BFA) 

# sample printing is as follows - top 5 values by default
print('Type of the dataset given: \n', type(BFA), '\n')
print()

print('Size of the data set (BFA): \n',BFA.shape) # puts out as a tuple rows x columns

print()

# info() method provides the essential details about your dataset, such as
# the number of rows and columns, the number of non-null values, what type of
# data is in each column, and how much memory your DataFrame is using.

print('BFA Dataframe Info:',BFA.info(), '\n')
print()
print("Sample (top 5) values from your data file:\n ",BFA.head(), '\n')
print("Sample (last 2) values from your data file:\n ",BFA.tail(2), '\n')
#

# Standard stats parameters are displayed when you print a summary.

BFA_summary = BFA.describe() # This is also a data frame

print('BFA_summary: \n\n', BFA_summary, '\n')
print()
print('BFA_summary: 2nd row data \n\n', BFA_summary[1:2]) # uses slicing
print()
print('BFA_summary: Rows 2 to 4 data \n\n', BFA_summary[2:5])
print()

# From the BFA, we can extract anything.

print('BFA data on knees (top 5 entries): \n',BFA["knee"].head())
print()

# different ways to extract - try to use at[] method - dataframe.at[]

print('BFA data on knees (on row 3): ',BFA.at[3,"knee"]) # uses feature knee; Note the .at() method
# If the above does not work, try using 
print(BFA.iloc[3].at["knee"]) # - try printing this and check

print('BFA data on knees (on row 3 using indices): ',BFA.iat[3,10]) # uses indices; note the iat() method

'''
#=======

# Example A
'''
mydata = {'product': ['A', 'B', 'C', 'C', 'D'], 
	  'price': [22000, 27000, 25000, 29000, 35000], 
	  'year': [2014, 2015, 2016, 2017, 2018] } 
DF = pd.DataFrame(mydata) 
print(DF)

# We can get a description specifically for certain categories;

stats_categorical = DF['product'].describe()
print(stats_categorical)
'''

#=========
'''
# ===Ex 2.2 (continued) ====

# You can group data using a shared common value and then summarize the
# values in another column using those groups.
# This is done using "groupby" method - Important for clustering apps to
# learn about the knowledge of the groups

# Use -  bodyfat_Example 2.2.csv and do the following. 

#  dataframe.groupby(['label_column'])[["value_column"]].method()

# Here the "label_column" is the column is used to create the
# groups and the "value_column" is the column that will be
# summarized for each group.

# Let us try the following.
# To see this effect, we will add another column to the bodyfat
# data - "category" integers between say 1 to 10. Then we
# groupby this category for a particular feature and report statistics!

X = BFA.groupby(['category'])[['bodyfat']].describe()
print('Grouping by Category for bodyfat stats: \n', X)                        

# Note that X is again a DF!! 
# You can then extarct any specific category you want to display
print('For categories 4 and 5:', X[0:5])

# Suppose we want to group accorning to age using average fat in the chest.
# How do we extract?

chestFatgroup = BFA.groupby("age")["chest"].mean()
print(type(chestFatgroup))
print('Grouping accorning to age using average fat in the chest: \n', chestFatgroup[:5])

# Multiple aggregation of data as groups
# If we want to group more than one quantity, we can do by listing
# them in the value col parameter w.r.t a specific label col parameter
# W.r.t "age" we want to group, chest and weight info.

multiGroup = BFA.groupby("age")["chest","weight"].mean()
print(type(multiGroup))
print('Multiple Grouping : \n', multiGroup[0:5])

'''
# =========


#================== =================   ================  =========

# PP: 2.3 - Cleaning up features and Displaying/Extracting the required features

'''

# USE EmpSmalldata0.csv

ESD = pd.read_csv('EmpSmalldata0.csv')

print(ESD.shape, '\n', ESD.head(2))

# How  to print the column names (features) of our dataset?

# Many times each dataset will have several features. We may not know the
# names of these features obviously. We can extract them as:

ColNames = ESD.columns # ColNames is a LIST; - features of the dataset
print(type(ColNames)) # chk the type 
print('Features of this data are: \n',ColNames, '\n')
print()

# Cleaning the names of the features as you like:
# Say you want to change all the names as capitals

ESD.columns = [col.upper() for col in ESD]
# 

print(ESD.columns)
print()
ColNames = ESD.columns

# Then, you can retrieve the data corresponding to any feature like:

print('Complete Salary Data: (as a Series) \n', ESD['SALARY'])
# This will print as a Pandas Series
# Now print the same 'Salary' info using DF;
print()

print('Complete Salary Data (using the ESD DF): \n', ESD[['SALARY']])
print()

print("Data Summary: \n",ESD.describe())
# What do you observe? It gives summary for only numerical data.

print()

ESD_summary = ESD.describe()
print("Summary of Salary info: \n", ESD_summary['SALARY'])
# Salary summary is extracted and printed
print()

print('Top 5 rows from the actual data \n', ESD[0:5])
# top 4 rows from the actual data
print()

print('Data from Rows 2 to 4: \n', ESD[2:5])   # from rows 2 to 4 

# start index is 2 and till 5th entry from 1st row(top row)
print()

print(' Complete Bonus and Team data \n', ESD[['BONUS %', 'TEAM']])
# extracting from multiple columns, but all data!
# How to extract only top 5 values from the specific columns?

print(' Top 5 rows of Team data (as Series): \n', ESD['TEAM'][0:5])
# top 5 rows from the actual data

#
'''

#================== =================   ================  =========
#
#PP: 2.4 - Consider another data file employees.csv given to you

'''

empDF0 = pd.read_csv("employees.csv")

#====  Part 1 - Use of Index and value_count() methods ====

# Pandas index and value_counts() method - Very useful to know
# if duplicate entries are there

mylist = empDF0["First Name"] # this will give a series 
print(mylist) # for debugging
print(type(mylist))
print()

L = empDF0["First Name"].tolist()  # series to list
print("Printing from the list L", L[0:5]) # for debugging
print()

idx = pd.Index(L)
print(idx)
print()

# Now using this idx, we can use value_counts()-counts the
# freq of items in descending order

X = idx.value_counts() 
print('Duplicates: \n',X.head())
print()

'''
#===
'''

# New file data here for this example  - Identifying duplicate
# rows for all cols

# givenDF[givenDF.duplicated(keep='first')]

# 'keep' argument decides which # element first or last to keep in a DF
# By default keep is set to 'first' and hence we don't see the first
# duplicate in the display. You can try with 'last' too

empDF1 = pd.read_csv("EmpSmalldata1.csv")
duplicateRowsDF = empDF1[empDF1.duplicated()] # keep = first, by default
print("Duplicate Rows except first occurrence based on all columns are :")
print(duplicateRowsDF, '\n')

# Find all Duplicate Rows based on specific columns
# In this case, we need to pass our choice of columns as a list in
# subset argument of the Dataframe.duplicate() function. 
# Then, it will select & return duplicate rows based ONLY on these columns.

# For example let’s find & select rows based on 2 columns

duplicateRowsColsDF = empDF1[empDF1.duplicated(['First Name', 'Salary'])]
print("Duplicate Rows based on specific cols except first occurrence based on specific columns are :")
print(duplicateRowsColsDF)

# find & select rows based on just the name and see what it prints

'''
#===== ====  Part 2 

'''
# Try to use the index as names of the persons. 

empDF = pd.read_csv("employees.csv", index_col = 'First Name')

# You can use "first Name" as the index of the first col and therefore you can
# access any row simply using "First Name"; 

# In the above, if you don't set the index_col then by default row indices
# 0, 1,2, ...999 will be used;
print('Top 5 rows: \n',empDF.head(5))
print('Features of this dataset: \n', empDF.columns)
print('Shape of the employees DF: \n',empDF.shape)
print()

# ==== Row data extraction ======

# loc() method - to extract a single row of data

print('Using loc() function:\n', empDF.loc['Douglas'])

# What do you observe here?? 
# Since we set 'First Name' as the index_col, the actual names now
# become the row indices! In this example, all "douglas' entries will
# be retrieved!

print()

# iloc() method - To select a single row of data using numerical
# value as an index

# This function allows us to retrieve rows and columns by position (numerical indices).
# In order to do that, we need to specify the positions of the rows
# that we want, and the positions of the columns that we want as well.

# The df.iloc() indexer is very similar to df.loc() but only uses integer
# locations to make its selections.

print('Using iloc() function to extract Row 3: \n', empDF.iloc[3])
# see what you get!
print()

# Extract a Set of rows using loc[]

X = empDF.loc[['Douglas', 'Jerry', 'Larry']]
# only these rows will be extracted with all features
print('Extracting a Set of rows using loc  \n', X)
print('X is a: \n',type(X)) # what is the type of X? 
print()

# Now extract a set of rows for a specific set of columns using loc[]

Y = empDF.loc[['Douglas', 'Jerry', 'Larry'], ['Salary', 'Team', 'Senior Management'] ] 
# Note the first [] - rows  and second [] - cols
print(Y)
print('Y is a: \n',type(Y))
print()


# In the above, we specified the ROWS as 'Douglas', 'Jerry', 'Larry'.

# But, now, I want to extract rows 10 to 15 for columns Salary, team and Senior management
# How do I do that?

# Involves 2 step process
# first extract those rows and then extract the reqd cols

Z1 = empDF[10:16]  # from the original empDF
#print('Z1 is: \n', Z1) # you need not print this; just for debug
Z2 = Z1[['Salary', 'Team', 'Senior Management']] 
print('Z2 (rows 10 to 15) is: \n',Z2)
#print('Z2 is a: \n',type(Z2))
print()

# ===== Column data extraction ====== ==============  ============ 

# How to extract a set of columns and print from a DF?

first = empDF[['Salary', 'Team']]  # gets ALL the rows for these 2 cols
print(first[0:5]) # we can print as per our requirement, say top 5 rows
'''
#==========
'''
#  DIY!  -  Try the following with Example 1.1 
#  loc(), iloc(), at() iat() can be combined - 

print('extracts element in row 0 under column 2_Capital using iloc() and at \n')
print(country_info.iloc[0].at["2_Capital"])
# extracts element in row 0 under column 2_Capital

print()
print('extracts element in row 0 under column 2_Capital using iat')
print(country_info.iat[0,1])
# extracts element in row 0 under column 2_Capital

'''
#================== =================   ================  =========

# Handling Missing Data  - PP Ex 2.5
'''

# Refer to EmpSmalldata  given to you

ESD = pd.read_csv("EmpSmalldata.csv")
print('ESD -  Shape of the data: \n',ESD.shape)
print()
print('Index method gives: ', ESD.index)
print()

ESDcols = ESD.columns
print("Features of this ESD: \n",ESDcols)
print()

# testing - extract female statistics alone
print('Female Gender Stats: \n', ESD[ESD.Gender == 'Female'])
print()
# Sometime we need to remove and present the data by removing
# the Gender col from this ESD and print as all are females;
Xf = ESD[ESD.Gender == 'Female']
print('Female Gender Stats: \n', Xf.drop(['Gender'], axis=1))
print()

#Identifying the gaps/voids in the data

ESDnull = ESD.isnull() # isnull() method identifies the voids, if any
# ESDnull is also a DF

print("ESDnull is: \n", ESDnull.head(10))  # What do you observe?
print()

print("Number of missing data in each feature: \n")
missingdata_stats = ESD.isnull().sum()
print(type(missingdata_stats)) # what do you observe?
print(missingdata_stats)
print()

# Now, use the above missingdata_stats and remove those columns
# in which there are more than 3 missing values - applic req

# print(missingdata_stats["Salary"]) # just checking!

f = [] # creating a feature list to delete from ESD
for i in range(len(missingdata_stats)):
       if(missingdata_stats[i] >= 3):
              # print(missingdata_stats[i]) # this will print the value
              feature = ESDcols[i] # extracting the name of the feature here
              # print("Column to delete in ESD: ",feature)
              f.append(feature)
print("Columns to delete in ESD are: ",f)

# above is a detailed implementation; You can try writing with comprehensions

print()
for j in range(len(f)):
       ESD = ESD.drop(f[j],axis=1)

print('After removing identified columns - EmpSmalldata0  Shape: \n',ESD.shape)
print(ESD.head(5))

'''
#=================================

# Example B - Categorical data to column vectors

'''

import numpy as np
df = pd.DataFrame({'X': ['potato', 'carrot', 'nuts'], 'Y': ['carrot', 'butter', 'nuts'],
                   'Q': ['potato','potato','potato'], 'M': ['nuts',np.NaN,'nuts'], 'Z': [7,9,13]})
print(df)

X = pd.get_dummies(df, prefix=['col1', 'col2', 'col3','col4'])
print(X)

#
'''
#=======================

# PP 2.6 apply() method 
'''
data = pd.DataFrame({'EmployeeName': ['Xavier Simon', 'Sarah Nayer', 'Andrea Salim', 'Kasim Akram', 'Henry Sebastein', 'Amenda Bailey', 'Susan Paul', 'Tham Khong', 'Alex Chang', 'Kim Wang'],
                    'Department': ['Accounting', 'Engineering', 'Engineering', 'HR', 'HR', 'HR', 'Data Science', 'Data Science', 'Accounting', 'Data Science'],
                    'HireDate': [2010, 2018, 2012, 2014, 2014, 2018, 2020, 2018, 2020, 2012],
                    'Sex': ['M', 'F', 'F', 'M', 'M', 'F', 'F', 'M', 'M', 'F'],
                    'Birthdate': ['04/09/1982', '14/04/1981', '06/05/1997', '08/01/1986', '10/10/1988', '12/11/1992', '10/04/1991', '16/07/1995', '08/10/1992', '11/10/1979'],
                    'Weight': [78, 80, 66, 67, 90, 57, 115, 87, 95, 57],
                    'Height': [176, 160, 169, 157, 185, 164, 195, 180, 174, 165],
                    'Kids': [2, 1, 0, 1, 1, 0, 2, 0, 3, 1]
                    })
print(data)
print()
# 1 Create two columns by separating the first and the last names of the employees
# In this case we apply lambda func to Emp name column and split them.

data['FirstName'] = data['EmployeeName'].apply(lambda x : x.split()[0])
data['LastName'] = data['EmployeeName'].apply(lambda x : x.split()[1])
print(data)
print()
# 2 Compute the age of the employees and store as a separate column

# We need to write a function furst to derive the age of a person
# We need to use the date format in the dd/mm/yyyy format;
# We use the following

from datetime import datetime, date

def compute_age(birthdate):
    birthdate = datetime.strptime(birthdate, '%d/%m/%Y').date()
    today = date.today()
    return today.year - birthdate.year - (today.month < birthdate.month)

# now we can apply the above func to all under 'Birthdate' column in our DF

data['Age'] = data['Birthdate'].apply(compute_age)
print(data)
print()
# 3 Compute the average age of the employees in that organization.
print('Average age of this org: ', data['Age'].mean())
'''
#=======================


