'''
Now that we have looked at all three data files, we will look at how to align the three time-series to each other.
Write a Python script that will create a figure with three subplots that contain
- the x-position in Unity as a function of time;
- the eye position x as a function of time, and
- the broadband signal as a function of time.
Remember to add the markers to each of the subplots like you did previously.
'''

import numpy as np
import matplotlib.pyplot as plt
import hickle
import pandas as pd
from neo.io import BlackrockIO

# script running in picasso/20181105
# Load Unity data
data_unity = np.loadtxt("session01/RawData_T1-400/session_1_5112018105323.txt", skiprows=14)
uind = np.arange(300)
ut = np.cumsum(data_unity[uind,1])

# Load and process eye tracking
samples = pd.read_pickle('samples.pkl')
events = pd.read_pickle('events.pkl')
messages = pd.read_pickle('messages.pkl')
esr = 1000
samples['time'] = samples['time']/esr
events[['start', 'end']] = events[['start', 'end']]/esr
messages[['trialid_time','Cue_time','End_time']] = messages[['trialid_time','Cue_time','End_time']]/esr

eind = np.arange(15000)
ex = samples['gx_left'][eind]
et_eye = samples['time'][eind]
ex[ex>1920] = np.nan
ex[ex<0] = np.nan

# Load Blackrock data
reader = BlackrockIO('session01/181105_Block1.nev')
ev_rawtimes, _, ev_markers = reader.get_event_timestamps()
data_broadband = hickle.load('session01/data_raw6.hkl')
eind = np.arange(500000)
ev = data_broadband[eind]
et = [x for x in range(len(ev))]
et = [x/30000 for x in et]

plt.figure()

# Subplot 1: Unity X-Position vs. Time
plt.subplot(3, 1, 1)
plt.plot(ut,data_unity[uind,2])
plt.xlabel('Time (s)')
plt.ylabel('X-Pos')
mi = data_unity[uind,0].nonzero()
xl = plt.xlim()
yl = plt.ylim()
t2 = ut[mi[0][1:]]
pt2 = np.kron(np.ones((2,1)),t2)
py2 = np.kron(np.ones((np.size(pt2,1),1)),yl).transpose()
plt.plot(pt2,py2)

# align subplot 1
start = (pt2[0][0] - xl[0]) / (xl[1] - xl[0]) # Ratio of first event to left bound
end = (xl[1] - pt2[0][2]) / (xl[1] - xl[0]) # Ratio of last event to right bound
ratio = (xl[1] - xl[0])

# Subplot 2: Eye Position X vs. Time
plt.subplot(3, 1, 2)
plt.plot(et_eye, ex)
plt.ylabel("Eye Position X")
xl = plt.xlim()
yl = plt.ylim()
xval1 = messages['trialid_time'][0]
plt.plot([xval1,xval1],yl)
xval = messages['Cue_time'][0]
plt.plot([xval,xval],yl)
xval2 = messages['End_time'][0]
plt.plot([xval2,xval2],yl)
xleft = (xval1 - (ratio / (xl[1] - xl[0])) * start * (xl[1] - xl[0]))
xright = ((xval2 + (ratio / (xl[1] - xl[0])) * end * (xl[1] - xl[0])))
plt.xlim(xleft, xright)

# Subplot 3: Broadband Signal vs. Time
plt.subplot(3, 1, 3)
plt.plot(et, ev)
plt.xlabel("Time (s)")
plt.ylabel("Voltage (uV)")
yl = plt.ylim()
xval1 = ev_rawtimes[2]/30000
plt.plot([xval1,xval1],yl)
xval = ev_rawtimes[4]/30000
plt.plot([xval,xval],yl)
xval2 = ev_rawtimes[6]/30000
plt.plot([xval2,xval2],yl)
xleft = (xval1 - (ratio / (xl[1] - xl[0])) * start * (xl[1] - xl[0]))
xright = ((xval2 + (ratio / (xl[1] - xl[0])) * end * (xl[1] - xl[0])))
plt.xlim(xleft, xright)
