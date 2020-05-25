import matplotlib.pyplot as plt
import seaborn as sns
import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.mohfw.gov.in/'

web_content = requests.get(url).content

soup = BeautifulSoup(web_content, "html.parser")

extract_contents = lambda row: [x.text.replace('\n', '') for x in row]

stats = [] 
all_rows = soup.find_all('tr')
for row in all_rows:
    stat = extract_contents(row.find_all('td')) 

    if len(stat) == 5:
        stats.append(stat)  

new_cols = ["Sr.No", "States/UT","Confirmed","Recovered","Deceased"]
state_data = pd.DataFrame(data = stats, columns = new_cols)


state_data["Confirmed"] = state_data["Confirmed"].astype(int)


sns.set_style('ticks')
plt.figure(figsize = (15,10))
plt.barh(state_data['States/UT'],    state_data['Confirmed'].map(int),align = 'center', color = 'lightblue', edgecolor = 'blue')    
plt.gca().invert_yaxis()
plt.xticks(fontsize = 14)
plt.yticks(fontsize = 14)
plt.title('Total Confirmed Cases Statewise', fontsize = 18 )
for index, value in enumerate(state_data['Confirmed']):
    plt.text(value, index, str(value), fontsize = 12)
