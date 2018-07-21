import numpy as np
import pandas as pd
import math
import csv
from operator import itemgetter

with open('kdd-nsl.csv', 'r') as f:
    d_reader = csv.DictReader(f)

    #get fieldnames from DictReader object and store in list
    header = d_reader.fieldnames


df = pd.read_csv('kdd-nsl.csv', skipinitialspace=True, usecols=header)
# print(df.keys())
# # print(df.no)
# print(df.no.size)
# ageNames = df.age.unique()

print('------------Start---------------\n')

# print(df.groupby('age').count())
# print(df.groupby(['income', 'usage']).count())

total = len(df.index)

className = header[len(header)-1]

usage = df.groupby([className])[className].count()

infoUsage = 0

for usageNumber in usage:
    infoUsage += (-(usageNumber/total * math.log2(usageNumber/total)))

print('Info',className,':',infoUsage)


def run(feature,className):
    # featureCount = df.groupby(['income'])['income'].count()
    # featureClassCount = df.groupby(['income','usage'])['usage'].count()
    featureCount = df.groupby([feature])[feature].count()
    featureClassCount = df.groupby([feature,className])[className].count()

    # print(featureCount)
    # print(featureClassCount)

    info_feature_class = 0.0
    conditional=0

    for i in featureCount.index:
        prior = featureCount[i]

        for j in featureClassCount[i]:
            conditional += -( (j/prior) * math.log2(j/prior) ) 

        info_feature_class += (prior/total) * conditional
        conditional = 0

    return info_feature_class

# printing info(D) of all Attributes
for i in range(1,len(header)-1):
    print('Info',header[i],className,':',run(header[i],className))

print('\n')

gain = list()

# Taking Attributes names and their gain in list
for i in range(1,len(header)-1):
    gain.append([header[i],infoUsage-run(header[i],className)])
    print('Gain',header[i],':',infoUsage-run(header[i],className))

# gain.sort(reverse=True)

print(len(gain)) #Number of Attributes
gainSorted = sorted(gain, key=itemgetter(1)) # Sorting by the Gain values, thats why itemgetter(1)


# Writing Attributes and their gain ratio in output.csv file
with open('output.csv', 'a', newline='') as csvfile:
    fieldnames = ['Attribute', 'GainRatio']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()


    for i in gainSorted:
        writer.writerow({'Attribute': i[0], 'GainRatio': i[1]})
        # print(i[0],':',i[1])   
    writer.writerow({})
    writer.writerow({'Attribute': 'Accuracy', 'GainRatio': ''})
    # printing newlines
    writer.writerow({})
    writer.writerow({})
    writer.writerow({})
    writer.writerow({})



#print(gain[0],':',gain[1])


# info_feature_class = run('income','usage')
# info_age_usage = run('age','usage')
# info_education_usage = run('education','usage')
# info_marital_usage = run('marital','usage')


# print('\n\n')
# print('Gain Income: ',infoUsage-info_feature_class)
# print('Gain Age: ',infoUsage-info_age_usage)
# print('Gain Education: ',infoUsage-info_education_usage)
# print('Gain Marital: ',infoUsage-info_marital_usage)



# for i in featureCount.index:
#     print(featureCount[i])
#     for j in featureClassCount[i]:
#         print(j)
    

# for i in featureClassCount.high:
#     print(i)