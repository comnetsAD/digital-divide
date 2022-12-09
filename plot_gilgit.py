
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import statsmodels.stats.api as sms


mean_plt = {'original': [62.04745408163265, 53.27309500000001, 65.54677551020409, 64.90196428571429], 'combined': [19.985163265306124, 26.317239999999998, 20.843683673469382, 25.291132653061226]}
ci_plt = {'original': np.array([[54.94904541355357, 69.14586274971174], [46.533855573544265, 60.012334426455745], [57.589425929420884, 73.50412509098729], [56.71539228781552, 73.08853628361305]]), 'combined': np.array([[17.487400276680525, 22.482926253931723], [23.27337785899261, 29.361102141007386], [18.44313628795397, 23.24423105898481], [22.048928060731786, 28.533337245390666]])}
yerr_plt = {"original": np.c_[mean_plt["original"]-ci_plt["original"][:,0],ci_plt["original"][:,1]-mean_plt["original"] ].T, "combined": np.c_[mean_plt["combined"]-ci_plt["combined"][:,0],ci_plt["combined"][:,1]-mean_plt["combined"] ].T}

mean_plt_ad = [12.899108695652172]
ci_plt_ad = np.array([(11.201428575438166, 14.596788815866189)])
yerr_plt_ad = np.c_[mean_plt_ad-ci_plt_ad[:,0],ci_plt_ad[:,1]-mean_plt_ad ].T

mean_si = {'original': [21.250448979591834, 18.56923, 22.436617346938778, 22.858535714285715], 'combined': [8.264244897959184, 9.818005000000001, 8.59608163265306, 9.579438775510203]}
ci_si = {'original': np.array([(17.845296976809284, 24.655600982374384), (15.900375663167539, 21.238084336832465), (18.56902876422966, 26.304205929647896), (18.865279944741395, 26.851791483830034)]), 'combined': np.array([(7.3268124704962245, 9.201677325422144), (8.686174152699508, 10.949835847300495), (7.6194441468790375, 9.572719118427084), (8.512296864407789, 10.646580686612621)])}
yerr_si = {"original": np.c_[mean_si["original"]-ci_si["original"][:,0],ci_si["original"][:,1]-mean_si["original"] ].T, "combined": np.c_[mean_si["combined"]-ci_si["combined"][:,0],ci_si["combined"][:,1]-mean_si["combined"] ].T}

mean_si_ad = [5.33641304347826]
ci_si_ad = np.array([(4.422923492222058, 6.249902594734463)])
yerr_si_ad = np.c_[mean_si_ad-ci_si_ad[:,0],ci_si_ad[:,1]-mean_si_ad ].T

mean_size = {'original': [0.5416346485148515, 0.5920016138613861, 0.5449163600000001, 0.47196729000000004], 'combined': [0.28073489, 0.28863312999999996, 0.28513377, 0.28970081]}
ci_size = {'original': np.array([(0.4575188711836862, 0.6257504258460169), (0.49414990239739015, 0.6898533253253819), (0.45663653181721436, 0.6331961881827859), (0.3936181333395371, 0.550316446660463)]), 'combined': np.array([(0.21624879427429727, 0.34522098572570276), (0.22093641933963123, 0.35632984066036866), (0.22010507560403025, 0.35016246439596976), (0.22344288267201812, 0.35595873732798194)])}
yerr_size = {"original": np.c_[mean_size["original"]-ci_size["original"][:,0],ci_size["original"][:,1]-mean_size["original"] ].T, "combined": np.c_[mean_size["combined"]-ci_size["combined"][:,0],ci_size["combined"][:,1]-mean_size["combined"] ].T}

mean_size_ad = [0.6835778977272727]
ci_size_ad = np.array([(0.5841580249960046, 0.7829977704585409)])
yerr_size_ad = np.c_[mean_size_ad-ci_size_ad[:,0],ci_size_ad[:,1]-mean_size_ad ].T


