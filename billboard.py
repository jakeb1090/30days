import requests
from requests_html import HTML
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pandas as pd
import time
from requests_html import HTMLSession

url = 'https://www.billboard.com/charts/pop-songs'

class ChartScrape:
    

    def start_driver(url):
        options = Options()
        options.add_argument("--headless")
        driver = webdriver.Chrome('c:/chromedriver/chromedriver.exe', options=options)
        driver.get(url)
        return driver
        
    def create_req_obj():
        body_el = driver.find_element_by_css_selector('body')
        html_str = body_el.get_attribute('innerHTML')
        requests_obj = HTML(html=html_str)
        return requests_obj
        
    def get_data():
        rank_el = requests_obj.find('.chart-list-item__rank')
        ranks = [x.text for x in rank_el]

        title_el = requests_obj.find('.item-details__title')
        titles = [x.text for x in title_el]

        artist_el = requests_obj.find('.item-details__artist')
        artists = [x.text for x in artist_el]
        
        r_dict = {
        'rank': ranks,
        'title': titles,
        'artist': artists,
        'genre': requests_obj.find('.print-chart__title')[0].text,
        'date': requests_obj.find('.print-chart__week')[0].text
        }
        return r_dict

        
    def to_output():
        df = pd.DataFrame(data=_dict)
        output_dict = df.T.to_dict()
        return output_dict

    def process_page(url):
        driver = start_driver(url)
        requests_obj = create_req_obj()
        r_dict = get_data()
        output_dict = to_output()
        return output_dict