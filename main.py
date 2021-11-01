import os
import pandas as pd
#C:\Users\tan.j.53\Procter and Gamble\AMA eBiz Data Hub - Documents\XByte Data\KCP\2021\09.09\Search
path = r"C:\Users\tan.j.53\OneDrive - Procter and Gamble\Desktop\2021"
import numpy as np
import pandas as pd
import glob
all_data = pd.DataFrame()

for f in glob.glob(path+"\**\*.xlsx",recursive=True):
    print("hi")
    if "Search" in f:
        print(f)
        df = pd.read_excel(f)
        df["Time"]=f.rsplit('\\', 2)[-1].rsplit('.', 2)[-2].rsplit('_', 7)[-1]
        df["Time"]=pd.to_datetime(df["Time"], format='%I%M%p').dt.time
        print(f.rsplit('\\', 2)[-1].rsplit('.', 2)[-2].rsplit('_', 7)[-1])
        df["Date"] = f.rsplit('\\', 2)[-1].rsplit('.', 2)[-2].rsplit('_', 4)[1]+f.rsplit('\\', 2)[-1].rsplit('.', 2)[-2].rsplit('_', 4)[2]+f.rsplit('\\', 2)[-1].rsplit('.', 2)[-2].rsplit('_', 4)[3]
        print(f.rsplit('\\', 2)[-1].rsplit('.', 2)[-2].rsplit('_', 4))
        all_data = all_data.append(df,ignore_index=True)

all_data["Date"] = all_data["Date"] .map({'IDSearch10-10-2021': '20211010',
                                          'MYSearch10-10-2021':'20211010',
'PHSearch10-10-2021':'20211010',
                                          'SGSearch10-10-2021': '20211010',
                                          'THSearch10-10-2021': '20211010',
'VNSearch10-10-2021': '20211010'
                                       }).fillna(all_data["Date"] )
print(all_data['Date'].unique())
all_data['Date']=all_data['Date'].replace(['09102021'], '20211009')
all_data['Date']=all_data['Date'].replace(['08102021'], '20211008')
all_data['Date']=all_data['Date'].replace(['08092021'], '20210908')
all_data['Date']=all_data['Date'].replace(['09092021'], '20210909')
all_data['Date']=all_data['Date'].replace(['10092021'], '20210910')
all_data['Date']=all_data['Date'].replace(['10102021'], '20211010')


#
all_data=all_data.drop_duplicates(subset=['Date', 'Time', 'Keyword', 'Potision', 'Market',
       'eCustomer'], keep='last')
print(all_data["Market"])
all_data = all_data[( (all_data['Keyword'] != "Shampoo")|(all_data['Market'] != "MY") )]
all_data["Keyword2"]=all_data["Keyword"].str.lower()
all_data["Keyword2"]=all_data["Keyword2"].str.replace(' ', '')
#
brand_keyword=pd.read_excel("brand_keyword.xlsx")
brand_keyword["Keyword"]=brand_keyword["Keyword"].str.lower()
brand_keyword["Keyword"]=brand_keyword["Keyword"].str.replace(' ', '')
pat =  '('+'|'.join(brand_keyword['Keyword'].str.split().str[-1])+')'
print(all_data.columns)
all_data['Date']=all_data['Date'].replace(['08092021'], '20210908')
all_data['Date']=all_data['Date'].replace(['09092021'], '20210909')
all_data['category type2'] = ('Brand ' + all_data['Keyword2'].str.extract(pat)).fillna('Category Keyword')
all_data['category type'] = np.where(all_data['category type2'].str.startswith('Brand'), 'Brand', 'Category')
all_data["Brand2"]=all_data["Category"]
category_mapping=pd.read_excel(r"category_rules.xlsx")

category_mapping["Brand"]=category_mapping["Brand"].str.lower()
all_data["Brand2"]=all_data["Brand2"].str.lower()
#all_data=pd.merge(all_data,category_mapping,left_on=["Brand2"],right_on="")
all_data=all_data.replace({'Brand2' : { 'head and shoulders' : "head & shoulders",
                                         'gillette venus' : "venus",

                                         }})
