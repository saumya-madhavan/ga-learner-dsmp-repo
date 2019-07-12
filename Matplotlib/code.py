# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Code starts here
data = pd.read_csv(path)
data.shape
loan_status=data['Loan_Status'].value_counts()
print (loan_status)
loan_status.plot(kind='bar',stacked=True,figsize=(15,10))
plt.show()



# --------------
#Code starts here
property_and_loan=data.groupby(['Property_Area','Loan_Status'])
property_and_loan=property_and_loan.size().unstack()
print(property_and_loan)
property_and_loan.plot(kind='bar',stacked=False,figsize=(15,10))
plt.xlabel('Property Area')
plt.ylabel('Loan Status')
plt.tick_params(axis='x', labelrotation=45)
plt.show()



# --------------
#Code starts here
education_and_loan=data.groupby(['Education','Loan_Status'])
education_and_loan=education_and_loan.size().unstack()
print (education_and_loan)
education_and_loan.plot(kind='bar',stacked=True,figsize=(15,10))
plt.xlabel('Education Status')
plt.ylabel('Loan Status')
plt.tick_params(axis='x', labelrotation=45)
plt.show()



# --------------
#Code starts here
graduate=data[data['Education'] == 'Graduate']
not_graduate=data[data['Education'] == 'Not Graduate']
graduate['LoanAmount'].plot(kind='density', label='Graduate')
not_graduate['LoanAmount'].plot(kind='density',label='Not Graduate')

#plt.show()

#Code ends here

#For automatic legend display
plt.legend()



# --------------
#Code starts here



fig ,(ax_1,ax_2,ax_3)=plt.subplots(nrows=3, ncols=1, figsize=(29,10))
#plt.scatter(data['ApplicantIncome'],data['LoanAmount'],ax=ax_1)
data.plot.scatter(x='ApplicantIncome', y='LoanAmount',ax=ax_1)
ax_1.set_title('Applicant Income')
#plt.scatter(data['CoapplicantIncome'],data['LoanAmount'],ax=ax_2)
data.plot.scatter(x='CoapplicantIncome', y='LoanAmount',ax=ax_2)
ax_2.set_title('Coapplicant Income')

#new_data=data.fillna(0)
data['TotalIncome']=data['ApplicantIncome']+data['CoapplicantIncome']
#plt.scatter(data['TotalIncome'],data['LoanAmount'],ax=ax_3)
data.plot.scatter(x='TotalIncome', y='LoanAmount',ax=ax_3)
ax_3.set_title('Total Income')
plt.show()



