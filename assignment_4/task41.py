import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load eye tracking data from pickle files
samples = pd.read_pickle('samples.pkl')
events = pd.read_pickle('events.pkl')
messages = pd.read_pickle('messages.pkl')

# Extract the first 15000 data points for plotting
eind = np.arange(15000)
ex = samples['gx_left'][eind]  # X-coordinate of the left eye
ey = samples['gy_left'][eind]  # Y-coordinate of the left eye
et = samples['time'][eind]     # Timestamps

# Create a new Matplotlib figure for plotting
plt.figure()

# Remove data points that fall outside the monitor's range
ex[ex > 1920] = np.nan
ex[ex < 0] = np.nan
ey[ey > 1080] = np.nan
ey[ey < 0] = np.nan

# Set up the first subplot (top) in a 2x1 grid
plt.subplot(2, 1, 1)

# Plot Eye Position X against time
plt.plot(et, ex)
plt.ylabel("Eye Position X")  # Label the y-axis
xl = plt.xlim()  # Store x-axis limits for both Eye Position X and Eye Position Y
yl = plt.ylim()  # Store y-axis limits

# Add markers to indicate specific time points on the plot
xval = messages['trialid_time'][0]
plt.plot([xval, xval], yl)  # Vertical line for trial start
xval = messages['Cue_time'][0]
plt.plot([xval, xval], yl)  # Vertical line for cue presentation
xval = messages['End_time'][0]
plt.plot([xval, xval], yl)  # Vertical line for trial end

# Set up the second subplot (bottom) in a 2x1 grid
plt.subplot(2, 1, 2)

# Plot Eye Position Y against time
plt.plot(et, ey)
plt.xlabel("Time (s)")  # Label the x-axis
plt.ylabel("Eye Position Y")  # Label the y-axis
plt.xlim(xl)  # Set x-axis limits to match the first subplot
yl = plt.ylim()  # Store y-axis limits

# Add markers to indicate specific time points on the plot
xval = messages['trialid_time'][0]
plt.plot([xval, xval], yl)  # Vertical line for trial start
xval = messages['Cue_time'][0]
plt.plot([xval, xval], yl)  # Vertical line for cue presentation
xval = messages['End_time'][0]
plt.plot([xval, xval], yl)  # Vertical line for trial end
