#!/usr/bin/env python
# coding: utf-8

# In[94]:


import os
import re

import numpy as np
import pandas as pd


# In[95]:


# define parameters
filepath = "C:\\Users\\kgreen001\\Finance_scripts"
save_filepath = "C:\\Users\\kgreen001\\Finance_scripts\\processed"
amex = 'amex_feb21_raw.xlsx'
macu = 'macu_feb21_raw.xlsx'
xlsx_file = 'processed_transactions.xlsx'
csv_file = 'processed_transactions.csv'


# In[96]:


# read in data
amex_file = pd.read_excel(filepath + "\\" + amex)
macu_file = pd.read_excel(filepath + "\\" + macu)
# drop unnecessary columnns
amex_file.drop(inplace=True, columns=['Card Member', 'Account #', 'Extended Details', 'Appears On Your Statement As', 'Address', 'City/State', 'Zip Code', 'Country', 'Reference', 'Category'])
macu_file.drop(inplace=True, columns=['Transaction ID', 'Effective Date', 'Transaction Type', 'Check Number', 'Reference Number', 'Type', 'Balance', 'Memo', 'Extended Description', 'Transaction Category'])


# In[97]:


# rearrange columns to match other
amex_file = amex_file[['Date', 'Amount', 'Description']]


# In[98]:


amex_file['account'] = 'amex'
macu_file['account'] = 'macu'


# In[99]:


# rename columns
macu_file.columns = ['date', 'amount', 'description', 'account']
amex_file.columns = ['date', 'amount', 'description', 'account']


# In[100]:


# append macu and amex dataframes together
df = macu_file.append(amex_file, ignore_index=False)


# In[101]:


# string to search
grocery = "walmart|costco|safeway|wal-mart|food lion|trader joe"
car_gas = "sunoco|exxonmobil|aldie liberty|costco gas"
dine_out = "baker|chick-fil-a|king street|market house|kilwin|mcdonald|wendy|red horse|panda express|dunkin"
shopping = "target|marshalls|hydrapeak|amzn|amazon.com|sugar land|h&m|walgreens|amazon"
gym = "nordictrack"
phone = "sprint"
subscription = "amazon prime|highfitness|canva|apple|netflix|onedrive|covenant|microsoft services"
internet = "comcast"
college_fund = "invest529"
incoming_transfer = "from share"
outgoing_transfer = "to share"
debt_payment = "bank of america|loan administration|mobile payment|payment to american express"
other_income = "remote deposit"
paycheck = "guidehouse"
water = "town of middlebu"
electric = "arcadia"
alcohol = "alcoholic beverage|abc|fine wine"
car_insurance = "geico"
home_improvement = "home depot|lowe|sherwin williams|millwork|harbor freight"
travel = "delta|hillman"
irregular_income = "usaa"


# In[102]:


# create subcategory column
df.loc[df['description'].str.contains(grocery, case=False, na=False), 'subcategory'] = 'grocery'
df.loc[df['description'].str.contains(car_gas, case=False, na=False), 'subcategory'] = 'car gas'
df.loc[df['description'].str.contains(dine_out, case=False, na=False), 'subcategory'] = 'dine out'
df.loc[df['description'].str.contains(shopping, case=False, na=False), 'subcategory'] = 'shopping'
df.loc[df['description'].str.contains(gym, case=False, na=False), 'subcategory'] = 'gym'
df.loc[df['description'].str.contains(phone, case=False, na=False), 'subcategory'] = 'phone'
df.loc[df['description'].str.contains(subscription,case=False, na=False), 'subcategory'] = 'subscription'
df.loc[df['description'].str.contains(internet,case=False, na=False), 'subcategory'] = 'internet'
df.loc[df['description'].str.contains(college_fund, case=False,na=False), 'subcategory'] = 'college fund'
df.loc[df['description'].str.contains(incoming_transfer,case=False, na=False), 'subcategory'] = 'incoming transfer'
df.loc[df['description'].str.contains(outgoing_transfer,case=False, na=False), 'subcategory'] = 'outgoing transfer'
df.loc[df['description'].str.contains(debt_payment,case=False, na=False), 'subcategory'] = 'debt payment'
df.loc[df['description'].str.contains(other_income,case=False, na=False), 'subcategory'] = 'other income'
df.loc[df['description'].str.contains(paycheck,case=False, na=False), 'subcategory'] = 'paycheck'
df.loc[df['description'].str.contains(water,case=False, na=False), 'subcategory'] = 'water'
df.loc[df['description'].str.contains(electric,case=False, na=False), 'subcategory'] = 'electric'
df.loc[df['description'].str.contains(alcohol,case=False, na=False), 'subcategory'] = 'alcohol'
df.loc[df['description'].str.contains(car_insurance,case=False, na=False), 'subcategory'] = 'car insurance'
df.loc[df['description'].str.contains(home_improvement,case=False, na=False), 'subcategory'] = 'home improvement'
df.loc[df['description'].str.contains(travel,case=False, na=False), 'subcategory'] = 'travel'
df.loc[df['description'].str.contains(irregular_income,case=False, na=False), 'subcategory'] = 'irregular income'


# In[103]:


## test samples of df to spot check correct classification
df.sample(4)


# In[104]:


# check for nulls
df[df['subcategory'].isnull()]


# In[105]:


## fill null values with miscellaneous category
df.fillna("miscellaneous", inplace=True)
## check for null values
df[df['subcategory'].isnull()]


# In[106]:


# create category column based on subcategory
essential = "grocery|car gas|water|electric"
fixed = "phone|subscription|internet|car insurance"
saving = "college fund"
disposable = "dine out|shopping|miscellaneous|gym|alcohol|home improvement|travel|big purchase"
income = "paycheck|other income|irregular income"
liabilities = "debt payment"
transfers = "incoming transfer|outgoing transfer"


# In[107]:


df.loc[df['subcategory'].str.contains(essential, case=False, na=False), 'category'] = 'essential'
df.loc[df['subcategory'].str.contains(fixed, case=False, na=False), 'category'] = 'fixed'
df.loc[df['subcategory'].str.contains(saving, case=False, na=False), 'category'] = 'saving'
df.loc[df['subcategory'].str.contains(disposable, case=False, na=False), 'category'] = 'disposable'
df.loc[df['subcategory'].str.contains(income, case=False, na=False), 'category'] = 'income'
df.loc[df['subcategory'].str.contains(liabilities, case=False, na=False), 'category'] = 'liabilities'
df.loc[df['subcategory'].str.contains(transfers, case=False, na=False), 'category'] = 'transfers'


# In[108]:


## test sampling of df
df.sample(4)


# In[109]:


## check for null values
df[df['category'].isnull()]


# In[110]:


# exploring and filtering data
mask = df['description']
mask1 = df['category']
mask2 = df['subcategory']
mask3 = df['account']


# In[111]:


# export to excel or csv
df.to_excel(save_filepath + "\\" + xlsx_file)
df.to_csv(save_filepath + "\\" + csv_file, index=False)




