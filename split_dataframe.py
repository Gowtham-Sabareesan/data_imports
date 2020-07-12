#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def split_dataframe(df):
    
    horizontal_nulls = list(df[df.isnull().all(axis=1)].index)

    sliced_df = []
    for i in range(len(horizontal_nulls) - 1):
        sliced_df.append(df.iloc[horizontal_nulls[i]+1:horizontal_nulls[i+1],:])

    cleaned_df = []
    for _df in sliced_df:
        cleaned_df.append(_df.dropna(axis=1, how='all'))

    return(cleaned_df[-3],cleaned_df[-2])

