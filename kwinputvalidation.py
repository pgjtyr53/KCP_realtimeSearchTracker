import pandas as pd
sg=pd.read_excel(r"C:\Users\tan.j.53\OneDrive - Procter and Gamble\Project42\Campaign\11.11.2021\11.11 Search scraper keywords for Gina.xlsx",sheet_name="SG",header=1)
sg["Country"]="SG"
my=pd.read_excel(r"C:\Users\tan.j.53\OneDrive - Procter and Gamble\Project42\Campaign\11.11.2021\11.11 Search scraper keywords for Gina.xlsx",sheet_name="MY",header=1)
my["Country"]="MY"
vn=pd.read_excel(r"C:\Users\tan.j.53\OneDrive - Procter and Gamble\Project42\Campaign\11.11.2021\11.11 Search scraper keywords for Gina.xlsx",sheet_name="VN",header=1)
vn["Country"]="VN"
ph=pd.read_excel(r"C:\Users\tan.j.53\OneDrive - Procter and Gamble\Project42\Campaign\11.11.2021\11.11 Search scraper keywords for Gina.xlsx",sheet_name="PH",header=1)
ph["Country"]="PH"
id=pd.read_excel(r"C:\Users\tan.j.53\OneDrive - Procter and Gamble\Project42\Campaign\11.11.2021\11.11 Search scraper keywords for Gina.xlsx",sheet_name="ID",header=1)
id["Country"]="ID"
th=pd.read_excel(r"C:\Users\tan.j.53\OneDrive - Procter and Gamble\Project42\Campaign\11.11.2021\11.11 Search scraper keywords for Gina.xlsx",sheet_name="TH",header=1)
th["Country"]="TH"
merged_df = pd.concat([sg, my,vn,ph,id,th])
print(merged_df)
#forjuoutput
merged_df.to_excel("testest.xlsx")
merged_df.to_excel("final_kwinputvaldiation.xlsx")
# merged_df.to_excel("checkinput.xlsx",index=False)
#
#
# merged_df.to_excel("final_kwinputvaldiation.xlsx",index=False)