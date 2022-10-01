from obspy import read
import matplotlib.pyplot as plt

st = read("C:\Users\Constantinos Ar\Desktop\NASA Space Apps\Moonquake Map\Data Analysis\data\xa.s15.00.mh1.1975.001.0.mseed")
tr = st[0]

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.plot(tr.times("matplotlib"), tr.data, "b-")
ax.xaxis_date()
fig.autofmt_xdate()
plt.show() 