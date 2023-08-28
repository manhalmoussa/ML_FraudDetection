import pandas as pd

df = pd.read_csv(r'C:\Users\Manhal.Moussa\Documents\GitHub\ML_FraudDetection\Data\creditcard.csv')


columns = df.columns
columns = columns.drop(['Time','Amount','Class'])
for column in columns:
    std = df[column].std()
    mean = df[column].mean()
    max_limit = mean + 2*std
    min_limit = mean-2*std
    print('hi')
    df_filtered = df.loc[(df[column]>= min_limit) & (df[column]<=max_limit)]



print('Hi')