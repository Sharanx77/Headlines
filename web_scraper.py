import requests
from bs4 import BeautifulSoup
url="https://www.bbc.com/news"
f=open("urls.txt","w")
print("Welcome to the Web Scraper App!")
response =requests.get(url)
headlines =[]
line=BeautifulSoup(response.text,'html.parser')
for item in line.find_all('h2'):
    headlines.append(item.get_text())       
for headline in headlines:
    f.write(headline + "\n")
print("Headlines have been saved to 'urls.txt'.")
f.close()
print("Exiting the Web Scraper App. Goodbye!")
