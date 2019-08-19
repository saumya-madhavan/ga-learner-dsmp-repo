# --------------
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# code starts here
df=pd.read_csv(path)
total=len(df)
p_a=len(df[df['fico']>700])/total
print(p_a)

p_b=len(df[df['purpose']=='debt_consolidation'])/total
print(p_b)

df1=df[df['purpose']=='debt_consolidation']

p_a_b=len(df[(df['purpose']=='debt_consolidation') & (df['fico']>700)])/total
print(p_a_b)

p_b_a = (p_a_b*p_a)/p_b
print(p_b_a)

result=p_b_a==p_a
print(result)
# code ends here


# --------------
# code starts here
total=len(df)
prob_lp=len(df[df['paid.back.loan']=='Yes'])/total
print(prob_lp)

prob_cs=len(df[df['credit.policy']=='Yes'])/total
print(prob_cs)

new_df=df[df['paid.back.loan']=='Yes']
prob_pd_cs=len(df[(df['paid.back.loan']=='Yes') & (df['credit.policy']=='Yes')])/len(new_df)
print(prob_pd_cs)

bayes=prob_pd_cs*prob_lp/prob_cs
print(bayes)
# code ends here


# --------------
# code starts here
df['purpose'].value_counts().plot(kind='bar')
plt.show()

df1=df[df['paid.back.loan']=='No']
df1['purpose'].value_counts().plot(kind='bar')
plt.show()


# code ends here


# --------------
# code starts here
inst_median=df['installment'].median()
print(inst_median)

inst_mean=df['installment'].mean()
print(inst_mean)

df.hist(column='installment',bins=50)
df.hist(column='log.annual.inc',bins=2)
plt.show()
# code ends here


