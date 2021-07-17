import csv
import pandas as pd

data=["ねずこ","たんじろう","きょうじゅろう","ぎゆう","げんや","かなお","ぜんいつ"]
col = ['name']

df = pd.DataFrame(data,columns=col)
print(df) 
df.to_csv("sample01.csv")