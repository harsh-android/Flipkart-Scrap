from bs4 import BeautifulSoup
import requests
import pandas as pd

link = []
image = []
title = []
description = []
price = []
rate = []

url = "https://www.flipkart.com/search?q=laptop&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"


while True:

    response = requests.get(url)

    soup = BeautifulSoup(response.content, 'html.parser')

    mainBox = soup.find('div',class_="_1YokD2 _3Mn1Gg")

    an = soup.find_all('a', class_="_1fQZEK")

    for i in an:
        inLink = i.get('href')
        link.append("https://www.flipkart.com"+inLink)
        img = i.find('img', class_="_396cs4")
        image.append(img)
        ti = i.find('div',class_="_4rR01T").text
        title.append(ti)
        des = i.find('ul',class_="_1xgFaf").text
        description.append(des)
        pr = i.find('div',class_="_30jeq3 _1_WHN1").text
        price.append(pr)
        rt = i.find('span',{"class":"_3LWZlK"})
        # rt1 = rt.replace('<div class="_3LWZlK">', "")
        # rt2 = rt.replace('<img class="_1wB99o" src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxMyIgaGVpZ2h0PSIxMiI+PHBhdGggZmlsbD0iI0ZGRiIgZD0iTTYuNSA5LjQzOWwtMy42NzQgMi4yMy45NC00LjI2LTMuMjEtMi44ODMgNC4yNTQtLjQwNEw2LjUuMTEybDEuNjkgNC4wMSA0LjI1NC40MDQtMy4yMSAyLjg4Mi45NCA0LjI2eiIvPjwvc3ZnPg=="/></div>', "")
        rate.append(rt)
        # print(rt)


    end = ''
    for np in mainBox.find_all("a",class_="_1LKTO3"):
        end = np.get('href')
    print(end,"\n")
    cnp =   "https://www.flipkart.com" + end 
    url = cnp
    if end == '':
        break
    
print("Name = ",len(title))
print("Price = ",len(price))
print("Description = ",len(description))
print("Image = ",len(image))
print("Link = ",len(link))
print("Rate = ",len(rate))

df = pd.DataFrame({"Product Name":title,"Price":price,"Description":description,"Images":image,"Rate":rate,"Link":link})
df.to_csv("E:\Harsh\Python\FlipKart Scrap\LaptopFlipkart.csv")