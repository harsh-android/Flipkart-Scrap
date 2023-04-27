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
url = "https://www.flipkart.com/search?q=iphone&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_7_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_7_na_na_na&as-pos=1&as-type=RECENT&suggestionId=iphone%7CMobiles&requestId=0e3a1efc-a109-4210-8b0a-1fad03b79f97&as-backfill=on";
# while True:
for item in range(1,10):
    
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
    price.append(pr.text)

  for de in box.find_all('ul',class_='_1xgFaf'):
    description.append(de.text)

  # for re in box.find_all('div',class_='_3LWZlK'):
  #   if(re.text == ''):
  #     review.append(' ')
  #   else:
  #     review.append(re.text)
  img = box.find_all('div',class_="CXW8mj")
  for im in img:
    ii  = im.find('img',class_='_396cs4')
    image.append(ii.get('src'))


  url = cnp
  print(cnp,"\n\n")
  if end == '':
    break
  
print("Name = ",len(name))
print("Price = ",len(price))
print("Description = ",len(description))
print("Image = ",len(image))
# print("Review = ",len(review))
  
df = pd.DataFrame({"Product Name":name,"Price":price,"Description":description,"Images":image})
df.to_csv("E:\Harsh\Python\FlipKart Scrap\Flipkart.csv")