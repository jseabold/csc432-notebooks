# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <headingcell level=2>

# Introduction to Pandas

# <markdowncell>

# This is a brief 5-minute introduction to **pandas**. 5-minutes isn't even enough time to scratch the surface of pandas. I encourage you to go through the official [pandas documentation](http://pandas.pydata.org/pandas-docs/stable/) to really get a feel for what the library can do. Or better yet, purchase [Python for Data Analysis](http://www.amazon.com/gp/product/1449319793/ref=as_li_ss_tl?ie=UTF8&camp=1789&creative=390957&creativeASIN=1449319793&linkCode=as2&tag=scistapro-20) by Wes McKinney.

# <headingcell level=4>

# Import Convention

# <codecell>

import pandas as pd

# <headingcell level=4>

# Reading in Data

# <codecell>

import os

path = "/home/skipper/school/csc432/notebooks/"
target = os.path.join(path, "data", "salary_table.csv")
salary_data = pd.read_csv(target)

# <codecell>

type(salary_data)

# <codecell>

salary_data.head(5)

# <codecell>

salary_data["job_role"]

# <codecell>

salary_data.ix[:5]

# <headingcell level=4>

# Grouping the data

# <codecell>

grouped = salary_data.groupby("job_role")

# <codecell>

grouped.mean()

# <headingcell level=4>

# Time-Series

# <codecell>

dates = pd.date_range('1/1/2000', periods=50)
df = pd.DataFrame(np.random.randn(50, 4), index=dates, 
                  columns=['A', 'B', 'C', 'D'])

# <codecell>

pd.set_printoptions(max_rows=49)

# <codecell>

df

# <codecell>

df.head(5)

# <codecell>

df.ix["2000-1-5":"2000-1-15"]

# <codecell>

df.resample("W")

# <codecell>

df.ix["2000-1-3":"2000-1-9"].mean()

# <headingcell level=4>

# Creating New Variables

# <codecell>

df["xs_mean"] = 0.0
df["xs_mean"] = df.mean(axis=1)

# <codecell>

df.head(5)