mean_js = {'original': [5.145960396039603, 5.076405940594058, 5.00457, 4.10149], 'combined': [2.0689100000000002, 1.9780099999999998, 2.1123199999999995, 1.9871000000000003]}
ci_js = {'original': np.array([(4.226381022181988, 6.065539769897221), (3.9106783199734325, 6.242133561214685), (4.046736971972795, 5.962403028027202), (3.2343631870454606, 4.968616812954539)]), 'combined': np.array([(1.499694604504762, 2.6381253954952393), (1.4311086499450392, 2.5249113500549605), (1.5417888803819175, 2.6828511196180815), (1.441000350811215, 2.5331996491887856)])}
yerr_js = {"original": np.c_[mean_js["original"]-ci_js["original"][:,0],ci_js["original"][:,1]-mean_js["original"] ].T, "combined": np.c_[mean_js["combined"]-ci_js["combined"][:,0],ci_js["combined"][:,1]-mean_js["combined"] ].T}

mean_js_ad = [1.408967391304348]
ci_js_ad = np.array([(1.087259658088369, 1.7306751245203267)])
yerr_js_ad = np.c_[mean_js_ad-ci_js_ad[:,0],ci_js_ad[:,1]-mean_js_ad ].T


plt.rcParams['text.latex.preamble']=[r'\boldmath']
params = {
          'legend.fontsize': 80,
          }
plt.rcParams.update(params)

plt.rcParams['ytick.labelsize'] = 90
plt.rcParams['xtick.labelsize'] = 90
plt.rcParams['hatch.linewidth'] = 3
plt.rcParams['xtick.major.pad']='50'
plt.rcParams['ytick.major.pad']='50'
plt.rcParams['hatch.linewidth'] = 5

fig3 = plt.figure(figsize=(120,70))

gs = gridspec.GridSpec(3, 4, height_ratios=[500,1,500])

mpp_colors = [['#2b83ba', '#2b83ba'],['#FAD933', '#FAD933']]
mpp_edges = [["black","black"],["black","black"]]
axis = [[1.0,2.5,4.0,5.5],[0.5,2,3.5,5.0]]

ax1 = fig3.add_subplot(gs[0,:2])
ax2 = fig3.add_subplot(gs[0,2:4])
ax3 = fig3.add_subplot(gs[2,:2])
ax4 = fig3.add_subplot(gs[2,2:4])

ax1.bar(axis[0], height=mean_plt["combined"], width = 0.4, yerr=yerr_plt["combined"], error_kw=dict(lw=10, capsize=70, capthick=10), edgecolor=mpp_edges[0], color=mpp_colors[0], zorder=10,)
ax1.bar(axis[1], height=mean_plt["original"], width = 0.4, yerr=yerr_plt["original"], error_kw=dict(lw=10, capsize=70, capthick=10), edgecolor=mpp_edges[1], color=mpp_colors[1], zorder=10)
ax1.bar(-.5, height=mean_plt_ad, width=0.4, yerr=yerr_plt_ad, error_kw=dict(lw=10, capsize=70, capthick=10),edgecolor="black", color="#e78ac3", zorder=10)

print (sum(mean_plt["combined"])/4)
print (sum(mean_plt["original"])/4)

ax1.set_xticks([-0.5, 0.75, 2.25,3.75,5.25])
ax1.set_xticklabels(["Dubai", "Taus","Hundur","Sherqilla","Puniyal"])

ax1.grid(color='#DCDCDC', linewidth=0.01, zorder=0)
legend = ax1.legend(['Lite-Web (Gilgit)','Original (Gilgit)','Original (Dubai)'], loc="upper left")
legend.get_frame().set_edgecolor("black")

pos = [0.75, 2.25,3.75,5.25]
txt_pos = [0.165,0.26,0.356,0.45]

