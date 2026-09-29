from sklearn.model_selection import  StratifiedShuffleSplit
from src.EDA import df

# separeting the data in test and train in our income_cat

split =  StratifiedShuffleSplit(
    n_splits=1,
    test_size=0.2,
    random_state=42)

for train_index, test_index in split.split(df, df["income_cat"]):
    start_train_set = df.loc[train_index]
    start_test_set = df.loc[test_index]
    
print(
      start_test_set["income_cat"].value_counts() / len(start_test_set)
      )

for set_ in (start_test_set, start_train_set):
    set_.drop("income_cat", axis=1, inplace=True)