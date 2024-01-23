# Import necessary libraries/modules
import hickle  # For loading data from a file
from neo.io import BlackrockIO  # For reading Blackrock data files
import matplotlib.pyplot as plt  # For creating plots
import numpy as np  # For numerical operations

# Load data from a file named 'data_raw6.hkl' using hickle
data = hickle.load('data_raw6.hkl')

# Initialize a BlackrockIO reader to read data from '181105_Block1.nev'
reader = BlackrockIO('181105_Block1.nev')

# Retrieve event timestamps from the Blackrock data file
ev_rawtimes, _, ev_markers = reader.get_event_timestamps()

# Create a matplotlib figure for plotting
plt.figure()

# Create an array 'eind' containing values from 0 to 499999
eind = np.arange(500000)

# Extract a subset of the 'data' using 'eind' and assign it to 'ev'
ev = data[eind]

# Create an array 'et' representing time points in seconds
et = [x for x in range(len(ev))]  # Create a time axis
et = [x/30000 for x in et]  # Convert time axis to seconds

# Plot the data on the graph with time on the x-axis and voltage on the y-axis
plt.plot(et, ev)
plt.xlabel("Time (s)")  # Label for the x-axis
plt.ylabel("Voltage (uV)")  # Label for the y-axis

# Get the y-axis limits of the plot
yl = plt.ylim()

# Plot vertical lines at specific time points based on 'ev_rawtimes'
xval = ev_rawtimes[2]/30000
plt.plot([xval, xval], yl)  # Vertical line at the third event time
xval = ev_rawtimes[4]/30000
plt.plot([xval, xval], yl)  # Vertical line at the fifth event time
xval = ev_rawtimes[6]/30000
plt.plot([xval, xval], yl)  # Vertical line at the seventh event time
