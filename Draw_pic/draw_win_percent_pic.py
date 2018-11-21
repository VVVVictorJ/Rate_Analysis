
# coding: utf-8

# In[62]:


import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import pandas as pd
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
from matplotlib.ticker import FuncFormatter

data=pd.read_excel(r'C:\Users\Pasto\Desktop\etar.xlsx',sheet_name='Sheet3')
data.rename(columns={'赛事':'A','独赢':'B','全场 - 让球':'C','全场 - 大小':'D','单双':'E','胜负':'F'},inplace=True)
data=data[['A','B','C','D','E','F']]
all=data['F'][data.F>=-1].value_counts()
print(all[1])
#data=data[['A','B','F']][data.F==1]
#data=data[['B','F']][(data.F==1)&(data.B>1)&(data.B<1.24)]
count=data['B'][(data.F==1)&(data.B>1)&(data.B<1.24)].value_counts()
count2=data['B'][(data.F==1)&(data.B>0)&(data.B<1)].value_counts()
# print(len(count2))
# if len(count2)==0:
#     print(666)
#count=data['F'].value_counts()
#count=data['F'][data.F==1].value_counts()
# print(count)
# print(count2)
#print('precent: {:.2f}%'.format(count[1]/all[1]))
#print(data)

# count3=data['F'][(data.F==1)&(data.B>i)&(data.B<j)].value_counts()
# i=j
# j=j+0.04
# count4=data['F'][(data.F==1)&(data.B>i)&(data.B<j)].value_counts()
# print(count3[1])
# print(count4[1])
i=1
j=1.10
# print("kaishi")
lll=[]
for l in range(1,21):
    lll.append(l)
kkk=[]
for z in range(20):
    #print('precent1: {:.1f}'.format(i),'precent2: {:.1f}'.format(j))
    count5=data['F'][(data.F==1)&(data.B>i)&(data.B<j)].value_counts()
    if len(count5)==0:
        i=j
        j=j+0.5
        kkk.append(0)
        continue
    #jie_guo='{:.3f}'.format(count5[1]/all[1]*100)#转百分数
    #jie_guo="%.3f" % (count5[1]/all[1] * 100)
    jie_guo=count5[1]/all[1]
    kkk.append(jie_guo)
    #print(jie_guo)
    i=j
    j=j+0.04
#print(kkk)
#ppp=[lll,kkk]
ccc={
    'a':lll,
    'b':kkk
}
xintu=pd.DataFrame(ccc)
xintu=xintu[['a','b']][xintu.b!=0]
print(xintu)
'''
去掉0点
'''
# ax = plt.gca()
# ax.spines['top'].set_color('none')
# ax.spines['right'].set_color('none')
fig=matplotlib.pyplot.gcf()
fig.set_size_inches(30.5,15.5)

# def to_percent(temp, position):
#     return '%1.0f'%(10*temp) + '%'
# plt.gca().yaxis.set_major_formatter(FuncFormatter(to_percent))
# so=xintu.loc[[1]]
# print(so)
# plt.scatter(xintu.loc[[0]],xintu.loc[[1]])
xintu.plot.scatter(x='a',y='b',color='DarkBlue')
#fig.savefig(r'C:\Users\vanPersie\Desktop\distribute.png',dpi=100)
plt.show()

