#test

import pandas as pd
#opgave 5.a
url5a = "https://api.statbank.dk/v1/data/FOLK1A/CSV?valuePresentation=CodeAndValue&delimiter=Semicolon&Tid=2020K1%2C2008K1&OMR%C3%85DE=000&CIVILSTAND=G%2CF"
data5a = pd.read_csv(url5a,sep=';')
print(data5a)
pctIn2008 = (data5a["INDHOLD"][1]/data5a["INDHOLD"][0]*100)
pctIn2020 = (data5a["INDHOLD"][3]/data5a["INDHOLD"][2]*100)
increase = pctIn2020 - pctIn2008
increase20 = (data5a["INDHOLD"][3]/data5a["INDHOLD"][2]*100-data5a["INDHOLD"][1]/data5a["INDHOLD"][0]*100)
print(increase20)
#opgave 5.b
url = 'https://api.statbank.dk/v1/data/FOLK1A/CSV?valuePresentation=CodeAndValue&delimiter=Semicolon&Tid=2020K1&CIVILSTAND=TOT%2CU&K%C3%98N=TOT&OMR%C3%85DE=101%2C851%2C561%2C461%2C751&ALDER=IALT'
data = pd.read_csv(url,sep=';')
not_married_pct = {data['OMRÅDE'][not_married][4:]:data['INDHOLD'][not_married]/data['INDHOLD'][all_people]*100 for not_married, all_people in zip(range(5,10),range(0,5))}
#result = {}
#for not_married, all_people in zip(range(5,10),range(0,5)):
#    pct_not_married = data['INDHOLD'][not_married]/data['INDHOLD'][all_people]*100
#    city = data['OMRÅDE'][not_married][4:]
#    result[city] = pct_not_married
sorted(not_married_pct,key=not_married_pct.get, reverse=True)
print(not_married_pct)

#opgave 5.c






#opgave 5.d