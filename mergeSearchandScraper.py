import pandas as pd

df=pd.read_excel("checkAriSearch20210929.xlsx")
df1=pd.read_excel("finallist.xlsx")
print(df.columns)
print(df1.columns)

df["lowerKW"]=df["Keyword"].str.lower()
df["lowerKW"]=df["lowerKW"].str.replace(' ', '')
df1["lowerKW"]=df1["KW"].str.lower()
df1["lowerKW"]=df1["lowerKW"].str.replace(' ', '')
indomerge_shopee=pd.merge(df1,df, left_on=["Market","eCustomer","lowerKW","SKU ID"],right_on=["Market","eCustomer","lowerKW","ItemID"], how='left',indicator=True)
# indoshopee["eCustomer"]="Shopee"
# indoshopee["Market"]="ID"
# # merged_df["Brand"]=merged_df["Brand"].str.lower()
# # merged_df["Brand"] = merged_df["Brand"].str.replace(' ', '')
# indoshopee["lowerKW"]=indoshopee["KW"].str.lower().str.replace(" ","")



target=pd.read_excel("target.xlsx")
target["KW to check"]=target["KW to check"].str.lower()
target["KW to check"] = target["KW to check"].str.replace(' ', '')
indomerge_shopee=pd.merge(indomerge_shopee,target,left_on=["Market","lowerKW"],right_on=["Market","KW to check"],how='left')
indomerge_shopee["target"]=indomerge_shopee["target"].fillna("4/10")
indomerge_shopee["target2"]=indomerge_shopee["target2"].fillna(4)
indomerge_shopee["Date"]=indomerge_shopee["Date"].fillna("20211010")
print(indomerge_shopee["Time"].unique())
indomerge_shopee["Time"]=indomerge_shopee["Time"].fillna("00:00:00")
indomerge_shopee["Value"]=indomerge_shopee["Value"].fillna(0)
indomerge_shopee["Potision"]=indomerge_shopee["Potision"].fillna(0)
indomerge_shopee["Sponsored"].fillna("No",inplace=True)
indomerge_shopee.to_excel("finalcheckcheck.xlsx",index=False)