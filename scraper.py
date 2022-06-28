from selenium import webdriver
from bs4 import BeautifulSoup
import time 
import csv
import pandas as pd
import requests
# find td in every tr tag and if the td tag has the anchor tag then do the else if part
start_url = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"


templist_arr = []
            
page = requests.get(start_url)
soup = BeautifulSoup(page.text, "html.parser")
star_table = soup.find_all("table")
table_rows = star_table[7].find_all('tr')

for row in table_rows:
    td_tags = row.find_all("td")
    row_data= [i.text.strip() for i in td_tags]
    templist_arr.append(row_data)
                                    
star_name = []
distance = [] 
mass = []
radius = []
print(templist_arr[:10])
for i in range(1,len(templist_arr)):
    star_name.append(templist_arr[i][0])
    distance.append(templist_arr[i][5])
    mass.append(templist_arr[i][7])
    radius.append(templist_arr[i][8])
                    

df = pd.DataFrame(list(zip(star_name , distance , mass , radius )) , columns = ["Star_Name" , "Distance" , "Star_Mass" , "Star_Radius" ])
df.to_csv("Brown_star_main.csv")
