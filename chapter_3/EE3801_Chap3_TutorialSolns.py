import random
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import pandas as pd 
import numpy as np 

'''
Some Remarks: To make things a little more
customizable for graphical user interfaces,
matplotlib separates the concept of the
renderer (the thing that actually does the
drawing) from the canvas (the place where
the drawing goes). The canonical renderer
for user interfaces is Agg which uses the
Anti-Grain Geometry C++ library to make a
raster (pixel) image of the figure.  

'''
#======================================

# Simple line plotting - Example 3.1
'''

X = [i for i in range(10)] # list comprehension style
Y = [2*X[i] for i in range(10)]
plt.title('Y=2X')
plt.xlabel('X values')
plt.ylabel('Y Values')
plt.plot(X, Y, marker='o',
     markerfacecolor='blue', markersize=3)

plt.show()
# for the same X, Y values show a different style
plt.title('Y=2X')
plt.xlabel('X values')
plt.ylabel('Y Values')
plt.plot(X, Y, linestyle = 'dashed',marker='o',
     markerfacecolor='blue', markersize=3)

plt.show()

'''
#======================================

# Plotting more than one line in the same graph - Example 3.2
'''

X = [i for i in range(10)] 
Y1 = [X[i] for i in range(10)]
Y2 = [2*X[i] for i in range(10)]
Y3 = [3*X[i] for i in range(10)]

# 
plt.title('Linear graphs')
plt.xlabel('X values')
plt.ylabel('Y Values')

plt.plot(X, Y1, marker='*',
     markerfacecolor='red', markersize=3, label='Y=X')
plt.plot(X, Y2, marker='o',
     markerfacecolor='blue', markersize=3, label='Y=2X')
plt.plot(X, Y3, marker='*',
     markerfacecolor='purple', markersize=3, label='Y=3X')

plt.xlabel('X Values')
plt.ylabel('Y Values')
#plt.legend()  # release this and show
plt.show()
'''

#========================

#  Example 3.3 
'''

x = [i for i in range(50)]

y1 = [x[i] for i in range(50)]  # y = x data
y2 = [x[i]**2 for i in range(50)]  # y = x^2 data
y3 = [x[i]**3 for i in range(50)]  # y = x^3 data

y4 = [x[i]**2-10*x[i]+3 for i in range(50)]  # a polynomial function

plt.title('Linear & Non-linear graphs')
plt.xlabel('X values')
plt.ylabel('Y Values')

plt.xlim([0, 50])
plt.ylim([-50, 50]) # adjust these limits and see the effect

plt.plot(x, y1, linestyle = 'dashed',marker='o',
     markerfacecolor='blue', markersize=3, label='Linear')

plt.plot(x, y2, linestyle = 'dashed',marker='o',
     markerfacecolor='red', markersize=3, label='Quadratic')

plt.plot(x, y4, linestyle = 'dashed',marker='o',
     markerfacecolor='orange', markersize=3, label='2nd order polynomial')

plt.plot(x, y3, linestyle = 'dashed',marker='o',
     markerfacecolor='green', markersize=3, label='Cubic')


plt.legend()
plt.show()

'''
#==========================

# Example 3.4 - Scatter plot

'''
# We will first generate 150 points in the range 0 to 50

X = [random.randint(10,50) for x in range(150)]
Y = [random.randint(10,50) for y in range(150)] 

plt.title('Scatter Plot')
plt.xlabel('X values')
plt.ylabel('Y Values')

plt.scatter(X, Y, label= "stars", color= "red",  
            marker= "*", s=15) 
plt.show()
'''

#==========
# Example 3.5 - Scatter plot
# students marks in a specific subject
'''
GirlsMarks = [89, 90, 70, 89, 100, 80, 42, 100, 80, 35]
BoysMarks = [30, 29, 73, 48, 100, 48, 38, 45, 81, 30]
MarksRange = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

plt.scatter(MarksRange, GirlsMarks, color='r')
plt.scatter(MarksRange, BoysMarks, color='g')
plt.xlabel('Marks Range')
plt.ylabel('Marks Scored')
plt.show()
'''

