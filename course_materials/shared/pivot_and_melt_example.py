
import pandas as pd

df = pd.DataFrame({
    "shopping_list": [
    "Bill", "Bill", "Bill", "Ken", "Ken", "Ken", "Ken", "Tim", "Tim", "Fred"],
    "item_number": [
    1, 2, 3, 1, 2, 3, 4, 1, 2, 1],
    "item": [
    "Apple", "Orange", "Pepper", "Jar", "Pipe", "Desk", "Dog", "Gum", "Peach", "Pen"]
})

print ("Original DataFrame ",df)

pivot_df = df.pivot(index = 'shopping_list', columns = 'item_number', values = 'item')

print ("Pivoted DataFrame \n", pivot_df)

melt_df = pivot_df.reset_index().melt(id_vars='shopping_list', value_name='item').dropna().sort_values(by=['shopping_list', 'item_number'])

print ("melted back to normal \n", melt_df)
