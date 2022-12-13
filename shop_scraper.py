# This script allows one to input:
# i) a search_term to be searched in the Etsy shop search engine and 
# ii) the number of pages to scrape. Note that as of 11/2022, there are 10 Etsy shops per page.
# 
# The script writes a csv file with one row per Etsy shop and 15 columns, each column being a characteristic of the given Etsy shop


#import libraries
import requests
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
import math
import re

#string to be searched in Etsy's shop search engine
search_term = 'glassblowing'

#total number of pages containing shops to scrape
number_pages_to_scrape = 1

#number of shops to scrape between saving the data; we do this so that if we get an error, our work is not lost
data_save_step = 2

#define dataframe which will contain our data and which we will eventually write to csv
df = pd.DataFrame()


#exactly one item will be appended to each of these lists for every shop scraped
shop_name = []
shop_id = []
currency_id = []
country_id = []
listing_enabled = []
browsing_enabled = []
buyer_location_restricted = []
rate_updates_enabled = []
test_account = []
accepts_custom_requests = []
number_admirers = []
number_items_listed = [] 
total_sales = []
number_reviews = []
avg_rating = []
starting_year = []
number_items_for_sale = []
avg_price = []
std_price = []
avg_feat_price = []
std_feat_price = []
number_feature_items = []
shop_number = 0


