import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import pandas as pd
import seaborn as sns
import textwrap
from scipy import stats

plt.rcParams['text.latex.preamble']=[r'\boldmath']
params = {
          'font.size' : 14,
          'legend.fontsize': 16,
          }
plt.rcParams.update(params)

plt.rcParams['ytick.labelsize'] = 16
plt.rcParams['ytick.labelsize'] = 16

plt.figure(figsize=(12,16))

gspec = gridspec.GridSpec(3, 5)

ax2 = plt.subplot(gspec[0, 0:2])
ax3 = plt.subplot(gspec[0, 2:])
ax4 = plt.subplot(gspec[1, 0:2])
ax5 = plt.subplot(gspec[1, 2:])
ax1 = plt.subplot(gspec[2, 0:])

df = pd.read_csv("data/survey_results_gilgit.csv", sep=";")

ques = 'Please indicate the extent to which you agree with the following statement: I occasionally avoid visiting certain websites because my Internet is too slow to load them.'

df2 = df[ques].value_counts(normalize=True)

sns.barplot(df2.index, df2.values*100, ax=ax1,\
            palette=['#d7191c','#fdae61','#ffffbf','#a6d96a','#1a9641'], hatch="//", edgecolor="black", \
            order=['Strongly agree','Somewhat agree','Neither agree nor disagree','Somewhat disagree','Strongly disagree'])

ax1.set_title("Please indicate the extent to which you agree with the following statement:\nI occasionally avoid visiting certain websites because my Internet is too slow to load them.")

max_width = 15
ax1.set_xticklabels(textwrap.fill(x.get_text(), max_width) for x in ax1.get_xticklabels())
ax1.set_ylim([0,50])
ax1.set_yticklabels(['0%','10%','20%','30%','40%','50%'])
ax1.set_ylabel("% of participants", fontsize=16)
ax1.text(-0.8,55, "c", fontsize=30, weight="bold")

##################################################
control = df[(df['_submitted_by']=="normal80")] 
treatment = df[(df['_submitted_by']=="modified90")]
##################################################

ques = 'In terms of how the 4 websites looked, did you notice anything missing or out of the ordinary?'

c = control[ques].value_counts(normalize=True)
t = treatment[ques].value_counts(normalize=True)

x = ['Original Page','Lite-Web']
y = [c["Yes"]*100, t["Yes"]*100]

sns.barplot(x, y, alpha=1,palette=['#FAD933','#2b83ba'], edgecolor=["black"], ax=ax2)

#hypothesis test (fisher_exact)
c = control[ques].value_counts()
t = treatment[ques].value_counts()

oddsratio, pvalue = stats.fisher_exact([[c["No"], t["No"]],[c["Yes"], t["Yes"]]])  

print ("oddsratio, pvalue:", oddsratio, pvalue)

ax2.plot([0, 0, 1, 1], [24, 33, 33, 29], lw=1, c="black")
ax2.text((0+1)*.5, 33, "ns", ha='center', va='bottom', color="black")
ax2.set_ylim(0,100)

ax2.set_ylabel("% of participants that answered \"Yes\"", fontsize=16)
ax2.set_yticklabels(['0%','20%','40%','60%','80%','100%'])
ax2.set_title('In terms of how the 4 websites\nlooked, did you notice anything\nmissing or out of the ordinary?')
ax2.text(-1,115, "a", fontsize=30, weight="bold")
###################################################

ques2 = 'Please rate the impact of the missing component(s) on the browsing experience'

t_yes = treatment[treatment[ques]=="Yes"]
t = t_yes[ques2].value_counts().reset_index()
t.columns = ['impact','count']
t['tc']='Lite-Web'
 
c_yes = control[control[ques]=="Yes"]
c = c_yes[ques2].value_counts().reset_index()
c.columns = ['impact','count']
c['tc']='Original Page'

sns.barplot(x='impact', y='count', data=c.append(t), alpha=1, ax=ax3,\
            palette=['#FAD933','#2b83ba'],edgecolor=["black"],\
            order=['High impact','Moderate impact','Slight impact','No impact'], hue='tc')

