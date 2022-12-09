#-*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import matplotlib.cm
from matplotlib.lines import Line2D
import matplotlib.gridspec as gridspec
import numpy as np
import operator
import os
from matplotlib.lines import Line2D
from matplotlib.cbook import get_sample_data
from matplotlib.offsetbox import (TextArea, DrawingArea, OffsetImage, AnnotationBbox)
import matplotlib.image as mpimg
import matplotlib.gridspec as gridspec

PATH = os.getcwd()+"/"

plt.rcParams['text.latex.preamble']=[r'\boldmath']
params = {'legend.fontsize': 80}
plt.rcParams.update(params)
plt.rcParams['ytick.labelsize'] = 90
plt.rcParams['xtick.labelsize'] = 90
plt.rcParams['hatch.linewidth'] = 3
plt.rcParams['xtick.major.pad']='50'
plt.rcParams['ytick.major.pad']='50'

a = list(range(1,7))
xtick = []
for i in range(2015,2021):
	xtick.append(i)

fig3 = plt.figure(figsize=(120,50))
gs = gridspec.GridSpec(1, 4)
ax1 = fig3.add_subplot(gs[0,:2])
ax2 = fig3.add_subplot(gs[0,2:])

low_end_js =  [2.6, 4.93, 4.78, 4.62, 5.93, 7.98]
high_end_js = [2.67, 3.11, 2.48, 1.59, 1.67, 1.88]

phonesNames = ["Samsung\nGalaxy S20","Nokia C1","Samsung\nGalaxy S10+","Alcatel 1C","Huawei\nMate 20 Pro","Xiamoi\nRedmi Go","Samsung\nGalaxy S8+","Huawei P9","Huawei Y3II","Samsung\nGalaxy S6 edge","HTC\nDesire 520"]
phones = ["phones/2020_HE.png","phones/2020_LE.png","phones/2019_HE.png","phones/2019_LE.png","phones/2018_HE.png","phones/2018_LE.png","phones/2017_HE.png","phones/2016_HE.png","phones/2016_LE.png","phones/2015_HE.png","phones/2015_LE.png"]

phonesXY = [(5,-1),(5,1),(4,-1),(4,1),(3,-1),(3,1),(2,-1),(1,-1),(1,1),(0,-1),(0,1)]
arrowsXY = [(5,1.8),(5,8.1),(4,1.6),(4,6),(3,1.5),(3,4.7),(2,2.4),(1,3),(1,5),(0,2.5),(0,2.7)]

for i in range(len(phones)):
    angle = "angle3,angleA=-45,angleB=-90"
    fn = get_sample_data(PATH+phones[i], asfileobj=False)
    arr_img = plt.imread(fn, format='png')

    imagebox = OffsetImage(arr_img, zoom=0.5)
    imagebox.image.axes = ax1

    if phonesXY[i][1] < 0:
        ab = AnnotationBbox(imagebox, xy=arrowsXY[i],
                xybox=(phonesXY[i][0],0),
                xycoords='data',
                pad=0.01,
                bboxprops =dict(color='none', edgecolor='none'),
                arrowprops=dict(arrowstyle="-|>, head_width=0.3, head_length=1.0", lw=15, fc='black', ls='-',
                    connectionstyle=angle))
        if "edge" in phonesNames[i]:
            ax1.text(phonesXY[i][0]-0.5, -0.6, phonesNames[i], fontsize=70, rotation=90)
        elif "\n" in phonesNames[i]:
            ax1.text(phonesXY[i][0]-0.48, -0.6, phonesNames[i], fontsize=70, rotation=90)
        else:
            ax1.text(phonesXY[i][0]-0.38, -0.6, phonesNames[i], fontsize=70, rotation=90)
    else:
        ab = AnnotationBbox(imagebox, xy=arrowsXY[i],
                xybox=(phonesXY[i][0],10),
                xycoords='data',
                pad=0.01,
                bboxprops =dict(color='none', edgecolor='none'),
                arrowprops=dict(arrowstyle="-|>, head_width=0.3, head_length=1.0", lw=15, fc='black', ls='-',
                    connectionstyle=angle))
        if "\n" in phonesNames[i]:
            ax1.text(phonesXY[i][0]-0.5, 9.3, phonesNames[i], fontsize=70, rotation=90)
        else:
            ax1.text(phonesXY[i][0]-0.35, 9.3, phonesNames[i], fontsize=70, rotation=90)
    ax1.add_artist(ab)

