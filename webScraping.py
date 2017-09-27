import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
my_url="https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphics%20card"
uClient=uReq(my_url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, "html.parser")
containers = page_soup.findAll("div",{"class":"item-container"})
container = containers[0]
container.findAll("a",{"class":"item-tile"})
filename="products.csv"
f = open(filename,"w")
headers="brand, product_name, shipping \n"
f.write(headers)
for container in containers:
	brand = container.div.div.a.img["title"]

	title_container=container.findAll("a",{"class":"item-title"})
	product_name=title_container[0].text

	shipping_container = container.findAll("li",{"class":"price-ship"})
	shipping_cost=shipping_container[0].text.strip()
	
	print(product_name)
	print(shipping_cost)

	f.write(brand + ","+ product_name.replace(",","|") + "," + shipping_cost + "\n")
f.close()