all_data=pd.merge(all_data,category_mapping,left_on="Brand2",right_on="Brand",how="left")

all_data["Sponsored"].fillna("No",inplace=True)
all_data["Sponsored"]= all_data["Sponsored"].map({'No': "No", 1.0: "Yes"})
all_data["SellerName"] = all_data["SellerName"].astype(str)
all_data['Paid']=np.where(all_data['SellerName'].str.contains('pampers_official_store|pampersofficial|Lazada Retail P&G|P&G Chăm Sóc Gia Đình|P&G Official Shop|P&G|P&G Beauty|P&G Home Care|P&G Official Store|Braun|Braun Official Store|braunofficialstore|braunphilippines|Lazada Retail P&G|Lazada Retail Olay|Lazada Retail Pampers|pgofficial|pgofficialstore|pgstoremy|P&G|Pampers|olay_official_shop|olay.my|olayofficialstore|pg_officialstorevn|olay_officialstorevn|pampers_officialstore|pg_official_store|pampersdiaper|Gilette|braunofficialstore|pghomecare_officialstore|pghomecareofficialstore|pgbeautyofficialstore') & all_data['Sponsored'].str.startswith("Yes")  , 1, 0)

all_data['Organic']=np.where(all_data['SellerName'].str.contains('pampers_official_store|pampersofficial|Lazada Retail P&G|P&G Chăm Sóc Gia Đình|P&G Official Shop|P&G|P&G Beauty|P&G Home Care|P&G Official Store|Braun|Braun Official Store|braunofficialstore|braunphilippines|Lazada Retail P&G|Lazada Retail Olay|Lazada Retail Pampers|pgofficial|pgofficialstore|pgstoremy|P&G|Pampers|olay_official_shop|olay.my|olayofficialstore|pg_officialstorevn|olay_officialstorevn|pampers_officialstore|pg_official_store|pampersdiaper|Gilette|braunofficialstore|pghomecare_officialstore|pghomecareofficialstore|pgbeautyofficialstore') & all_data['Sponsored'].str.startswith("No")  , 1, 0)
#all_data["checkdifference"]=np.where(all_data["Keyword"].str.lower().replace(' ', '') ==all_data["Brand"].str.lower().replace(' ', ''), 1, 0)
print(all_data.columns)
#Index(['Id', 'Category_x', 'Date', 'Time', 'Keyword', 'Potision', 'ItemID',
      #  'ShopID', 'pageurl', 'Name', 'SellerName', 'Sponsored', 'Market',
      #  'eCustomer', 'Brand_x', 'Keyword2', 'category type2', 'category type',
      #  'Brand2', 'Brand_y', 'Category_y', 'Paid', 'Organic'],
      # dtype='object')
all_data.rename(columns={'Category_x':'Brand', 'Brand_x':'Brand_scraper'}, inplace=True)
all_data.rename(columns={'Category_y':'Category'}, inplace=True)
all_data=all_data[['Id', 'Category', 'Date', 'Time', 'Keyword', 'Potision', 'ItemID',
       'ShopID', 'pageurl', 'Name', 'SellerName', 'Sponsored', 'Market',
       'eCustomer', 'Brand_scraper', 'Keyword2', 'category type2', 'category type'
       , 'Paid', 'Organic','Brand']]
def conditions_check(s):
    if (s['Organic'] == 1) and (s['Paid'] == 0):
        return "Organic"
    elif (s['Organic'] == 0) and (s['Paid'] == 1):
        return "Paid"
    elif (pd.notnull(s['Brand_scraper'])) and (s['Organic'] == 0) and (s['Paid'] == 0):
        return"PGOthers"
    else:
        return "Othersbrand "
all_data['KPI']=all_data.apply(conditions_check,axis=1)
all_data['Value']=1
all_data.to_excel("checkAriSearch20210929.xlsx")
all_data.to_excel("checkAriSearch.xlsx",index=False)
shop_id=pd.read_excel(r"C:\Users\tan.j.53\Downloads\data (21).xlsx")
final_checkbrand=pd.merge(all_data,shop_id,left_on=["ItemID"], right_on=["Product ID"],how='left')
final_checkbrand.to_excel("hiAri.xlsx")