ax1.plot(range(6),high_end_js,marker="s", markersize=50, color="tab:blue",label="High-end phone",lw=20)
ax1.plot(range(6),low_end_js, marker="o", markersize=50, color = "tab:red",label="Low-end phone",lw=20)
ax1.set_xticks(range(0,6))
ax1.set_xticklabels(xtick, rotation=90)

plt.rcParams['patch.linewidth'] = 5
legend=ax1.legend(loc="center right", bbox_to_anchor=(0.95,0.4))
legend.get_frame().set_edgecolor("black")

ax1.set_ylim([-1.5,12])
ax1.set_xlim([-1,6])
ax1.set_ylabel("Time (seconds)", fontsize=100, labelpad=50)
ax1.set_xlabel("Year corresponding to the evaluated websites' versions", fontsize=100, labelpad=80)

ttl = ax1.set_title('Time spent processing JavaScript (seconds)\n', fontsize=100)
# ttl.set_position([.5, -1.05])
ax1.grid(color='#DCDCDC', linewidth=0.01)

plt.gcf().text(0.01, 0.965, "a", fontsize=170, weight='bold')
plt.gcf().text(0.51, 0.965, "b", fontsize=170, weight='bold')


low_end_plt =  [22,44,45,46,48,49]
high_end_plt = [27,37,34,19,20,20]

low_end_js =  [22,44,45,46,48,49]
high_end_js = [27,37,34,19,20,20]

map_object = map(operator.sub, high_end_plt, high_end_js)
high_end_plt = list(map_object)

map_object = map(operator.sub, low_end_plt, low_end_js)
low_end_plt = list(map_object)

data_lowend = [low_end_js,low_end_js]
data_highend = [high_end_js,high_end_js]

category_labels = xtick
series_labels = ['Low-end phone',"High-end phone"]
colors=['tab:red', 'tab:red']
colors2=['tab:red', 'tab:blue']

plt.rcParams['hatch.linewidth'] = 5
plt.rcParams.update({'hatch.color': 'orange'})

def shift2 (a):
    return a+0.17

ny = len(data_highend[0])
ind = list(map(shift2, range(ny)))

axes = []
cum_size = np.zeros(ny)

data_highend = np.array(data_highend)

for i, row_data in enumerate(data_highend):
    if i == 0:
        axes.append(ax2.bar(ind, row_data, 0.3, bottom=cum_size, lw=10, 
                        label=series_labels[1], color="none", hatch='/',edgecolor="tab:blue"))
    cum_size += row_data

def shift (a):
	return a-0.17

ny = len(data_lowend[0])
ind = list(map(shift, range(ny)))

axes = []
cum_size = np.zeros(ny)

data_lowend = np.array(data_lowend)

for i, row_data in enumerate(data_lowend):
    if i == 0:
        axes.append(ax2.bar(ind, row_data, 0.3, bottom=cum_size, lw=10,
                        label=series_labels[0], color="none", hatch='/', edgecolor="tab:red"))
        cum_size += row_data

ax2.set_xticks(range(0,6))
ax2.set_xticklabels(xtick, rotation=90)
ax2.grid(color='#DCDCDC', linewidth=0.01)
ax2.set_ylim(0,100)

plt.rcParams['patch.linewidth'] = 5
legend=ax2.legend(loc="best", bbox_to_anchor=(0.95,0.95))
legend.get_frame().set_edgecolor("black")

ttl = ax2.set_title('Percentage of page load time spent on JavaScript processing\n', fontsize=100)

ax2.set_ylabel("Percentage", fontsize=100)
ax2.set_xlabel("Year corresponding to the evaluated websites' versions", fontsize=100, labelpad=80)
ax2.set_xticks(range(0,6))
ax2.set_xticklabels(xtick, rotation=90)
plt.subplots_adjust(left=0.04, right=0.99, bottom=0.13, top=0.93)
plt.savefig("figures/Time_machine.pdf")