#==========

# Example 3.6 - Simple Bar Graph
'''

# create a list of labels - this is given to us

objects = ['Adventure', 'Romance', 'Drama', 'Comedy', 'Thriller/Suspense', 'Horror']

# we need to knwo the number of items in the objects list above
L = len(objects)
X_index = [i for i in range(L)]

# put the num of movies as a list - Also, given to us. 

Num_of_movies = [941,854, 4595, 2125,942,509]

# to add values on top of bars, we write a small function
def addlabels(x,y):
    for i in range(len(x)):
        plt.text(i,y[i],y[i])

plt.bar(X_index, Num_of_movies, tick_label = objects, width=0.4)  # see the graph - Cluttering on x axis ??
# plt.xticks(rotation=50) # use this line and see

addlabels(X_index, Num_of_movies)

plt.title('Movie Distribution')
plt.xlabel('Categories of movies')
plt.ylabel('Num of movies in each genre')


plt.show()

'''
# ===== plotting a bar and pie charts - freq distribution

# Example 3.7 

'''

# Screws varying diameter produced by a vendor (20mm to 50mm)
# 200 samples are taken for inspection; Generate a bar chart distribution. 

# Since data is not available, we generate the freqs first
# (We are preparing the data here actually)


freq = [] # list to collect the freq distribution 
visited = [] # this is avoid repeating while counting

screws = [random.randint(20,50) for i in range(500)] # a list of screw dia's
screws.sort()
#print(screws)

for num in screws:  # a screw is taken here
       if num not in visited: # check if we have already counted its frequency
              c = screws.count(num) # if not, count it here; c gives the count!
              #print(num,c)
              freq.append(c) # add that freq to the freq list
              visited.append(num) # add that screw to the visited list
print()
#print(visited) # shows the actual numbers generated in sorted order
#print(freq) # captures the resp freq of the numbers generated

# Example:
# freq = [3,5,...]
# visited = [20,21,...] - Means there are 3 samples of screw dia 20 
# 

plt.title('Screw Diameter Distribution (Fine-grain)')
plt.xlabel('Screw Diameter values(in mm)')
plt.ylabel('Number of Screws')

plt.bar(visited,freq)
plt.show()
'''

#=============================

# Example 3.8 Histogram plot

# Same example above and we will do a histogram plot.

'''

freq = []
visited = [] # this is avoid repeating while counting
screws = [random.randint(20,50) for i in range(500)]
screws.sort()
#print(screws)

for num in screws:  # a screw is taken here
       if num not in visited: # check if we have already counted its frequency
              c = screws.count(num) # if not, count it here
              #print(num,c)
              freq.append(c) # add that freq to the freq list
              visited.append(num) # add that screw to the visited list
print()

range = (20,50) # range on x axis values
bins = 8  # can be varied;
# Based on the range and bins, the size of each bin will be decided automatically

plt.hist(screws,bins, range, color='green',histtype='bar', rwidth = 0.7)

plt.xlabel('Screws')
plt.ylabel('# of Screws')
plt.title('Screws Distribution')
plt.show()

'''

#=============================

# Example 3.9 Pie Chart plot

# For the same example above we will do a Pie Chart plot.

# This Pie chart is a very fine grained!
# For every freq, it puts a slice! So display will be
# cluttered. See it!

'''

freq = []
visited = [] # this is avoid repeating while counting
screws = [random.randint(20,50) for i in range(500)]
screws.sort()
#print(screws)

for num in screws:  # a screw is taken here
       if num not in visited: # check if we have already counted its frequency
              c = screws.count(num) # if not, count it here
              #print(num,c)
              freq.append(c) # add that freq to the freq list
              visited.append(num) # add that screw to the visited list
print()

plt.pie(freq, labels = visited,   
        startangle=90, shadow = True,  
        radius = 1.2, autopct = '%1.1f%%')
plt.title('Screws distribution - Fine-grain')
plt.show()

'''

