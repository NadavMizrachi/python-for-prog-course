import random
import pandas as pd


def rand_dice(times):
    return [random.randint(1, 6) for i in range(times)]


def create_dices_df():
    dice1 = pd.Series(rand_dice(100))
    dice2 = pd.Series(rand_dice(100))

    return pd.DataFrame({
        "dice1": dice1,
        "dice2": dice2
    })
