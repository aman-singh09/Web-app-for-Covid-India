import matplotlib.pyplot as plt
import requests 
from bs4 import BeautifulSoup
import geopandas as gpd
link = 'https://www.mohfw.gov.in/'

import pandas as pd
req = requests.get(link)

soup = BeautifulSoup(req.content, "html.parser")
thead = soup.find_all('thead')[-1]

head = thead.find_all('tr')

tbody = soup.find_all('tbody')[-1]

body = tbody.find_all('tr')
head_rows = []

body_rows = []

for tr in head:
    td = tr.find_all(['th', 'td'])
    row = [i.text for i in td]
    head_rows.append(row)



for tr in body:
    td = tr.find_all(['th', 'td'])
    row = [i.text for i in td]
    body_rows.append(row)

new_cols = ["Sr.No", "States","Confirmed","Recovered","Deceased"]
df_bs = pd.DataFrame(body_rows[:len(body_rows)-6],columns=head_rows[0])         


df_bs.drop('S. No.', axis=1, inplace=True)

df_bs['Name of State / UT'] = df_bs['Name of State / UT'].str.replace('#', '')
# print(df_bs)

plt.figure(figsize=(28,15))

plt.barh(df_bs["Name of State / UT"],df_bs["Active Cases*"].map(int),  color = 'blue',align='center')
plt.gca().invert_yaxis()
plt.title("Number of Active Covid-19 cases in India",fontsize = 30)
plt.xlabel("Active Cases", fontsize=30)
plt.ylabel("State/UT", fontsize=30)
plt.xticks(fontsize = 14)
plt.yticks(fontsize = 14)
