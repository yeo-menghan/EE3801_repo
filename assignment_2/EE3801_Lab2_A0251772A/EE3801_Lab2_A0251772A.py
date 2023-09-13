import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

df = pd.read_csv('taxis.csv', encoding='unicode_escape')

# ------------------------------------------------------------------------
# Question 1a
print("Question 1a")

# Convert pickup and dropoff columns into datetime
df['pickup'] = pd.to_datetime(df['pickup'])
df['dropoff'] = pd.to_datetime(df['dropoff'])

# Extract day and time from pickup and dropoff columns
df['pickup_date'] = df['pickup'].dt.day
df['pickup_time'] = df['pickup'].dt.time
df['dropoff_date'] = df['dropoff'].dt.day
df['dropoff_time'] = df['dropoff'].dt.time

# Print top 5 rows, dropping pickup and dropoff temporarily
print("After spliting the date and time for pick and dropoff, here's the resultant df:\n")
print(df.head(5).to_string(header=True, index=False, col_space=10))
print()

# ------------------------------------------------------------------------
# Question 1b
print("Question 1b")

# Calculate the time of travel for each row and add it as a new column
df['travel_time'] = (df['dropoff'] - df['pickup'])

# Group by car_type and compute the totals
color_agg_results = df.groupby('color').agg({
    'fare': 'sum',
    'passengers': 'sum',
    'distance': 'sum',
    'travel_time': 'sum'
})

print("The aggregated results of fare, passengers, distance and travel_time for each colour is:")
print(color_agg_results.to_string(header=True, index=True, col_space=10))
print()

# ------------------------------------------------------------------------
# Question 2
print("Question 2")
# Filter for cash payments and specific pickup dates
cash_df = df[(df['payment'] == 'cash') & (df['pickup_date']).isin([10, 15, 20, 25, 30])]

# Function to get row with max distance for each group
def get_max_distance_trip(group):
    idx = group['distance'].idxmax()
    if pd.notna(idx):  # checks if idx is not NaN
        return group.loc[idx]
    else:
        return pd.Series({'distance': 0})

# Group by car color and pickup date, then apply the function
max_distance_df = cash_df.groupby(['color', 'pickup_date']).apply(get_max_distance_trip)

# Filter and rearrange columns
GY_cash = max_distance_df[['color', 'distance', 'pickup', 'pickup_date', 'pickup_time', 'dropoff', 'dropoff_date', 'dropoff_time', 'fare']]
GY_cash.columns = ['color', 'distance', 'pickup', 'pickup_date', 'pickup_time', 'dropoff', 'dropoff_date', 'dropoff_time', 'fare']

GY_cash = GY_cash.reset_index(drop=True)

print("Longest distance on date 10, 15, 20, 25 and 30 for each color cab: ")
print(GY_cash.to_string(header=True, index=False, col_space=10))
print()

# ------------------------------------------------------------------------
# Question 3
print("Question 3")

# Group by 'pickup_date' and find the index with the maximum 'distance'
idx = GY_cash.groupby('pickup_date')['distance'].idxmax()

# Create a new dataframe with only the rows with the maximum 'distance' for each 'pickup_date'
GY_maxDist = GY_cash.loc[idx]

# Display the new DataFrame
print("Showing trip details of cabs with longest distances on pickup date of 10, 15, 20, 25, 30: ")
print(GY_maxDist.to_string(header=True, index=False, col_space=10))
print()

# ------------------------------------------------------------------------
# Question 4
print("Question 4")

# Function to calculate speed
def calculate_speed(row):
    # Convert date and time columns to datetime objects
    pickup_datetime = row['pickup']
    dropoff_datetime = row['dropoff']

    # Convert distance from kilometers to meters
    distance_m = row['distance'] * 1000

    # Calculate time difference in seconds
    time_difference = (dropoff_datetime - pickup_datetime).total_seconds()

    # Handle cases where time_difference is zero to avoid division by zero error
    if time_difference == 0:
        return 0

    # Calculate speed in meters per second
    speed = distance_m / time_difference

    return speed

# Applying the function to calculate speed
GY_maxDist['speed'] = GY_maxDist.apply(calculate_speed, axis=1)

print("GY_maxDist showing the actual speed in m/s of the vehicle: ")
print(GY_maxDist.to_string(header=True, index=False, col_space=10))
print()

# ------------------------------------------------------------------------
# Question 5
print("Question 5")