for i in range(4):
	ax1.arrow(pos[i], mean_plt["original"][i]-3, 0.0, -1*(mean_plt["original"][i]-mean_plt["combined"][i])+6, fc="k",ec="k",head_width=0.05, head_length=2, lw=8, zorder=10)
	ax1.arrow(pos[i], mean_plt["combined"][i]+3, 0.0, (mean_plt["original"][i]-mean_plt["combined"][i])-6, fc="k",ec="k",head_width=0.05, head_length=2, lw=8, zorder=10)
	plt.gcf().text(txt_pos[i], 0.76, "{:.0f}%".format((mean_plt["original"][i]-mean_plt["combined"][i])/mean_plt["original"][0]*100.0), fontsize=90, weight='bold')

ax1.set_ylabel('Time (seconds)', fontsize=100, labelpad=80)
ax1.set_ylim([0,88])
ttl = ax1.set_title('Page load time', fontsize=100)
ttl.set_position([.5, 1.02])


ax2.bar(axis[0], height=mean_si["combined"], width = 0.4, yerr=yerr_si["combined"], error_kw=dict(lw=10, capsize=70, capthick=10), edgecolor=mpp_edges[0], color=mpp_colors[0], zorder=10,)
ax2.bar(axis[1], height=mean_si["original"], width = 0.4, yerr=yerr_si["original"], error_kw=dict(lw=10, capsize=70, capthick=10), edgecolor=mpp_edges[1], color=mpp_colors[1], zorder=10)
ax2.bar(-.5, height=mean_si_ad, width=0.4, yerr=yerr_si_ad, error_kw=dict(lw=10, capsize=70, capthick=10),  edgecolor="black", color="#e78ac3", zorder=10)

ax2.set_xticks([-0.5, 0.75, 2.25,3.75,5.25])
ax2.set_xticklabels(["Dubai","Taus","Hundur","Sherqilla","Puniyal"])
ax2.set_ylim([0,31])

ax2.set_ylabel('Time (seconds)', fontsize=100, labelpad=80)
ttl = ax2.set_title('Speed index', fontsize=100)
ttl.set_position([.5, 1.02])

ax2.grid(color='#DCDCDC', linewidth=0.01, zorder=0)
legend = ax2.legend(['Lite-Web (Gilgit)','Original (Gilgit)','Original (Dubai)'], loc="upper left")
legend.get_frame().set_edgecolor("black")

pos = [0.75, 2.25,3.75,5.25]
txt_pos = [0.165,0.26,0.356,0.45]

for i in range(4):
	ax2.arrow(pos[i], mean_si["original"][i]-1, 0.0, -1*(mean_si["original"][i]-mean_si["combined"][i])+2, fc="k",ec="k",head_width=0.05, head_length=0.75, lw=8, zorder=10)
	ax2.arrow(pos[i], mean_si["combined"][i]+1, 0.0, (mean_si["original"][i]-mean_si["combined"][i])-2, fc="k",ec="k",head_width=0.05, head_length=0.75, lw=8, zorder=10)
	plt.gcf().text(txt_pos[i]+0.5, 0.76, "{:.0f}%".format((mean_si["original"][i]-mean_si["combined"][i])/mean_si["original"][0]*100.0), fontsize=90, weight='bold')


ax3.bar(axis[0], height=mean_js["combined"], width = 0.4, yerr=yerr_js["combined"], error_kw=dict(lw=10, capsize=70, capthick=10), edgecolor=mpp_edges[0], color=mpp_colors[0], zorder=10,)
ax3.bar(axis[1], height=mean_js["original"], width = 0.4, yerr=yerr_js["original"], error_kw=dict(lw=10, capsize=70, capthick=10), edgecolor=mpp_edges[1], color=mpp_colors[1], zorder=10)
ax3.bar(-.5, height=mean_js_ad, width=0.4, yerr=yerr_js_ad, error_kw=dict(lw=10, capsize=70, capthick=10),  edgecolor="black", color="#e78ac3", zorder=10)

ax3.set_xticks([-0.5, 0.75, 2.25,3.75,5.25])
ax3.set_xticklabels(["Dubai","Taus","Hundur","Sherqilla","Puniyal"])

ax3.set_ylabel('Time (seconds)', fontsize=100, labelpad=80)
ttl = ax3.set_title('JavaScript processing time', fontsize=100)
ttl.set_position([.5, 1.02])

