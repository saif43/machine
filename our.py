import numpy as np
import pandas as pd
import math
import csv

with open('our.csv', 'r') as f:
    d_reader = csv.DictReader(f)

    #get fieldnames from DictReader object and store in list
    header = d_reader.fieldnames


df = pd.read_csv('our.csv', skipinitialspace=True, usecols=header)
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


def run(x,y):
    # incomeCount = df.groupby(['income'])['income'].count()
    # incomeUsageCount = df.groupby(['income','usage'])['usage'].count()
    incomeCount = df.groupby([x])[x].count()
    incomeUsageCount = df.groupby([x,y])[y].count()

    # print(incomeCount)
    # print(incomeUsageCount)

    info_income_usage = 0.0
    conditional=0

    for i in incomeCount.index:
        prior = incomeCount[i]

        for j in incomeUsageCount[i]:
            conditional += -( (j/prior) * math.log2(j/prior) ) 

        info_income_usage += (prior/total) * conditional
        conditional = 0

    return info_income_usage

for i in range(len(header)-1):
    print('Info',header[i],className,':',run(header[i],className))

print('\n')

for i in range(len(header)-1):
    print('Gain',header[i],':',infoUsage-run(header[i],className))

# info_income_usage = run('income','usage')
# info_age_usage = run('age','usage')
# info_education_usage = run('education','usage')
# info_marital_usage = run('marital','usage')


# print('\n\n')
# print('Gain Income: ',infoUsage-info_income_usage)
# print('Gain Age: ',infoUsage-info_age_usage)
# print('Gain Education: ',infoUsage-info_education_usage)
# print('Gain Marital: ',infoUsage-info_marital_usage)



# for i in incomeCount.index:
#     print(incomeCount[i])
#     for j in incomeUsageCount[i]:
#         print(j)
    

# for i in incomeUsageCount.high:
#     print(i)