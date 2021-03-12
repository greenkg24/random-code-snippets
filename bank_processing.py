import os
import re

import numpy as np
import pandas as pd

# define parameters
filepath = r''
grocery = "walmart|costco|safeway|wal-mart|food lion|trader joe"
car_gas = "sunoco|exxonmobil|aldie liberty|costco gas"
dine_out = "baker|chick-fil-a|king street|market house|kilwin|mcdonald|wendy|red horse|panda express|dunkin"
shopping = "target|marshalls|hydrapeak|amzn|amazon.com|sugar land|h&m|walgreens|amazon"
gym = "nordictrack"
phone = "sprint"
subscription = "amazon prime|highfitness|canva|apple|netflix|onedrive|covenant"
internet = "comcast"
college_fund = "invest529"
incoming_transfer = "from share"
outgoing_transfer = "to share"
debt_payment = "bank of america"|loan administration|mobile payment|payment to american express"
other_income = "remote deposit"
paycheck = "guidehouse"
water = "town of middlebu"
electric = "arcadia"
alcohol = "alcoholic beverage|abc|fine wine"
car_insurance = "geico"
home_improvement = "home depot|lowe|sherwin williams|millwork|harbor freight"
travel = "delta|hillman"
irregular_income = "usaa"

# functions
def miscellaneous(df):
	if df['subcategory'].isnull():
		df['subcategory'] == 'miscellaneous'
	else:
		break


# create subcategory column
df.loc[df['description'].str.contains(grocery), 'subcategory'] = 'grocery'
df.loc[df['description'].str.contains(car_gas), 'subcategory'] = 'car gas'
df.loc[df['description'].str.contains(dine_out), 'subcategory'] = 'dine out'
df.loc[df['description'].str.contains(shopping), 'subcategory'] = shopping'
df.loc[df['description'].str.contains(gym), 'subcategory'] = 'gym'
df.loc[df['description'].str.contains(phone), 'subcategory'] = 'phone'
df.loc[df['description'].str.contains(subscription), 'subcategory'] = 'subscription'
df.loc[df['description'].str.contains(internet), 'subcategory'] = 'internet'
df.loc[df['description'].str.contains(college_fund), 'subcategory'] = 'college fund'
df.loc[df['description'].str.contains(incoming_transfer), 'subcategory'] = 'incoming transfer'
df.loc[df['description'].str.contains(outgoing_transfer), 'subcategory'] = 'outgoing transfer'
df.loc[df['description'].str.contains(debt_payment), 'subcategory'] = 'debt payment'
df.loc[df['description'].str.contains(other_income), 'subcategory'] = 'other income'
df.loc[df['description'].str.contains(paycheck), 'subcategory'] = 'paycheck'
df.loc[df['description'].str.contains(water), 'subcategory'] = 'water'
df.loc[df['description'].str.contains(electric), 'subcategory'] = 'electric'
df.loc[df['description'].str.contains(alcohol), 'subcategory'] = 'alcohol'
df.loc[df['description'].str.contains(car_insurance), 'subcategory'] = 'car insurance'
df.loc[df['description'].str.contains(home_improvement), 'subcategory'] = 'home improvement'
df.loc[df['description'].str.contains(travel), 'subcategory'] = 'travel'
df.loc[df['description'].str.contains(irregular_income), 'subcategory'] = 'irregular income'

## test samples of df to spot check correct classification
df.sample(4)

# create category column based on subcategory
essential = "grocery|car gas|water|electric"
fixed = "phone|subscription|internet|car insurance"
saving = "college fund"
disposable = "dine out|shopping|miscellaneous|gym|alcohol|home improvement|travel|big purchase"
income = "paycheck|other income|irregular income"
liabilities = "debt payment"
transfers = "incoming transfer|outgoing transfer"

df.loc[df['subcategory'].str.contains(essential), 'category'] = 'essential'
df.loc[df['subcategory'].str.contains(fixed), 'category'] = 'fixed'
df.loc[df['subcategory'].str.contains(saving), 'category'] = 'saving'
df.loc[df['subcategory'].str.contains(disposable), 'category'] = 'disposable'
df.loc[df['subcategory'].str.contains(income), 'category'] = 'income'
df.loc[df['subcategory'].str.contains(liabilities), 'category'] = 'liabilities'
df.loc[df['subcategory'].str.contains(transfers), 'category'] = 'transfers'

## test sampling of df
df.sample(4)

 