ax3.grid(color='#DCDCDC', linewidth=0.01, zorder=0)
legend = ax3.legend(['Lite-Web (Gilgit)','Original (Gilgit)','Original (Dubai)'], loc="best")
legend.get_frame().set_edgecolor("black")


pos = [0.75, 2.25,3.75,5.25]
txt_pos = [0.165,0.26,0.356,0.45]

for i in range(4):
	ax3.arrow(pos[i], mean_js["original"][i]-0.2, 0.0, -1*(mean_js["original"][i]-mean_js["combined"][i])+0.4, fc="k",ec="k",head_width=0.05, head_length=0.15, lw=8, zorder=10)
	ax3.arrow(pos[i], mean_js["combined"][i]+0.2, 0.0, (mean_js["original"][i]-mean_js["combined"][i])-0.4, fc="k",ec="k",head_width=0.05, head_length=0.15, lw=8, zorder=10)
	plt.gcf().text(txt_pos[i], 0.25, "{:.0f}%".format((mean_js["original"][i]-mean_js["combined"][i])/mean_js["original"][0]*100.0), fontsize=90, weight='bold')

ax4.bar(axis[0], height=mean_size["combined"], width = 0.4, yerr=yerr_size["combined"], error_kw=dict(lw=10, capsize=70, capthick=10), edgecolor=mpp_edges[0], color=mpp_colors[0], zorder=10,)
ax4.bar(axis[1], height=mean_size["original"], width = 0.4, yerr=yerr_size["original"], error_kw=dict(lw=10, capsize=70, capthick=10), edgecolor=mpp_edges[1], color=mpp_colors[1], zorder=10)
ax4.bar(-.5, height=mean_size_ad, width=0.4, yerr=yerr_size_ad, error_kw=dict(lw=10, capsize=70, capthick=10),  edgecolor="black", color="#e78ac3", zorder=10)

print (sum(mean_size["combined"])/4)
print (sum(mean_size["original"])/4)


ax4.set_xticks([-0.5, 0.75, 2.25,3.75,5.25])
ax4.set_xticklabels(["Dubai","Taus","Hundur","Sherqilla","Puniyal"])

ax4.set_ylabel('Size (MB)', fontsize=100, labelpad=80)
ttl = ax4.set_title('Page size', fontsize=100)
ttl.set_position([.5, 1.02])

ax4.grid(color='#DCDCDC', linewidth=0.01, zorder=0)
legend = ax4.legend(['Lite-Web (Gilgit)','Original (Gilgit)','Original (Dubai)'], loc="best")
legend.get_frame().set_edgecolor("black")

pos = [0.75, 2.25,3.75,5.25]
txt_pos = [0.165,0.26,0.356,0.45]

for i in range(4):
	ax4.arrow(pos[i], mean_size["original"][i]-0.02, 0.0, -1*(mean_size["original"][i]-mean_size["combined"][i])+0.04, fc="k",ec="k",head_width=0.05, head_length=0.02, lw=8, zorder=10)
	ax4.arrow(pos[i], mean_size["combined"][i]+0.02, 0.0, (mean_size["original"][i]-mean_size["combined"][i])-0.04, fc="k",ec="k",head_width=0.05, head_length=0.02, lw=8, zorder=10)
	plt.gcf().text(txt_pos[i]+0.5, 0.25, "{:.0f}%".format((mean_size["original"][i]-mean_size["combined"][i])/mean_size["original"][0]*100.0), fontsize=90, weight='bold')

plt.gcf().text(0.02, 0.97, "a", fontsize=170, weight='bold')
plt.gcf().text(0.52, 0.97, "b", fontsize=170, weight='bold')
plt.gcf().text(0.02, 0.49, "c", fontsize=170, weight='bold')
plt.gcf().text(0.52, 0.49, "d", fontsize=170, weight='bold')


fig3.tight_layout(pad=5.0)
plt.savefig("figures/gilgit_phase1.pdf")
