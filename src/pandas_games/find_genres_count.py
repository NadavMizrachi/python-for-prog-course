import pandas as pd

movies_df = pd.read_csv("movies.csv")

count = movies_df.groupby(["genres"], sort=True)["genres"].count()
print(movies_df.value_counts())
# print(count.sort_values('genres'))