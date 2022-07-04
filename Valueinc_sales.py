# -*- coding: utf-8 -*-
"""
Created on Sat May 14 10:44:05 2022

@author: Jeffa
"""

import pandas as pd

# file name = pd.read_csv('file.csv') <----- Format of read_csv
data = pd.read_csv('transaction2.csv')
data = pd.read_csv('transaction2.csv', sep =  ";")

#summary of the data
data.info()

# working with calculations
# defining variables

CostPerItem = 11.73
SellingPricePerItem = 21.11
NumberOfItemsPurchased = 6

#Math Operations on Tableau
ProfitPerItem = SellingPricePerItem - CostPerItem

ProfitPerTransaction = NumberOfItemsPurchased * ProfitPerItem
CostPerTransaction = CostPerItem * NumberOfItemsPurchased

# SellingPricePer Transaction is also Total Revenue 
SellingPricePerTransaction = SellingPricePerItem * NumberOfItemsPurchased

#CostPerTransaction Column Calculation
#CostPerTransaction  = CostPerItem * NumberOfItemsPurchased
#Variable = Dataframe['coloumn_name']

CostPerItem = data["CostPerItem"]
NumberOfItemsPurchased = data["NumberOfItemsPurchased"]
CostPerTransaction = CostPerItem * NumberOfItemsPurchased

#adding a new coloum to data frame

data["CostPerTransaction"] = CostPerTransaction 
#  OR 
data["CostPerTransaction"] = data["CostPerItem"] * data["NumberOfItemsPurchased"]
 
# Sales Per Transaction
data["SalesPerTransaction"] = data["SellingPricePerItem"] * data["NumberOfItemsPurchased"]

#Profit Calculation

data["Profit"] = data["SalesPerTransaction"] - data["CostPerItem"]
# Markup = (Sales-Costs)/Costs      ----------------   you can use the full formula below or use the data["SalesPerTransaction"] variable
data["Markup"] = ( data["SalesPerTransaction"] - data["CostPerTransaction"]  ) / data["CostPerTransaction"]

#Rounding the Markup
roundmarkup = round(data["Markup"],2 )    
data["Markup"] = round(data["Markup"],2)                                                     

#combing data fields

my_name = 'John'+' Rad' 
my_date = 'Day'+"-"+'Month'+'-'+'Year'

#my_date = data['Day'] + '_'

#checking coloumns data type

print(data["Day"].dtype)

#change Columns type,   Converting Ints to strs- Printing to double check the data type

Day = data["Day"].astype(str)
Year = data["Year"].astype(str)
print(Day.dtype)
print(Year.dtype)
# Adding the str month and variable year/ day to the columns. Month is different due to it already being a str in the data, vs an int
my_date = Day+'-'+data['Month']+'-'+Year

data['date'] = my_date

# using iloc to view specific columsn/rows

data.iloc[0]  # viewing rows with index = 0
data.iloc[0:3]  #viewing first 3 rows
data.iloc[0:6]  # viewing first 6 rows 
data.iloc[-5]  #brings last 5 rows

data.head(5) #brings first 5 rows

data.iloc[:,2] #brings in all rows from the 2nd column
data.iloc[4,2] #brings in 4th row, 2nd columns

#using split to split the client keyword field
#new_var = Colimn.str.split('sep' , expand = True)

split_col = data['ClientKeywords'].str.split(',' , expand=True)
#creating new coloumns for the split columns in the Client Keywords

data['ClientAge'] = split_col[0]
data['Clienttype'] = split_col[1]
data['LenghtofContract'] = split_col[2]

# using the replace function

data['ClientAge'] = data['ClientAge'].str.replace('[' , '')
data['LenghtofContract'] = data['LenghtofContract'].str.replace(']' , '')

# using the lower function to change item to lowercase
data['ItemDescription'] = data['ItemDescription'].str.lower()

#how to merge files
#binging in a new dataset

seasons = pd.read_csv('value_inc_seasons.csv', sep =  ";")

#mergin files: merge_df = pd.merge(df_old, df_new, on = 'key')
data = pd.merge(data, seasons, on = "Month")


#dropping columns
# df = df.drop('columnname' , axis =1)
data = data.drop('ClientKeywords' , axis = 1)
data = data.drop('Day' , axis = 1)
data = data.drop(['Year', 'Month'] , axis = 1)


#Export into a CSV file

data = data.to_csv('ValueInc_Cleaned.csv' , index = False)


