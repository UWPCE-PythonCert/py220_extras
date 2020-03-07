# conda install pandas
# https://pandas.pydata.org/pandas-docs/stable/getting_started/10min.html
# https://www.datacamp.com/community/blog/python-pandas-cheat-sheet

import pandas as pd


def main():
    pd.options.display.max_columns = None

    data = pd.read_csv("breastCancerDataReducedDimensions.csv")
    print(data.head())

    q3_gte_13 = data[data.radius_mean.ge(13)]
    print(q3_gte_13.head())
    q3_gte_13.to_csv(r'q3_gte_13.csv')

    q4_gte_18 = data[data.texture_mean.ge(18)]
    print(q4_gte_18.head())
    q4_gte_18.to_csv(r'q4_gte_18.csv')

    q5_gte_85 = data[data.perimeter_mean.ge(85)]
    print(q5_gte_85.head())
    q5_gte_85.to_csv(r'q5_gte_85.csv')

    q6_gte_500 = data[data.area_mean.ge(500)]
    print(q6_gte_500.head())
    q6_gte_500.to_csv(r'q6_gte_500.csv')

    first = pd.merge(left=q3_gte_13, right=q4_gte_18,
                     left_on='id', right_on='id')

    second = pd.merge(left=first, right=q5_gte_85,
                      left_on='id', right_on='id')

    intersection = pd.merge(left=second, right=q6_gte_500,
                            left_on='id', right_on='id')

    intersection.to_csv(r'intersection.csv')

    print('Unique ids')
    for id in intersection.id.unique():
        print(id)


if __name__ == "__main__":
    main()
