import os
import pandas as pd
#C:\Users\tan.j.53\Procter and Gamble\AMA eBiz Data Hub - Documents\XByte Data\KCP\2021\09.09\Search
path = r"C:\Users\tan.j.53\OneDrive - Procter and Gamble\KCP\2021\11.11\Search"
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
        df["Time"]=pd.to_datetime(df["Time"], format='%H%M%p').dt.time
        print(f.rsplit('\\', 2)[-1].rsplit('.', 2)[-2].rsplit('_', 7)[-1])
        df["Date"] = f.rsplit('\\', 2)[-1].rsplit('.', 2)[-2].rsplit('_', 4)[1]+f.rsplit('\\', 2)[-1].rsplit('.', 2)[-2].rsplit('_', 4)[2]+f.rsplit('\\', 2)[-1].rsplit('.', 2)[-2].rsplit('_', 4)[3]
        df = df.drop_duplicates(subset=['Category'
                                        ,'Date', 'Keyword', 'Potision', 'Market',
                                                    'eCustomer'], keep='last')
        (f.rsplit('\\', 2)[-1].rsplit('.', 2)[-2].rsplit('_', 4))
        all_data = all_data.append(df,ignore_index=True)



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
all_data["Sponsored"].fillna("No",inplace=True)
all_data["Sponsored"]= all_data["Sponsored"].map({'No': "No", 1.0: "Yes"})
all_data["SellerName"] = all_data["SellerName"].str.lower()
seller=pd.read_excel(r"C:\Users\tan.j.53\OneDrive - Procter and Gamble\Desktop\list of official stores for Shopee and Lzada by coutries.xlsx")
seller["Mapping"]=seller["Mapping"].str.lower()
all_data=pd.merge(all_data,seller,left_on=["SellerName","eCustomer","Market"],right_on=["Mapping","eCustomer","Market"],how='left')
all_data['Paid']=np.where( pd.notnull(all_data['Mapping']) & all_data['Sponsored'].str.startswith("Yes")  , 1, 0)

all_data['Organic']=np.where( pd.notnull(all_data['Mapping']) & all_data['Sponsored'].str.startswith("No")  , 1, 0)

all_data["Brand_scraper"]=all_data["Brand"]
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
all_data.loc[all_data['Keyword'].isin(['braun', 'braun electric razor',
'braun electric shaver','braun electric shavers',
'braun epilator',
'Braun Hair',
'braun ipl',
'braun ipl silk expert pro 5',
'braun ipl silk expert pro 6',
'braun ipl silk pro',
'braun series 7',
'braun series 9',
'braun shaver',
'braun silk epil 9',
'braun trimmer',
'electric razor',
'electric shave',
'electric shaver',
'electric shaver for men',
'electric shaver men',
'epilator',
'hair dryer',
'hair removal',
'Hair Clipper',
'hair removal ipl',
'hair remover',
'hair straightener',
'hair trimmer',
'ipl',
'ipl device',
'ipl devices',
'ipl hair removal',
'ipl hair removal device',
'ipl machine',

                                       ]),'Category'] = 'Appliances'
data1010=pd.read_excel("checkAriSearch20210929_1010.xlsx")
df_final = pd.concat([all_data, data1010])
df_final.to_excel("checkAriSearch20210929.xlsx")
