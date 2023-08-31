import pandas as pd
mydict = {"Country": ["Brazil", "Russian", "India", "China", "South Africa"], "Capital": ["Brasilia", "Moscow", "New Delhi", "Beijing", "Pretoria"], "Currency":["R$", "Russian Ruble", "Indian Rupee", "Chinese Yuan", "South African Rand"], "Currency_Sym": ["A", "B", "C", "D", "E"]}

country_info = pd.DataFrame(mydict)
country_info.index = ["BR", "RU", "IN", "CH", "SA"] # replacing the left most column with custom indexes

new = country_info["Country"].copy() # making a copy of Country Feature column
country_info["Currency"] = country_info["Currency_Sym"].str.cat(new, sep=", ") # concat Currency_Sym with Currency

print(country_info)

# reading from csv
BFA = pd.read_csv('bodyfat.csv')
# print(BFA[2:3]) # accessing the 2nd row - same as slicing mechanism
print(BFA.info())
