import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import pandas as pd
samples = pd.read_pickle('samples.pkl')
events = pd.read_pickle('events.pkl')
messages = pd.read_pickle('messages.pkl')
samples.columns
samples[['time','gx_left','gy_left']][0:9]
events[['type','start','end']][0:9]

# convert the relevant data from sample numbers to timestamps using the sampling rate of 1,000 samples per second
esr = 1000
samples['time'] = samples['time']/esr
events[['start','end']] = events[['start','end']]/esr
messages = messages/esr

# extract the first 15000 points in samples to plot
eind = np.arange(15000)
ex = samples['gx_left'][eind]
et = samples['time'][eind]
plt.figure()
plt.plot(et,ex)
plt.xlabel('Time (s)')
plt.ylabel('Eye Position X')

# remove points outside the range of the monitor
ex[ex>1920] = np.nan
ex[ex<0] = np.nan

# remove points outside the range of the monitor
ax = plt.gca()
ax.clear()
plt.plot(et,ex)
plt.xlabel('Time (s)')
plt.ylabel('Eye Position X')

# add plots of the first event
yl = plt.ylim()
xval = events['start'][0]
plt.plot([xval,xval],yl)
xval = events['end'][0]
plt.plot([xval,xval],yl)

# plot the start and end of the second event (saccade)
xval = events['start'][1]
plt.plot([xval,xval],yl)
xval = events['end'][1]
plt.plot([xval,xval],yl)

# add markers
xval = messages['trialid_time'][0]
plt.plot([xval,xval],yl)
xval = messages['Cue_time'][0]
plt.plot([xval,xval],yl)
xval = messages['End_time'][0]
plt.plot([xval,xval],yl)