#loop through pages on the Etsy shop search engine webpage; note that there are 10 Etsy shops per page as of 11/2022
for page_number in range(0, number_pages_to_scrape):
    #this is the url obtained by searching 'woodworking' into the shop search engine in Etsy and navigating to the page_number-th page of shops
    url = f"https://www.etsy.com/search/shops?order=most_relevant&search_type=shops&page={page_number}&ref=pagination&search_query={search_term}"
    
    #get response and soup objects which represents the page_number-th page
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    #iterate through the shop hyperlinks on the page_number-th page
    for page_links in soup.find_all('a', class_='wt-card__link wt-display-flex-xs wt-width-full wt-mt-xs-2', href=True):
        #get response and soup objects for the given Etsy shop on the page_number-th page
        shop_page = requests.get(page_links['href'])
        shop_soup = BeautifulSoup(shop_page.content, 'html.parser')

        #get shop identifiers, currency, and country
        shop_name.append(shop_soup.find_all('title')[0].contents[0][0:(len(shop_soup.find_all('title')[0].contents[0])-7)])
        shop_id.append(shop_page.text[shop_page.text.find('shop_id')+9:shop_page.text.find('shop_id')+16])
        currency_id.append(shop_page.text[shop_page.text.find('currency_id')+13:shop_page.text.find('currency_id')+16])
        country_id.append(shop_page.text[shop_page.text.find('country_id')+12:shop_page.text.find('country_id')+15])

        #t/f flags:
        listing_enabled.append(shop_page.text[shop_page.text.find('listing_enabled')+17:shop_page.text.find('listing_enabled')+18])
        browsing_enabled.append(shop_page.text[shop_page.text.find('browsing_enabled')+18:shop_page.text.find('browsing_enabled')+19])
        buyer_location_restricted.append(shop_page.text[shop_page.text.find('buyer_location_restricted')+27:shop_page.text.find('buyer_location_restricted')+28])
        rate_updates_enabled.append(shop_page.text[shop_page.text.find('rate_updates_enabled')+22:shop_page.text.find('rate_updates_enabled')+23])
        test_account.append(shop_page.text[shop_page.text.find('test_account')+11:shop_page.text.find('test_account')+12])
        accepts_custom_requests.append(shop_page.text[shop_page.text.find('accepts_custom_requests')+25:shop_page.text.find('accepts_custom_requests')+26])
        number_feature_items.append(int(len(re.findall('shop_home_feat', shop_page.text))/2))

        #get number of shop admirers
        tmp_str = shop_page.text[shop_page.text.find('Favorite Shop')+15:shop_page.text.find('Favorite Shop')+20]
        if tmp_str[0] == '0' or tmp_str[0] == '1' or tmp_str[0] == '2' or tmp_str[0] == '3' or tmp_str[0] == '4' or tmp_str[0] == '5' or tmp_str[0] == '6' or tmp_str[0] == '7' or tmp_str[0] == '8' or tmp_str[0] == '9':
            if tmp_str[1] != '0' and tmp_str[1] != '1' and tmp_str[1] != '2' and tmp_str[1] != '3' and tmp_str[1] != '4' and tmp_str[1] != '5' and tmp_str[1] != '6' and tmp_str[1] != '7' and tmp_str[1] != '8' and tmp_str[1] != '9':
                number_admirers.append(int(tmp_str[0]))
            elif tmp_str[2] != '0' and tmp_str[2] != '1' and tmp_str[2] != '2' and tmp_str[2] != '3' and tmp_str[2] != '4' and tmp_str[2] != '5' and tmp_str[2] != '6' and tmp_str[2] != '7' and tmp_str[2] != '8' and tmp_str[2] != '9':
                number_admirers.append(int(tmp_str[0:2]))
            elif tmp_str[3] != '0' and tmp_str[3] != '1' and tmp_str[3] != '2' and tmp_str[3] != '3' and tmp_str[3] != '4' and tmp_str[3] != '5' and tmp_str[3] != '6' and tmp_str[3] != '7' and tmp_str[3] != '8' and tmp_str[3] != '9':
                number_admirers.append(int(tmp_str[0:3]))
            elif tmp_str[4] != '0' and tmp_str[4] != '1' and tmp_str[4] != '2' and tmp_str[4] != '3' and tmp_str[4] != '4' and tmp_str[4] != '5' and tmp_str[4] != '6' and tmp_str[4] != '7' and tmp_str[4] != '8' and tmp_str[4] != '9':
                number_admirers.append(int(tmp_str[0:4]))    
            elif tmp_str[5] != '0' and tmp_str[5] != '1' and tmp_str[5] != '2' and tmp_str[5] != '3' and tmp_str[5] != '4' and tmp_str[5] != '5' and tmp_str[5] != '6' and tmp_str[5] != '7' and tmp_str[5] != '8' and tmp_str[5] != '9':
                number_admirers.append(int(tmp_str[0:5]))
        else:
            number_admirers.append(math.nan)           


        #get the average shop rating rounded to the nearest half
        tmp_str = shop_page.text[shop_page.text.find('ratingValue')+15:shop_page.text.find('ratingValue')+18]
        if tmp_str[1] == '.':
            avg_rating.append(float(tmp_str[0:3]))
        elif tmp_str[0] == '<' or tmp_str[0] == '>':
            avg_rating.append(math.nan)
        else:
            avg_rating.append(int(tmp_str[0]))
        

        #get total number of items listed for sale by the shop
        tmp_str = shop_page.text[shop_page.text.find('listings_total_count')+22:shop_page.text.find('listings_total_count')+26]
        res = " " in tmp_str
        if tmp_str[1] != '0' and tmp_str[1] != '1' and tmp_str[1] != '2' and tmp_str[1] != '3' and tmp_str[1] != '4' and tmp_str[1] != '5' and tmp_str[1] != '6' and tmp_str[1] != '7' and tmp_str[1] != '8' and tmp_str[1] != '9' and res != True:
            number_items_listed.append(int(tmp_str[0]))
        elif tmp_str[2] != '0' and tmp_str[2] != '1' and tmp_str[2] != '2' and tmp_str[2] != '3' and tmp_str[2] != '4' and tmp_str[2] != '5' and tmp_str[2] != '6' and tmp_str[2] != '7' and tmp_str[2] != '8' and tmp_str[2] != '9' and res != True:
            number_items_listed.append(int(tmp_str[0:2]))
        elif tmp_str[3] != '0' and tmp_str[3] != '1' and tmp_str[3] != '2' and tmp_str[3] != '3' and tmp_str[3] != '4' and tmp_str[3] != '5' and tmp_str[3] != '6' and tmp_str[3] != '7' and tmp_str[3] != '8' and tmp_str[3] != '9' and res != True:
            number_items_listed.append(int(tmp_str[0:3]))
        else:
            number_items_listed.append(0)
    

        #get total number of item reviews for the shop
        if shop_soup.find('div', class_='display-inline-block vertical-align-middle') == None:
            number_reviews.append(math.nan)
        else:
            number_reviews.append(int(shop_soup.find('div', class_='display-inline-block vertical-align-middle').contents[0][1:len(shop_soup.find('div', class_='display-inline-block vertical-align-middle').contents[0])-1]))


        #get total number of sales for the shop
        if shop_soup.find('div', class_='shop-sales-reviews') != None:
            if shop_soup.find('div', class_='shop-sales-reviews').find('a', class_='') != None:
                tmp_char = shop_soup.find('div', class_='shop-sales-reviews').find('a', class_='').contents[0][0]
                if tmp_char == '0' or tmp_char == '1' or tmp_char == '2' or tmp_char == '3' or tmp_char == '4' or tmp_char == '5' or tmp_char == '6' or tmp_char == '7' or tmp_char == '8' or tmp_char == '9': 
                    total_sales.append(int(shop_soup.find('div', class_='shop-sales-reviews').find('a', class_='').contents[0].replace(',','').replace(' Sales','').replace('Sale','')))
                else:
                    total_sales.append(math.nan)
            elif shop_soup.find('div', class_='shop-sales-reviews').find('span', class_='wt-text-caption wt-no-wrap') == None:
                total_sales.append(math.nan)
            else:
                total_sales.append(int(shop_soup.find('div', class_='shop-sales-reviews').find('span', class_='wt-text-caption wt-no-wrap').contents[0][0:len(shop_soup.find('div', class_='shop-sales-reviews').find('span', class_='wt-text-caption wt-no-wrap'))-6].replace(',','')))
        else:
            total_sales.append(0)


        #get starting year of shop
        if len(shop_soup.find_all('span', class_='wt-text-title-03 wt-display-block')) == 0:
            starting_year.append(math.nan)
        else:
            starting_year.append(int(shop_soup.find_all('span', class_='wt-text-title-03 wt-display-block')[1].contents[0]))


        #get the average and standard deviation of the prices of featured items
        feat_price_vec = []
        for i in range(0, number_feature_items[len(number_feature_items)-1]):
            feat_price_vec.append(float(shop_soup.find_all('div', class_='n-listing-card__price')[i].find_all('span', class_='currency-value')[0].contents[0].replace(',','')))            
        if len(feat_price_vec) > 0:
            avg_feat_price.append(np.mean(feat_price_vec))
            std_feat_price.append(np.std(feat_price_vec))
        else:
            avg_feat_price.append(math.nan)
            std_feat_price.append(math.nan)


        #get the average price of listed items for the shop's first page of listed items
        if number_items_listed[len(number_items_listed)-1] > 0:
            price_vec = []
            for i in range(number_feature_items[len(number_feature_items)-1], len(shop_soup.find_all('div', class_='n-listing-card__price'))):
                if shop_soup.find_all('div', class_='n-listing-card__price')[i].find_all('span', class_='currency-value')[0] != None:
                    price_vec.append(float(shop_soup.find_all('div', class_='n-listing-card__price')[i].find_all('span', class_='currency-value')[0].contents[0].replace(',','')))
                else:
                    price_vec.append(math.nan)

            #if there are more than 40 items listed for sale, get the total number of pages of listings; note that each page lists up to 40 items inclusive
            if number_items_listed[len(number_items_listed)-1] > 40:
                page_stop = number_items_listed[len(number_items_listed)-1] // 40
                for i in range(2, page_stop+1):
                    next_page = requests.get(f"https://www.etsy.com/shop/{shop_name[len(shop_name)-1]}?page={i}#items")
                    next_soup = BeautifulSoup(next_page.content, 'html.parser')
                    for i in range(0, len(shop_soup.find_all('div', class_='n-listing-card__price'))):
                        price_vec.append(float(shop_soup.find_all('div', class_='n-listing-card__price')[i].find_all('span', class_='currency-value')[0].contents[0].replace(',','')))
            if len(price_vec) > 0:
                avg_price.append(np.mean(price_vec))
                std_price.append(np.std(price_vec))
            else:
                avg_price.append(math.nan)
                std_price.append(math.nan)
        else:
            avg_price.append(math.nan)
            std_price.append(math.nan)
        
        #increment the shop number
        shop_number += 1
        


        #save data every 'data_save_step' many iterations so that we don't lose our data if/when an error occurs
        if shop_number % data_save_step == 0:
            print('\n\n\n\n\n\ndata saved to csv\n\n\n\n\n\n')
            df = pd.DataFrame(list(zip(shop_name, shop_id, currency_id, country_id, listing_enabled, browsing_enabled, buyer_location_restricted,
rate_updates_enabled, test_account, accepts_custom_requests, number_admirers, total_sales,
starting_year, number_reviews, avg_rating, number_items_listed, avg_price, std_price, avg_feat_price, std_feat_price, number_feature_items)), columns=['shop_name', 
'shop_id', 'currency_id', 'country_id', 'listing_enabled', 'browsing_enabled', 'buyer_location_restricted', 'rate_updated_enabled', 'test_account', 'accepts_custom_requests', 
'number_admirers', 'total_sales', 'starting_year', 'number_reviews', 'avg_rating', 'number_items_listed', 'avg_price', 'std_price', 'avg_feat_price', 'std_feat_price', 'number_feature_items'])
            df.to_csv('/home/hunter/STA6840/final_project/data/output.csv')

