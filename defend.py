import pandas as pd
import random


def runsize(colum):
    q = pd.Series([df[colum].quantile(0.35), df[colum].quantile(0.98)])
    insert = df[df[colum] > df[colum].quantile(.95)]
    indexlist = []
    i = 0
    while i < len(insert) - 3:
        if (insert.index[i + 1] - insert.index[i] == 1) and (insert.index[i + 2] - insert.index[i + 1] == 1):
            indexlist.extend([insert.index[i], insert.index[i + 1], insert.index[i + 2]])
            i += 3
        else:
            i += 1
    print(indexlist)
    extend = 0
    for i in range(0, len(df)-3):
        if extend > 0:
            extend -= 1
            if df.iloc[i][colum] < df.iloc[i - 1][colum]:
                df.loc[i, colum] = df.loc[i - 1, colum]
                continue
        boo = random.randint(0, 100)
        if boo > 99:
            ins = random.randint(0, len(insert) - 3)
            df.loc[i - 2, colum] = insert.iloc[ins][colum]
            df.loc[i - 1, colum] = insert.iloc[ins + 1][colum]
            df.loc[i, colum] = insert.iloc[ins + 2][colum]

        if (df.iloc[i][colum] > q[0]) and (df.iloc[i][colum] < q[1]):
            df.loc[i, colum] = q[1]

        if df.iloc[i][colum] > q[1]:
            df.loc[i, colum] = df.iloc[i][colum] * random.uniform(1.1, 1.3)
            extend = random.randint(0, 1)
    df[[colum]] = df[[colum]].astype(int)
    print(df)


def rundevice(colum):
    q = pd.Series([df[colum].quantile(0.10), df[colum].quantile(0.98)])
    insert = df[df[colum] > df[colum].quantile(.95)]
    indexlist = []
    i = 0
    while i < len(insert) - 3:
        if (insert.index[i + 1] - insert.index[i] == 1) and (insert.index[i + 2] - insert.index[i + 1] == 1):
            indexlist.extend([insert.index[i], insert.index[i + 1], insert.index[i + 2]])
            i += 3
        else:
            i += 1
    print(indexlist)
    extend = 0
    for i in range(0, len(df)-3):
        if extend > 0:
            extend -= 1
            if df.iloc[i][colum] < df.iloc[i - 1][colum]:
                df.loc[i, colum] = df.loc[i - 1, colum]
                continue
        boo = random.randint(0, 100)
        if boo > 99:
            ins = random.randint(0, len(insert) - 3)
            df.loc[i - 2, colum] = insert.iloc[ins][colum]
            df.loc[i - 1, colum] = insert.iloc[ins + 1][colum]
            df.loc[i, colum] = insert.iloc[ins + 2][colum]

        if (df.iloc[i][colum] > q[0]) and (df.iloc[i][colum] < q[1]):
            df.loc[i, colum] = q[1]

        if df.iloc[i][colum] > q[1]:
            df.loc[i, colum] = df.iloc[i][colum] * random.uniform(1.1, 1.3)
            extend = random.randint(0, 1)
    df[[colum]] = df[[colum]].astype(int)
    print(df)


df = pd.read_csv('/home/cybercamp2023/git/lab2/data/activity/original.csv')
col = df.columns.values.tolist()
runsize('Size')
for j in range(2, len(col)):
    rundevice(col[j])
df.to_csv('/home/cybercamp2023/git/lab2/data/activity/edited.csv', index=False)

