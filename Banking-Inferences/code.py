# --------------
import pandas as pd
import scipy.stats as stats
import math
import numpy as np
import warnings

warnings.filterwarnings('ignore')
#Sample_Size
sample_size=2000

#Z_Critical Score
z_critical = stats.norm.ppf(q = 0.95)  


# path        [File location variable]
data=pd.read_csv(path)
data.head(3)
#Code starts here
data_sample=data.sample(n=sample_size,random_state=0)
sample_mean=data_sample['installment'].mean()
print("Sample mean = ",sample_mean)

sample_std=data_sample['installment'].std()
print("Sample Std_dev = ",sample_std)

margin_of_error=z_critical*sample_std/math.sqrt(sample_size)
print ("Margin of errors = ",margin_of_error)

confidence_interval=(sample_mean-margin_of_error,sample_mean+margin_of_error)
print("Confidence Interval = ",confidence_interval)

true_mean=data['installment'].mean()
print("True Mean =", true_mean)




# --------------
import matplotlib.pyplot as plt
import numpy as np

#Different sample sizes to take
sample_size=np.array([20,50,100])

#Code starts here
fig,axes=plt.subplots(3,1)
for i in range(len(sample_size)):
    m=[]
    for j in range(1000):
        #df=data['installment'].sample(n=sample_size[i])
        #m_df=df.mean()
        #m.append(m_df)
        mean=data['installment'].sample(sample_size[i]).mean()
        m.append(mean)
    #mean_series=pd.series(m)
    mean_series=pd.Series(m)
    #axes[i].hist(column='mean_series')
    plt.hist(mean_series[i],bins=[20])
    plt.show()




# --------------
#Importing header files

from statsmodels.stats.weightstats import ztest

#Code starts here
#data['int.rate']=data['int.rate'].astype(str).str.extract('%').astype(float)
data['int.rate']=data['int.rate'].astype(str).str.replace('%','').astype(float)
data['int.rate']=data['int.rate']/100
x1=data[data['purpose']=='small_business']['int.rate']
value=data['int.rate'].mean()
z_statistic,p_value=ztest(x1,value=value,alternative='larger')
print("Z statistic = ",z_statistic)
print("p_value = ",p_value)
if (p_value<0.05):
    print("Reject Null Hypothesis")
else:
    print("Accept Null Hypothesis")
    


# --------------
#Importing header files
from statsmodels.stats.weightstats import ztest

#Code starts here
x1=data[data['paid.back.loan']=='No']['installment']
x2=data[data['paid.back.loan']=='Yes']['installment']
z_statistic,p_value=ztest(x1,x2)
print("Z statistic = ",z_statistic)
print("p_value = ",p_value)
if (p_value < 0.05):
    print("Reject Null Hypothesis")
else:
    print("Accept Null Hypothesis")



# --------------
#Importing header files
from scipy.stats import chi2_contingency

#Critical value 
critical_value = stats.chi2.ppf(q = 0.95, # Find the critical value for 95% confidence*
                      df = 6)   # Df = number of variable categories(in purpose) - 1

#Code starts here
yes=data[data['paid.back.loan']=='Yes']['purpose'].value_counts()
print(yes)
no=data[data['paid.back.loan']=='No']['purpose'].value_counts()
print(no)
yes1=yes.transpose()
print(yes1)
no1=no.transpose()
print(no1)
observed=pd.concat([yes1,no1],axis=1,keys=['Yes','No'])
print(observed)

chi2,p,dof,ex=chi2_contingency(observed)
print("Critical Value = ",critical_value)
print("Chi 2",chi2)
if (chi2>critical_value):
    print("Reject Null Hypothesis")
else:
    print("Accept Null Hypothesis")