ax3.legend_.set_title(None)
ax3.set_ylabel("% of participants", fontsize=16)
ax3.set_xlabel("")
ax3.grid()

#calc the pvalue
def switch_to_num(argument):
    switcher = {
        "High impact": 3,
        "Moderate impact": 2,
        "Slight impact": 1,
        "No impact": 0
    }
    return switcher.get(argument, "Invalid entry")

c_yes['ans_num'] = c_yes[ques2].apply(lambda x: switch_to_num(x))
t_yes['ans_num'] = t_yes[ques2].apply(lambda x: switch_to_num(x))

# print(stats.ttest_ind(c_yes['ans_num'],t_yes['ans_num']))

max_width = 10
ax3.set_xticklabels(textwrap.fill(x.get_text(), max_width) for x in ax3.get_xticklabels())

ax3.set_title('If you chose yes, please rate the impact of the\nmissing component(s) on the browsing experience')
ax3.set_ylim(0,100)

######################################################
ques = 'In terms of how the 4 websited FUNCTIONED, did you notice anything missing or out of the ordinary?'

c = control[ques].value_counts(normalize=True)
t = treatment[ques].value_counts(normalize=True)

x = ['Original Page','Lite-Web']
y = [c["Yes"]*100, t["Yes"]*100]

sns.barplot(x, y, alpha=1,palette=['#FAD933','#2b83ba'], edgecolor=["black"], ax=ax4)

#hypothesis test (fisher_exact)
c = control[ques].value_counts()
t = treatment[ques].value_counts()

oddsratio, pvalue = stats.fisher_exact([[c["No"], t["No"]],[c["Yes"], t["Yes"]]])  

print (oddsratio, pvalue)

ax4.plot([0, 0, 1, 1], [18, 22, 22, 20], lw=1, c="black")
ax4.text((0+1)*.5, 22, "ns", ha='center', va='bottom', color="black")
ax4.set_ylim(0,100)

ax4.set_ylabel("% of participants that answered \"Yes\"", fontsize=16)

ax4.set_yticklabels(['0%','20%','40%','60%','80%','100%'])
ax4.set_title(u'In terms of how the 4 websites\nfunctioned, did you notice anything\nmissing or out of the ordinary?')

ax4.text(-1,115, "b", fontsize=30, weight="bold")
#########################################################

ques2 = 'Please rate the impact of the missing component(s) on the browsing experience.1'

c_yes = control[control[ques]=="Yes"]
c = c_yes[ques2].value_counts().reset_index()
c.columns = ['impact','count']
c['tc']='Original Page'

t_yes = treatment[treatment[ques]=="Yes"]
t = t_yes[ques2].value_counts().reset_index()
t.columns = ['impact','count']
t['tc']='Lite-Web'


print (c['count'])
print (t['count'])

sns.barplot(x='impact', y='count', data=c.append(t), alpha=1,ax=ax5,\
            palette=['#FAD933','#2b83ba'], edgecolor=["black"],\
            order=['High impact','Moderate impact','Slight impact','No impact'], hue='tc')

ax5.legend_.set_title(None)

ax5.set_ylabel("% of participants", fontsize=16)
ax5.set_xlabel("")

# c_yes['ans_num'] = c_yes[ques2].apply(lambda x: switch_to_num(x))
# t_yes['ans_num'] = t_yes[ques2].apply(lambda x: switch_to_num(x))
# print(stats.ttest_ind(c_yes['ans_num'],t_yes['ans_num']))
      
max_width=10
ax5.set_xticklabels(textwrap.fill(x.get_text(), max_width) for x in ax5.get_xticklabels())

ax5.set_title('If you chose yes, please rate the impact of the\nmissing component(s) on the browsing experience')
ax5.legend()
ax5.set_ylim(0,100)
ax5.grid()

plt.tight_layout()
plt.savefig("figures/survey_results_gilgit.pdf", format="pdf")
