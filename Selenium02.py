from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
import time



class stock:
    def __init__(self, stock_number):
        self.stock_number = stock_number

    def daily (self, year, month):
        browser = webdriver.Chrome(ChromeDriverManager().install())
        browser.get('https://www.twse.com.tw/zh/page/trading/exchange/STOCK_DAY_AVG.html')
        select_year = Select(browser.find_element_by_name("yy"))
        select_year.select_by_value(year)

        select_month = Select(browser.find_element_by_name("mm"))
        select_month.select_by_value(month)

        stockno = browser.find_element_by_name("stockNo")
        
        result = []

        stockno.send_keys(self.stock_number)
        stockno.submit()
        
        time.sleep(2)
        
        soup = BeautifulSoup(browser.page_source, "lxml")
        
        table = soup.find("table", {"id": "report-table"})
        
        elements = table.find_all(
			"td", {"class": "dt-head-center dt-body-center"})
        
        data = [self.stock_number] + [element.getText() for element in elements]
        result.append(data)
        print(result)

if __name__ == "__main__":
    stock = stock('2330')
    stock.daily("2021","1")