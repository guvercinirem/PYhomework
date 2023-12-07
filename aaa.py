#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 10:24:38 2023

@author: iremguvercin
"""

import pandas as pd
import numpy as np
import warnings

df=pd.read_csv("/Users/iremguvercin/Downloads/poke_updated1.csv")

pd.set_option("display.max_columns",None)



def check_df(dataframe):
    print("##################### Shape #####################")
    print(dataframe.shape)
    print("##################### Types #####################")
    print(dataframe.dtypes)
    print("##################### Head #####################")
    print(dataframe.head(7))
    print("##################### Tail #####################")
    print(dataframe.tail(7))
    print("##################### NA #####################")
    print(dataframe.isnull().sum())
    print("##################### Quantiles #####################")
    print(dataframe.describe().T)


check_df(df)

df.loc[df.Name.str.contains("aur")]
df.loc[~df.Name.str.contains("aur")]
df.loc[df.Speed>=100]
df.loc[df.Generation==2]
df.loc[df.Legendary==True]
df.columns=[col.lower() for col in df.columns]
df.columns=[col.replace(' ','_') for col in df.columns]

df.loc[df.type_1.str.contains("Dark")]
df["count1"]=0
df.groupby(["type_1","speed","defense"]).count()["count1"]
df.groupby(["type_1","speed","defense"]).size()

df.describe()
df.drop("#",axis=1,inplace=True)
df["type_2"] #386 tane n/a var
df["type_2"].unique()
df["type_2"].nunique()
df["type_2"].median()
df["type_2"].value_counts()
df["type_2"].isnull()
df["type_2"].fillna("Flying",inplace=True)
df["type_2"].isnull().sum()
df.head(20)

df.speed.max()
df.loc[df.speed==180]


df.speed.min()
df.loc[df.speed==5]




df.total.mean()

grupdf=df.groupby("name")[["total","attack","defense"]].mean()
ordereddf=grupdf.sort_values(by=["total"],ascending=False)
ordereddf.head()



































