import numpy as np
import pandas as pd
import math
fields = ['no','income','age','education','marital','usage']

df = pd.read_csv('our.csv', skipinitialspace=True, usecols=fields)
# print(df.keys())
# # print(df.no)
# print(df.no.size)
# ageNames = df.age.unique()

print('------------Start---------------\n')

# print(df.groupby('age').count())
# print(df.groupby(['income', 'usage']).count())

total = df.no.size

usage = df.groupby(['usage'])['usage'].count()
infoUsage = 0

for usageNumber in usage:
    infoUsage += (-(usageNumber/total * math.log2(usageNumber/total)))

print('Info Usage: ',infoUsage)


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


info_income_usage = run('income','usage')
info_age_usage = run('age','usage')
info_education_usage = run('education','usage')
info_marital_usage = run('marital','usage')

print('Info Income Usage: ',info_income_usage)
print('Info Age Usage: ',info_age_usage)
print('Info Education Usage: ',info_education_usage)
print('Info Marital Usage: ',info_marital_usage)

print('\n\n')
print('Gain Income: ',infoUsage-info_income_usage)
print('Gain Age: ',infoUsage-info_age_usage)
print('Gain Education: ',infoUsage-info_education_usage)
print('Gain Marital: ',infoUsage-info_marital_usage)



# for i in incomeCount.index:
#     print(incomeCount[i])
#     for j in incomeUsageCount[i]:
#         print(j)
    

# for i in incomeUsageCount.high:
#     print(i)