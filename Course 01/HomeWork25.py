import bs4
import requests

request_home_page = requests.get("https://electro.madrasthemes.com/")
if request_home_page.status_code == 200:
    soup_home_page =  bs4.BeautifulSoup(request_home_page.text)
    title = soup_home_page.select("title")[0]
    print(f"Home page title: {title.text}")


print()
print("*********************************")
print()

request_products_page = requests.get("https://electro.madrasthemes.com/")
if request_products_page.status_code == 200:
    soup_products_page = bs4.BeautifulSoup(request_products_page.text)
    products_box = soup_products_page.select('li.product')

    for product_box in products_box:
        product = product_box.select("h2.woocommerce-loop-product__title")

        image = product_box.select("div.product-thumbnail img")
        print(f"Product: {product[0].text}")
        if len(image) > 0:
            print(f"Image Url: {image[0].attrs["src"]}")
        print()
        