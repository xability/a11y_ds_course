import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import maidr

ans = [
    pd.read_csv("anscombes_I.csv"),
    pd.read_csv("anscombes_II.csv"),
    pd.read_csv("anscombes_III.csv"),
    pd.read_csv("anscombes_IV.csv"),
]
for index, df in enumerate(ans, start=1):
    plt.figure(figsize=(4, 3))
    ans_plot = sns.scatterplot(data=df, x="x", y="y")
    plt.title(f"Anscomb set {index}")
    plt.xlabel("X values")
    plt.ylabel("Y values")
    # plt.show()
    maidr.show(ans_plot)

    plt.close()
    input("Hit enter")
