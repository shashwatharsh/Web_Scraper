import csv
from urllib.error import HTTPError
import requests
from bs4 import BeautifulSoup
import json

file = open('Amazon Scraping - Sheet1.csv')

csvreader = csv.reader(file)

header = []
header = next(csvreader)
print(header)

row = []
nos =0
jdata={}
for row in csvreader:
    # for rcol in row:
    country = row[3]
        
    asin = row[2]

    url = "https://www.amazon."+str(country)+"/dp/"+str(asin)
    req = requests.get(url)
    htmlcontent = req.content

    soup = BeautifulSoup(htmlcontent, 'html.parser')
    title = soup.title.get_text()
    print(url+" done!")
    img = soup.find_all('img')
    desc = soup.find_all('p')
    nos +=1
    jdata ={
        ""+str(nos)+"":{
            "url":""+str(url)+"",
        "title":""+str(title)+"",
        "image":""+str(img)+"",
        "description":""+str(desc)+""
        }
    }
    with open('data.json', 'a') as outfile:
        json.dump(jdata, outfile)


