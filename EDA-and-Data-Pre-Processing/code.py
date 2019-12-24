# --------------
#Importing header files
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Code starts here
data=pd.read_csv(path)
print(data.head(5))
data.hist(column='Rating', bins=2)
plt.show()
#data['Rating'].value_counts()

data=data[data['Rating']<=5]
data.hist(column='Rating', bins=2)
plt.show()
#Code ends here



# --------------
# code starts here
total_null=data.isnull().sum()
print(total_null)
percent_null=(total_null/data.isnull().count())
print(percent_null)

missing_data=pd.concat([total_null,percent_null],axis=1,keys=['Total','Percent'] )
print(missing_data)

data=data.dropna()
total_null1=data.isnull().sum()
print(total_null1)
percent_null1=(total_null1/data.isnull().count())
print(percent_null1)

missing_data_1=pd.concat([total_null1,percent_null1],axis=1,keys=['Total','Percent'] )
print(missing_data_1)

# code ends here



# --------------
import seaborn as sns
#Code starts here
chart=sns.catplot(x="Category",y="Rating",data=data, kind="box", height = 10)
#chart.set_title("Rating vs Category [BoxPlot]")
chart.fig.suptitle("Rating vs Category [BoxPlot]")
chart.set_xticklabels(rotation=90)


#Code ends here


# --------------
#Importing header files
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler, LabelEncoder

#Code starts here
print("Before",data['Installs'].value_counts())
data['Installs'] = data['Installs'].str.replace('+','')
data['Installs'] = data['Installs'].str.replace(',','')
data['Installs'] = data['Installs'].astype(int)

print("After",data['Installs'].value_counts())

le = LabelEncoder()
data['Installs'] = le.fit_transform(data['Installs'])
g=sns.regplot(x="Installs", y="Rating",data=data)
#g.fig.suptitle("Rating vs Installs [RegPlot]")
#Code ends here



# --------------
#Code starts here
print(data['Price'].value_counts())

data['Price'] = data['Price'].str.replace('$','')
data['Price'] = data['Price'].astype(float)

print("After",data['Price'].value_counts())

g=sns.regplot(x="Price", y="Rating",data=data)
plt.title("Rating vs Price [RegPlot]")

#Code ends here


# --------------

#Code starts here
print(data['Genres'].unique())

new = data["Genres"].str.split(";", n = 1, expand = True) 
data["Genres"]= new[0] 
print(data['Genres'].unique())

gr_mean = data.groupby("Genres", as_index=False)['Genres','Rating'].mean()
gr_mean.describe()
gr_mean=gr_mean.sort_values(['Rating'],ascending = True)
print(gr_mean.head(1))
print(gr_mean.tail(1))
#Code ends here


# --------------
import pandas as pd
import seaborn as sns
#Code starts here
print(data['Last Updated'])

data['Last Updated'] = pd.to_datetime(data['Last Updated'])
print(data['Last Updated'])
max_date=max(data['Last Updated'])
print (max_date)

data['Last Updated Days']=(max_date-data['Last Updated']).dt.days
print(data['Last Updated Days'])

sns.regplot(x="Last Updated Days", y="Rating", data=data)
plt.title('Rating vs Last Updated [RegPlot]')
#Code ends here


