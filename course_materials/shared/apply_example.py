# Create a Times table in pandas for fun using apply.

import pandas as pd
import numpy as np


df = pd.DataFrame(np.arange(1, 11), columns=[1], index=np.arange(1, 11))
for i in range(2, 11):
    df[i] = df[1].apply(lambda x: x * i)


print(df)