# Filter the dataset for the specified conditions
filtered_df = df[
    (df['pickup_borough'] == 'Brooklyn') &
    (df['dropoff_borough'] == 'Manhattan') &
    (df['pickup_date'] >= 10) &
    (df['pickup_date'] <= 25)].copy()

filtered_df['speed'] = filtered_df.apply(calculate_speed, axis=1)

# Calculate the mean speed for green and yellow cars
mean_speeds = filtered_df.groupby('color')['speed'].mean()

# Print number of trips
print("Number of trips made with the pickup date between the dates 10th March and 25th March: ")
print(len(filtered_df))

# Print mean speeds
print()
print("Mean speed of each color cab:")
print(mean_speeds.to_string(header=True, index=True))
print()

# ------------------------------------------------------------------------
# Question 6
print("Question 6")

# Define the start and end time
start_time = pd.to_datetime('2019-03-17 14:30:00', format='%Y-%m-%d %H:%M:%S')
end_time = pd.to_datetime('2019-03-17 16:00:00', format='%Y-%m-%d %H:%M:%S')

# Filter the dataframe for the specified date and time range
filtered_df = df[
    (df['pickup'] >= start_time) &
    (df['pickup'] <= end_time)
]

# Group by 'color' and count the number of pickups for each color
color_pickup_counts = filtered_df.groupby('color')['pickup_time'].count()

# Find the color with the maximum number of pickups
print("Number of pickups per color: ")
print(color_pickup_counts.to_string(header=False, index=True))
most_pickups_color = color_pickup_counts.idxmax()

print(f"The color with the most pickups between 2:30 pm and 4:00 pm on March 17th was: {most_pickups_color}")
print()

# ------------------------------------------------------------------------
# Question 7
print("Question 7")

# Group the data by pickup zone and calculate the required statistics
result_df = df.groupby('pickup_zone').aggregate({
    'passengers': ['sum', 'min', 'max'],
    'fare': ['sum', 'min', 'max'],
    }
)

# Display the first 5 rows of the resulting dataframe
print(result_df.head().to_string(header=True, index=True, col_space=10))
print()

# ------------------------------------------------------------------------
# Question 8
print("Question 8")

# Calculate fuel cost
df['fuel_cost'] = (df['distance'] * 5.5 * 3 / 100)
# Group the data by color, pickup zone and calculate the required statistics
# https://pandas.pydata.org/pandas-docs/dev/reference/api/pandas.NamedAgg.html
stats_q8 = df.groupby(['color', 'pickup_zone']).agg(
    num_trips=pd.NamedAgg(column='pickup', aggfunc='count'),
    total_passengers=pd.NamedAgg(column='passengers', aggfunc='sum'),
    total_distance=pd.NamedAgg(column='distance', aggfunc='sum'),
    total_fare=pd.NamedAgg(column='fare', aggfunc='sum'),
    total_fuel_cost=pd.NamedAgg(column='fuel_cost', aggfunc='sum'),
)

# Split the data into two separate DataFrames based on the color
Yellow_stats_df = stats_q8.loc['yellow'].reset_index()
Green_stats_df = stats_q8.loc['green'].reset_index()

# Display the top 5 rows of each DataFrame
print("From the color yellow:")
print(Yellow_stats_df.head().to_string(header=True, index=True, col_space=10))
print("\nFrom the color green:")
print(Green_stats_df.head().to_string(header=True, index=True, col_space=10))
print()

# ------------------------------------------------------------------------
# Question 9
print("Question 9")

# Compute the total stats for yellow cabs
yellow_total_passengers = Yellow_stats_df['total_passengers'].sum()
yellow_total_distance = Yellow_stats_df['total_distance'].sum()
yellow_total_fare = Yellow_stats_df['total_fare'].sum()
yellow_total_fuel_cost = Yellow_stats_df['total_fuel_cost'].sum()

# Compute the total stats for green cabs
green_total_passengers = Green_stats_df['total_passengers'].sum()
green_total_distance = Green_stats_df['total_distance'].sum()
green_total_fare = Green_stats_df['total_fare'].sum()
green_total_fuel_cost = Green_stats_df['total_fuel_cost'].sum()

# Print the results
print("Yellow cabs:")
print(f"Total number of passengers travelled: {yellow_total_passengers}")
print(f"Total distance travelled: {yellow_total_distance:.2f} kms")
print(f"Total fare: ${yellow_total_fare:.2f}")
print(f"Total fuel cost: ${yellow_total_fuel_cost:.2f}")