# DIY - Try to group according to a range of diameters and plot a coarse-grained
# pie-chart

#============================

#   Example 3.10 - Sg Haze Data Grouped Barcharts

# Read data from a file and plot. 

# first we will geenrate a random data [Haze data in Sg
# in the Band II and III)

# ============ (data generation below) ========


# East West below

'''
with open('haze_east.txt','w') as feast:
       for i in range(0,24):
              h = random.randint(0,200)
              feast.write('%d ' %h)
with open('haze_west.txt','w') as fwest:
       for i in range(0,24):
              h = random.randint(55,220)
              fwest.write('%d ' %h)

'''
#===
'''
# North South below

with open('haze_north.txt','w') as fnorth:
       for i in range(0,24):
              h = random.randint(0,180)
              fnorth.write('%d ' %h)

with open('haze_south.txt','w') as fsouth:
       for i in range(0,24):
              h = random.randint(50,200)
              fsouth.write('%d ' %h)
'''

#=============== 

# We need to read from each file and plot bar graphs

# Release this - Use only east and west for testing

'''

time_24hr_clk = [i for i in range(0,24) ]
print(time_24hr_clk)

hazeEast = []
with open("haze_east.txt", "r") as feast:
       for val in feast.read().split():
           hazeEast.append(int(val))
print(hazeEast)

hazeWest = []
with open("haze_west.txt", "r") as fwest:
       for val in fwest.read().split():
           hazeWest.append(int(val))
print(hazeWest)

'''

# north south below ===

'''
hazeNorth = []
with open("haze_north.txt", "r") as fnorth:
       for val in fnorth.read().split():
           hazeNorth.append(int(val))
print(hazeNorth)

hazeSouth = []
with open("haze_south.txt", "r") as fsouth:
       for val in fsouth.read().split():
           hazeSouth.append(int(val))
print(hazeNorth)
'''

#=====

'''

fig, ax = plt.subplots()
bar_width = 0.4
opacity = 0.9

# 
# Setting the position of a bar on X axis
# Note - You need to use r3 and r4 if you are plotting all 4 domains

r1 = time_24hr_clk
r2 = [x + bar_width for x in r1]
#r3 = [x + bar_width for x in r2]
#r4 = [x + bar_width for x in r3]

# actual bar plotting for each domain

ax.bar(r1, hazeEast, bar_width, alpha=opacity, color='r',
                label='East')
ax.bar(r2, hazeWest, bar_width, alpha=opacity, color='b',
                label='West')
#ax.bar(r3, hazeNorth, bar_width, alpha=opacity, color='k', label='North')

#ax.bar(r4, hazeSouth, bar_width, alpha=opacity, color='s', label='South')


ax.set_xlabel('Time (24-hour scale)')
ax.set_ylabel('PSI Index')
ax.set_title('SG Haze Distribution')


# Add xticks on the middle of the group bars
plt.xticks([r + bar_width for r in range(0,24)], time_24hr_clk)

ax.legend(ncol=4)
plt.show()

'''
#===================

# Following is just one domain - East - You can print and see
'''
plt.bar(time_24hr_clk, hazeEast)  # see the graph - Cluttering on x axis ??
plt.xticks(time_24hr_clk, fontsize=5, rotation=30) # use this line and see
plt.title('Haze Distribution (East)')
plt.xlabel('Time (24-hour scale)')
plt.ylabel('PSI Index')
plt.show()
'''

#============================

# Example 3.11 - Barcharts on subplots


# Syntax:  fig, a = plt.subplots(nrows, ncols, sharex, sharey)

# The function returns a figure object and a tuple
# containing axes objects equal to nrows*ncols.
# Each axes object is accessible by its index.
# optional keywords sharex and sharey allows you to
# specify the relationships between different axes.

