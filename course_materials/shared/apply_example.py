# Create a Times table in pandas for fun using apply.

import pandas as pd
import numpy as np


df = pd.DataFrame(np.arange(1, 11), columns=[1], index=np.arange(1, 11))
for i in range(2, 11):
    df[i] = df[1].apply(lambda x: x * i)


print("Times table \n\n",df)

print ("Multiply all elements by 2  using applymap\n\n")
print ("Never mind applymap was depricated now you use map so here it is with map\n\n")

#this is the original with apply map if you try it , it will warn you.
#two_df = df.applymap(lambda x: x * 2)

two_df = df.map(lambda x: x * 2)

print ("two_df: \n\n",two_df)

print("Divide all elements by 20 using apply and axis 1\n\n")

twenty_df = df.apply(lambda x: x / 20, axis=1)

print("twenty_df: \n\n",twenty_df)

print("multiply all elements by 20 using apply and axis 0\n\n")

twenty_times_df = df.apply(lambda x: x * 20, axis=0)

print("twenty_times_df: \n\n",twenty_times_df)

print ("Divide the 5 column by 2\n\n")

five_divide_df = df[5].apply(lambda x: x / 2)

print("five_divide_df: \n\n",five_divide_df)

