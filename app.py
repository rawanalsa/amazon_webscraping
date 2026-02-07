# This app scraps product data from Amazon website 

#BeautifulSoup4
#requests
#lxml
#selenium
#webdriver-manager

from cProfile import label
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import csv

url = "https://www.amazon.com/Apple-Headphones-Cancellation-Transparency-Personalized/dp/B0DGJKT2X9/ref=sr_1_3?crid=QSDYHZE0R4O6&dib=eyJ2IjoiMSJ9.zbZDwWckTNbr4vqMJlyuIhFv0GbgC56Dy1uv4mgD8UDg6uW8yE8xIzukmWZj3gsJO2Hcc4Eokc_clkk0wR9ZiGcyaRiVJu6t2QnS8YRGKelhkH6ra9Banf49O9HYv-jd721aOp5noqj3eEe3QWxVrGQ6VCUmo-05ESJexTeI5Luurs0iYGQ-nVYhCE3vhlRMxjFjMqvDljO7wB0rQWfmN9woXwRvjslKXUIOSwEbf7k.Y44uhyvXlf2vACKTQEvT92anPxkufSEXgc851X_2lXM&dib_tag=se&keywords=apple%2Bairpods%2Bmax&qid=1770330314&sprefix=apple%2Bairpods%2Bmax%2Caps%2C166&sr=8-3&th=1"

driver = webdriver.Safari()
driver.get(url)

time.sleep(5) #wait for page to load completely

html_content = driver.page_source
driver.quit()

soup = BeautifulSoup(html_content, "lxml")

product_title = soup.find("span", id="productTitle")
product_price = soup.find("span", class_="aok-offscreen")
product_rating = soup.find("span", class_="a-icon-alt")
product_bullets = soup.find("ul", class_="a-unordered-list a-vertical a-spacing-mini")
product_tech_details = soup.find("table", id="productDetails_techSpec_section_1")
product_reviews = soup.find("div", class_="a-section a-spacing-large reviews-content filterable-reviews-content celwidget")

def print_text(element, label):
    if element:
        print(f"\n{label}: {element.text.strip()}")
    else:
        print(f"{label} not found")

def print_tech_details(table, label):
    if table: 
        print(f"\n{label}:")
        rows = table.find_all("tr")
        for row in rows:
            key = row.find("th")
            value = row.find("td")
            if key and value:
                print(f" {key.text.strip()}: {value.text.strip()}")
    else:
        print(f"{label} not found")

print_text(product_title, "Product Title")
print_text(product_price, "Product Price")
print_text(product_rating, "Product Rating")
print_text(product_bullets, "Product Bullets")
print_tech_details(product_tech_details, "Product Technical Details")
print_text(product_reviews, "Product Reviews")

#find, find_all 

#saving the data in a text file 
with open("amazon_airpod_max.csv", mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["product_title", "product_price", "product_rating", "product_bullets", "product_tech_details", "product_reviews"])

    writer.writerow([product_title.text.strip() if product_title else "Not Found", 
                     product_price.text.strip() if product_price else "Not Found", 
                     product_rating.text.strip() if product_rating else "Not Found", 
                     product_bullets.text.strip() if product_bullets else "Not Found", 
                     product_tech_details.text.strip() if product_tech_details else "Not Found", 
                     product_reviews.text.strip() if product_reviews else "Not Found"])

print("data saved!")