'''

# Let us compute the functions to plot

def create_plots(functype):
        x = [i for i in range(12)]
        if functype == 'Pop':
                y = [random.randrange(1,10) for i in range(12)]
        elif functype == 'Electricity':
                y = [random.randrange(1,10) for i in range(12)]
        elif functype == 'Water':
                y = [random.randrange(1,10) for i in range(12)]
        elif functype == 'Gas':
                y = [random.randrange(1,10) for i in range(12)]

        return(x,y)

#====
# setting a style to use 
# plt.style.use('fivethirtyeight') 

# First create a figure object

fig = plt.figure() 

# We need to define subplots and their positions in figure

# Here it is a 2 x 2 grid;
# Subplots are filled up along the rows;
# So, 22k means  - 22 represents rows x cols; k represents k-thh subplot
# so the arrangement will be:
# 221 222 
# 223 224


plt1 = fig.add_subplot(221) # object plt1 for subplot 221 is generated
plt2 = fig.add_subplot(222) 
plt3 = fig.add_subplot(223) 
plt4 = fig.add_subplot(224)

# plotting points on each subplot
x,y = create_plots('Pop')
plt1.set_xlabel('Months (in 2019)')
plt1.set_ylabel('in ($x 10^3$)')
plt1.bar(x, y, color ='r') 
plt1.set_title('Population') 

x,y = create_plots('Electricity')
plt2.set_xlabel('Months (in 2019)')
plt2.set_ylabel('in Kw/zone')
plt2.bar(x, y, color ='b') 
plt2.set_title('Electricity') 

x,y = create_plots('Water')
plt3.set_xlabel('Months (in 2019)')
plt3.set_ylabel('in $10^3$ lits/zone')
plt3.bar(x, y, color ='g') 
plt3.set_title('Water') 

x,y = create_plots('Gas')
plt4.set_xlabel('Months (in 2019)')
plt4.set_ylabel('in $10^3$ Cubic-mts/zone')
plt4.bar(x, y, color ='k') 
plt4.set_title('Gas') 

# adjusting space between subplots 
fig.subplots_adjust(hspace=.5,wspace=0.8) 

# function to show the plot 
plt.show()

'''
#======

# Ex 3.11 on JUPYTER NOTEBOOK
# Use the following organization for the above prog:

'''
# Note: BEFORE importing matplotlib use the following line:

%matplotlib inline

def create_plots(functype):
        x = np.arange(-10, 10, 0.01)
        if functype == 'linear':
                y = x
        elif functype == 'quadratic':
                y = x**2
        elif functype == 'cubic':
                y = x**3
        elif functype == 'quartic':
                y = x**4
        elif functype == 'sinx':
                y = np.sin(x)
        elif functype == 'cosx':
                y = np.cos(x)
        return(x,y)


fig = plt.figure() 
plt1 = fig.add_subplot(231) # object plt1 for subplot 221 is generated
x, y = create_plots('linear') 
plt1.plot(x, y, color ='r') 
plt1.set_title('$y_1 = x$') 

plt2 = fig.add_subplot(232)
x, y = create_plots('quadratic') 
plt2.plot(x, y, color ='b') 
plt2.set_title('$y_2 = x^2$')

plt3 = fig.add_subplot(233) 
x, y = create_plots('cubic') 
plt3.plot(x, y, color ='g') 
plt3.set_title('$y_3 = x^3$') 

plt4 = fig.add_subplot(234)
x, y = create_plots('quartic') 
plt4.plot(x, y, color ='k') 
plt4.set_title('$y_4 = x^4$')

plt5 = fig.add_subplot(235)
x, y = create_plots('sinx') 
plt5.plot(x, y, color ='k') 
plt5.set_title('sin(x)')

plt6 = fig.add_subplot(236)
x, y = create_plots('cosx') 
plt6.plot(x, y, color ='b') 
plt6.set_title('cos(x)')

# adjusting space between subplots 
fig.subplots_adjust(hspace=.8,wspace=0.6)

'''
# ===== End: for jupyter =====

#=====================================================

