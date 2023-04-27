from bs4 import BeautifulSoup
import requests
import pandas as pd

name = []
price = []
image = []
description = []
review = []

# url = "https://www.practo.com/search/doctors?q=%5B%7B%22word%22%3A%22Dentist%22%2C%22autocompleted%22%3Atrue%2C%22category%22%3A%22subspeciality%22%7D%5D&city=Surat&results_type=doctor&location_type=locality&location_value=varachha%20road";

# for i in range(1,10):
url = "https://www.flipkart.com/search?q=laptop&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page=1";
while True:
  response = requests.get(url)
  # print(response.status_code)

  soup = BeautifulSoup(response.content, 'html.parser')
  end = ''
  for np in soup.find_all("a",class_="_1LKTO3"):
  # end = np.get("href")
    end = np.get('href')
  print(end,"\n")
  cnp =   "https://www.flipkart.com" + end 
  
  box = soup.find('div',class_='_1YokD2 _3Mn1Gg')

  for na in box.find_all('div',class_='_4rR01T'):
    name.append(na.text)

  for pr in box.find_all('div',class_='_30jeq3 _1_WHN1'):
    price.append(na.text)

  for de in box.find_all('div',class_='_1xgFaf'):
    description.append(de.text)

  for re in box.find_all('div',class_='_3LWZlK'):
    review.append(re.text)

  for im in box.find_all('div',class_='_396cs4'):
    image.append(re.get('src'))


  url = cnp
  print(cnp,"\n\n")
  if end == '':
    break
  
df = pd.DataFrame({"Product Name":name,"Price":price,"Description":description,"Review":review,"Images":image})
df.to_csv("E:\Harsh\Python\FlipKart Scrap\Flipkart.csv")