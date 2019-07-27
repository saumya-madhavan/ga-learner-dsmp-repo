# --------------
# Import packages
import numpy as np
import pandas as pd
from scipy.stats import mode 
 



# code starts here
bank=pd.read_csv(path)
categorical_var=bank.select_dtypes(include = 'object')
print(categorical_var)

numerical_var=bank.select_dtypes(include = 'number')
print(numerical_var)


# code ends here


# --------------
# code starts here
print (bank.shape)
#banks=bank.drop("Loan_ID",axis=1, inplace=True)
banks= bank.drop(columns='Loan_ID')
print (banks.shape)
print(banks.isnull().sum())

#bank_mode=banks.mode()
bank_mode = banks.mode().iloc[0]
print("--"*30)
print(bank_mode)

#banks=banks.fillna(banks.mode())
banks.fillna(bank_mode, inplace=True)
print(banks.isnull().sum())
#code ends here


# --------------
# Code starts here



avg_loan_amount = pd.pivot_table(banks, index=['Gender','Married','Self_Employed'], values='LoanAmount', aggfunc='mean')

print(avg_loan_amount)

# code ends here



# --------------
# code starts here




loan_approved_se=banks[(banks['Self_Employed']=="Yes") &(banks['Loan_Status']=="Y")].count()
print(loan_approved_se)

loan_approved_nse=banks[(banks['Self_Employed']=="No") &(banks['Loan_Status']=="Y")].count()
print(loan_approved_nse)

percentage_se=loan_approved_se['Loan_Status']/banks['Loan_Status'].count()*100
percentage_nse=loan_approved_nse['Loan_Status']/banks['Loan_Status'].count()*100
print(percentage_se)
print(percentage_nse)

# code ends here


# --------------
# code starts here
#banks['loan_term']=banks['Loan_Amount_Term'].apply(lambda x: int(x)/12)
#print (banks['loan_term'])

#big_loan_term=banks[(banks['loan_term']>=25)].count()
#print (big_loan_term)


loan_term = banks['Loan_Amount_Term'].apply(lambda x: int(x)/12 )
big_loan_term=len(loan_term[loan_term>=25])
print(big_loan_term)
# code ends here


# --------------
# code starts here


#loan_groupby=banks.groupby(['Loan_Status']).count()

#loan_groupby=banks.groupby(['Loan_Status'])[['ApplicantIncome','Credit_History']].count()
#print(loan_groupby)

#mean_values=banks.groupby(['Loan_Status'])[['ApplicantIncome','Credit_History']].agg([np.mean])
#loan_groupby.mean()
#print(mean_values)

columns_to_show = ['ApplicantIncome', 'Credit_History']
 
loan_groupby=banks.groupby(['Loan_Status'])

loan_groupby=loan_groupby[columns_to_show]

mean_values=loan_groupby.agg([np.mean])

print(mean_values)

# code ends here