# Example 3.12 - BOX PLOT  
'''
# Useful plot in statistics to understand the distribution of the data

#  BOX PLOT - We have not done this. Ignore this BOX Plot part.
# If you are interested, run and see. 

# Boxplot is also used for detect the outlier in data set.
# It captures the summary of the data efficiently with a
# simple box and whiskers and allows us to compare easily
# across groups. Boxplot summarizes a sample data using 25th,
# 50th and 75th percentiles. These percentiles are also known
# as the lower quartile, median and upper quartile.

# A box plot consist of 5 things.

# Minimum
# First Quartile or 25%
# Median (Second Quartile) or 50%
# Third Quartile or 75%
# Maximum



# Use bodyfat_Example 2.2.csv data and we can plot 
BFA = pd.read_csv('bodyfat_Example 2.2.csv')
print('BFA head: \n', BFA.head())
print()

# group by - Recall from Chap 2

X = BFA.groupby(['category'])[['bodyfat']].describe()
print('Grouping by Category for bodyfat stats: \n', X)

BFA.boxplot(by ='category', column =['bodyfat'], grid = False)
plt.show()
# In this data we do not see any outliers because data was
# already categorized.

'''
# ===========

'''
# Consider a data like tips.csv
mytips = pd.read_csv('tips.csv')
print('mytips head: \n', mytips.head())
# Data captures - hotel bill, tips, registered person,
# num of persons(size), dinner or lunch, etc
print()
print('mytips head: \n', mytips.head())
print()
mytips.boxplot(by ='day', column =['total_bill'], grid = False)
plt.show()


'''
#==================================

#  Ex. 3.13 - Correlation matrix and heatmap generation 

from matplotlib import cm as cm

# Import the bodyfat correlation file data  
BFA = pd.read_csv('bodyfat_Example_Correlation.csv')

BFA_summary = BFA.describe() # This is also a data frame
print('BFA_summary: \n\n', BFA_summary, '\n')

print('BFA_summary: 2nd row data \n\n', BFA_summary[1:2])

print()
my_corr_mat1 = BFA.corr(method='kendall') #spearman                       
print('Corr matrix (Kendall): \n', my_corr_mat1)

print()
my_corr_mat2 = BFA.corr(method='spearman') #spearman                       
print('Corr matrix (Spearman): \n', my_corr_mat2)

col_names = BFA.columns
print('Featrures: \n',col_names)

# Heatmaps creation

fig = plt.figure()
ax1 = fig.add_subplot(111)
cmap = cm.get_cmap('jet', 30)
cax = ax1.imshow(my_corr_mat1, interpolation="nearest", cmap=cmap)
ax1.grid(True)
plt.title('Bodyfat Feature Correlation (Kendall)')
labels= col_names
ax1.set_xticklabels(labels,fontsize=6)
ax1.set_yticklabels(labels,fontsize=6)
# Add colorbar, make sure to specify tick locations to match desired ticklabels
tickvals = [x/10 for x in range(-15,15)]
fig.colorbar(cax, ticks= tickvals)

plt.show()

fig = plt.figure()
ax1 = fig.add_subplot(111)
cmap = cm.get_cmap('jet', 30)
cax = ax1.imshow(my_corr_mat2, interpolation="nearest", cmap=cmap)
ax1.grid(True)
plt.title('Bodyfat Feature Correlation (Spearman')
labels= col_names
ax1.set_xticklabels(labels,fontsize=6)
ax1.set_yticklabels(labels,fontsize=6)
# Add colorbar, make sure to specify tick locations to match desired ticklabels
tickvals = [x/10 for x in range(-15,15)]
fig.colorbar(cax, ticks= tickvals)

plt.show()
#


#================== =================   ================  =========

# Subplots - Use this format, if needed!

'''
rows, cols = 2, 3
fig, ax = plt.subplots(rows, cols,
                       sharex='col', 
                       sharey='row')

for row in range(2):
    for col in range(3):
        ax[row, col].text(0.5, 0.5, 
                          str((row, col)),
                          color="green",
                          fontsize=18, 
                          ha='center')

plt.show()
'''
#===========================
