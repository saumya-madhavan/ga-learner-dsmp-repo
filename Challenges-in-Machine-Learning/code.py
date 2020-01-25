# --------------
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

# Code starts here
df=pd.read_csv(path)
print(df.head(5))
#print(df.info)

df['INCOME']=df['INCOME'].str.replace("$","")
df['INCOME']=df['INCOME'].str.replace(",","")

df['HOME_VAL']=df['HOME_VAL'].str.replace("$","")
df['HOME_VAL']=df['HOME_VAL'].str.replace(",","")

df['BLUEBOOK']=df['BLUEBOOK'].str.replace("$","")
df['BLUEBOOK']=df['BLUEBOOK'].str.replace(",","")

df['OLDCLAIM']=df['OLDCLAIM'].str.replace("$","")
df['OLDCLAIM']=df['OLDCLAIM'].str.replace(",","")

df['CLM_AMT']=df['CLM_AMT'].str.replace("$","")
df['CLM_AMT']=df['CLM_AMT'].str.replace(",","")

print(df.head(3))

X=df.drop(['CLAIM_FLAG'],axis=1)
print(X.head(3))
y=df['CLAIM_FLAG']

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.3,random_state=6)


# Code ends here


# --------------
# Code starts here
cols=['INCOME','HOME_VAL','BLUEBOOK','OLDCLAIM','CLM_AMT']

#print(type(X_train['INCOME']))
for i in cols:
    X_train[i]=X_train[i].astype(float)
    X_test[i]=X_test[i].astype(float)

print(X_train.isnull().sum())
print("*"*20)
print(X_test.isnull().sum())
# Code ends here


# --------------
# Code starts here
# print(X_train.shape)
# X_train=X_train.dropna(subset=['YOJ','OCCUPATION'],inplace=True)
# X_test=X_test.dropna(subset=['YOJ','OCCUPATION'],inplace=True)

#y_train['Id_new']=y_train[X_train.index]
#y_test['Id_new']=y_test[X_test.index]

# y_train=y_train[X_train.index]
# y_test=y_test[X_test.index]

#print(y_train.index)

# col1=['AGE','CAR_AGE','INCOME','HOME_VAL']
# for i in col1:
#     X_train[i].fillna((X_train[i].mean()),inplace=True)
#     X_test[i].fillna((X_train[i].mean()),inplace=True)

# print(X_train.isnull().sum())    
# print("*"*20)    
# print(X_test.isnull().sum())    
# print(X_train.shape)

# Code ends here

# drop missing values
X_train.dropna(subset=['YOJ','OCCUPATION'],inplace=True)
X_test.dropna(subset=['YOJ','OCCUPATION'],inplace=True)


y_train=y_train[X_train.index]
y_test=y_test[X_test.index]



# fill missing values with mean
X_train['AGE'].fillna((X_train['AGE'].mean()), inplace=True)
X_test['AGE'].fillna((X_train['AGE'].mean()), inplace=True)

X_train['CAR_AGE'].fillna((X_train['CAR_AGE'].mean()), inplace=True)
X_test['CAR_AGE'].fillna((X_train['CAR_AGE'].mean()), inplace=True)



X_train['INCOME'].fillna((X_train['INCOME'].mean()), inplace=True)
X_test['INCOME'].fillna((X_train['INCOME'].mean()), inplace=True)



X_train['HOME_VAL'].fillna((X_train['HOME_VAL'].mean()), inplace=True)
X_test['HOME_VAL'].fillna((X_train['HOME_VAL'].mean()), inplace=True)


print(X_train.isnull().sum())
print(X_test.isnull().sum())




# --------------
from sklearn.preprocessing import LabelEncoder
columns = ["PARENT1","MSTATUS","GENDER","EDUCATION","OCCUPATION","CAR_USE","CAR_TYPE","RED_CAR","REVOKED"]

# Code starts here
for i in columns:
    le=LabelEncoder()
    X_train[i]=le.fit_transform(X_train[i].astype(str))
    X_test[i]=le.transform(X_test[i].astype(str))

#le=LabelEncoder()
#X_train['PARENT1']=le.fit_transform(X_train['PARENT1'].astype(str))
#X_test['PARENT1']=le.fit_transform(X_test['PARENT1'].astype(str))
# Code ends here



# --------------
from sklearn.metrics import precision_score 
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression



# code starts here 
model = LogisticRegression(random_state=6)
model.fit(X_train,y_train)
y_pred = model.predict(X_test)

score=model.score(X_test,y_test)
print(score)
# Code ends here


# --------------
from sklearn.preprocessing import StandardScaler
from imblearn.over_sampling import SMOTE

# code starts here
smote=SMOTE(random_state=9)

X_train,y_train = smote.fit_sample(X_train,y_train)

scaler=StandardScaler()
X_train=scaler.fit_transform(X_train)
X_test=scaler.transform(X_test)



# Code ends here


# --------------
# Code Starts here
model=LogisticRegression()
model.fit(X_train,y_train)
y_pred=model.predict(X_test)

score=model.score(X_test,y_test)
print(score)


# Code ends here


