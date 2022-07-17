import requests
from bs4 import BeautifulSoup


URL = "https://elnour-tech.com/product-category/laptop/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

laptops_dict = {}

laps = soup.find(class_="products grid large-block-grid-4 small-block-grid-2 medium-block-grid-2")

laptops = laps.find_all("li", class_="product-warp-item nasa-ver-buttons")

for l in laptops:
  name = l.find(class_="product-info-wrap").find(class_="name").text
  
  price = l.find(class_="product-info-wrap").find(class_="price").text

  laptops_dict[name] = price


for name, price in laptops_dict.items():
  # price = float(price[-1: -3])
  # if(price > 15000 and price < 21000):
  if(name.__contains__("RTX 3050") or name.__contains__("RTX 3050 Ti")):
    print(f"{name}: {price}")


