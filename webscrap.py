from bs4 import BeautifulSoup
import requests

url = "https://www.flipkart.com/search?q=laptop&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off";
# url = "https://www.practo.com/search/doctors?q=%5B%7B%22word%22%3A%22Dentist%22%2C%22autocompleted%22%3Atrue%2C%22category%22%3A%22subspeciality%22%7D%5D&city=Surat&results_type=doctor&location_type=locality&location_value=varachha%20road";



while True:
  response = requests.get(url)

  # print(response.status_code)

  htmlContatnt = response.content

  soup = BeautifulSoup(htmlContatnt, 'html.parser')

  np = soup.find("a",class_ = "_1LKTO3").get("href")

  cnp =   "https://www.flipkart.com/" + np

  url = cnp 