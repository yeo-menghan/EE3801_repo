import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

plt.figure()
plt.subplot(3,1,1)
plt.plot(ut,data[uind,2])
plt.xlabel('Time (s)')
plt.ylabel('X-Pos')
mi = data[uind,0].nonzero()
yl = plt.ylim()
t2 = ut[mi[0][1:]]
pt2 = np.kron(np.ones((2,1)),t2)
py2 = np.kron(np.ones((np.size(pt2,1),1)),yl).transpose()
plt.plot(pt2,py2)

plt.subplot(3,1,2)
plt.plot(ut,data[uind,3])
plt.xlabel('Time (s)')
plt.ylabel('Y-Pos')
yl = plt.ylim()
py2 = np.kron(np.ones((np.size(pt2,1),1)),yl).transpose()
plt.plot(pt2,py2)

plt.subplot(3,1,3)
plt.plot(ut,data[uind,4])
plt.xlabel('Time (s)')
plt.ylabel('Orientation')
yl = plt.ylim()
py2 = np.kron(np.ones((np.size(pt2,1),1)),yl).transpose()
plt.plot(pt2,py2)
