# conda install pandas / pip install pandas
# https://pandas.pydata.org/pandas-docs/stable/getting_started/10min.html
# https://www.datacamp.com/community/blog/python-pandas-cheat-sheet
# https://towardsdatascience.com/a-guide-to-pandas-and-matplotlib-for-data-exploration-56fad95f951c

import pandas as pd

pd.options.display.max_columns = None

data = pd.read_csv("breastCancerDataReducedDimensions.csv")
print(data.head())
q3_gte_13 = data[data.radius_mean.ge(13)]
q3_gte_13.to_csv(r'q3_gte_13.csv')

q4_gte_18 = data[data.texture_mean.ge(18)]
q4_gte_18.to_csv(r'q4_gte_18.csv')
17.9
q5_gte_85 = data[data.perimeter_mean.ge(85)]
q5_gte_85.to_csv(r'q5_gte_85.csv')

q6_gte_500 = data[data.area_mean.ge(500)]
q6_gte_500.to_csv(r'q6_gte_500.csv')

first = pd.merge(left=q3_gte_13, right=q4_gte_18,
                 left_on='id', right_on='id')

second = pd.merge(left=first, right=q5_gte_85,
                  left_on='id', right_on='id')

intersection = pd.merge(left=second, right=q6_gte_500,
                        left_on='id', right_on='id')

intersection.to_csv(r'intersection.csv')
new_result = list(intersection.id.unique())

q3_e = q3_gte_13[q3_gte_13.diagnosis.eq('E')]
q3_e.to_csv(r'q3e.csv')
q3_b = q3_gte_13[q3_gte_13.diagnosis.eq('B')]
q3_b.to_csv(r'q3b.csv')
q3_m = q3_gte_13[q3_gte_13.diagnosis.isin(['B', 'E'])]
q3_m.to_csv(r'q3m.csv')

q4_e = q4_gte_18[q4_gte_18.diagnosis.eq('E')]
q4_e.to_csv(r'q4e.csv')
q4_b = q4_gte_18[q4_gte_18.diagnosis.eq('B')]
q4_b.to_csv(r'q4b.csv')
q4_m = q4_gte_18[q4_gte_18.diagnosis.isin(['B', 'E'])]
q4_m.to_csv(r'q4m.csv')

q5_e = q5_gte_85[q5_gte_85.diagnosis.eq('E')]
q5_e.to_csv(r'q5e.csv')
q5_b = q5_gte_85[q5_gte_85.diagnosis.eq('B')]
q5_b.to_csv(r'q5b.csv')
q5_m = q5_gte_85[q5_gte_85.diagnosis.isin(['B', 'E'])]
q5_m.to_csv(r'q5m.csv')

q6_e = q6_gte_500[q6_gte_500.diagnosis.eq('E')]
q6_e.to_csv(r'q6e.csv')
q6_b = q6_gte_500[q6_gte_500.diagnosis.eq('B')]
q6_b.to_csv(r'q6b.csv')
q6_m = q6_gte_500[q6_gte_500.diagnosis.isin(['B', 'E'])]
q6_m.to_csv(r'q6m.csv')


# method 1
SubsetMResult = pd.concat([q3_m, q4_m, q5_m, q6_m])
subset_result = list(SubsetMResult.id.unique())
difference_m1 = list(set(subset_result) - set(new_result))
print("\nMethod 1 difference")
print(f"\n# diffs = {len(difference_m1)}")
print(sorted(difference_m1))

# method 2
m2_data = pd.read_csv("breastCancerData.csv")
OriginalResult = m2_data[m2_data.diagnosis.eq('M')]
original_unique_ids = list(OriginalResult.id.unique())
difference_m2 = list(set(subset_result) - set(new_result))
print("\nMethod 2 difference")
print(f"\n# diffs = {len(difference_m1)}")
print(sorted(difference_m2))
