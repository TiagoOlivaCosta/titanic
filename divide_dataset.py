import pandas as pd

df = pd.read_csv('titanic.csv')  # pandas dataframe

train_fraction = 0.7
test_fraction = 1 - train_fraction

train = df.sample(frac=train_fraction).reset_index(drop=True)
test = df.sample(frac=test_fraction).reset_index(drop=True)

# export datasets
train.to_csv('./train.csv')
test.to_csv('./test.csv')