print("\nGreen cabs:")
print(f"Total number of passengers travelled: {green_total_passengers}")
print(f"Total distance travelled: {green_total_distance:.2f} kms")
print(f"Total fare: ${green_total_fare:.2f}")
print(f"Total fuel cost: ${green_total_fuel_cost:.2f}")
print()

# ------------------------------------------------------------------------
# Question 10a
print("Question 10a")

# Sort the pickup zones by total fare in descending order and get the top 10 zones for yellow cabs
top10_yellow_pickup_zones = Yellow_stats_df.sort_values(by='total_fare', ascending=False).head(10)

# Reset the index to start from 1 instead of 0
top10_yellow_pickup_zones.reset_index(drop=True, inplace=True)
top10_yellow_pickup_zones.index += 1

# Sort the pickup zones by total fare in descending order and get the top 10 zones for green cabs
top10_green_pickup_zones = Green_stats_df.sort_values(by='total_fare', ascending=False).head(10)

# Reset the index to start from 1 instead of 0
top10_green_pickup_zones.reset_index(drop=True, inplace=True)
top10_green_pickup_zones.index += 1

# Display the top 10 pickup zones for yellow and green cabs
print("Top 10 pickup zones for yellow cabs:")
print(top10_yellow_pickup_zones.to_string(header=True, index=True, col_space=10))

print("\nTop 10 pickup zones for green cabs:")
print(top10_green_pickup_zones.to_string(header=True, index=True, col_space=10))
print()

# ------------------------------------------------------------------------

# Question 10b
print("Question 10b")

# (After you have created your Yellow_stats_df and Green_stats_df as mentioned in the previous parts of your question...)

# Define a function to create bar charts for the specified statistics
def create_bar_charts(df, color):
    fig, axes = plt.subplots(2, 2, figsize=(15, 10))
    fig.suptitle(f'Top 10 Pickup Zones for {color.capitalize()} Cabs')

    # Total number of passengers travelled
    df.plot(kind='bar', x='pickup_zone', y='total_passengers', ax=axes[0, 0])
    axes[0, 0].set_title('Total Number of Passengers Travelled')

    # Total distance travelled
    df.plot(kind='bar', x='pickup_zone', y='total_distance', ax=axes[0, 1])
    axes[0, 1].set_title('Total Distance Travelled (in km)')

    # Total fare
    df.plot(kind='bar', x='pickup_zone', y='total_fare', ax=axes[1, 0])
    axes[1, 0].set_title('Total Fare (in $)')

    # Number of trips made
    df.plot(kind='bar', x='pickup_zone', y='num_trips', ax=axes[1, 1])
    axes[1, 1].set_title('Number of Trips Made')

    # Adjust layout to prevent labels from overlapping
    plt.tight_layout()
    plt.subplots_adjust(top=0.95)

    plt.show()

# Create bar charts for the top 10 pickup zones for yellow and green cabs
print("Bar Graph for Yellow Cars:")
create_bar_charts(top10_yellow_pickup_zones, 'yellow')
print("Bar Graph for Green Cars:")
create_bar_charts(top10_green_pickup_zones, 'green')
print()

# ------------------------------------------------------------------------
# Question 10c
print("Question 10c")
# Assuming that we're referring to the top 10 pickup zones (which is not explicitly stated in the question)

# Define a function to create pie charts for the specified statistics
def create_pie_charts(df, color):
    fig, axes = plt.subplots(1, 2, figsize=(14, 7))

    # Pie chart for total fare cost
    df.plot(kind='pie', y='total_fare', labels=df['pickup_zone'], autopct='%1.1f%%', ax=axes[0], legend=False, fontsize=10)
    axes[0].set_ylabel('')
    axes[0].set_title('Total Fare Cost by Zone')

    # Pie chart for total fuel cost
    df.plot(kind='pie', y='total_fuel_cost', labels=df['pickup_zone'], autopct='%1.1f%%', ax=axes[1], legend=False, fontsize=10)
    axes[1].set_ylabel('')
    axes[1].set_title('Total Fuel Cost by Zone')

    # Set the main title for the whole figure
    fig.suptitle(f'{color.capitalize()} Cabs: Top 10 Pickup Zones', fontsize=16)

    # Display the pie charts
    plt.show()

# Create pie charts for the top 10 pickup zones for yellow and green cabs
create_pie_charts(top10_yellow_pickup_zones, 'yellow')
create_pie_charts(top10_green_pickup_zones, 'green')
print()
