# Dependencies
from bs4 import BeautifulSoup as bs
import requests
from splinter import Browser
import pandas as pd
import lxml

def scrape():# Store data in a dictionary
    url="https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204%3A165&blank_scope=Latest"
    response = requests.get(url)
    soup = bs(response.text, 'html.parser')
    news_title = soup.find("div", class_="content_title").find("a").get_text()
    news_title=news_title.replace('\n', '')

    news_p = soup.find("div", class_="rollover_description_inner").get_text()
    news_p=news_p.replace('\n', '')

    featured_image_url = "https://www.jpl.nasa.gov/spaceimages/images/largesize/PIA23376_hires.jpg"

    url="https://twitter.com/marswxreport?lang=en"
    response = requests.get(url)
    soup = bs(response.text, 'html.parser')
    mars_weather=soup.find("p", class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text").get_text()
    mars_weather=mars_weather.replace('\n', ' ')
    mars_weather=mars_weather.replace('hPapic.twitter.com/RIAb2fzSY4','')

    url="https://space-facts.com/mars/"
    tables = pd.read_html(url)
    df = tables[0]
    df.columns = ['Description','Value']
    df.set_index('Description', inplace=True)
    html_table = df.to_html()
    df.to_html('table.html')

    hemisphere_image_urls = [
    {"title": "Valles Marineris Hemisphere", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif"},
    {"title": "Cerberus Hemisphere", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif"},
    {"title": "Schiaparelli Hemisphere", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif/full.jpg"},
    {"title": "Syrtis Major Hemisphere", "img_url": "https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif"},
    ]

    mars_data = {
        "news_title": news_title,
        "news_p": news_p,
        "featured_image_url": featured_image_url,
        "mars_weather":mars_weather,
        "hemisphere_image_urls":hemisphere_image_urls
    }
    return mars_data


