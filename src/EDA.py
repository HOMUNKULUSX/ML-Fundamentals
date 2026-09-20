import pandas as pd
import matplotlib.pyplot as plt
from data import df

pd.set_option(
    "display.max_columns",
    None
)

df.hist(
    bins=50,
    figsize=(20, 15)
)

plt.show()