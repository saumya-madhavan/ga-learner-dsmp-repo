# --------------
# Importing header files
import numpy as np

# Path of the file has been stored in variable called 'path'
data = np.genfromtxt(path, delimiter=",", dtype=str, skip_header=1)
print (data)
print (type(data))
print (data.shape)
#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]
print (new_record, type(new_record))
x = np.asarray(new_record)
print (x, type(x))

#Code starts here

census = np.concatenate ((data,x),axis=0)
print (census)



# --------------
#Code starts here
age = census[:,0]
print (age)

max_age = np.max(age.astype(np.int64))
print (max_age)
min_age = np.min(age.astype(np.int64))
print (min_age)
#age_Mean = sum(age.astype(np.int64)) / len(age)
age_mean = np.mean(age.astype(np.int64))
print (age_mean)
age_std = np.std(age.astype(np.int64))
print (age_std)



# --------------
#Code starts here
census = census.astype(np.int64)
race_0 = census[census[:,2]==0]
print (race_0)
race_1 = census[census[:,2]==1]
print (race_1)
race_2 = census[census[:,2]==2]
print (race_2)
race_3 = census[census[:,2]==3]
print (race_3)
race_4 = census[census[:,2]==4]
print (race_4)

len_0 = len(race_0)
print (len_0)
len_1 = len(race_1)
print (len_1)
len_2 = len(race_2)
print (len_2)
len_3 = len(race_3)
print (len_3)
len_4 = len(race_4)
print (len_4)

minority = min(len_0,len_1,len_2,len_3,len_4)
if minority == len_0:
    minority_race = 0
elif minority == len_1:     
    minority_race = 1
elif minority == len_2:     
    minority_race = 2
elif minority == len_3:     
    minority_race = 3
elif minority == len_4:     
    minority_race = 4
print (minority_race)





# --------------
#Code starts here
census = census.astype(np.int64)
senior_citizens = census[census[:,0]>60]
print (senior_citizens)

working_hours_sum=np.sum(senior_citizens[:,6])
print(working_hours_sum)

senior_citizens_len = len(senior_citizens)
print(senior_citizens_len)

avg_working_hours = working_hours_sum / senior_citizens_len
print (avg_working_hours)


# --------------
#Code starts here
census = census.astype(np.int64)
high = census[census[:,1]>10]
print (high)

low = census[census[:,1]<=10]
print (low)

avg_pay_high = round ((np.sum(high[:,7])/len(high[:,7])),2)
print (avg_pay_high)

avg_pay_low = round(np.mean(low[:,7]),2)
print (avg_pay_low)




