from selenium import webdriver   #import scraping tool
import pygsheets
gc = pygsheets.authorize(service_file='client_secret.json') #authorizing google sheets API


options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
DRIVER_PATH = r"chromedriver"
options.binary_location = r"../../../../Applications/Google Chrome 3.app/Contents/MacOS/Google Chrome"
driver = webdriver.Chrome(executable_path=DRIVER_PATH, options=options)

url = "https://www.amazon.com/s?k=macbook"  #URL to Amazon Macbook products
driver.get(url)

products = driver.find_elements_by_class_name("s-include-content-margin")
for product in products:
    try:
        product_url = product.find_element_by_class_name("a-link-normal.a-text-normal").get_attribute('href')
        product_name = product.find_element_by_class_name("a-size-medium.a-color-base.a-text-normal").text
        product_price = product.find_element_by_class_name("a-price").text

        # print(product_url,product_name, product_price)
        products_list = [product_url, product_name, product_price]
        worksheet = gc.open('Amazon Products').sheet1
        header = worksheet.get_row(1, include_tailing_empty=False)
        header.update_values = ["Product URL", "Product Name", "Product Price"]
        worksheet = worksheet.insert_rows(1, values= products_list)  #Insert all products to worksheet
    except:
        pass