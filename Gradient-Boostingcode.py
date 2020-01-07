# --------------
import pandas as pd
from sklearn.model_selection import train_test_split
#path - Path of file 
df=pd.read_csv(path)
# Code starts here

print(df.head(3))
#Extracting features
X=df.drop(['customerID','Churn'],1)

#Extracting target class
y=df['Churn'].copy()

#Splitting features and target class
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)





# --------------
import numpy as np
from sklearn.preprocessing import LabelEncoder

# Code starts here
print(X_train['TotalCharges'].value_counts())
X_train['TotalCharges'] = (X_train['TotalCharges'].replace(' ', np.nan)).astype(float)
print(X_train['TotalCharges'].value_counts())
X_test['TotalCharges'] = (X_test['TotalCharges'].replace(' ', np.nan)).astype(float)
print(X_test['TotalCharges'].value_counts())

print(X_train.isnull().sum())

X_train['TotalCharges']=X_train['TotalCharges'].fillna(X_train['TotalCharges'].mean())
X_test['TotalCharges']=X_test['TotalCharges'].fillna(X_test['TotalCharges'].mean())

print(X_train.isnull().sum())

le_gender=LabelEncoder()
le_Partner=LabelEncoder()
le_Dependents=LabelEncoder()
le_PhoneService=LabelEncoder()
le_MultipleLines=LabelEncoder()
le_InternetService=LabelEncoder()
le_OnlineSecurity=LabelEncoder()
le_OnlineBackup=LabelEncoder()
le_DeviceProtection=LabelEncoder()
le_TechSupport=LabelEncoder()
le_StreamingTV=LabelEncoder()
le_StreamingMovies=LabelEncoder()
le_Contract=LabelEncoder()
le_PaperlessBilling=LabelEncoder()
le_PaymentMethod=LabelEncoder()

X_train['gender']=le_gender.fit_transform(X_train['gender'])
X_train['Partner']=le_Partner.fit_transform(X_train['Partner'])
X_train['Dependents']=le_Dependents.fit_transform(X_train['Dependents'])
X_train['PhoneService']=le_PhoneService.fit_transform(X_train['PhoneService'])
X_train['MultipleLines']=le_MultipleLines.fit_transform(X_train['MultipleLines'])
X_train['InternetService']=le_InternetService.fit_transform(X_train['InternetService'])
X_train['OnlineSecurity']=le_OnlineSecurity.fit_transform(X_train['OnlineSecurity'])
X_train['OnlineBackup']=le_OnlineBackup.fit_transform(X_train['OnlineBackup'])
X_train['DeviceProtection']=le_DeviceProtection.fit_transform(X_train['DeviceProtection'])
X_train['TechSupport']=le_TechSupport.fit_transform(X_train['TechSupport'])
X_train['StreamingTV']=le_StreamingTV.fit_transform(X_train['StreamingTV'])
X_train['StreamingMovies']=le_StreamingMovies.fit_transform(X_train['StreamingMovies'])
X_train['Contract']=le_Contract.fit_transform(X_train['Contract'])
X_train['PaperlessBilling']=le_PaperlessBilling.fit_transform(X_train['PaperlessBilling'])
X_train['PaymentMethod']=le_PaymentMethod.fit_transform(X_train['PaymentMethod'])

X_test['gender']=le_gender.fit_transform(X_test['gender'])
X_test['Partner']=le_Partner.fit_transform(X_test['Partner'])
X_test['Dependents']=le_Dependents.fit_transform(X_test['Dependents'])
X_test['PhoneService']=le_PhoneService.fit_transform(X_test['PhoneService'])
X_test['MultipleLines']=le_MultipleLines.fit_transform(X_test['MultipleLines'])
X_test['InternetService']=le_InternetService.fit_transform(X_test['InternetService'])
X_test['OnlineSecurity']=le_OnlineSecurity.fit_transform(X_test['OnlineSecurity'])
X_test['OnlineBackup']=le_OnlineBackup.fit_transform(X_test['OnlineBackup'])
X_test['DeviceProtection']=le_DeviceProtection.fit_transform(X_test['DeviceProtection'])
X_test['TechSupport']=le_TechSupport.fit_transform(X_test['TechSupport'])
X_test['StreamingTV']=le_StreamingTV.fit_transform(X_test['StreamingTV'])
X_test['StreamingMovies']=le_StreamingMovies.fit_transform(X_test['StreamingMovies'])
X_test['Contract']=le_Contract.fit_transform(X_test['Contract'])
X_test['PaperlessBilling']=le_PaperlessBilling.fit_transform(X_test['PaperlessBilling'])
X_test['PaymentMethod']=le_PaymentMethod.fit_transform(X_test['PaymentMethod'])

y_train = (y_train.replace({'No':0, 'Yes':1}).astype(int))
y_test = (y_test.replace({'No':0, 'Yes':1}).astype(int))



# --------------
from sklearn.ensemble import AdaBoostClassifier
from sklearn.metrics import accuracy_score,classification_report,confusion_matrix

# Code starts here
print(X_train, X_test, y_train, y_test)

ada_model=AdaBoostClassifier(random_state=0)
ada_model.fit(X_train,y_train)
y_pred=ada_model.predict(X_test)
ada_score=accuracy_score(y_test,y_pred)
print(ada_score)

ada_cm=confusion_matrix(y_test,y_pred)
print(ada_cm)

ada_cr=classification_report(y_test,y_pred)
print(ada_cr)



# --------------
from xgboost import XGBClassifier
from sklearn.model_selection import GridSearchCV

#Parameter list
parameters={'learning_rate':[0.1,0.15,0.2,0.25,0.3],
            'max_depth':range(1,3)}

# Code starts here
xgb_model=XGBClassifier(random_state=0)
xgb_model.fit(X_train,y_train)
y_pred=xgb_model.predict(X_test)

xgb_score=accuracy_score(y_test,y_pred)
print(xgb_score)

xgb_cm=confusion_matrix(y_test,y_pred)
print(xgb_cm)

xgb_cr=classification_report(y_test,y_pred)
print(xgb_cr)

clf_model=GridSearchCV(estimator=xgb_model,param_grid=parameters)
clf_model.fit(X_train,y_train)
y_pred=clf_model.predict(X_test)
clf_score=accuracy_score(y_test,y_pred)
print(clf_score)
clf_cm=confusion_matrix(y_test,y_pred)
print(clf_cm)
clf_cr=classification_report(y_test,y_pred)
print(clf_cr)





