import pandas as pd
import numpy as np

'''
new=pd.DataFrame({'name':'lisa',
         'gender':'F',
         'city':'北京',
         'age':19,
         'score':100},
         index=[1])  # 自定义索引为：1 ，这里也可以不设置index
'''

origin = pd.read_excel('./AMD APO loading 20200207.xlsx')
target = pd.read_excel('./APO-Amphenol-3250002360 on 2020204.xlsx')
count = 4
for i in range(len(origin)):
    Global = pd.DataFrame({'PART_NUMBER':origin['COMPONENT'][i],
                           'MFG_PLANT':'WW',
                        'M1':format(origin['Global'][i],'.2f')
                           }, index=[0])
    target = target.append(Global, sort=False)
    LSTC = pd.DataFrame({'PART_NUMBER':origin['COMPONENT'][i],
                         'MFG_PLANT':'L070',
                        'M1':format(origin['LSTC'][i],'.2f')
                         }, index=[0])
    target = target.append(LSTC, sort=False)
    MTY = pd.DataFrame({'PART_NUMBER': origin['COMPONENT'][i],
                        'MFG_PLANT':'X470',
                         'M1':format(origin['MTY'][i],'.2f')}, index=[0])
    target = target.append(MTY, sort=False)
    HGY = pd.DataFrame({'PART_NUMBER': origin['COMPONENT'][i],
                        'MFG_PLANT':'FLEX',
                         'M1':format(origin['HGY'][i],'.2f')}, index=[0])
    target = target.append(HGY, sort=False)
target.to_excel('./target.xlsx')


