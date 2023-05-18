from dices_file_creation import create_dices_df
import matplotlib.pyplot as plt

fig = plt.figure()
x = range(100)
dices_dfs = [create_dices_df() for i in range(100)]
y = [len(dices_df[dices_df["dice1"] == dices_df["dice2"]]) for dices_df in dices_dfs]

plt.plot(x, y)
plt.show()
