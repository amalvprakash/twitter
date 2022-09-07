import pandas as pd
vnm = input("Enter the name")
data = []

#data.append([tweet.created_at, tweet.text])
df = pd.DataFrame(data, columns=columns)
df.to_csv('myfile_{}.csv'.format(vnm), sep=',', index=False)